from dataclasses import dataclass
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
    time_taken: timedelta = None

    def __repr__(self):
        """Print a better representation of the class."""
        return f"{self.domain},{self.username},{self.cracked},{self.cracked_password},{self.ntlm_hash},{self.start_date},{self.finished_at},{self.time_taken}"
