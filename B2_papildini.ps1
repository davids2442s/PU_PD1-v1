# ----------------------------------------------------------------------
# B2. PowerShell — apturētie servisi failā
# ----------------------------------------------------------------------

# Saglabā apturētos servisus CSV failā apturetie.csv, ko var atvērt Excel. Aizpildi vietu, kur stāv TODO.
#
# Aizpildi vietu, kur stāv TODO. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Pēc saglabāšanas izvadi Write-Host rindu "Fails gatavs".

$apturetie = Get-Service |
    Where-Object { $_.Status -eq "Stopped" } |
    Sort-Object Name |
    Select-Object Name, Status

$apturetie | Export-Csv -Path "apturetie.csv" -NoTypeInformation -Encoding UTF8
Write-Host "done"

