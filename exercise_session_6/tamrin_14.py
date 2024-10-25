import csv


file_path = input("Adres file CSV ra vared konid: ")


total_cost = 0

try:
  
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        print(f"{'Date':<15}{'Description':<20}{'Cost':<10}")
        print("-" * 45)
        
       
        for row in reader:
            date = row['date']
            description = row['description']
            cost = int(row['cost'])
            total_cost += cost
            print(f"{date:<15}{description:<20}{cost:<10}")
        
        print("=" * 45)
        print(f"Total Cost: {total_cost}")
    
except FileNotFoundError:
    print("File mored nazar yaft nashod! Lotfan yek adres mo'tabar vared konid.")
except Exception as e:
    print(f"Khataei rokh dade: {e}")

