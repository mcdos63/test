from tkinter import *

def add_task():
    task = task_entry.get() # здесь мы получаем слова из поля для ввода
    if task:
        task_listBox.insert(END, task) # здесь с помощью константы END вставляем полученное слово в конец списка
        task_entry.delete(0, END) # здесь очищаем поле для ввода, от нулевого индекса и до конца

def delete_task():
    selected_task = task_listBox.curselection() # с помощью функции **curselection** элемент, на который мы нажмём, будет передавать свой ID, индекс, в переменную  selected_task
    if selected_task:
        task_listBox.delete(selected_task) # удаляем выбранный элемент из списка

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="DarkViolet")  # с помощью функции **itemconfig** выполненная задача изменит цвет заливки


root = Tk()
root.title("Простейшее приложение")
root.geometry("470x500")

ph = PhotoImage(file='Monogram3.png')
ph1 = Label(root, image=ph)
ph1.place(x=5, y=5)

text1 = Label(root, text="Введите вашу задачу:", font='ArialBold 14 bold', fg='DarkViolet')
text1.place(x=40, y=3)

task_entry = Entry(root, width=50, bg="grey19", fg='White', font='Arial 12', cursor='xterm')
task_entry.place(x=5, y=30)

button1 = Button(text=f"Добавить \nзадачу",width=19, wraplength=150, activeforeground='White', activebackground='DarkViolet', command=add_task)
button2 = Button(text=f"Удалить \nзадачу",width=19, wraplength=150, activeforeground='White', activebackground='DarkViolet', command=delete_task)
button3 = Button(text="Отметить выполненную задачу",width=19, wraplength=150, activeforeground='White', activebackground='DarkViolet', command=mark_task)

button1.place(x=5, y=60)
button2.place(x=155, y=60)
button3.place(x=305, y=60)

task_listBox = Listbox(root, height=10, width=50, bg="grey19", fg='White', font='Arial 12')
task_listBox.place(x=5, y=110)

if __name__  == '__main__':
    try:
        print('Приложение работает')
        root.mainloop()
    except KeyboardInterrupt:
        print('Выход из приложения!')