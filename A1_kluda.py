# ----------------------------------------------------------------------
# A1. Python — CRITICAL rindu skaits
# ----------------------------------------------------------------------

# Jāsaskaita, cik žurnālā ir CRITICAL rindu. Izvadās nulle, lai gan tādas rindas failā ir. Atrodi un salabo kļūdu.
#
# Atrodi un salabo. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Rezultātu izvadi ar tekstu "Kopā:" pirms skaitļa.

skaits = 0

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        if "CRITICAL" in rinda:
            skaits = skaits + 1

print("Kopā:", skaits)
