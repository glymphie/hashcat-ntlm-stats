#!/usr/bin/env python

import argparse


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
        return f"{self.domain}\\{self.username},{self.cracked_password},{self.ntlm_hash},{self.date},{self.time_taken}"


def load_file(filename):
    """Load a file and get a list."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def parse_user_hashes(user_hashes, list_of_users):
    """Parse the user hashes."""
    for user in user_hashes:
        new_cracked_user = CrackedUser()

        user_split = user.split(":")

        # ntlm_hash
        new_cracked_user.ntlm_hash = user_split[3]

        # domain and username
        domain_and_username = user_split[0].split("\\")
        if len(domain_and_username) == 2:
            new_cracked_user.domain = domain_and_username[0]
            new_cracked_user.username = domain_and_username[1]
        else:
            new_cracked_user.username = domain_and_username[0]

        list_of_users.append(new_cracked_user)


def parse_cracked_passwords(cracked_passwords, list_of_users):
    """Parse the cracked passwords."""
    return 0


def parse_logfile(logfile, list_of_users):
    """Parse the logfile to get the date and time taken."""
    return 0


def input_parser():
    """Parse input."""
    parser = argparse.ArgumentParser(
        description="Correlate hashcat input, cracked results, and logs."
    )
    parser.add_argument("--user-hashes", required=True, help="Path to user_hashes file")
    parser.add_argument(
        "--cracked-passwords", required=True, help="Path to cracked passwords file"
    )
    parser.add_argument("--logfile", required=True, help="Path to hashcat log file")
    return parser.parse_args()


def main():
    """Do the thing."""
    list_of_users = []
    args = input_parser()

    parse_user_hashes(load_file(args.user_hashes), list_of_users)
    parse_cracked_passwords(load_file(args.cracked_passwords), list_of_users)
    parse_logfile(load_file(args.logfile), list_of_users)

    __import__("pprint").pprint(list_of_users)


if __name__ == "__main__":
    main()
