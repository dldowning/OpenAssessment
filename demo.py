from tkinter import *
import mysql.connector
from mysql.connector import Error

#this is just a test change

def put():


    connection = mysql.connector.connect(host='localhost',
                                         database='Assessment',
                                         user='root',
                                         password='T.srsdv123')

    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO quests (q_id,Label,quest,op_1,op_2,op_3,op_4,ans) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        (quest_id.get(), L_name.get(), question.get(), option_1.get(), option_2.get(), option_3.get(), option_4.get(),
        ans.get()))

    cursor.close()
    connection.commit()
    connection.close()
    status.set("data added successfully")


master = Tk()

global quest_id, L_name, question, option_1, option_2, option_3, option_4, ans

quest_id = IntVar()
L_name = StringVar()
question = StringVar()
option_1 = StringVar()
option_2 = StringVar()
option_3 = StringVar()
option_4 = StringVar()
ans = StringVar()
status = StringVar()

Label(master, text='question_id').grid(row=0, column=0)
Label(master, text='Label_name').grid(row=1, column=0)
Label(master, text='question').grid(row=2, column=0)
Label(master, text='option_1').grid(row=3, column=0)
Label(master, text='option_2').grid(row=4, column=0)
Label(master, text='option_3').grid(row=5, column=0)
Label(master, text='option_4').grid(row=6, column=0)
Label(master, text='answer').grid(row=7, column=0)
Label(master, text='', textvariable=status).grid(row=9, columnspan=2)

Entry(master, textvariable=quest_id).grid(row=0, column=1)
Entry(master, textvariable=L_name).grid(row=1, column=1)
Entry(master, textvariable=question).grid(row=2, column=1)
Entry(master, textvariable=option_1).grid(row=3, column=1)
Entry(master, textvariable=option_2).grid(row=4, column=1)
Entry(master, textvariable=option_3).grid(row=5, column=1)
Entry(master, textvariable=option_4).grid(row=6, column=1)
Entry(master, textvariable=ans).grid(row=7, column=1)

Button(master, text='Submit', command=put).grid(row=8, columnspan=2)

mainloop()

