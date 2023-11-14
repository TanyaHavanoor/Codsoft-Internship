#TO_DO LIST

from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    
w = Tk()
w.geometry('700x550+500+200')
w.title('To-do List')
w.config(bg='violet red')
w.resizable(width=False, height=False)

frame = Frame(w)
frame.pack(padx=10)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=50,
    height=10,
    font=('Times', 18),
    bd=0,
    fg='black',
    highlightthickness=0,
    selectbackground='floral white',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = ['Learn a new language','Learn how to bake']

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    w,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(w)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='bisque',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='bisque',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


w.mainloop()
