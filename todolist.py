from argparse import RawTextHelpFormatter
import tkinter 
import tkinter.messagebox
import pickle


root = tkinter.Tk()
root.config(bg='#009dc4')
root.title("To Do List")
root.resizable(width=False, height=False)

def add_new_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Enter Task.")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You Must Select A Task.")


def load_tasks():
    try:
        tasks = pickle.load(open("ToDoListTasksFile.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find ToDoListTasksFile.dat .")
def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("ToDoListTasksFile.dat", "wb"))

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=29, width=50, bg="#87CEEB")
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=40, bg='#8a7aac')
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add New Task", width=25, bg='#acace6', command=add_new_task)
button_add_task.pack()

button_save_tasks = tkinter.Button(root, text="Save", width=25, bg='#330066', command=save_tasks)
button_save_tasks.pack()

button_load_tasks = tkinter.Button(root, text="Load", width=25, bg='#48929b', command=load_tasks)
button_load_tasks.pack()

button_delete_task = tkinter.Button(root, text="Delete", width=25, bg='#ff80ff', command=delete_task)
button_delete_task.pack()


root.mainloop()