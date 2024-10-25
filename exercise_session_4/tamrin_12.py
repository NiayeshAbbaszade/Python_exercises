import json

def create_company_intro(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    sector = data['sector']
    employees = data['fullTimeEmployees']
    summary = data['longBusinessSummary']
    city = data['city']
    country = data['country']
    phone = data['phone']

    intro_text = (
        f"Company: Apple Inc.\n"
        f"Sector: {sector}\n"
        f"Full Time Employees: {employees}\n"
        f"Location: {city}, {country}\n"
        f"Phone: {phone}\n\n"
        f"Introduction:\n{summary}\n"
    )

    print(intro_text)

file_path = input('adres_file_ra_vared_konid')
create_company_intro(file_path)