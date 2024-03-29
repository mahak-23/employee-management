import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="organization")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO  registration (Employee_ID,Employee_Name,Phone_No,Salary) VALUES (%s, %s, %s, %s)"
        val = (studid, studname, coursename, feee)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Employee inserted successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="organization")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update  registration set Employee_Name= %s,Phone_No= %s,Salary= %s where Employee_ID= %s"
        val = (studname, coursename, feee, studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Updateddddd successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    studid = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="organization")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from registration where Employee_ID = %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Deleteeeee successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="organization")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT Employee_ID,Employee_Name,Phone_No,Salary FROM registration")
    records = mycursor.fetchall()
    if len(records) >= 0:
        listBox.delete(*listBox.get_children())
        for row in records:
            listBox.insert("", END, values=row)
            mysqldb.close()


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['employee_ID'])
    e2.insert(0, select['employee_Name'])
    e3.insert(0, select['phone_No'])
    e4.insert(0, select['salary'])


root = Tk()
root.geometry("900x550+300+0")
global e1
global e2
global e3
global e4
MFrame = Frame(root, bd=10, width=770, height=700, relief=RIDGE, bg='lavender')
MFrame.grid()
TFrame = Frame(MFrame, bd=7, width=770, height=100, relief=RIDGE)
TFrame.grid(row=0, column=0)
TopFrame = Frame(MFrame, bd=5, width=770, height=500, relief=RIDGE)
TopFrame.grid(row=1, column=0)
LFrame = Frame(TopFrame, bd=5, width=770, height=400, padx=2, relief=RIDGE)
LFrame.pack(side=LEFT)
LFrame1 = Frame(LFrame, bd=5, width=600, height=180, padx=2, pady=4, relief=RIDGE)
LFrame1.pack(side=TOP, padx=0, pady=0)
RFrame = Frame(TopFrame, bd=5, width=100, height=400, padx=2, relief=RIDGE)
RFrame.pack(side=RIGHT)
RFrame1 = Frame(RFrame, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
RFrame1.pack(side=TOP)
l = Label(TFrame, text="Employee Registration", fg="blue", font=('arial', 40, 'bold'), bd=7)
l.grid(row=0, column=0, padx=132)
Eid = Label(LFrame1, text="Employee_ID", fg="purple", font=('arial', 12, 'italic', 'bold'))
Eid.grid(row=1, column=0, padx=5, sticky=W)
Ename = Label(LFrame1, text="Employee_Name", fg="purple", font=('arial', 12, 'bold', 'italic'))
Ename.grid(row=2, column=0, padx=5, sticky=W)
Ep = Label(LFrame1, text="Phone_No", fg="purple", font=('arial', 12, 'bold', 'italic'))
Ep.grid(row=3, column=0, padx=5, sticky=W)
Es = Label(LFrame1, text="Salary", fg="purple", font=('arial', 12, 'italic', 'bold'))
Es.grid(row=4, column=0, padx=5, sticky=W)
e1 = Entry(LFrame1, font=('arial', 12), width=44, bd=5)
e1.grid(row=1, column=1, sticky=W, padx=5)

e2 = Entry(LFrame1, font=('arial', 12), width=44, bd=5)
e2.grid(row=2, column=1, sticky=W, padx=5, )

e3 = Entry(LFrame1, font=('arial', 12), width=44, bd=5)
e3.grid(row=3, column=1, sticky=W, padx=5)

e4 = Entry(LFrame1, font=('arial', 12), width=44, bd=5)
e4.grid(row=4, column=1, sticky=W, padx=5)

Button(RFrame1, text="ADD", font=('arial', 12, 'bold'), fg="indigo", command=Add, bd=4, pady=1, padx=24, height=3,
       width=13).grid(row=0, column=0, padx=1)
Button(RFrame1, text="UPDATE", font=('arial', 12, 'bold'), fg="indigo", command=update, bd=4, pady=1, padx=24, height=3,
       width=13).grid(row=1, column=0, padx=1)
Button(RFrame1, text="DELETE", font=('arial', 12, 'bold'), fg="indigo", command=delete, bd=4, pady=1, padx=24, height=3,
       width=13).grid(row=2, column=0, padx=1)
Button(RFrame1, text="SHOW", font=('arial', 12, 'bold'), fg="indigo", command=show, bd=4, pady=1, padx=24, height=3,
       width=13).grid(row=3, column=0, padx=1)
s_y = Scrollbar(LFrame, orient=VERTICAL)
listBox = ttk.Treeview(LFrame, height=12, columns=('employee_ID', 'employee_Name', 'phone_No', 'salary'),
                       yscrollcommand=s_y.set)
s_y.pack(side=RIGHT, fill=Y)
listBox.heading('employee_ID', text='Employee_ID')
listBox.heading('employee_Name', text='Employee_Name')
listBox.heading('phone_No', text='Phone_No')
listBox.heading('salary', text='Salary')
listBox['show'] = 'headings'
listBox.column('employee_ID', width=10)
listBox.column('employee_Name', width=10)
listBox.column('phone_No', width=10)
listBox.column('salary', width=10)
listBox.pack(fill=BOTH, expand=1)

show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()
