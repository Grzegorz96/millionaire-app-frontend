import Config
from re import match
from random import choice
from pygame import mixer
from tkinter import messagebox
from Backend_requests import registration_user_request, send_activation_number_request, \
    get_questions_request, login_user_request, get_user_info_request, check_for_registration_request, \
    get_best_scores_request, send_score_request, update_user_request, delete_user_request, add_questions_request
from requests import codes
from sys import exit
from User_class import User


def download_questions():
    response_for_downloading_questions = get_questions_request()
    if response_for_downloading_questions.status_code == codes.ok:
        Config.list_of_questions = response_for_downloading_questions.json()["result"]

    else:
        messagebox.showerror("Błąd podczas pobierania pytań z bazy danych.",
                             "W chwili obecnej nie można pobrać pytań do gry, spróbuj zagrać później.")
        exit()


def validation_for_register(first_name_entry, last_name_entry, login_entry, password_entry, email_entry,
                            register_window, init_activation_window):
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", first_name):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", last_name):
            if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", login):
                if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", password):
                    if match(
                            "^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9._-]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9._-]+[A-Za-z0-9])\.[A-Za-z0-9]+$",
                            email):
                        response_for_checking_registration = check_for_registration_request(login, email)

                        if response_for_checking_registration.status_code == codes.ok:
                            response_for_sending_number = send_activation_number_request(email)

                            if response_for_sending_number.status_code == codes.ok:
                                register_window.destroy()
                                activation_number = response_for_sending_number.json()["result"]["activation_number"]
                                init_activation_window(activation_number, first_name, last_name, login, password, email)

                            else:
                                register_window.destroy()
                                messagebox.showerror("Nie udało sie wysłać numeru aktywacyjnego.",
                                                     "Wysyłanie numeru aktywacyjnego na podany adres e-mail "
                                                     "nie powiodło sie, spróbuj ponownie później.")

                        elif response_for_checking_registration.status_code == codes.im_used:
                            messagebox.showerror("Nie udało sie utworzyć konta.",
                                                 "Użytkownik o podanym emailu lub loginie, jest już zarejestrowany.")

                        else:
                            register_window.destroy()
                            messagebox.showerror("Nie udało sie utworzyć konta.",
                                                 "Wystąpił problem z utworzeniem konta, spróbuj później.")

                    else:
                        messagebox.showerror("Niepoprawny email.", "Wprowadzono niepoprawne dane email.")
                else:
                    messagebox.showerror("Niepoprawne hasło.", "Wprowadzono niepoprawne dane hasła.")
            else:
                messagebox.showerror("Niepoprawny login.", "Wprowadzono niepoprawne dane loginu.")
        else:
            messagebox.showerror("Niepoprawne nazwisko.", "Wprowadzono niepoprawne dane nazwiska.")
    else:
        messagebox.showerror("Niepoprawne imię.", "Wprowadzono niepoprawne dane imienia.")


def check_activation_number(activation_number, activation_entry, first_name, last_name, login, password, email,
                            activation_window):
    if activation_entry.get() == activation_number:
        response_for_registration_user = registration_user_request(first_name, last_name, login, password, email)

        if response_for_registration_user.status_code == codes.created:
            activation_window.destroy()
            messagebox.showinfo("Użytkownik zarejestrowany i aktywowany.",
                                "Rejestracja oraz aktywacja użytkownika przebiegła pomyślnie,"
                                " możesz zalogować sie na swoje konto.")

        elif response_for_registration_user.status_code == codes.bad_request:
            if "login_error" in response_for_registration_user.json():
                activation_window.destroy()
                messagebox.showerror("Nie udało sie utworzyć konta.",
                                     "Użytkownik o podanym loginie jest już zarejestrowany.")

            elif "email_error" in response_for_registration_user.json():
                activation_window.destroy()
                messagebox.showerror("Nie udało sie utworzyć konta.",
                                     "Użytkownik o podanym adresie e-mail jest już zarejestrowany.")
            else:
                activation_window.destroy()
                messagebox.showerror("Nie udało się utworzyć konta.",
                                     "Utworzenie konta nie powiodła się, spróbuj później.")
        else:
            activation_window.destroy()
            messagebox.showerror("Nie udało się utworzyć konta.",
                                 "Utworzenie konta nie powiodła się, spróbuj później.")

    else:
        messagebox.showerror("Błędy numer aktywacyjny.",
                             f"Wpisany numer aktywacyjny nie pasuje do numeru wysłanego na adres {email}.")


