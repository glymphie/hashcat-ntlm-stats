# Crack passwords with Hashcat

## Prerequisites:
- Get a big password list e.g.: [weakpass_4.txt](https://weakpass.com/wordlists/weakpass_4.txt)
- Get a ruleset e.g.: [Optimised hashcat Rule](https://github.com/stealthsploit/Optimised-hashcat-Rule)

## Use Hashcat to crack passwords

If you are using a GPU, find your devices (GPU):
```sh
hashcat -I
```

### Run Hashcat with a wordlist

This is a good baseline run. It attempts to crack the NTLM hashes using words
directly from the selected wordlist.
```sh
hashcat -m 1000 -d 1 user-hashes.txt wordlist.txt --status --status-timer 10 | tee hashcat-output.txt
```

This command:
- Uses hash mode `1000` for NTLM
- Uses device `1`
- Reads hashes from `user-hashes-no-machines.txt`
- Uses `wordlist.txt` as the candidate password list
- Prints Hashcat status every 10 seconds
- Writes the status output to `hashcat-output.txt` while also showing it in the terminal

The status log is used later to estimate when each password was cracked.

### Run Hashcat with a wordlist and ruleset

This is a more thorough run. Hashcat uses the wordlist as a base and applies
rules to generate password variations, such as appended numbers, changed
casing, or added symbols.
```sh
hashcat -m 1000 -w 4 -O -d 1 user-hashes.txt -r OneRuleToRuleThemAll.rule wordlist.txt --status --status-timer 10 | tee hashcat-output-with-rules.txt
```

This command:
- Uses hash mode `1000` for NTLM
- Uses workload profile `4`, which is aggressive and may make the system less responsive
- Enables optimized kernels with `-O`
- Uses device `1`
- Reads hashes from `user-hashes-no-machines.txt`
- Applies the rule file `OneRuleToRuleThemAll.rule`
- Uses `wordlist.txt` as the base wordlist
- Prints Hashcat status every 10 seconds
- Writes the status output to `hashcat-output-with-rules.txt` while also showing it in the terminal

The status log is used later to estimate when each password was cracked.
