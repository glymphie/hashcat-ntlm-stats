import re

from .models import CrackedUser


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
    for password in cracked_passwords:
        password_hash, cracked_password = password.split(":")

        for user in list_of_users:
            if user.ntlm_hash == password_hash:
                user.cracked_password = cracked_password


def parse_logfile(logfile, list_of_users):
    """Parse the logfile to get the date and time taken."""
    password_regex = re.compile(r"^(\w+):(.*)$")
    time_regex = re.compile(r"^Time\.Started.*: (.*) \((.*)\)$")

    for line in logfile:
        match_password = password_regex.match(line)
        match_time = time_regex.match(line)

        if match_time:
            print(match_time.group(1), match_time.group(2))

        if match_password:
            print(match_password.group(1), match_password.group(2))


def parse_hashcat(user_hashes, cracked_passwords, logfile):
    list_of_users = []

    parse_user_hashes(load_file(user_hashes), list_of_users)
    parse_cracked_passwords(load_file(cracked_passwords), list_of_users)
    parse_logfile(load_file(logfile), list_of_users)

    return list_of_users
