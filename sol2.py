# Сол2: Приложение с едой

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# Функция для добавления еды в корзину
def add_to_cart(item):
    cart.append(item)
    messagebox.showinfo("Успех", f"{item} добавлен в корзину!")

# Функция для отображения корзины
def view_cart():
    cart_frame.grid_forget()
    cart_list = "\n".join(cart)
    cart_label.config(text=f"Ваши заказы:\n{cart_list}")
    cart_frame.grid(row=0, column=1, padx=20, pady=10)

# Создаем основное окно
root = Tk()
root.title("Приложение с едой")
root.geometry("600x400")
root.configure(bg="#f8f8f8")  # Задаем цвет фона

cart = []

# Фрейм для меню еды
menu_frame = Frame(root, bg="#74b9ff")
menu_frame.grid(row=0, column=0, padx=10, pady=10)

Label(menu_frame, text="Меню:", font=("Arial", 16), bg="#74b9ff", fg="white").grid(row=0, column=0, pady=10)

# Добавление картинок еды
pizza_image = ImageTk.PhotoImage(Image.open("pizza.jpg").resize((100, 100)))
burger_image = ImageTk.PhotoImage(Image.open("burger.jpg").resize((100, 100)))
sushi_image = ImageTk.PhotoImage(Image.open("sushi.jpg").resize((100, 100)))

# Кнопки для заказа еды
Button(menu_frame, text="Пицца", image=pizza_image, compound=TOP, command=lambda: add_to_cart("Пицца")).grid(row=1, column=0, pady=10)
Button(menu_frame, text="Бургер", image=burger_image, compound=TOP, command=lambda: add_to_cart("Бургер")).grid(row=1, column=1, pady=10)
Button(menu_frame, text="Суши", image=sushi_image, compound=TOP, command=lambda: add_to_cart("Суши")).grid(row=1, column=2, pady=10)

# Кнопка для просмотра корзины
Button(menu_frame, text="Посмотреть корзину", command=view_cart, bg="#00b894", fg="white").grid(row=2, column=0, columnspan=3, pady=20)

# Фрейм для отображения корзины
cart_frame = Frame(root, bg="#a29bfe")
cart_label = Label(cart_frame, text="Ваша корзина пуста", bg="#a29bfe", fg="white", font=("Arial", 12))
cart_label.grid(row=0, column=0, pady=10)

# Запуск программы
root.mainloop()
