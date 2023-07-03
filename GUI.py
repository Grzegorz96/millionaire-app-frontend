from tkinter import *
import datetime
import Config
import Functions
from Functions import draw_question


def init_main_window():
    root = Tk()
    window_width = 500
    window_height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root.title("MILLIONAIRE.APP")
    root.resizable(width=True, height=True)
    root.config(bg="#B0C4DE")
    root.call("wm", "iconphoto", root._w, PhotoImage(file="millionaire_icon.png"))
    return root


# Initialization time label
def init_date(root):
    time_label = Label(root, width=71)
    time_label.pack()
    # Starting update date
    update_date(root, time_label)


# Updating date
def update_date(root, time_label):
    # assignment new date and time from now to variables
    date = f"{datetime.datetime.now().date()}"
    time = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"
    # Config time_label for new data
    time_label.config(text=f"{date} {time}")
    # Recursion of function after 1s
    root.after(1000, update_date, root, time_label)


def init_authentication_label(root):
    if isinstance(Config.current_page, Label):
        Config.current_page.destroy()

    Config.photo = PhotoImage(file="background_start.png")
    login_label = Label(root, width=500, height=700, image=Config.photo)
    login_label.pack()
    Label(login_label, text="MILIONERZY",font=("Arial", 35), bg="#A9A9A9").place(x=100, y=150)
    Button(login_label, text="Zaloguj się", width=30, bg="#A9A9A9",
           command=lambda: init_login_window()).place(x=135, y=500)
    Button(login_label, text="Nie masz konta? Zarejestruj sie", width=30, bg="#A9A9A9",
           command=lambda: init_register_window()).place(x=135, y=530)
    Button(login_label, text="Kontynuuj jako gość", width=30, bg="#A9A9A9",
           command=lambda: init_start_label(root)).place(x=135, y=560)
    Config.current_page = login_label


def init_start_label(root):
    Config.current_page.destroy()
    Config.photo = PhotoImage(file="background_start.png")
    start_label = Label(root, width=500, height=700, image=Config.photo)
    start_label.pack()
    Label(start_label, text="MILIONERZY", font=("Arial", 35), bg="#A9A9A9").place(x=100, y=150)
    Button(start_label, text="Nowa gra", width=30, bg="#A9A9A9",
           command=lambda: init_game_label(root)).place(x=135, y=500)
    Button(start_label, text="Najlepsze wyniki", width=30, bg="#A9A9A9").place(x=135, y=530)
    Button(start_label, text="Cofnij", width=30, bg="#A9A9A9",
           command=lambda: init_authentication_label(root)).place(x=135, y=560)
    Config.current_page = start_label


def init_login_window():
    login_window = Toplevel()
    login_window_width = 300
    login_window_height = 150
    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()
    center_x = int(screen_width / 2 - login_window_width / 2)
    center_y = int(screen_height / 2 - login_window_height / 2)
    login_window.geometry(f"{login_window_width}x{login_window_height}+{center_x}+{center_y}")
    login_window.title("Logowanie")
    login_window.resizable(width=True, height=True)
    login_window.config(bg="#B0C4DE")
    login_icon = PhotoImage(file="login.png")
    login_window.wm_iconphoto(False, login_icon)

    Label(login_window, text="Logowanie", font=("Arial", 13), width=33).place(x=0, y=10)

    Label(login_window, text="Login", width=7).place(x=235, y=50)
    login_entry = Entry(login_window, width=30, font=("Arial", 10))
    login_entry.place(x=10, y=50)

    Label(login_window, text="Hasło", width=7).place(x=235, y=80)
    password_entry = Entry(login_window, width=30, font=("Arial", 10))
    password_entry.place(x=10, y=80)

    Button(login_window, text="Zaloguj", width=8).place(x=225, y=110)


def init_register_window():
    register_window = Toplevel()
    register_window_width = 300
    register_window_height = 240
    screen_width = register_window.winfo_screenwidth()
    screen_height = register_window.winfo_screenheight()
    center_x = int(screen_width / 2 - register_window_width / 2)
    center_y = int(screen_height / 2 - register_window_height / 2)
    register_window.geometry(f"{register_window_width}x{register_window_height}+{center_x}+{center_y}")
    register_window.title("Rejestracja")
    register_window.resizable(width=True, height=True)
    register_window.config(bg="#B0C4DE")
    login_icon = PhotoImage(file="login.png")
    register_window.wm_iconphoto(False, login_icon)

    Label(register_window, text="Tworzenie konta", font=("Arial", 13), width=33).place(x=0, y=10)

    Label(register_window, text="Imie", width=7).place(x=235, y=50)
    login_entry = Entry(register_window, width=30, font=("Arial", 10))
    login_entry.place(x=10, y=50)

    Label(register_window, text="Nazwisko", width=7).place(x=235, y=80)
    password_entry = Entry(register_window, width=30, font=("Arial", 10))
    password_entry.place(x=10, y=80)

    Label(register_window, text="Login", width=7).place(x=235, y=110)
    password_entry = Entry(register_window, width=30, font=("Arial", 10))
    password_entry.place(x=10, y=110)

    Label(register_window, text="Hasło", width=7).place(x=235, y=140)
    password_entry = Entry(register_window, width=30, font=("Arial", 10))
    password_entry.place(x=10, y=140)

    Label(register_window, text="Email", width=7).place(x=235, y=170)
    password_entry = Entry(register_window, width=30, font=("Arial", 10))
    password_entry.place(x=10, y=170)

    Button(register_window, text="Zarejestruj", width=8).place(x=225, y=200)


