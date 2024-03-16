import tkinter as tk

# Создание окна
root = tk.Tk()
root.title("Пример grid")

# Создание виджета Label c надписью "Hello World"
label1 = tk.Label(root, text="Hello World", bg="red", fg="white")
label1.grid(row=0, column=0, sticky='nsew')

# Создание виджета Label c надписью "Меня зовут Имя Фамилия"
label2 = tk.Label(root, text="Меня зовут Лебедев Денис", bg="red", fg="white")
label2.grid(row=1, column=1, sticky='nsew')

# Задаем стиль для рамки и расстояние между столбцами и строками
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(1, weight=2)

# Запуск цикла обработки событий
root.mainloop()
