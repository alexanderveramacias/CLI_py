import sys
import csv

notes=[]
try:
    if sys.argv[1]=="--create":

        title=input("To write a title: ")
        contend=input("To write content: ")
        name=input("Who is sends the notes: ")

        notes.append({
            'title':title,
            'contend':contend,
            'name':name
        })
        print(notes)
        with open("saved_notes.csv",'w',newline='') as saved_notes:
            header=['title','contend','name']
            writter=csv.DictWriter(saved_notes,fieldnames=header)


            for note in notes:
                writter.writerow(note)

    else: 
        print("create was not executed")
except IndexError as error_message:
    print(error_message)
    print("you must add some of the arguments")
    print("delete")
    print("update")
    print("create")
    print("read")