from tkinter import *
import datetime
import Config
from Functions import draw_question, run_theme, check_answer, fifty_fifty, validation_for_register, logout_user, \
    check_activation_number, validation_for_login, download_best_scores


# Initialization main window of app.
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
    # Start start_soundtrack theme and then queue main_theme.
    run_theme("start_soundtrack_mp3.mp3", "main_theme_mp3.mp3")
    # Return root object into Main
    return root


# Initialization time label.
def init_date(root):
    time_label = Label(root, width=71)
    time_label.pack()
    # Starting update date.
    update_date(root, time_label)


# Updating date
def update_date(root, time_label):
    # assignment new date and time from now to variables.
    date = f"{datetime.datetime.now().date()}"
    time = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"
    # Config time_label for new data.
    time_label.config(text=f"{date} {time}")
    # Recursion of function after 1s.
    root.after(1000, update_date, root, time_label)


# Initialization authentication label.
def init_authentication_label(root):
    # Function called first time will not enter this part of code, because current_page = None.
    if isinstance(Config.current_page, Label):
        Config.current_page.destroy()

    Config.photo = PhotoImage(file="background_start.png")
    login_label = Label(root, width=500, height=700, image=Config.photo)
    login_label.pack()
    # Making labels and buttons.
    Label(login_label, text="MILIONERZY",font=("Arial", 35), bg="#A9A9A9").place(x=100, y=150)
    Button(login_label, text="Zaloguj się", width=30, bg="#A9A9A9",
           command=lambda: init_login_window(root)).place(x=135, y=500)
    Button(login_label, text="Nie masz konta? Zarejestruj sie", width=30, bg="#A9A9A9",
           command=lambda: init_register_window()).place(x=135, y=530)
    Button(login_label, text="Kontynuuj jako gość", width=30, bg="#A9A9A9",
           command=lambda: init_start_label(root)).place(x=135, y=560)
    # assignment login_label into Config.current_page.
    Config.current_page = login_label


# Initialization start label.
def init_start_label(root):
    # destroying current_page and then assignment this into now label.
    Config.current_page.destroy()
    Config.photo = PhotoImage(file="background_start.png")
    start_label = Label(root, width=500, height=700, image=Config.photo)
    start_label.pack()
    # Making label and buttons.
    Label(start_label, text="MILIONERZY", font=("Arial", 35), bg="#A9A9A9").place(x=100, y=150)
    Button(start_label, text="Nowa gra", width=30, bg="#A9A9A9",
           command=lambda: init_game_label(root)).place(x=135, y=500)
    Button(start_label, text="Najlepsze wyniki", width=30, bg="#A9A9A9",
           command=lambda: download_best_scores(init_best_scores_window)).place(x=135, y=530)
    if Config.is_user_logged_in:
        Button(start_label, text="Twoje konto", bg="#A9A9A9",
               command=lambda: print("to twoje konto")).place(x=355, y=10)
        Button(start_label, text="Wyloguj", bg="#A9A9A9",
               command=lambda: logout_user(init_authentication_label, root)).place(x=435, y=10)
        Button(start_label, text="Dodaj pytania", width=30, bg="#A9A9A9",
               command=lambda: print("dodano pytania")).place(x=135, y=560)

    else:
        Button(start_label, text="Cofnij", width=30, bg="#A9A9A9",
               command=lambda: init_authentication_label(root)).place(x=135, y=560)

    Config.current_page = start_label


def init_best_scores_window(best_scores):
    best_scores_window = Toplevel()
    best_scores_window_width = 400
    best_scores_window_height = 600
    screen_width = best_scores_window.winfo_screenwidth()
    screen_height = best_scores_window.winfo_screenheight()
    center_x = int(screen_width / 2 - best_scores_window_width / 2)
    center_y = int(screen_height / 2 - best_scores_window_height / 2)
    best_scores_window.geometry(f"{best_scores_window_width}x{best_scores_window_height}+{center_x}+{center_y}")
    best_scores_window.title("Najlepsze wyniki")
    best_scores_window.resizable(width=True, height=True)
    best_scores_window.config(bg="blue")
    login_icon = PhotoImage(file="millionaire_icon.png")
    best_scores_window.wm_iconphoto(False, login_icon)
    Label(best_scores_window, text="Lista najlepszych wyników", font=("Arial", 13), width=44).place(x=0, y=10)
    text = Text(best_scores_window, bg="#D3D3D3", borderwidth=0, font=("Arial", 12))
    text.place(x=0, y=35, height=564, width=382)
    scrollbar = Scrollbar(best_scores_window, command=text.yview)
    scrollbar.place(x=382, y=35, height=564)
    text["yscrollcommand"] = scrollbar.set
    text["state"] = "normal"
    text.delete("1.0", END)
    number_of_position = 1
    place_in_the_table = 1
    for player in best_scores:
        first_name = player["first_name"]
        last_name = player["last_name"]
        points = player["points"]
        position = f"{number_of_position}.0"
        text.insert(position, f"Miejsce {place_in_the_table}:{'':<5} {first_name} {last_name} - {points}\n\n")
        number_of_position += 2
        place_in_the_table += 1
    text["state"] = "disabled"


