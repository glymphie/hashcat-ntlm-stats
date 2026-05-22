import csv
import sys
import json
from dataclasses import asdict, fields
from rich.console import Console
from rich.table import Table

from .models import CrackedUser


def print_csv(list_of_cracked_users: list[CrackedUser]):
    """Print CSV output."""
    fieldnames = [field.name for field in fields(CrackedUser)]

    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()

    for user in list_of_cracked_users:
        writer.writerow(asdict(user))


def print_text(list_of_cracked_users: list[CrackedUser]):
    """Print Text output."""
    cracked_user_table = Table(title="Cracked Users")

    cracked_user_table.add_column("Domain")
    cracked_user_table.add_column("Username")
    cracked_user_table.add_column("Cracked")
    cracked_user_table.add_column("Password")
    cracked_user_table.add_column("NTLM Hash")
    cracked_user_table.add_column("Start Date")
    cracked_user_table.add_column("Finished At")
    cracked_user_table.add_column("Time Taken (s)", justify="right")

    for user in list_of_cracked_users:
        cracked_user_table.add_row(*user.to_print_row())

    Console().print(cracked_user_table)


def print_json(list_of_cracked_users: list[CrackedUser]):
    """Print JSON output."""
    json.dump(
        [user.to_json_dict() for user in list_of_cracked_users],
        sys.stdout,
        indent=2,
    )


def write_output(list_of_cracked_users: list[CrackedUser], output_format: str):
    """Handle which method to call depending on the output format."""
    writers = {
        "text": print_text,
        "csv": print_csv,
        "json": print_json,
    }

    writers[output_format](list_of_cracked_users)
