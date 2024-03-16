import tkinter as tk

# Создаем главное окно
root = tk.Tk()

# Создаем виджет Label с текстом "Hello World!"
label = tk.Label(root, text="Hello World!", fg="blue", bg="red")

# Размещаем виджет с помощью метода pack()
label.pack()

# Запускаем главный цикл обработки событий
root.mainloop()