# Initialization login window.
def init_login_window(root):
    # Making new instance of TopLevel().
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
    # Making labels, entries and button.
    Label(login_window, text="Logowanie", font=("Arial", 13), width=33).place(x=0, y=10)

    Label(login_window, text="Login", width=7).place(x=235, y=50)
    login_entry = Entry(login_window, width=30, font=("Arial", 10))
    login_entry.place(x=10, y=50)

    Label(login_window, text="Hasło", width=7).place(x=235, y=80)
    password_entry = Entry(login_window, width=30, font=("Arial", 10))
    password_entry.place(x=10, y=80)

    Button(login_window, text="Zaloguj", width=8,
           command=lambda: validation_for_login(login_entry, password_entry, login_window,
                                                init_start_label, root)).place(x=225, y=110)


# Initialization register window.
def init_register_window():
    # Making instance of TopLevel().
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
    # Making labels, entries and button.
    Label(register_window, text="Tworzenie konta", font=("Arial", 13), width=33).place(x=0, y=10)

    Label(register_window, text="Imie", width=7).place(x=235, y=50)
    first_name_entry = Entry(register_window, width=30, font=("Arial", 10))
    first_name_entry.place(x=10, y=50)

    Label(register_window, text="Nazwisko", width=7).place(x=235, y=80)
    last_name_entry = Entry(register_window, width=30, font=("Arial", 10))
    last_name_entry.place(x=10, y=80)

    Label(register_window, text="Login", width=7).place(x=235, y=110)
    login_entry = Entry(register_window, width=30, font=("Arial", 10))
    login_entry.place(x=10, y=110)

    Label(register_window, text="Hasło", width=7).place(x=235, y=140)
    password_entry = Entry(register_window, width=30, font=("Arial", 10))
    password_entry.place(x=10, y=140)

    Label(register_window, text="Email", width=7).place(x=235, y=170)
    email_entry = Entry(register_window, width=30, font=("Arial", 10))
    email_entry.place(x=10, y=170)

    Button(register_window, text="Zarejestruj", width=8,
           command=lambda: validation_for_register(first_name_entry, last_name_entry, login_entry, password_entry,
                                                   email_entry, register_window,
                                                   init_activation_window)).place(x=225, y=200)


def init_activation_window(activation_number, first_name, last_name, login, password, email):
    activation_window = Toplevel()
    activation_window_width = 300
    activation_window_height = 150
    screen_width = activation_window.winfo_screenwidth()
    screen_height = activation_window.winfo_screenheight()
    center_x = int(screen_width / 2 - activation_window_width / 2)
    center_y = int(screen_height / 2 - activation_window_height / 2)
    activation_window.geometry(f"{activation_window_width}x{activation_window_height}+{center_x}+{center_y}")
    activation_window.title("Aktywacja konta")
    activation_window.resizable(width=True, height=True)
    activation_window.config(bg="#B0C4DE")
    login_icon = PhotoImage(file="login.png")
    activation_window.wm_iconphoto(False, login_icon)
    Label(activation_window, text="Aktywacja konta", font=("Arial", 13), width=33).place(x=0, y=10)
    activation_entry = Entry(activation_window, width=23, font=("Arial", 13))
    activation_entry.place(x=15, y=71)
    Button(activation_window, text="Aktywuj",
           command=lambda: check_activation_number(activation_number, activation_entry, first_name, last_name,
                                                   login, password, email, activation_window)).place(x=230, y=70)
    Label(activation_window, text=f"Kod aktywacyjny został wysłany na adres:\n {email}",
          font=("Arial", 8)).place(x=0, y=110, width=300)


