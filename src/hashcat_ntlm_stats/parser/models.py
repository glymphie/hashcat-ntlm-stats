class CrackedUser:
    """A cracked user."""

    def __init__(
        self,
        domain=None,
        username=None,
        cracked_password=None,
        ntlm_hash=None,
        date=None,
        time_taken=None,
    ) -> None:
        """Init."""
        self.domain = domain
        self.username = username
        self.cracked_password = cracked_password
        self.ntlm_hash = ntlm_hash
        self.date = date
        self.time_taken = time_taken

    def __repr__(self):
        """Print a better representation of the class."""
        if self.domain is None:
            return f"{self.username},{self.cracked_password},{self.ntlm_hash},{self.date},{self.time_taken}"
        else:
            return f"{self.domain}\\{self.username},{self.cracked_password},{self.ntlm_hash},{self.date},{self.time_taken}"
