# Getting the NTDS.dit file and SYSTEM hive for extracting password hashes
<div align="center">
  **This should be done by an authorized domain admin user account!**
</div>

> [!NOTE]
> Make sure you know where the NTDS database is located. It might not be the C: drive!
> This Location is used throughout this extraction.


```cmd
reg query HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Parameters /v "DSA Database file"
```


## Make the shadow copy
Login to the Domain controller and open cmd.

Create a shadow copy of Windows.
```cmd
vssadmin create shadow /for=C:
```

This will create a shadow copy of the Windows folder and provide a ID and Volume Name.

Take note of these:
- Shadow Copy ID
- Shadow Copy Volume Name

Copy the NTDS.dit to a different location:
```cmd
copy {SHADOW COPY VOLUME NAME}\Windows\NTDS\NTDS.dit C:\path\of\your\choice\ntds.dit
```

Copy the SYSTEM hive file to a different location:
```cmd
copy {SHADOW COPY VOLUME NAME}\Windows\System32\config\SYSTEM C:\path\of\your\choice\SYSTEM
```

Remember to delete the shadow copy!
```cmd
vssadmin delete shadows /shadow={{SHADOW COPY ID}}
```
