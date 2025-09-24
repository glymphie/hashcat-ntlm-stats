import argparse
from hashcat_ntlm_stats import parser


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
    """Do the thing."""
    list_of_users = []
    args = get_args()

    parser.parse_user_hashes(parser.load_file(args.user_hashes), list_of_users)
    parser.parse_cracked_passwords(
        parser.load_file(args.cracked_passwords), list_of_users
    )
    parser.parse_logfile(parser.load_file(args.logfile), list_of_users)

    __import__("pprint").pprint(list_of_users)


if __name__ == "__main__":
    main()
