# Modules import.
from tkinter import *
from datetime import datetime
# Config module for global variables.
import Config
# Functions module for executing functions and connecting with Backend_requests module.
from Functions import draw_question, run_theme, check_answer, fifty_fifty, validation_for_register, logout_user, \
    check_activation_number, validation_for_login, download_best_scores, send_score, update_user_data, delete_user, \
    add_questions, update_date


def init_main_window():
    """The function responsible for initialization main widow of application and returning it."""
    # Making instance of Tk() class. It is main object of app, every single object which will be created,
    # will be added (Inheritance) into root and packing/placing into root.
    root = Tk()
    # Definition width and height of app window.
    window_width = 500
    window_height = 700
    # Definition width and height of monitor window.
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Setting center of window
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # Making tittle, geometry, resizable, color background, icon.
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root.title("MILLIONAIRE.APP")
    root.resizable(width=False, height=False)
    root.config(bg="#B0C4DE")

    try:
        root.call("wm", "iconphoto", root._w, PhotoImage(file="photos/millionaire_icon.png"))
    except TclError:
        pass

    # Start start_soundtrack theme and then queue main_theme.
    run_theme("start_soundtrack_mp3.mp3", "main_theme_mp3.mp3")
    # Return root object into Main module.
    return root


def init_date(root):
    """The function responsible for initialization time_label and start update_date function."""
    # Init time label.
    time_label = Label(root, width=71)
    # Packing time label into root.
    time_label.pack()
    # Starting update date function from Functions.
    update_date(root, time_label)


def init_authentication_label(root):
    """The function responsible for initialization authentication_label."""
    # Function called first time will not enter this part of code, because current_page = None.
    if isinstance(Config.current_page, Label):
        Config.current_page.destroy()

    authentication_label = Label(root, width=500, height=700, image=Config.images["background"])
    authentication_label.pack()
    # Making labels and buttons.
    Label(authentication_label, text="MILIONERZY", font=("Arial", 35), bg="#A9A9A9").place(x=100, y=150)
    Button(authentication_label, text="Zaloguj się", width=30, bg="#A9A9A9",
           command=lambda: init_login_window(root)).place(x=135, y=500)
    Button(authentication_label, text="Nie masz konta? Zarejestruj sie", width=30, bg="#A9A9A9",
           command=lambda: init_register_window()).place(x=135, y=530)
    Button(authentication_label, text="Kontynuuj jako gość", width=30, bg="#A9A9A9",
           command=lambda: init_start_label(root)).place(x=135, y=560)
    # assignment login_label into Config.current_page.
    Config.current_page = authentication_label


def init_start_label(root):
    """The function responsible for initialization start_label."""
    # destroying current_page and then assignment this into now label.
    Config.current_page.destroy()
    start_label = Label(root, width=500, height=700, image=Config.images["background"])
    start_label.pack()
    # Making label and buttons.
    Label(start_label, text="MILIONERZY", font=("Arial", 35), bg="#A9A9A9").place(x=100, y=150)
    Button(start_label, text="Nowa gra", width=30, bg="#A9A9A9",
           command=lambda: init_game_label(root)).place(x=135, y=500)
    Button(start_label, text="Najlepsze wyniki", width=30, bg="#A9A9A9",
           command=lambda: download_best_scores(init_best_scores_window=init_best_scores_window)).place(x=135, y=530)
    # In case of user is logged in, your account button, logout button and add questions button will be initialized
    # instead of back button.
    if Config.is_user_logged_in:
        Button(start_label, text="Twoje konto", bg="#A9A9A9",
               command=lambda: init_user_label(root)).place(x=355, y=10)
        Button(start_label, text="Wyloguj", bg="#A9A9A9",
               command=lambda: logout_user(init_authentication_label, root)).place(x=435, y=10)
        Button(start_label, text="Dodaj pytanie", width=30, bg="#A9A9A9",
               command=lambda: init_add_question_label(root)).place(x=135, y=560)

    else:
        Button(start_label, text="Cofnij", width=30, bg="#A9A9A9",
               command=lambda: init_authentication_label(root)).place(x=135, y=560)

    # Assignment start_label into global current_page.
    Config.current_page = start_label