# Initialization game label.
def init_game_label(root):
    # Start start_question theme and then queue question_theme.
    run_theme("start_question_mp3.mp3", "question_theme_mp3.mp3")
    # Destroying current_page.
    Config.current_page.destroy()
    # Drawing question with the current difficulty level.
    question = draw_question()
    # Assignment new photo to global Config.photo.
    Config.photo = PhotoImage(file="background.png")
    # Making game_label.
    game_label = Label(root, width=500, height=700, image=Config.photo)
    game_label.pack()
    # Making number of question label.
    Label(game_label, text=f"Pytanie: {Config.current_question_number+1}", bg="#A9A9A9", width=20,
          font=("Arial", 15)).place(x=135, y=425)
    # Making text of question content.
    question_text = Text(game_label, width=49, height=6, bg="#A9A9A9", font=("Arial", 12))
    question_text.place(x=25, y=460)
    question_text.insert("1.0", question["content"])
    question_text["state"] = "disabled"
    # Making list of A,B,C,D strings for initialization content of questions and response indication for a given button.
    a_b_c_d = ["A", "B", "C", "D"]
    # Making list of content answers.
    list_of_answers = []
    for i in a_b_c_d:
        list_of_answers.append(question[i])

    # Making buttons to select right answer.
    list_of_buttons = []
    rows = 2
    columns = 2
    for i in range(rows):
        for j in range(columns):
            index = i*columns+j
            # Initialization buttons.
            button = Button(game_label, text=f"{a_b_c_d[index]}: {list_of_answers[index]}", width=30, bg="#A9A9A9",
                            anchor=W, disabledforeground="black")
            # Creating function for particular buttons.
            button.config(command=lambda selected_answer=a_b_c_d[index], button=button:
                          check_answer(question, selected_answer, init_game_label, root, button,
                          list_of_buttons, init_end_label, end_game_button, fifty_fifty_button))
            # Creating list of buttons for disable state of all buttons and in case when user select wrong button
            # function will find right button and change color on green.
            list_of_buttons.append((button, a_b_c_d[index]))
            # 2d placing buttons on gui.
            button.place(x=25+(j*225), y=580+(i*30))

    # Making fifty/fifty button.
    fifty_fifty_button = Button(game_label, text="50/50", anchor=W, disabledforeground="black",
                                command=lambda: fifty_fifty(question, list_of_buttons, fifty_fifty_button))
    fifty_fifty_button.place(x=370, y=10)
    # Checking if global is_fifty_fifty_available is True.
    fifty_fifty_button["state"] = ["normal"] if Config.is_fifty_fifty_available else ["disabled"]
    fifty_fifty_button["bg"] = ["#A9A9A9"] if Config.is_fifty_fifty_available else ["#473a3a"]
    # Making end_game_button with function init_end_game with current_won parameter
    end_game_button = Button(game_label, text="Zakończ gre", bg="#A9A9A9", anchor=W, disabledforeground="black",
                             command=lambda current_won=Config.list_of_amounts[Config.current_question_number-1]
                             : init_end_label(root, current_won))
    end_game_button.place(x=415, y=10)
    # Variable y for positioning amount labels.
    y = 1
    # List of indexes for guaranteed amounts.
    guaranteed_amount_indexes = [1, 6, 11]
    # Creating labels of amounts into game_label.
    for i in range(len(Config.list_of_amounts)-1):
        # If index of creating labels is equal to global current question number, this label will be golden.
        if Config.current_question_number == i:
            amount = Label(game_label, text=f"{y} - {Config.list_of_amounts[i]} zł", bg="#FFD700", width=11, anchor=E)
            amount.place(x=405, y=400-(y*25))
        # Otherwise color will be gray.
        else:
            amount = Label(game_label, text=f"{y} - {Config.list_of_amounts[i]} zł", bg="#A9A9A9", width=11, anchor=E)
            amount.place(x=405, y=400-(y*25))
        # Making white foreground for amount labels with guaranteed amounts.
        if i in guaranteed_amount_indexes:
            amount.config(foreground="white")
            # If player achieve this guaranteed amount, label of this amount will have other color.
            if Config.current_question_number > i:
                amount.config(bg="#B8860B")
        # Adding +=1 to y for positioning next label.
        y += 1
    # Assignment game_label into current_page.
    Config.current_page = game_label


# initialization end label.
def init_end_label(root, current_won):
    # Start millioner theme and then queue main_theme.
    run_theme("millioner_mp3.mp3", "main_theme_mp3.mp3")
    # destroying current_page.
    Config.current_page.destroy()
    # Assignment global user's variables into default data for starting game again.
    Config.is_fifty_fifty_available = True
    Config.current_question_number = 0
    Config.guaranteed_amount = 0
    # Assignment new photo into global Config.photo.
    Config.photo = PhotoImage(file="background_start.png")
    # Making end_label.
    end_label = Label(root, width=500, height=700, image=Config.photo)
    end_label.pack()
    Label(end_label, text="MILIONERZY", font=("Arial", 35), bg="#A9A9A9").place(x=100, y=150)
    Label(end_label, text=f"Wygrana kwota: {current_won} zł", font=("Arial", 25), bg="#A9A9A9",
          width=26).place(x=0, y=250)
    # Button to move user to start label.
    Button(end_label, text="Wyjdź do menu", width=30, bg="#A9A9A9",
           command=lambda: init_start_label(root)).place(x=135, y=500)
    # Assignment end_label into current_page.
    Config.current_page = end_label
