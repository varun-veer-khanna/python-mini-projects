#Program to write into a .CSV file from a Tkinter based GUI
from tkinter import *
from tkinter import ttk
import csv

class Contact:

    def __init__(self, root):

        root.title("Contact Management ")

        mainframe = ttk.Frame(root, padding="100 100 150 150")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        
       
        self.name = StringVar()
        name_entry = ttk.Entry(mainframe, width=7, textvariable=self.name)
        name_entry.grid(column=2, row=1, sticky=(W, E))
        
        self.number = StringVar()
        number_entry = ttk.Entry(mainframe, width=7, textvariable=self.number)
        number_entry.grid(column=2, row=2, sticky=(W, E))
        #ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Add", command=self.add).grid(column=2, row=4, sticky=W)

        self.email = StringVar()
        email_entry = ttk.Entry(mainframe, width=7, textvariable=self.email)
        email_entry.grid(column=2, row=3, sticky=(W, E))

        ttk.Label(mainframe, text="Name").grid(column=1, row=1, sticky=E)
        ttk.Label(mainframe, text="Number").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="E-mail").grid(column=1, row=3, sticky=E)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        #feet_entry.focus()
        root.bind("<Return>", self.add)
        
    def add(self, *args):
        try:
            conname=self.name.get()
            connumber=self.number.get()
            conmail=self.email.get()
            
            with open('contacts.csv', 'a', newline='') as file:
                writer = csv.writer(file)
        
                #writer.writerow(["name", "number", "email"])
                writer.writerow([conname, connumber, conmail])
                        

            #mycursor = mydb.cursor()
            #mycursor.execute("CREATE TABLE contacts (conname varchar(255), connumber int, conmail varchar(255))")
            #mycursor.execute("CREATE DATABASE contactbase")
            #value = float(self.feet.get())
            #self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass

root = Tk()
Contact(root)
root.mainloop()