def init_user_label(root):
    """The function responsible for initialization user_label for user account management."""
    Config.current_page.destroy()
    user_label = Label(root, width=500, height=700, image=Config.images["background"])
    user_label.pack()
    Label(user_label, text="Panel użytkownika", font=("Arial", 35), bg="#A9A9A9").place(x=0, y=150, width=500)
    # Creating button for deleting account.
    Button(user_label, text="Usuń konto", bg="#A9A9A9",
           command=lambda: delete_user(init_authentication_label, root)).place(x=418, y=10)
    # List of data for display for user.
    list_of_user_info = [
        ("Imie:", Config.logged_in_user_info.first_name),
        ("Nazwisko:", Config.logged_in_user_info.last_name),
        ("Hasło:", Config.logged_in_user_info.password),
        ("Login:", Config.logged_in_user_info.login),
        ("Email:", Config.logged_in_user_info.email)
    ]

    # Init labels and entries for updating user's data.
    y = 1
    for attribute, value in list_of_user_info:
        label = Label(user_label, text=f"{attribute} {value}", font=("Arial", 12), bg="#A9A9A9", anchor=W)
        label.place(x=87, y=y * 70 + 150, width=320)
        entry = Entry(user_label, font=("Arial", 12), bg="#A9A9A9", borderwidth=0, disabledbackground="#A9A9A9")
        entry.place(x=87, y=y * 70 + 175, width=256, height=25)
        # Init buttons for updating particular fields.
        button = Button(user_label, text="Aktualizuj", bg="#A9A9A9",
                        command=lambda label=label, entry=entry, attribute=attribute:
                        update_user_data(label, entry, attribute))
        button.place(x=345, y=y * 70 + 175)
        # Login and Email has unique value in database and user cant change this data, buttons and entries for these
        # fields have disabled state.
        if y == 4 or y == 5:
            entry.insert("0", "Nie możesz zmienić tych danych")
            entry["state"] = "disabled"
            button["state"] = "disabled"
        y += 1

    # Init back to start label button.
    Button(user_label, text="Cofnij", width=30, bg="#A9A9A9",
           command=lambda: init_start_label(root)).place(x=135, y=560)
    # Assignment user_label into global current_page.
    Config.current_page = user_label


def init_add_question_label(root):
    """The function responsible for initialization add_question_label for adding new questions by users."""
    Config.current_page.destroy()
    add_question_label = Label(root, width=500, height=700, image=Config.images["background"])
    add_question_label.pack()
    Label(add_question_label, text="Dodaj pytanie", font=("Arial", 35), bg="#A9A9A9").place(x=0, y=150, width=500)
    # parts of question for displaying in add question label.
    parts_of_question = ("Treść pytania:",
                         "Odpowiedź A:",
                         "Odpowiedź B:",
                         "Odpowiedź C:",
                         "Odpowiedź D:",
                         "Poprawna odpowiedź:",
                         "Trudność (0-11):"
                         )

    # Variable y for positioning labels and entries.
    y = 1
    # Temporary list for adding entries to transfer into Functions.add_questions(list_of_entries).
    list_of_entries = []
    # Making labels and entries and placing it into add_question_label.
    for element in parts_of_question:
        Label(add_question_label, text=element, font=("Arial", 12), bg="#A9A9A9",
              anchor=W).place(x=50, y=y*40+200, width=165)
        entry = Entry(add_question_label, font=("Arial", 12), bg="#A9A9A9", borderwidth=0)
        entry.place(x=230, y=y*40+200, width=220, height=24)
        list_of_entries.append(entry)
        y += 1

    # Buttons for adding question and backing into start label.
    Button(add_question_label, text="Dodaj pytanie", bg="#A9A9A9",
           command=lambda: add_questions(list_of_entries)).place(x=366, y=515)
    Button(add_question_label, text="Cofnij", width=30, bg="#A9A9A9",
           command=lambda: init_start_label(root)).place(x=135, y=560)
    # Assignment add_question_label into global current_page.
    Config.current_page = add_question_label