def validation_for_login(login_entry, password_entry, login_window, init_start_label, root):
    login = login_entry.get()
    password = password_entry.get()
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", login):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", password):
            response_for_login_user = login_user_request(login, password)

            if response_for_login_user.status_code == codes.ok:
                access_token = response_for_login_user.headers["access-token"]
                refresh_token = response_for_login_user.headers["refresh-token"]
                user_id = response_for_login_user.json()["result"]
                response_for_getting_user_info = get_user_info_request(user_id, access_token, refresh_token)
                if response_for_getting_user_info.status_code == codes.ok:
                    user_info = response_for_getting_user_info.json()["result"][0]
                    user_info["access_token"] = access_token
                    user_info["refresh_token"] = refresh_token
                    Config.is_user_logged_in = True
                    Config.logged_in_user_info = User(
                        user_info["active_flag"],
                        user_info["email"],
                        user_info["first_name"],
                        user_info["last_name"],
                        user_info["login"],
                        user_info["password"],
                        user_info["user_id"],
                        user_info["access_token"],
                        user_info["refresh_token"]
                    )
                    login_window.destroy()
                    init_start_label(root)
                    messagebox.showinfo("Pomyślnie zalogowano.", "Zostałeś pomyślnie zalogowany.")
                else:
                    login_window.destroy()
                    messagebox.showerror("Nie udało sie zalogować.",
                                         "W chwili obecnej nie możemy Cię zalogować, spróbuj ponownie później.")

            elif response_for_login_user.status_code == codes.unauthorized:
                messagebox.showerror("Błędy login lub hasło.", "Upewnij się, że podany login i hasło są prawidłowe.")
            else:
                login_window.destroy()
                messagebox.showerror("Nie udało sie zalogować.",
                                     "W chwili obecnej nie możemy Cię zalogować, spróbuj ponownie później.")
        else:
            messagebox.showerror("Niepoprawne hasło.", "Wprowadzono niepoprawne dane hasła.")
    else:
        messagebox.showerror("Niepoprawny login.", "Wprowadzono niepoprawne dane loginu.")


def logout_user(init_authentication_label, root):
    Config.is_user_logged_in = False
    Config.logged_in_user_info = None
    init_authentication_label(root)
    messagebox.showinfo("Pomyślnie wylogowano.", "Zostałeś pomyślnie wylogowany.")


# Function for drawing question from global list_of_question with particular difficulty level.
def draw_question():
    # Making local list for questions with current difficulty.
    list_of_questions_for_current_difficulty = []
    # Adding into list questions with specific difficulty from global current_question_number.
    for question in Config.list_of_questions:
        if question["difficulty"] == Config.current_question_number:
            list_of_questions_for_current_difficulty.append(question)
    # Drawing one question from local list with particular difficulty level.
    question = choice(list_of_questions_for_current_difficulty)
    # Removing drawn question from global list of all questions.
    Config.list_of_questions.remove(question)
    # Return drawn question to game label.
    return question


