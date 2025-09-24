import argparse

from .parser import parse_hashcat


def get_args():
    """Parse input."""
    argparser = argparse.ArgumentParser(
        description="Correlate hashcat input, cracked results, and logs."
    )
    argparser.add_argument(
        "--user-hashes", required=True, help="Path to user_hashes file"
    )
    argparser.add_argument(
        "--cracked-passwords", required=True, help="Path to cracked passwords file"
    )
    argparser.add_argument("--logfile", required=True, help="Path to hashcat log file")
    return argparser.parse_args()


def main():
    """Parse hashcat files."""
    args = get_args()

    list_of_users = parse_hashcat(
        args.user_hashes, args.cracked_passwords, args.logfile
    )

    __import__("pprint").pprint(list_of_users)


if __name__ == "__main__":
    main()