def init_best_scores_window(best_scores):
    """The function responsible for initialization additional best_score_window for displaying scores."""
    # Making instance of Toplevel class this is object which also inherits from Tk() when root window will close,
    # this window will automatically close with.
    best_scores_window = Toplevel()
    # Definition width and height of app window.
    best_scores_window_width = 400
    best_scores_window_height = 600
    # Definition width and height of monitor window.
    screen_width = best_scores_window.winfo_screenwidth()
    screen_height = best_scores_window.winfo_screenheight()
    # Definition centers
    center_x = int(screen_width / 2 - best_scores_window_width / 2)
    center_y = int(screen_height / 2 - best_scores_window_height / 2)
    best_scores_window.geometry(f"{best_scores_window_width}x{best_scores_window_height}+{center_x}+{center_y}")
    # Making tittle, geometry, resizable, color background, photos.
    best_scores_window.title("Najlepsze wyniki")
    best_scores_window.resizable(width=False, height=False)
    best_scores_window.config(bg="#D3D3D3")

    try:
        best_scores_window.wm_iconphoto(False, PhotoImage(file="photos/millionaire_icon.png"))
    except TclError:
        pass

    # Init label, text, scrollbar objects.
    Label(best_scores_window, text="Lista najlepszych wyników", font=("Arial", 13), width=44).place(x=0, y=10)
    text = Text(best_scores_window, bg="#D3D3D3", borderwidth=0, font=("Arial", 12))
    text.place(x=0, y=35, height=564, width=382)
    scrollbar = Scrollbar(best_scores_window, command=text.yview)
    scrollbar.place(x=382, y=35, height=564)
    text["yscrollcommand"] = scrollbar.set

    # Iterating at dictionary of best_scores downloaded from backend.
    number_of_position = 1
    place_in_the_table = 1
    for player in best_scores:
        first_name = player["first_name"]
        last_name = player["last_name"]
        points = player["points"]
        # Setting position for particular text insert.
        position = f"{number_of_position}.0"
        # Insertion string into text object.
        text.insert(position, f"Miejsce {place_in_the_table}:{'':<5} {first_name} {last_name} - {points}\n\n")
        # Adding integers to variables for getting other values in the next loop.
        number_of_position += 2
        place_in_the_table += 1

    # After adding all scores into text object, text state changes into disabled.
    text["state"] = "disabled"


def init_login_window(root):
    """The function responsible for initialization additional login_window for logging users."""
    # Making instance of Toplevel class this is object which also inherits from Tk() when root window will close,
    # this window will automatically close with.
    login_window = Toplevel()
    # Definition width and height of app window.
    login_window_width = 300
    login_window_height = 150
    # Definition width and height of monitor window.
    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()
    # Definition centers.
    center_x = int(screen_width / 2 - login_window_width / 2)
    center_y = int(screen_height / 2 - login_window_height / 2)
    # Making tittle, geometry, resizable, color background, photos.
    login_window.geometry(f"{login_window_width}x{login_window_height}+{center_x}+{center_y}")
    login_window.title("Logowanie")
    login_window.resizable(width=False, height=False)
    login_window.config(bg="#B0C4DE")

    try:
        login_window.wm_iconphoto(False, PhotoImage(file="photos/login.png"))
    except TclError:
        pass

    # Making labels, entries and button.
    Label(login_window, text="Logowanie", font=("Arial", 13), width=33).place(x=0, y=10)
    # Label and entry for login input.
    Label(login_window, text="Login", width=7).place(x=235, y=50)
    login_entry = Entry(login_window, width=30, font=("Arial", 10))
    login_entry.place(x=10, y=50)
    # Label and entry for password input.
    Label(login_window, text="Hasło", width=7).place(x=235, y=80)
    password_entry = Entry(login_window, width=30, font=("Arial", 10))
    password_entry.place(x=10, y=80)
    # Button for start login process. Going to Functions.validation_for_login.
    Button(login_window, text="Zaloguj", width=8,
           command=lambda: validation_for_login(login_entry, password_entry, login_window,
                                                init_start_label, root)).place(x=225, y=110)