# Function for checking selected question.
def check_answer(question, selected_answer, init_game_label, root, answer_button, list_of_buttons, init_end_label,
                 end_game_button, fifty_fifty_button):
    # Sub function for checking selected question called after 4.6s.
    def checking():
        # Comparing selected answer into value from question["right_answer"].
        if selected_answer == question["right_answer"]:
            # If enter into this statement, theme "win" starts.
            run_theme("win_mp3.mp3")
            # Adding 1 to current_question_number for drawing next level question and init new labels on game_label
            Config.current_question_number += 1
            # Selected right button will change color on green.
            answer_button.config(bg="green")
            # Checking if user achieve guaranteed amounts. If he did then global guaranteed amount will change.
            if Config.current_question_number == 2:
                Config.guaranteed_amount = 1000
                # Program will run init_game_label after 4.5s
                root.after(4500, init_game_label, root)
            elif Config.current_question_number == 7:
                Config.guaranteed_amount = 40000
                root.after(4500, init_game_label, root)
            # In case of user achieve 12 question number, global guaranteed amount will assignment into 1 000 000 and
            # program will run init_end_label after 4.5s
            elif Config.current_question_number == 12:
                Config.guaranteed_amount = 1000000
                current_won = Config.guaranteed_amount
                root.after(4500, init_end_label, root, current_won)
            # In case of user just selected right answer but didn't achieve guaranteed amount then just will run into
            # init_game_label after 4.5s
            else:
                root.after(4500, init_game_label, root)

        # If user selected wrong answer.
        else:
            # Start fail theme.
            run_theme("fail_mp3.mp3")
            # Setting right button on green light.
            for obj in list_of_buttons:
                if question["right_answer"] == obj[1]:
                    obj[0].config(bg="green")
            # Setting wrong selected button on red light.
            answer_button.config(bg="red")
            # Assignment into local variable current_won value from global guaranteed amount.
            current_won = Config.guaranteed_amount
            # Program will run init_end_label after 4.5s.
            root.after(4500, init_end_label, root, current_won)

    # Start checking question theme.
    run_theme("checking_question_mp3.mp3")
    # Setting state buttons on disabled.
    for obj in list_of_buttons:
        obj[0]["state"] = ["disabled"]
    end_game_button["state"] = ["disabled"]
    fifty_fifty_button["state"] = ["disabled"]

    # Config color of selected button on yellow.
    answer_button.config(bg="yellow")
    # Function checking will run 4,6s.
    root.after(4600, checking)


# Function fifty_fifty.
def fifty_fifty(question, list_of_buttons, fifty_fifty_button):
    # Making object of fifty/fifty sound effect, setting volume on 0.5 and run.
    fifty_fifty_sound = mixer.Sound(r"C:\Users\grzes\Desktop\Projekty Python\Milionarie.app\Frontend\songs\fifty_fifty_wav.wav")
    fifty_fifty_sound.set_volume(0.5)
    fifty_fifty_sound.play()
    # Setting global is_fifty_fifty_available on False.
    Config.is_fifty_fifty_available = False
    # Config state and background of 50/50 button.
    fifty_fifty_button["state"] = ["disabled"]
    fifty_fifty_button.config(bg="#473a3a")
    # Making local list of wrong answers to delete.
    wrong_answers = ["A", "B", "C", "D"]
    # Removing right answer from list.
    wrong_answers.remove(question["right_answer"])
    # Draw one wrong answer
    drawn_answer = choice(wrong_answers)
    # Removing drawn wrong answer from list.
    wrong_answers.remove(drawn_answer)
    # Config state and text for buttons with second element in wrong_answers. list_of_buttons =
    # [(button.obj,"A")(button.obj,"B")(button.obj,"C")(button.obj,"D")], wrong_answers = ["A","B"].
    for button in list_of_buttons:
        if button[1] in wrong_answers:
            button[0]["state"] = ["disabled"]
            button[0]["text"] = ""


# Initialization sound mixer for app.
def init_sound_mixer():
    mixer.init()
    # Setting volume on 0.2.
    mixer.music.set_volume(0.2)


# Function for run themes in app. In case of function is called with one argument there won't be queue.
def run_theme(theme1, theme2=False):
    # Called without queue
    if not theme2:
        mixer.music.load(fr"C:\Users\grzes\Desktop\Projekty Python\Milionarie.app\Frontend\songs\{theme1}")
        mixer.music.play()
    # Called with queue
    else:
        mixer.music.load(fr"C:\Users\grzes\Desktop\Projekty Python\Milionarie.app\Frontend\songs\{theme1}")
        mixer.music.play()
        mixer.music.queue(
            fr"C:\Users\grzes\Desktop\Projekty Python\Milionarie.app\Frontend\songs\{theme2}",
            loops=-1)


def download_best_scores(init_best_scores_window=None, limit=None):
    response_for_download_best_scores = get_best_scores_request(limit)
    if response_for_download_best_scores.status_code == codes.ok:
        best_scores = response_for_download_best_scores.json()["result"]
        if limit:
            return best_scores
        else:
            init_best_scores_window(best_scores)
    else:
        messagebox.showerror("Błąd podczas pobierania najlepszych wyników.",
                             "Nie udało się pobrać najlepszych wyników, spróbuj ponownie później.")


