# Overview

<a href="https://github.com/glymphie/hashcat-ntlm-stats/actions/workflows/tests.yml"><img src="https://github.com/glymphie/hashcat-ntlm-stats/actions/workflows/tests.yml/badge.svg" alt="Tests Badge"></a>
<a href="https://github.com/glymphie/hashcat-ntlm-stats/blob/main/LICENSE"><img src="https://img.shields.io/github/license/glymphie/hashcat-ntlm-stats?labelColor=353C43&color=2b9348&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAuMDAwMDkzODc0NSAwLjAwMDczMjQyMiAxNiAxNC41Ij4KCTxwYXRoIGQ9Ik04Ljc1Ljc1VjJoLjk4NWMuMzA0IDAgLjYwMy4wOC44NjcuMjMxbDEuMjkuNzM2Yy4wMzguMDIyLjA4LjAzMy4xMjQuMDMzaDIuMjM0YS43NS43NSAwIDAgMSAwIDEuNWgtLjQyN2wyLjExMSA0LjY5MmEuNzUuNzUgMCAwIDEtLjE1NC44MzhsLS41My0uNTMuNTI5LjUzMS0uMDAxLjAwMi0uMDAyLjAwMi0uMDA2LjAwNi0uMDA2LjAwNS0uMDEuMDEtLjA0NS4wNGMtLjIxLjE3Ni0uNDQxLjMyNy0uNjg2LjQ1QzE0LjU1NiAxMC43OCAxMy44OCAxMSAxMyAxMWE0LjQ5OCA0LjQ5OCAwIDAgMS0yLjAyMy0uNDU0IDMuNTQ0IDMuNTQ0IDAgMCAxLS42ODYtLjQ1bC0uMDQ1LS4wNC0uMDE2LS4wMTUtLjAwNi0uMDA2LS4wMDQtLjAwNHYtLjAwMWEuNzUuNzUgMCAwIDEtLjE1NC0uODM4TDEyLjE3OCA0LjVoLS4xNjJjLS4zMDUgMC0uNjA0LS4wNzktLjg2OC0uMjMxbC0xLjI5LS43MzZhLjI0NS4yNDUgMCAwIDAtLjEyNC0uMDMzSDguNzVWMTNoMi41YS43NS43NSAwIDAgMSAwIDEuNWgtNi41YS43NS43NSAwIDAgMSAwLTEuNWgyLjVWMy41aC0uOTg0YS4yNDUuMjQ1IDAgMCAwLS4xMjQuMDMzbC0xLjI4OS43MzdjLS4yNjUuMTUtLjU2NC4yMy0uODY5LjIzaC0uMTYybDIuMTEyIDQuNjkyYS43NS43NSAwIDAgMS0uMTU0LjgzOGwtLjUzLS41My41MjkuNTMxLS4wMDEuMDAyLS4wMDIuMDAyLS4wMDYuMDA2LS4wMTYuMDE1LS4wNDUuMDRjLS4yMS4xNzYtLjQ0MS4zMjctLjY4Ni40NUM0LjU1NiAxMC43OCAzLjg4IDExIDMgMTFhNC40OTggNC40OTggMCAwIDEtMi4wMjMtLjQ1NCAzLjU0NCAzLjU0NCAwIDAgMS0uNjg2LS40NWwtLjA0NS0uMDQtLjAxNi0uMDE1LS4wMDYtLjAwNi0uMDA0LS4wMDR2LS4wMDFhLjc1Ljc1IDAgMCAxLS4xNTQtLjgzOEwyLjE3OCA0LjVIMS43NWEuNzUuNzUgMCAwIDEgMC0xLjVoMi4yMzRhLjI0OS4yNDkgMCAwIDAgLjEyNS0uMDMzbDEuMjg4LS43MzdjLjI2NS0uMTUuNTY0LS4yMy44NjktLjIzaC45ODRWLjc1YS43NS43NSAwIDAgMSAxLjUgMFptMi45NDUgOC40NzdjLjI4NS4xMzUuNzE4LjI3MyAxLjMwNS4yNzNzMS4wMi0uMTM4IDEuMzA1LS4yNzNMMTMgNi4zMjdabS0xMCAwYy4yODUuMTM1LjcxOC4yNzMgMS4zMDUuMjczczEuMDItLjEzOCAxLjMwNS0uMjczTDMgNi4zMjdaIiBmaWxsPSIjOTE5OGExIi8+Cjwvc3ZnPg==" alt="License Badge"></a>
<a href="https://glymphie.github.io/hashcat-ntlm-stats"><img src="https://glymphie.github.io/hashcat-ntlm-stats/badge.svg" alt="License Badge"></a>

