from dataclasses import dataclass, asdict
from datetime import datetime, timedelta


@dataclass
class CrackedUser:
    """A cracked user."""

    domain: str = None
    username: str = None
    cracked: bool = False
    cracked_password: str = None
    ntlm_hash: str = None
    start_date: datetime = None
    finished_at: datetime = None
    time_taken_seconds: timedelta = None
    password_patterns: set[str] = None

    def __repr__(self):
        """Print a better representation of the class."""
        return f"{self.domain},{self.username},{self.cracked},{self.cracked_password},{self.ntlm_hash},{self.start_date},{self.finished_at},{self.time_taken_seconds}"

    def to_print_row(self):
        """Return string values of attributes of the class."""
        return ["" if value is None else str(value) for value in asdict(self).values()]

    def to_json_dict(self):
        """Return JSON-friendly dictionary of the class."""
        result = {}

        for key, value in asdict(self).items():
            if isinstance(value, datetime):
                value = str(value)

            result[key] = value

        return result
