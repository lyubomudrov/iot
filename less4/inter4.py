import tkinter as tk

def showData():
    entered_text = entry.get()
    message = f"Привет, {entered_text}!"
    new_window = tk.Toplevel(root)
    new_window.title("Введенные данные")
    label = tk.Label(new_window, text=message)
    label.pack()

# Создаем главное окно
root = tk.Tk()
root.title("Мое окно")

# Создаем виджет Entry
entry = tk.Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
entry.insert(0, "")
entry.pack(pady=20)

# Создаем кнопку с обработчиком showData
button = tk.Button(root, text="Показать данные", bg="white", fg="blue", command=showData)
button.pack()

# Запускаем главный цикл обработки событий
root.mainloop()
