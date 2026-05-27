# Extract hashes from NTDS.dit
Use [impacket/secretsdump](https://github.com/fortra/impacket/blob/master/examples/secretsdump.py)
to extract the hashes. Use the `LOCAL` option to use it on a retrieved NTDS.dit.

```sh
secretsdump.py -system /path/to/SYSTEM -ntds /path/to/NTDS.dit -outputfile /path/to/user-hashes.txt LOCAL
```

You can also get the password history for all accounts, for some password history analysis:

```sh
secretsdump.py -system /path/to/SYSTEM -ntds /path/to/NTDS.dit -outputfile /path/to/user-hashes-history.txt -history LOCAL
```

Machine accounts have long random passwords and are virtually impossible to crack.
To filter out machine accounts:

```sh
grep -v "$:" user-hashes.txt > user-hashes-no-machines.txt
```