def init_register_window():
    """The function responsible for initialization additional register_window for registering users."""
    # Making instance of Toplevel class this is object which also inherits from Tk() when root window will close,
    # this window will automatically close with.
    register_window = Toplevel()
    # Definition width and height of app window.
    register_window_width = 300
    register_window_height = 240
    # Definition width and height of monitor window.
    screen_width = register_window.winfo_screenwidth()
    screen_height = register_window.winfo_screenheight()
    # Definition centers.
    center_x = int(screen_width / 2 - register_window_width / 2)
    center_y = int(screen_height / 2 - register_window_height / 2)
    # Making tittle, geometry, resizable, color background, photos.
    register_window.geometry(f"{register_window_width}x{register_window_height}+{center_x}+{center_y}")
    register_window.title("Rejestracja")
    register_window.resizable(width=False, height=False)
    register_window.config(bg="#B0C4DE")

    try:
        register_window.wm_iconphoto(False, PhotoImage(file="photos/login.png"))
    except TclError:
        pass

    # Making labels, entries and button.
    Label(register_window, text="Tworzenie konta", font=("Arial", 13), width=33).place(x=0, y=10)
    # Label and entry for first name input.
    Label(register_window, text="Imie", width=7).place(x=235, y=50)
    first_name_entry = Entry(register_window, width=30, font=("Arial", 10))
    first_name_entry.place(x=10, y=50)
    # Label and entry for last name input.
    Label(register_window, text="Nazwisko", width=7).place(x=235, y=80)
    last_name_entry = Entry(register_window, width=30, font=("Arial", 10))
    last_name_entry.place(x=10, y=80)
    # Label and entry for login input.
    Label(register_window, text="Login", width=7).place(x=235, y=110)
    login_entry = Entry(register_window, width=30, font=("Arial", 10))
    login_entry.place(x=10, y=110)
    # Label and entry for password input.
    Label(register_window, text="Hasło", width=7).place(x=235, y=140)
    password_entry = Entry(register_window, width=30, font=("Arial", 10))
    password_entry.place(x=10, y=140)
    # Label and entry for E-mail input.
    Label(register_window, text="Email", width=7).place(x=235, y=170)
    email_entry = Entry(register_window, width=30, font=("Arial", 10))
    email_entry.place(x=10, y=170)
    # Button for start process of validation.
    Button(register_window, text="Zarejestruj", width=8,
           command=lambda: validation_for_register(first_name_entry, last_name_entry, login_entry, password_entry,
                                                   email_entry, register_window,
                                                   init_activation_window)).place(x=225, y=200)


def init_activation_window(activation_number, first_name, last_name, login, password, email):
    """The function responsible for initialization additional activation window for enter the received activation
    number."""
    # Making instance of Toplevel class this is object which also inherits from Tk() when root window will close,
    # this window will automatically close with.
    activation_window = Toplevel()
    # Definition width and height of app window.
    activation_window_width = 300
    activation_window_height = 150
    # Definition width and height of monitor window.
    screen_width = activation_window.winfo_screenwidth()
    screen_height = activation_window.winfo_screenheight()
    # Definition centers.
    center_x = int(screen_width / 2 - activation_window_width / 2)
    center_y = int(screen_height / 2 - activation_window_height / 2)
    # Making tittle, geometry, resizable, color background, photos.
    activation_window.geometry(f"{activation_window_width}x{activation_window_height}+{center_x}+{center_y}")
    activation_window.title("Aktywacja konta")
    activation_window.resizable(width=False, height=False)
    activation_window.config(bg="#B0C4DE")

    try:
        activation_window.wm_iconphoto(False, PhotoImage(file="photos/login.png"))
    except TclError:
        pass

    # Label and entry for putting number that was sent to the user's email.
    Label(activation_window, text="Aktywacja konta", font=("Arial", 13), width=33).place(x=0, y=10)
    activation_entry = Entry(activation_window, width=23, font=("Arial", 13))
    activation_entry.place(x=15, y=71)
    # Button for checking if number is correct, registration and activation user.
    Button(activation_window, text="Aktywuj",
           command=lambda: check_activation_number(activation_number, activation_entry, first_name, last_name,
                                                   login, password, email, activation_window)).place(x=230, y=70)
    # Statement about sending the activation code to the e-mail address provided.
    Label(activation_window, text=f"Kod aktywacyjny został wysłany na adres:\n {email}",
          font=("Arial", 8)).place(x=0, y=110, width=300)