def send_score(points):
    response_for_sending_score = send_score_request(points)
    if response_for_sending_score.status_code == codes.created:
        if "access-token" in response_for_sending_score.headers:
            Config.logged_in_user_info.access_token = response_for_sending_score.headers["access-token"]
            send_score(points)
        else:
            messagebox.showinfo("Gratulacje!", f"{Config.logged_in_user_info.first_name}, "
                                               f"Twój wynik trafił do listy najlepszych graczy!")

    elif response_for_sending_score.status_code == codes.unauthorized:
        if "Your session has expired" in response_for_sending_score.json():
            messagebox.showerror("Błąd podczas zapisywania wyniku.",
                                 "Nie mogliśmy zapisać Twojego wyniku z powodu wygaśnięcia sesji."
                                 " Zaloguj się ponownie.")
        else:
            messagebox.showerror("Błąd podczas zapisywania wyniku.",
                                 "Z powodu problemu z tokenem dostępu lub problemu z odświeżeniem tokenu dostępu"
                                 " nie mogliśmy zapisać Twojego wyniku.")
    else:
        messagebox.showerror("Błąd podczas zapisywania wyniku.",
                             "W chwili obecnej nie możemy zapisać Twojego wyniku, gdyż wystąpił błąd.")


def update_user_data(label, entry, attribute):
    new_value = entry.get()
    request_body = None
    if attribute == "Imie:":
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", new_value):
            request_body = {"first_name": new_value}
        else:
            messagebox.showerror("Niepoprawne imię.", "Wprowadzono niepoprawne dane do zmiany imienia.")

    elif attribute == "Nazwisko:":
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", new_value):
            request_body = {"last_name": new_value}
        else:
            messagebox.showerror("Niepoprawne nazwisko.", "Wprowadzono niepoprawne dane do zmiany nazwiska.")
    else:
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", new_value):
            request_body = {"password": new_value}
        else:
            messagebox.showerror("Niepoprawne hasło.", "Wprowadzono niepoprawne dane do zmiany hasła.")

    if request_body:
        response_for_updating_user = update_user_request(request_body)
        if response_for_updating_user.status_code == codes.ok:
            if "first_name" in request_body:
                Config.logged_in_user_info.first_name = new_value
            elif "last_name" in request_body:
                Config.logged_in_user_info.last_name = new_value
            else:
                Config.logged_in_user_info.password = new_value

            label["text"] = f"{attribute} {new_value}"
            messagebox.showinfo("Pomyślnie zaktualizowano użytkownika.", "Twój profil został pomyślnie zaktualizowany.")
        elif response_for_updating_user.status_code == codes.created:
            Config.logged_in_user_info.access_token = response_for_updating_user.headers["access-token"]
            update_user_data(label, entry, attribute)
        elif response_for_updating_user.status_code == codes.conflict:
            messagebox.showerror("Nie udało sie zaktualizować użytkownika.",
                                 "Dane, które wpisujesz już istnieją, zmień dane.")
        elif response_for_updating_user.status_code == codes.unauthorized:
            if "Your session has expired" in response_for_updating_user.json():
                messagebox.showerror("Nie udało sie zaktualizować użytkownika.",
                                     "Nie mogliśmy zaktualizować użytkownika z powodu wygaśnięcia sesji."
                                     " Zaloguj się ponownie.")
            else:
                messagebox.showerror("Nie udało sie zaktualizować użytkownika.",
                                     "Z powodu problemu z tokenem dostępu lub problemu z odświeżeniem tokenu dostępu"
                                     " nie mogliśy zaktualizować użytkownika.")
        else:
            messagebox.showerror("Nie udało sie zaktualizować użytkownika.",
                                 "W chwili obecnej nie możemy zaktualizować użykownika, gdyż wystąpił błąd.")


