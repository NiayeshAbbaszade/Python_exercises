def main():

    file_path = input("Lotfan adres file matan ra vared konid: ")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        word_count = len(text.split())
        line_count = len(text.splitlines())


        search_word = input("Lotfan kalamei ke mikhahid tedad an ra biabid vared konid: ")
        word_occurrences = text.count(search_word)

        with open('report.txt', 'w', encoding='utf-8') as report_file:
            report_file.write(f"Tedad kol kalamat: {word_count}\n")
            report_file.write(f"Tedad kol khat-ha: {line_count}\n")
            report_file.write(f"Tedad voghu kalame '{search_word}': {word_occurrences}\n")

        with open('report.txt', 'r', encoding='utf-8') as report_file:
            report_content = report_file.read()
            print("\nMohtavaye file gozaresh:")
            print(report_content)

    except FileNotFoundError:
        print("File mored nazar yaft nashod. Lotfan adres sahih ra vared konid.")
    main()