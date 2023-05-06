import sys
import csv
import os
import colorama


notes = []
try:
    if sys.argv[1] == "--create":

        title = input("To write a title: ")
        contend = input("To write content: ")
        name = input("Who is sends the notes: ")

        notes.append({
            'title': title,
            'contend': contend,
            'name': name
        })
        file_validation = os.path.isfile('saved_notes.csv')
        with open("saved_notes.csv", 'a', newline='', encoding="utf-8") as saved_notes:
            header = ['title', 'contend', 'name']
            writter = csv.DictWriter(saved_notes, fieldnames=header)
            if not file_validation or saved_notes.tell() == 0:
                writter.writeheader()

            for note in notes:
                writter.writerow(note)

    
except IndexError as error_message:
    print(error_message)
    print("you must add some of the arguments")
    print("delete")
    print("update")
    print("create")
    print("read")

if sys.argv[1] == "--read":
    with open("saved_notes.csv","r",encoding="utf-8")as saved_notes:
        header = ['title', 'contend', 'name']
        field_reader=csv.DictReader(saved_notes,fieldnames=header)
        next(field_reader)
        for note in field_reader:
            print(colorama.Fore.GREEN + f'title: {note["title"]}')
            print(colorama.Fore.LIGHTMAGENTA_EX + f'contend: {note["contend"]}')
            print("print innecesario")
