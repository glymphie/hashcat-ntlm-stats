import re
from zxcvbn import zxcvbn

MONTH_PATTERN = re.compile(
    r"(jan|january|feb|february|mar|march|apr|april|may|jun|june|"
    r"jul|july|aug|august|sep|sept|september|oct|october|"
    r"nov|november|dec|december)",
    re.IGNORECASE,
)

MONTH_PLUS_NUMBER_PATTERN = re.compile(
    r"^(jan|january|feb|february|mar|march|apr|april|may|jun|june|"
    r"jul|july|aug|august|sep|sept|september|oct|october|"
    r"nov|november|dec|december)[^A-Za-z0-9]?\d+$",
    re.IGNORECASE,
)

SEASON_PATTERN = re.compile(
    r"(spring|summer|autumn|fall|winter)",
    re.IGNORECASE,
)

SEASON_PLUS_NUMBER_PATTERN = re.compile(
    r"^(spring|summer|autumn|fall|winter)[^A-Za-z0-9]?\d+$",
    re.IGNORECASE,
)

RECENT_YEAR_PATTERN = re.compile(r"(19|20)\d{2}")


def find_custom_patterns(password):
    patterns = set()

    if RECENT_YEAR_PATTERN.search(password):
        patterns.add("contains_year")

    if re.search(r"\d+$", password):
        patterns.add("ends_with_number")

    if re.search(r"[^A-Za-z0-9]$", password):
        patterns.add("ends_with_symbol")

    if MONTH_PATTERN.search(password):
        patterns.add("contains_month")

    if MONTH_PLUS_NUMBER_PATTERN.search(password):
        patterns.add("month_plus_number")

    if SEASON_PATTERN.search(password):
        patterns.add("contains_season")

    if SEASON_PLUS_NUMBER_PATTERN.search(password):
        patterns.add("season_plus_number")

    return patterns


def find_zxcvbn_patterns(password):
    patterns = set()

    result = zxcvbn(password)

    for match in result["sequence"]:
        pattern = match.get("pattern")

        if pattern == "dictionary":
            patterns.add("dictionary_word")
        elif pattern == "spatial":
            patterns.add("keyboard_pattern")
        elif pattern == "repeat":
            patterns.add("repeated_chars")
        elif pattern == "sequence":
            patterns.add("sequence")
        elif pattern == "date":
            patterns.add("date_or_year")

    return patterns
