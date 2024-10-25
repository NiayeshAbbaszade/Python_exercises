print("addres file .txt ra dar ghesmat paeen bayad vared konid.")
print("~" * 40)

content = ""  

while True:
    try:
        index_text = input("address file ra vared konid : ")
        with open(index_text, "r", encoding='utf-8') as file_txt:
            content = file_txt.read()
            break
    except FileNotFoundError:
        print("[ lotfan addres file ra vared konid ! ]")

print("=-" * 30 + "=")

def kalame_shomar(matn):
    kalamat = 0
    kalame_kon = matn.split()
    for ch in kalame_kon:
        kalamat += 1
    return kalamat

def khat_shomar(matn):
    khat_ha = matn.count('\n') + 1
    return khat_ha

def Kalame_Yaab(matn, kalame):
    Number_kalame_yaab = matn.split().count(kalame)
    return Number_kalame_yaab

print("kalame iy ke mikhahid dar matn peyda konid ra dar paeen vared konid.")
print("~" * 40)

while True:
    kalame_yaab = input("kalame morede nazar ra vared konid : ")
    kalame_kon2 = kalame_yaab.split()
    if len(kalame_kon2) >= 2:
        print("faghar yek kalame vared konid!")
        continue
    else:
        break

output = Kalame_Yaab(content, kalame_yaab)

with open("report.txt", "w", encoding='utf-8') as report:
    report.write("=" * 40 + "\n")
    report.write(f"tadad kalamat : {kalame_shomar(content)}\n")
    report.write(f"tedad khat ha : {khat_shomar(content)}\n")
    if output == 0:
        report.write("[ kalame morede nazar yaft nashod! ]\n")
    else:
        report.write(f"Tedad Kalame morede nazar : {Kalame_Yaab(content, kalame_yaab)}\n")
    report.write("=" * 40 + "\n")

with open("report.txt", "r", encoding='utf-8') as report1:
    print(report1.read())
