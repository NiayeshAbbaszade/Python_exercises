karid_ha = {}
num_karid = int(input("Tedad kharidha ra vared konid: "))
for _ in range(num_karid):
    kala = input("Noe kharid ra vared konid: ")
    meghdar = float(input("Mablagh kharid ra vared konid: "))
    if kala in karid_ha:
        karid_ha[kala] += meghdar
    else:
        karid_ha[kala] = meghdar
kol_hazine = sum(karid_ha.values())
budge = float(input("Bodje mahiane ra vared konid: "))
if kol_hazine > budge:
    print("Hoshdar: Majmooe hazineha bishtar az bodje ast!")
else:
    print("Majmooe hazineha dar mahdode bodje ast.")