def delete_user(init_authentication_label, root):
    response_for_deleting_user = delete_user_request()
    if response_for_deleting_user.status_code == codes.ok:
        messagebox.showinfo("Pomyślnie usunięto konto.", "Twóje konto zostało pomyślnie usunięte.")
        logout_user(init_authentication_label, root)
    elif response_for_deleting_user.status_code == codes.created:
        Config.logged_in_user_info.access_token = response_for_deleting_user.headers["access-token"]
        delete_user(init_authentication_label, root)
    elif response_for_deleting_user.status_code == codes.unauthorized:
        if "Your session has expired" in response_for_deleting_user.json():
            messagebox.showerror("Nie udało sie usunąć konta.",
                                 "Nie mogliśmy usunąć konta z powodu wygaśnięcia sesji. Zaloguj się ponownie.")
        else:
            messagebox.showerror("Nie udało sie usunąć konta.",
                                 "Z powodu problemu z tokenem dostępu lub problemu z odświeżeniem tokenu dostępu"
                                 " nie mogliśmy usunąć konta.")

    else:
        messagebox.showerror("Nie udało sie usunąć konta.",
                             "W chwili obecnej nie możemy usunąć konta, gdyż wystąpił błąd.")


def add_questions(list_of_entries):
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*?/{}() ]{5,120}$", list_of_entries[0].get()):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*?/{}() ]{2,45}$", list_of_entries[1].get()):
            if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*?/{}() ]{2,45}$", list_of_entries[2].get()):
                if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*?/{}() ]{2,45}$", list_of_entries[3].get()):
                    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*?/{}() ]{2,45}$", list_of_entries[4].get()):
                        if match("^[ABCD]$", list_of_entries[5].get()):
                            if match("^(0|1|2|3|4|5|6|7|8|9|10|11)$", list_of_entries[6].get()):
                                request_body = {
                                      "tresc": list_of_entries[0].get(),
                                      "odp": [
                                         list_of_entries[1].get(),
                                         list_of_entries[2].get(),
                                         list_of_entries[3].get(),
                                         list_of_entries[4].get()
                                      ],
                                      "odp_poprawna": list_of_entries[5].get(),
                                      "trudnosc": int(list_of_entries[6].get())
                                }
                                response_for_adding_questions = add_questions_request(request_body)
                                if response_for_adding_questions.status_code == codes.created:
                                    if "access-token" in response_for_adding_questions.headers:
                                        Config.logged_in_user_info.access_token = \
                                            response_for_adding_questions.headers["access-token"]
                                        add_questions(list_of_entries)

                                    else:
                                        messagebox.showinfo("Pomyślnie dodano pytanie",
                                                            "Twoje pytanie zostało pomyślnie dodane, dziękujemy!")

                                elif response_for_adding_questions.status_code == codes.unauthorized:
                                    if "Your session has expired" in response_for_adding_questions.json():
                                        messagebox.showerror("Nie udalo sie dodać pytania.",
                                                             "Nie mogliśmy dodać pytania z powodu wygaśnięcia sesji."
                                                             " Zaloguj się ponownie.")
                                    else:
                                        messagebox.showerror("Nie udało sie dodać pytania.",
                                                             "Z powodu problemu z tokenem dostępu lub problemu z "
                                                             "odświeżeniem tokenu dostępu nie mogliśmy dodać pytania.")
                                else:
                                    messagebox.showerror("Nie udało sie dodać pytania.",
                                                         "W chwili obecnej nie możemy dodać pytania, "
                                                         "gdyż wystąpił błąd.")
                            else:
                                messagebox.showerror("Błędne dane poziomu trudności pytania.",
                                                     "Poziom trudności pytania powinien być określony od 0 do 11.")
                        else:
                            messagebox.showerror("Błędne dane prawidłowej odpowiedzi",
                                                 "Prawidłowa odpowiedź powinna odpowiadać wielkiej literze:"
                                                 " A, B, C lub D.")
                    else:
                        messagebox.showerror("Błędne dane odpowiedzi D.",
                                             "Odpowiedzi powinny zawierać od 2 do 45 znaków.")
                else:
                    messagebox.showerror("Błędne dane odpowiedzi C.",
                                         "Odpowiedzi powinny zawierać od 2 do 45 znaków.")
            else:
                messagebox.showerror("Błędne dane odpowiedzi B.",
                                     "Odpowiedzi powinny zawierać od 2 do 45 znaków.")
        else:
            messagebox.showerror("Błędne dane odpowiedzi A.",
                                 "Odpowiedzi powinny zawierać od 2 do 45 znaków.")
    else:
        messagebox.showerror("Błędne dane treści pytania.",
                             "Treść pytania powinna zawierać od 5 do 120 znaków.")

