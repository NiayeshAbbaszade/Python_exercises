import xml.etree.ElementTree as ET


file_path = input("Adres file XML ra vared konid: ")

try:
    tree = ET.parse(file_path)
    root = tree.getroot()

   
    for task in root.findall('Task'):
        title = task.find('Title').text
        due_date = task.find('DueDate').text
        print(f"Title: {title}")
        print(f"Date: {due_date}")
        print("-" * 40)  

except FileNotFoundError:
    print("File mored nazar yaft nashod! Lotfan yek adres mo'tabar vared konid.")
except ET.ParseError:
    print("Khata dar tajziye file XML! Lotfan yek file XML mo'tabar vared konid.")
