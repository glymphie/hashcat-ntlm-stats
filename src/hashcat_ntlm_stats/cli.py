import argparse

from .parser import parse_hashcat
from .parser import write_output
from .analyzer import analyze


def get_args():
    """Parse input."""
    argparser = argparse.ArgumentParser(
        description="Correlate hashcat input, cracked results, and logs."
    )
    argparser.add_argument(
        "-uh", "--user-hashes", required=True, help="Path to user_hashes file"
    )
    argparser.add_argument(
        "-cp",
        "--cracked-passwords",
        required=True,
        help="Path to cracked passwords file",
    )
    argparser.add_argument(
        "-hl", "--hashcat-logfile", required=True, help="Path to hashcat log file"
    )
    argparser.add_argument(
        "-f",
        "--format",
        choices=["text", "csv", "json"],
        default="text",
        help="Output format: text, csv, or json. Defualt: text",
    )
    argparser.add_argument(
        "-a",
        "--analyze",
        action="store_true",
        help="Analyze cracked passwords for patterns",
    )

    return argparser.parse_args()


def main():
    """Parse hashcat files."""
    args = get_args()

    list_of_cracked_users = parse_hashcat(
        args.user_hashes, args.cracked_passwords, args.hashcat_logfile
    )

    if args.analyze:
        analyze(list_of_cracked_users)

    write_output(list_of_cracked_users, args.format)


if __name__ == "__main__":
    main()