A Python tool for analyzing and generating statistics from password
hashes cracked with Hashcat. The project focuses on identifying patterns and
characteristics in NTLM password data, such as password length, complexity, and
common structures.

### Prerequisites:

- [Getting the NTDS.dit and System Hive for extracting password hashes](./docs/extract_passwords_from_domain.md)
- [Extract hashes from NTDS.dit](./docs/extract_hashes_ntds.md)
- [Crack passwords with Hashcat](./docs/crack_passwords_with_hashcat.md)

## Running the tool

Before running the tool, you should have three files available:

1. A user/hash file containing account names and NTLM hashes.
   This is produced by `secretsdump.py`.

2. A potfile containing cracked hashes and their plaintext passwords.
   This is the `hashcat.potfile` file produced by Hashcat.

3. A Hashcat status log:
   This should contain periodic status output from Hashcat, including timestamps and cracking progress.

The tool correlates these three files to produce a clearer overview of the
cracked accounts.

It matches NTLM hashes from the user/hash file with cracked passwords from the
Hashcat potfile. It also uses the Hashcat status log to estimate when each
password was cracked, making it possible to see how long it took before each
password appeared in the cracked set.

```sh
$ hashcat-ntlm-stats --help
usage: hashcat-ntlm-stats [-h] -uh USER_HASHES -cp CRACKED_PASSWORDS -hl HASHCAT_LOGFILE [-f {text,csv,json}] [-a]

Correlate hashcat input, cracked results, and logs.

options:
  -h, --help            show this help message and exit
  -uh, --user-hashes USER_HASHES
                        Path to user_hashes file
  -cp, --cracked-passwords CRACKED_PASSWORDS
                        Path to cracked passwords file
  -hl, --hashcat-logfile HASHCAT_LOGFILE
                        Path to hashcat log file
  -f, --format {text,csv,json}
                        Output format: text, csv, or json. Defualt: text
  -a, --analyze         Analyze cracked passwords for patterns
```

### Output examples:

#### text

```txt
┏━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Domain   ┃ Username ┃ Cracked ┃ Password     ┃ NTLM Hash                        ┃ Start Date          ┃ Finished At         ┃ Time Taken (s) ┃ Password Patterns                                               ┃
┡━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ local.dk │ user1    │ True    │ Password1!   │ 5f4dcc3b5aa765d61d8327deb882cf99 │ 2025-09-02 10:39:43 │ 2025-09-02 10:41:53 │            130 │ ['dictionary_word', 'ends_with_symbol']                         │
└──────────┴──────────┴─────────┴──────────────┴──────────────────────────────────┴─────────────────────┴─────────────────────┴────────────────┴─────────────────────────────────────────────────────────────────┘
```

#### csv

```csv
domain,username,cracked,cracked_password,ntlm_hash,start_date,finished_at,time_taken_seconds,password_length,password_patterns
local.dk,user1,True,Password1!,5f4dcc3b5aa765d61d8327deb882cf99,2025-09-02 10:39:43,2025-09-02 10:41:53,130,10,"['dictionary_word', 'ends_with_symbol']"
```

#### json

```json
[
  {
    "domain": "local.dk",
    "username": "user1",
    "cracked": true,
    "cracked_password": "Password1!",
    "ntlm_hash": "5f4dcc3b5aa765d61d8327deb882cf99",
    "start_date": "2025-09-02 10:39:43",
    "finished_at": "2025-09-02 10:41:53",
    "time_taken_seconds": 130,
    "password_length": 10,
    "password_patterns": ["dictionary_word", "ends_with_symbol"]
  }
]
```
