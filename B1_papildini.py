# ----------------------------------------------------------------------
# B1. Python — rindu skaits pa līmeņiem
# ----------------------------------------------------------------------

# Saskaiti, cik žurnālā ir rindu katram līmenim, un izvadi tos no biežākā uz retāko. Aizpildi abas vietas, kur stāv TODO.
#
# Aizpildi vietu, kur stāv TODO. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Pirms saraksta izvadi tekstu "Limenu kopsavilkums".

skaits = {}

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        limenis = rinda.split()[2]
        # TODO: pieskaiti vienu šim līmenim

# TODO: izvadi sakārtotus no lielākā uz mazāko
