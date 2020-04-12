from tkinter import *
from tkinter import messagebox


def insert_red(event):
    number_of_red = red_input.get()
    try:
        if (int(number_of_red) >= 0) and (int(number_of_red) <= 250):
            red_frame['bg'] = get_rgc(int(number_of_red), 0, 0)

        elif int(number_of_red) > 250:
            too_much()

        else:
            too_few()
    except ValueError:
        value_error()


def insert_green(event):
    number_of_green = green_input.get()
    try:
        if (int(number_of_green) >= 0) and (int(number_of_green) <= 250):
            green_frame['bg'] = get_rgc(0, int(number_of_green), 0)

        elif int(number_of_green) > 250:
            too_much()

        else:
            too_few()
    except ValueError:
        value_error()


def insert_blue(event):
    number_of_blue = blue_input.get()
    try:
        if (int(number_of_blue) >= 0) and (int(number_of_blue) <= 250):
            blue_frame['bg'] = get_rgc(0, 0, int(number_of_blue))

        elif int(number_of_blue) > 250:
            too_much()

        else:
            too_few()
    except ValueError:
        value_error()


def insert_rgb(event):
    number_of_red = int(red_input.get())
    number_of_green = int(green_input.get())
    number_of_blue = int(blue_input.get())
    rgb_frame['bg'] = get_rgc(number_of_red, number_of_green, number_of_blue)


def exit_app():
    root.destroy()


def reset_app():
    red_frame['bg'] = get_rgc(255, 255, 255)
    green_frame['bg'] = get_rgc(255, 255, 255)
    blue_frame['bg'] = get_rgc(255, 255, 255)
    rgb_frame['bg'] = get_rgc(255, 255, 255)


def get_rgc(r, g, b):
    rgb = '#%02x%02x%02x' % (r, g, b)
    return rgb


def too_much():
    messagebox.showerror('wrong value', 'too much')


def too_few():
    messagebox.showerror('wrong value', 'too_few')


def value_error():
    messagebox.showerror('wrong value', 'enter the number instead of string')


root = Tk()
root.title("Color generation")
main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Color', menu=first_item)
first_item.add_command(label="Reset", command=reset_app)
first_item.add_command(label="Exit", command=exit_app)

red_frame = Frame(root, width=300, heigh=100, bg='white', borderwidth=1, relief='groove')
red_input = Entry(root)
red_button = Button(root, text='Red', fg='red', borderwidth=1, relief='ridge')
red_frame.grid(row=0, column=1, padx=20, pady=20)
red_input.grid(row=1, column=1)
red_button.grid(row=2, column=1, pady=10)
red_button.bind('<Button-1>', insert_red)

green_frame = Frame(root, width=300, height=100, bg='white', borderwidth=1, relief='groove')
green_input = Entry(root)
green_button = Button(root, text='Green', fg='green', borderwidth=1, relief='ridge')
green_frame.grid(row=0, column=2, padx=20, pady=20)
green_input.grid(row=1, column=2)
green_button.grid(row=2, column=2, pady=10)
green_button.bind('<Button-1>', insert_green)

blue_frame = Frame(root, width=300, height=100, bg='white', borderwidth=1, relief='groove')
blue_input = Entry(root)
blue_button = Button(root, text='Blue', fg='blue', borderwidth=1, relief='ridge')
blue_frame.grid(row=0, column=3, padx=20, pady=20)
blue_input.grid(row=1, column=3)
blue_button.grid(row=2, column=3, pady=10)
blue_button.bind('<Button-1>', insert_blue)

rgb_frame = Frame(root, width=300, height=100, bg='white', borderwidth=1, relief='groove')
rgb_button = Button(root, text='RGB', borderwidth=1, relief='ridge')
rgb_frame.grid(row=3, column=2, padx=20)
rgb_button.grid(row=5, column=2, pady=10)
rgb_button.bind('<Button-1>', insert_rgb)

root.mainloop()
