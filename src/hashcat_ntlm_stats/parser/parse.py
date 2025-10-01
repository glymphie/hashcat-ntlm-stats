import re
from datetime import datetime, timedelta

from .models import CrackedUser


def load_file(filename):
    """Load a file and get a list."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def convert_to_datetime(date_time):
    """Convert to datetime format."""
    return datetime.strptime(date_time, "%a %b %d %H:%M:%S %Y")


def get_deltatime(date_time, time_taken):
    """Get the finished time and deltatime."""
    dt = convert_to_datetime(date_time)

    d = re.search(r"(\d+)\s*day", time_taken)
    h = re.search(r"(\d+)\s*hour", time_taken)
    m = re.search(r"(\d+)\s*min", time_taken)
    s = re.search(r"(\d+)\s*sec", time_taken)

    delta = timedelta(
        days=int(d.group(1)) if d else 0,
        hours=int(h.group(1)) if h else 0,
        minutes=int(m.group(1)) if m else 0,
        seconds=int(s.group(1)) if s else 0,
    )

    return dt + delta, delta


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


def get_set_time(time_regex, logfile, list_of_users):
    for line in logfile:
        match_time = time_regex.match(line)

        if match_time:
            start_date = match_time.group(1)

            for user in list_of_users:
                user.start_date = convert_to_datetime(start_date)

            time_taken = "0 secs"
            finished_at, time_taken = get_deltatime(start_date, time_taken)
            return finished_at, time_taken


def parse_logfile(logfile, list_of_users):
    """Parse the logfile to get the date and time taken."""
    password_regex = re.compile(r"^(\w+):(.*)$")
    time_regex = re.compile(r"^Time\.Started.*: (.*) \((.*)\)$")

    finished_at, time_taken = get_set_time(time_regex, logfile, list_of_users)

    for line in logfile:
        match_password = password_regex.match(line)
        match_time = time_regex.match(line)

        if match_time:
            date = match_time.group(1)
            time_taken = match_time.group(2)
            finished_at, time_taken = get_deltatime(date, time_taken)

        if match_password:
            password_hash = match_password.group(1)

            for user in list_of_users:
                if password_hash == user.ntlm_hash:
                    user.cracked = True
                    user.finished_at = finished_at
                    user.time_taken = time_taken


def parse_hashcat(user_hashes, cracked_passwords, logfile):
    """Parse the hashcat files."""
    list_of_users = []

    parse_user_hashes(load_file(user_hashes), list_of_users)
    parse_cracked_passwords(load_file(cracked_passwords), list_of_users)
    parse_logfile(load_file(logfile), list_of_users)

    return list_of_users