def init_game_label(root):
    """The function responsible for initialization game_label for displaying the game."""
    # With start game_label, checking if global is_game_playing is True. When False,
    # changing into True and getting the time to global game_start_time.
    if not Config.is_game_playing:
        Config.is_game_playing = True
        Config.game_start_time = datetime.now()

    # Start start_question theme and then queue question_theme.
    run_theme("start_question_mp3.mp3", "question_theme_mp3.mp3")
    # Destroying current_page.
    Config.current_page.destroy()
    # Drawing question with the current difficulty level.
    question = draw_question()
    # Making game_label.
    game_label = Label(root, width=500, height=700, image=Config.images["in_game"])
    game_label.pack()
    # Making number of question label.
    Label(game_label, text=f"Pytanie: {Config.current_question_number+1}", bg="#A9A9A9", width=20,
          font=("Arial", 15)).place(x=135, y=425)
    # Making text of question content.
    question_text = Text(game_label, width=49, height=6, bg="#A9A9A9", font=("Arial", 12))
    # Placing text at game_label.
    question_text.place(x=25, y=460)
    # Inserting the content of the question into question_text object.
    question_text.insert("1.0", question["content"])
    # Setting question_text state at disabled, it's only for reading.
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
                             command=lambda current_won=Config.list_of_amounts[Config.current_question_number-1]:
                             init_end_label(root, current_won))
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

    # Assignment game_label into global current_page.
    Config.current_page = game_label


def init_end_label(root, current_won):
    """The function responsible for initialization end_label, displaying five best scores, optionally adding user's
    score to the database."""
    # Creating a game_duration object. From object datetime.now() subtracting global object game_start_time, created
    # with starting game in game_label.
    game_duration = datetime.now() - Config.game_start_time
    # Start millioner theme and then queue main_theme.
    run_theme("millioner_mp3.mp3", "main_theme_mp3.mp3")
    # destroying current_page.
    Config.current_page.destroy()
    # Assignment global user's variables into default data for starting game again.
    Config.is_fifty_fifty_available = True
    Config.current_question_number = 0
    Config.guaranteed_amount = 0
    Config.is_game_playing = False
    Config.game_start_time = None
    # Downloading five best scores from backed API
    five_best_scores = download_best_scores(limit=5)
    # Creating numbers of points. Current_won is divided by game_duration in seconds and converted into integer.
    points_earned = int(current_won / game_duration.total_seconds())
    # Making end_label.
    end_label = Label(root, width=500, height=700, image=Config.images["background"])
    end_label.pack()
    # Making Labels and placing them on end_label object.
    Label(end_label, text="MILIONERZY", font=("Arial", 35), bg="#A9A9A9").place(x=100, y=150)
    Label(end_label, text=f"Wygrana kwota: {current_won} zł", font=("Arial", 25),
          bg="#A9A9A9").place(x=0, y=230, width=500)
    Label(end_label, text=f"Twoj wynik: {points_earned} pkt.", font=("Arial", 9), bg="#A9A9A9").place(x=0, y=274,
                                                                                                      width=500)
    Label(end_label, text="TOP 5 GRACZY:", font=("Arial", 14), bg="#A9A9A9").place(x=0, y=310, width=500)

    # Variable y for positioning labels of user's points
    y = 1
    # Iterating at json of five best scores and adding information about player and his score into labels, then placing
    # it at end_label.
    for user in five_best_scores:
        first_name = user["first_name"]
        last_name = user["last_name"]
        points = user["points"]
        Label(end_label, text=f"{first_name} {last_name}", font=("Arial", 10), bg="#A9A9A9", width=24,
              anchor=W).place(x=110, y=y*30+320)
        Label(end_label, text=f"{points} pkt.", font=("Arial", 10), bg="#A9A9A9", width=8,
              anchor=E).place(x=310, y=y*30+320)
        y += 1

    # Button to move user to start label.
    Button(end_label, text="Wyjdź do menu", width=30, bg="#A9A9A9",
           command=lambda: init_start_label(root)).place(x=135, y=500)
    
    # If player achieved more than 1000 points and also is logged in, his score will be saved in database.
    if points_earned > 1000 and Config.is_user_logged_in:
        send_score(points_earned)

    # Assignment end_label into global current_page.
    Config.current_page = end_label
