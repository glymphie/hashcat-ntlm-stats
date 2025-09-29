# Overview

[![Tests](https://github.com/glymphie/hashcat-ntlm-stats/actions/workflows/tests.yml/badge.svg)](https://github.com/glymphie/hashcat-ntlm-stats/actions/workflows/tests.yml)

This project is

You have 3 files:

- The file with all the hashes and the related cracked passwords
- The file with all the users and their hashes
- The log file with the status

You want to relate the hashes from the userfile to the cracked passwords to
get the user and their password. And you also want to know how long it took to
crack the password.

Output example:

```
[domain]\[username],[cracked_password],[password_NTLM_hash],[date],[time_taken]
local.dk\user1,sommer123!,8846f7eaee8fb117ad06bdd830b7586c,05-09-2025,00:00:10
```
