# ----------------------------------------------------------------------
# A2. PowerShell — servisi, kas darbojas
# ----------------------------------------------------------------------

# Jāizvada servisi, kuru statuss ir Running. Skripts nekā neizvada. Atrodi un salabo kļūdu.
#
# Atrodi un salabo. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Rezultātam pievieno arī kolonnu DisplayName.

Get-Service |
    Where-Object { $_.Status -eq "Running" } |
    Sort-Object Name |
    Select-Object Name, Status