def init_game_label(root):
    print(Config.current_question_number)
    print(Config.guaranteed_amount)
    Config.current_page.destroy()
    # Drawing question with the current difficulty level
    question = draw_question()
    Config.photo = PhotoImage(file="background.png")
    game_label = Label(root, width=500, height=700, image=Config.photo)
    game_label.pack()

    Label(game_label, text=f"Pytanie: {Config.current_question_number+1}", bg="#A9A9A9", width=20,
          font=("Arial", 15)).place(x=135, y=425)

    # question_frame = LabelFrame(game_label, text="Pytanie:", bg="#A9A9A9", font=("Arial", 12))
    # question_frame.place(x=25, y=460, width=445, height=110)
    #
    # question_text = Message(game_label, text=question["content"], font=("Arial", 12), justify=LEFT, aspect=200,
    #                         anchor=W)
    # question_text.place(x=10, y=10, width=400, height=60)

    question_text = Text(game_label, width=49, height=6, bg="#A9A9A9", font=("Arial", 12))
    question_text.place(x=25, y=460)
    question_text.insert("1.0", question["content"])
    question_text["state"] = "disabled"
    a = question["A"]
    b = question["B"]
    c = question["C"]
    d = question["D"]
    list_of_buttons = []
    button_a = Button(game_label, text=f"A: {a}", width=30, bg="#A9A9A9", anchor=W, disabledforeground="black",
                      command=lambda: Functions.check_answer(question, "A", init_game_label, root, button_a,
                                                             list_of_buttons, init_end_label, end_game_button,
                                                             fifty_fifty_button))
    list_of_buttons.append((button_a, "A"))
    button_a.place(x=25, y=580)
    button_b = Button(game_label, text=f"B: {b}", width=30, bg="#A9A9A9", anchor=W, disabledforeground="black",
                      command=lambda: Functions.check_answer(question, "B", init_game_label, root, button_b,
                                                             list_of_buttons, init_end_label, end_game_button,
                                                             fifty_fifty_button))
    button_b.place(x=250, y=580)
    list_of_buttons.append((button_b, "B"))
    button_c = Button(game_label, text=f"C: {c}", width=30, bg="#A9A9A9", anchor=W, disabledforeground="black",
                      command=lambda: Functions.check_answer(question, "C", init_game_label, root, button_c,
                                                             list_of_buttons, init_end_label, end_game_button,
                                                             fifty_fifty_button))
    button_c.place(x=25, y=610)
    list_of_buttons.append((button_c, "C"))
    button_d = Button(game_label, text=f"D: {d}", width=30, bg="#A9A9A9", anchor=W, disabledforeground="black",
                      command=lambda: Functions.check_answer(question, "D", init_game_label, root, button_d,
                                                             list_of_buttons, init_end_label, end_game_button,
                                                             fifty_fifty_button))
    button_d.place(x=250, y=610)
    list_of_buttons.append((button_d, "D"))

    fifty_fifty_button = Button(game_label, text="50/50", anchor=W, disabledforeground="black",
                                command=lambda: Functions.fifty_fifty(question, list_of_buttons, fifty_fifty_button))
    fifty_fifty_button.place(x=370, y=10)
    fifty_fifty_button["state"] = ["normal"] if Config.is_fifty_fifty_available else ["disabled"]
    fifty_fifty_button["bg"] = ["#A9A9A9"] if Config.is_fifty_fifty_available else ["#473a3a"]

    end_game_button = Button(game_label, text="Zakończ gre", bg="#A9A9A9", anchor=W, disabledforeground="black",
                             command=lambda current_won=Config.list_of_amounts[Config.current_question_number-1]
                             : init_end_label(root, current_won))
    end_game_button.place(x=415, y=10)

    y = 1

    guaranteed_amount_indexes = [1, 6, 11]
    for i in range(len(Config.list_of_amounts)-1):
        if Config.current_question_number == i:
            amount = Label(game_label, text=f"{y} - {Config.list_of_amounts[i]} zł", bg="#FFD700", width=11, anchor=E)
            amount.place(x=405, y=400-(y*25))
        else:
            amount = Label(game_label, text=f"{y} - {Config.list_of_amounts[i]} zł", bg="#A9A9A9", width=11, anchor=E)
            amount.place(x=405, y=400-(y*25))

        if i in guaranteed_amount_indexes:
            amount.config(foreground="white")
            if Config.current_question_number > i:
                amount.config(bg="#B8860B")
        y += 1

    Config.current_page = game_label


def init_end_label(root, current_won):
    Config.current_page.destroy()
    Config.is_fifty_fifty_available = True
    Config.current_question_number = 0
    Config.guaranteed_amount = 0
    Config.photo = PhotoImage(file="background_start.png")
    end_label = Label(root, width=500, height=700, image=Config.photo)
    end_label.pack()
    Label(end_label, text="MILIONERZY", font=("Arial", 35), bg="#A9A9A9").place(x=100, y=150)
    Label(end_label, text=f"Wygrana kwota: {current_won} zł", font=("Arial", 25), bg="#A9A9A9",
          width=26).place(x=0, y=250)
    Button(end_label, text="Wyjdź do menu", width=30, bg="#A9A9A9",
           command=lambda: init_start_label(root)).place(x=135, y=500)

    Config.current_page = end_label
