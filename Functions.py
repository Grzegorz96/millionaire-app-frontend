# Modules import.
# Module Config for global variables.
import Config
from re import match
from random import choice
from pygame import mixer
from tkinter import messagebox
from tkinter import *
# Module Backend_requests for executing requests.
from Backend_requests import registration_user_request, send_activation_number_request, \
    get_questions_request, login_user_request, get_user_info_request, check_for_registration_request, \
    get_best_scores_request, send_score_request, update_user_request, delete_user_request, add_questions_request
from requests import codes
from sys import exit
# Module User_class for getting User class and making user object.
from User_class import User
from datetime import datetime


def update_date(root, time_label):
    """The function responsible for updating time_label every second."""
    # Assignment new date and time from now to variables.
    date = f"{datetime.now().date()}"
    time = f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
    # Config time_label for new data.
    time_label.config(text=f"{date} {time}")
    # Recursion of function after 1s.
    root.after(1000, update_date, root, time_label)


def download_questions():
    """The function responsible for calling the function sending a request to download questions from database and
    handling the received response. This function is called from Main module one time, when the program starts."""
    # Response variable for get_question_request which located in Backend_requests module.
    response_for_downloading_questions = get_questions_request()
    # If status code of response will be 200, then global variable list_of_questions and its copy will be assigned to
    # [json]
    # list of dictionaries of questions.
    if response_for_downloading_questions.status_code == codes.ok:
        Config.list_of_questions = response_for_downloading_questions.json()["result"]
        Config.current_list_of_questions = Config.list_of_questions.copy()
    # If status code will be 404 or 500 there will display communicate of error and app will automatically close.
    else:
        messagebox.showerror("Błąd podczas pobierania pytań z bazy danych.",
                             "W chwili obecnej nie można pobrać pytań do gry, spróbuj zagrać później.")
        exit()


def load_images():
    """The function responsible for loading static images to global dictionary."""
    try:
        Config.images["background"] = PhotoImage(file="photos/background.png")
    except TclError:
        Config.images["background"] = None
    try:
        Config.images["in_game"] = PhotoImage(file="photos/in_game.png")
    except TclError:
        Config.images["in_game"] = None


def validation_for_register(first_name_entry, last_name_entry, login_entry, password_entry, email_entry,
                            register_window, init_activation_window):
    """The function responsible for validating the data entered for registration and calling the function sending
    the checking registration request. If successful, it will send a request to send the activation number to the user's
    email. The function handles the returned response."""
    # Assigning variables to user's input from entry objects by method .get().
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    # Validations of entered data.
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", first_name):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", last_name):
            if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", login):
                if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", password):
                    if match(
                            "^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9._-]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9._-]+[A-Za-z0-9])\.[A-Za-z0-9]+$",
                            email):
                        # If validations pass, then it will be checked in database whether the user can use the given
                        # login and e-mail.
                        response_for_checking_registration = check_for_registration_request(login, email)
                        if response_for_checking_registration.status_code == codes.ok:
                            # If response has status code 200, then generated activation number will be sent to the
                            # email provided by the user, which is to confirm its authenticity.
                            response_for_sending_number = send_activation_number_request(email)
                            if response_for_sending_number.status_code == codes.ok:
                                # After number will be sent and status code of response is 200, then we can create this
                                # user because login and email is available, but we have to wait for confirmation by the
                                # user's email. Register_window destroys itself and initialize activation_window.
                                register_window.destroy()
                                # Creating activation number from response_body and add them with other variables as
                                # arguments to the function call.
                                activation_number = response_for_sending_number.json()["result"]["activation_number"]
                                init_activation_window(activation_number, first_name, last_name, login, password, email)
                            # If response status from sending number is 404 or 500, then register window destroys and
                            # will be displayed communicate of error.
                            else:
                                register_window.destroy()
                                messagebox.showerror("Nie udało sie wysłać numeru aktywacyjnego.",
                                                     "Wysyłanie numeru aktywacyjnego na podany adres e-mail "
                                                     "nie powiodło sie, spróbuj ponownie później.")
                        # If status code of response for checking registration is 226 then will be displayed communicate
                        # that this login or email is already taken and user have to change this data.
                        elif response_for_checking_registration.status_code == codes.im_used:
                            messagebox.showerror("Nie udało sie utworzyć konta.",
                                                 "Użytkownik o podanym emailu lub loginie, jest już zarejestrowany.")
                        # If status code is 404, 500 then register window destroys and will be displayed communicate
                        # of error.
                        else:
                            register_window.destroy()
                            messagebox.showerror("Nie udało sie utworzyć konta.",
                                                 "Wystąpił problem z utworzeniem konta, spróbuj później.")
                    # Messages displayed when user input validations are invalid.
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
    """The function responsible for checking the activation number. If successful, it will invoke a function that sends
    a request to add a user to the database."""
    # Checking whether the number data entered by the user is consistent with the generated code sent to his email.
    if activation_entry.get() == activation_number:
        # If activation number is correct then program can add this user into database.
        response_for_registration_user = registration_user_request(first_name, last_name, login, password, email)
        # When response status is 201 (user successfully created) the registration window destroys itself and display
        # message about successfully creating and activating the user.
        if response_for_registration_user.status_code == codes.created:
            activation_window.destroy()
            messagebox.showinfo("Użytkownik zarejestrowany i aktywowany.",
                                "Rejestracja oraz aktywacja użytkownika przebiegła pomyślnie,"
                                " możesz zalogować sie na swoje konto.")
        # If status code is 400 and key in response body is "login_error" this mean that someone created user with
        # same login in this time (login and email has unique value in database cant be duplicated).
        elif response_for_registration_user.status_code == codes.bad_request:
            if "login_error" in response_for_registration_user.json():
                activation_window.destroy()
                messagebox.showerror("Nie udało sie utworzyć konta.",
                                     "Użytkownik o podanym loginie jest już zarejestrowany.")
            # If email is already taken.
            elif "email_error" in response_for_registration_user.json():
                activation_window.destroy()
                messagebox.showerror("Nie udało sie utworzyć konta.",
                                     "Użytkownik o podanym adresie e-mail jest już zarejestrowany.")
            # Other errors with status 400.
            else:
                activation_window.destroy()
                messagebox.showerror("Nie udało się utworzyć konta.",
                                     "Utworzenie konta nie powiodła się, spróbuj później.")
        # If status is 404 or 500.
        else:
            activation_window.destroy()
            messagebox.showerror("Nie udało się utworzyć konta.",
                                 "Utworzenie konta nie powiodła się, spróbuj później.")
    # If user's input of activation number is incorrect.
    else:
        messagebox.showerror("Błędy numer aktywacyjny.",
                             f"Wpisany numer aktywacyjny nie pasuje do numeru wysłanego na adres {email}.")


def validation_for_login(login_entry, password_entry, login_window, init_start_label, root):
    """The function responsible for validating the entered data, calling the function sending a request for the user ID
    and JWT tokens, and calling the function sending a request for downloading the logged-in user's data."""
    # Assignment variables to user's input.
    login = login_entry.get()
    password = password_entry.get()
    # Validation user's input.
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", login):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", password):
            # If validation passes, then program send login and password into database by backend and try to take
            # user id and JWT access token and refresh token.
            response_for_login_user = login_user_request(login, password)
            # If status 200, then access and refresh tokens from headers will be assigned to local variables, and
            # local user_id to user id from response body.
            if response_for_login_user.status_code == codes.ok:
                access_token = response_for_login_user.headers["access-token"]
                refresh_token = response_for_login_user.headers["refresh-token"]
                user_id = response_for_login_user.json()["result"]
                # Step 2 is getting information about user, using the received user id and tokens.
                response_for_getting_user_info = get_user_info_request(user_id, access_token, refresh_token)
                # If status 200 then program can log in the user.
                if response_for_getting_user_info.status_code == codes.ok:
                    # Creating dictionary with user info from response body json.
                    user_info = response_for_getting_user_info.json()["result"][0]
                    # Adding to dictionary tokens
                    user_info["access_token"] = access_token
                    user_info["refresh_token"] = refresh_token
                    # Setting global flag on True.
                    Config.is_user_logged_in = True
                    # Creating user object with datas from dictionary.
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

                    # Destroying active_windows.
                    for window in Config.active_windows:
                        window.destroy()

                    Config.active_windows.clear()
                    # Automatically starting start_label with global is_user_logged_in flag=True.
                    init_start_label(root)
                    # Creating a login success message.
                    messagebox.showinfo("Pomyślnie zalogowano.", "Zostałeś pomyślnie zalogowany.")
                # If getting info about user is not 200 (for example 404, 500, 401) then login window crashes and
                # message about error is displayed.
                else:
                    login_window.destroy()
                    messagebox.showerror("Nie udało sie zalogować.",
                                         "W chwili obecnej nie możemy Cię zalogować, spróbuj ponownie później.")
            # If response for login user is 401, it means that user typed wrong data and user with this login and
            # password doesn't exist in database.
            elif response_for_login_user.status_code == codes.unauthorized:
                messagebox.showerror("Błędy login lub hasło.", "Upewnij się, że podany login i hasło są prawidłowe.")
            # If 404/500 then login window crashes and message is displayed.
            else:
                login_window.destroy()
                messagebox.showerror("Nie udało sie zalogować.",
                                     "W chwili obecnej nie możemy Cię zalogować, spróbuj ponownie później.")
        # Messages about validations error of login and password.
        else:
            messagebox.showerror("Niepoprawne hasło.", "Wprowadzono niepoprawne dane hasła.")
    else:
        messagebox.showerror("Niepoprawny login.", "Wprowadzono niepoprawne dane loginu.")


def logout_user(init_authentication_label, root):
    """The function responsible for deleting the user object and changing the login flag to False."""
    # Setting default values of global is_user_logged_in and logged_in_user_info.
    Config.is_user_logged_in = False
    Config.logged_in_user_info = None
    # Initialization authentication label again.
    init_authentication_label(root)
    # Display message about success.
    messagebox.showinfo("Pomyślnie wylogowano.", "Zostałeś pomyślnie wylogowany.")


def draw_question():
    """The function responsible for drawing a question with the appropriate level of difficulty from the list and
    finally deleting it."""
    # Making local list for questions with current difficulty.
    list_of_questions_for_current_difficulty = []
    # Adding into list, questions with specific difficulty from global current_question_number.
    while not list_of_questions_for_current_difficulty:
        for question in Config.current_list_of_questions:
            if question["difficulty"] == Config.current_question_number:
                list_of_questions_for_current_difficulty.append(question)

        # If all questions from a given level are finished, the list will refill.
        if not list_of_questions_for_current_difficulty:
            Config.current_list_of_questions = Config.list_of_questions.copy()

    # Drawing one question from local list with particular difficulty level.
    question = choice(list_of_questions_for_current_difficulty)
    # Removing drawn question from global list of all questions.
    Config.current_list_of_questions.remove(question)
    # Return drawn question to game label.
    return question


def check_answer(question, selected_answer, init_game_label, root, answer_button, list_of_buttons, init_end_label,
                 end_game_button, fifty_fifty_button):
    """The function responsible for preparing the user to check the selected question."""
    def checking():
        """The function responsible for checking selected question called after 4.6s."""
        # Comparing selected answer into value from question["right_answer"].
        if selected_answer == question["right_answer"]:
            # If enter into this statement, theme "win" starts.
            run_theme("win_mp3.mp3")
            # Adding 1 to current_question_number for drawing next level question and init new labels on game_label.
            Config.current_question_number += 1
            # Selected right button will change color on green.
            answer_button.config(bg="green")
            # Checking if user achieve guaranteed amounts. If he did then global guaranteed amount will change.
            if Config.current_question_number == 2:
                Config.guaranteed_amount = 1000
                # Program will run init_game_label after 4.5s.
                root.after(4500, init_game_label, root)
            elif Config.current_question_number == 7:
                Config.guaranteed_amount = 40000
                root.after(4500, init_game_label, root)
            # In case of user achieve 12 question number, global guaranteed amount will assignment into 1 000 000 and
            # program will run init_end_label after 4.5s.
            elif Config.current_question_number == 12:
                Config.guaranteed_amount = 1000000
                current_won = Config.guaranteed_amount
                root.after(4500, init_end_label, root, current_won)
            # In case of user just selected right answer but didn't achieve guaranteed amount then just will run into
            # init_game_label after 4.5s.
            else:
                root.after(4500, init_game_label, root)

        # If user selected wrong answer.
        else:
            # Start fail theme.
            run_theme("fail_mp3.mp3")
            # Setting right button on green light.
            for element in list_of_buttons:
                if question["right_answer"] == element[1]:
                    element[0].config(bg="green")
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


def fifty_fifty(question, list_of_buttons, fifty_fifty_button):
    """The function responsible for randomly rejecting two incorrect answers."""
    # Making object of fifty/fifty sound effect, setting volume on 0.5 and run.
    fifty_fifty_sound = mixer.Sound(r"sounds/fifty_fifty_wav.wav")
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
    # Draw one wrong answer.
    drawn_answer = choice(wrong_answers)
    # Removing drawn wrong answer from list.
    wrong_answers.remove(drawn_answer)
    
    # Config state and text for buttons with second element in wrong_answers. list_of_buttons =
    # [(button.obj,"A")(button.obj,"B")(button.obj,"C")(button.obj,"D")], wrong_answers = ["A","B"].
    for button in list_of_buttons:
        if button[1] in wrong_answers:
            button[0]["state"] = ["disabled"]
            button[0]["text"] = ""


def init_sound_mixer():
    """The function responsible for initializing the sound mixer for application."""
    mixer.init()
    # Setting volume on 0.2.
    mixer.music.set_volume(0.2)


def run_theme(theme1, theme2=False):
    """The function responsible for running themes in application."""
    # Called without queue
    if not theme2:
        mixer.music.load(fr"sounds/{theme1}")
        mixer.music.play()
    # Called with queue
    else:
        mixer.music.load(fr"sounds/{theme1}")
        mixer.music.play()
        mixer.music.queue(fr"sounds/{theme2}", loops=-1)


def download_best_scores(init_best_scores_window=None, limit=None):
    """The function responsible for calling the function sending a request to download the best results from the
    database."""
    # Creating response and calling the get_bet_scores_request.
    response_for_download_best_scores = get_best_scores_request(limit)
    # If response status is 200 then the program will assign json from request body to best scores variable.
    if response_for_download_best_scores.status_code == codes.ok:
        best_scores = response_for_download_best_scores.json()["result"]
        # When user called function with limit (from GUI.init_end_label) then function just returns list of dictionaries
        if limit:
            return best_scores
        # When user called function without limit (from GUI.init_start_label) then function call init_best_scores_window
        # with list of dictionaries in argument.
        else:
            init_best_scores_window(best_scores)
    # If response status is 400, 404 or 500, an error message will be created.
    else:
        messagebox.showerror("Błąd podczas pobierania najlepszych wyników.",
                             "Nie udało się pobrać najlepszych wyników, spróbuj ponownie później.")


def send_score(points):
    """The function responsible for calling the function sending a request to place user's points in the database."""
    # Creating response and calling the send_score_request.
    response_for_sending_score = send_score_request(points)
    # If response status is 201, we have 2 options for this. Second of them is that we got response without
    # "access-token" header so successfully added record to database. First case is we got "access-token" in header, and
    # we have to overwrite access_token in user object and call function again. This endpoint is secured by
    # token_required function, so we need have active access token, when we don't have active access token but our
    # refresh token is active, program on backend automatically create new access token and return it.
    if response_for_sending_score.status_code == codes.created:
        if "access-token" in response_for_sending_score.headers:
            Config.logged_in_user_info.access_token = response_for_sending_score.headers["access-token"]
            send_score(points)
        else:
            messagebox.showinfo("Gratulacje!", f"{Config.logged_in_user_info.first_name}, "
                                               f"Twój wynik trafił do listy najlepszych graczy!")
    # We can get 401 status if is something wrong with our tokens.
    elif response_for_sending_score.status_code == codes.unauthorized:
        # When we got 401 status with "Your session has expired" in key in response body that means that our access
        # token (activity time 15min) has expired, program tried to refresh this token but our refresh token also
        # expired (activity time 10h) so our session has expired, and we need to log in again.
        if "Your session has expired" in response_for_sending_score.json():
            messagebox.showerror("Błąd podczas zapisywania wyniku.",
                                 "Nie mogliśmy zapisać Twojego wyniku z powodu wygaśnięcia sesji."
                                 " Zaloguj się ponownie.")
        # Other problems with access/refresh token.
        else:
            messagebox.showerror("Błąd podczas zapisywania wyniku.",
                                 "Z powodu problemu z tokenem dostępu lub problemu z odświeżeniem tokenu dostępu"
                                 " nie mogliśmy zapisać Twojego wyniku.")
    # If status code is 400, 404, 500.
    else:
        messagebox.showerror("Błąd podczas zapisywania wyniku.",
                             "W chwili obecnej nie możemy zapisać Twojego wyniku, gdyż wystąpił błąd.")


def update_user_data(label, entry, attribute):
    """The function responsible for validating the data entered by the user and calling the function sending a request
    for user updates in the database."""
    # new_value variable from user's input and request_body = None if validation for input would be wrong.
    new_value = entry.get()
    request_body = None
    # If transferred attribute into function is "Imie:" that mean user try to update first_name for user object.
    if attribute == "Imie:":
        # Validation for first_name.
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", new_value):
            # Creating new request body with correct new_value.
            request_body = {"first_name": new_value}
        # If validation fail then message error will create.
        else:
            messagebox.showerror("Niepoprawne imię.", "Wprowadzono niepoprawne dane do zmiany imienia.")
    # If transferred attribute into function is "Nazwisko:" that mean user try to update last_name for user object.
    elif attribute == "Nazwisko:":
        # Validation for last_name.
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", new_value):
            request_body = {"last_name": new_value}
        # If validation fail then message error will create.
        else:
            messagebox.showerror("Niepoprawne nazwisko.", "Wprowadzono niepoprawne dane do zmiany nazwiska.")
    # If transferred attribute into function is "hasło:" that mean user try to update password for user object.
    else:
        # Validation for password.
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", new_value):
            # Creating new request body with correct new_value.
            request_body = {"password": new_value}
        else:
            # If validation fail then message error will create.
            messagebox.showerror("Niepoprawne hasło.", "Wprowadzono niepoprawne dane do zmiany hasła.")
    # When new request_body with first_name, last_name, password key was created then entry in this block.
    if request_body:
        # Creating response and calling the update_user_request.
        response_for_updating_user = update_user_request(request_body)
        # If response status is 200.
        if response_for_updating_user.status_code == codes.ok:
            # Checking what was in request body.
            if "first_name" in request_body:
                # If "first_name" then field first_name in user object will change.
                Config.logged_in_user_info.first_name = new_value
            elif "last_name" in request_body:
                # If "last_name" then field last_name in user object will change.
                Config.logged_in_user_info.last_name = new_value
            else:
                # If "password" then field password in user object will change.
                Config.logged_in_user_info.password = new_value
            # After change in database and user object field, text of imported label from argument is also changed.
            label["text"] = f"{attribute} {new_value}"
            messagebox.showinfo("Pomyślnie zaktualizowano użytkownika.", "Twój profil został pomyślnie zaktualizowany.")
        # Case when we get 201 (created new access token) and we need overwrite user object and call function again.
        elif response_for_updating_user.status_code == codes.created:
            Config.logged_in_user_info.access_token = response_for_updating_user.headers["access-token"]
            update_user_data(label, entry, attribute)
        # Case when we want to change at the same data (409 status).
        elif response_for_updating_user.status_code == codes.conflict:
            messagebox.showerror("Nie udało sie zaktualizować użytkownika.",
                                 "Dane, które wpisujesz już istnieją, zmień dane.")
        # Case when our session has expired, or we have problem with our access or refresh token.
        elif response_for_updating_user.status_code == codes.unauthorized:
            if "Your session has expired" in response_for_updating_user.json():
                messagebox.showerror("Nie udało sie zaktualizować użytkownika.",
                                     "Nie mogliśmy zaktualizować użytkownika z powodu wygaśnięcia sesji."
                                     " Zaloguj się ponownie.")
            else:
                messagebox.showerror("Nie udało sie zaktualizować użytkownika.",
                                     "Z powodu problemu z tokenem dostępu lub problemu z odświeżeniem tokenu dostępu"
                                     " nie mogliśy zaktualizować użytkownika.")
        # Case when we got status 400, 404 or 500.
        else:
            messagebox.showerror("Nie udało sie zaktualizować użytkownika.",
                                 "W chwili obecnej nie możemy zaktualizować użykownika, gdyż wystąpił błąd.")


def delete_user(init_authentication_label, root):
    """The function responsible for calling the function that sends a request to delete the user."""
    # Creating response and calling the delete_user_request.
    response_for_deleting_user = delete_user_request()
    # If response status is 200, creating message and calling logout_user function.
    if response_for_deleting_user.status_code == codes.ok:
        messagebox.showinfo("Pomyślnie usunięto konto.", "Twóje konto zostało pomyślnie usunięte.")
        logout_user(init_authentication_label, root)
    # If response status is 201, overwriting access_token and calling delete_user function again.
    elif response_for_deleting_user.status_code == codes.created:
        Config.logged_in_user_info.access_token = response_for_deleting_user.headers["access-token"]
        delete_user(init_authentication_label, root)
    # If response status is 401, our session has expired, or we have problem with access or refresh token.
    elif response_for_deleting_user.status_code == codes.unauthorized:
        if "Your session has expired" in response_for_deleting_user.json():
            messagebox.showerror("Nie udało sie usunąć konta.",
                                 "Nie mogliśmy usunąć konta z powodu wygaśnięcia sesji. Zaloguj się ponownie.")
        else:
            messagebox.showerror("Nie udało sie usunąć konta.",
                                 "Z powodu problemu z tokenem dostępu lub problemu z odświeżeniem tokenu dostępu"
                                 " nie mogliśmy usunąć konta.")
    # If response status is 404, 409 or 500, creating message with error.
    else:
        messagebox.showerror("Nie udało sie usunąć konta.",
                             "W chwili obecnej nie możemy usunąć konta, gdyż wystąpił błąd.")


def add_questions(list_of_entries):
    """The function responsible for validating the data entered by the user and calling the function sending a request
    to add a question to the database."""
    # Validations for user's entry: content, answer A, answer B, answer C, answer D, right answer, difficulty.
    if match("^.{5,120}$", list_of_entries[0].get()):
        if match("^.{2,45}$", list_of_entries[1].get()):
            if match("^.{2,45}$", list_of_entries[2].get()):
                if match("^.{2,45}$", list_of_entries[3].get()):
                    if match("^.{2,45}$", list_of_entries[4].get()):
                        if match("^[ABCD]$", list_of_entries[5].get()):
                            if match("^(0|1|2|3|4|5|6|7|8|9|10|11)$", list_of_entries[6].get()):
                                # If everything ok, then creating request_body with json of question.
                                request_body = {
                                      "content": list_of_entries[0].get(),
                                      "answers": [
                                         list_of_entries[1].get(),
                                         list_of_entries[2].get(),
                                         list_of_entries[3].get(),
                                         list_of_entries[4].get()
                                      ],
                                      "right_answer": list_of_entries[5].get(),
                                      "difficulty": int(list_of_entries[6].get())
                                }
                                # Creating response and calling the add_questions_request with request body.
                                response_for_adding_questions = add_questions_request(request_body)
                                # If response status is 201.
                                if response_for_adding_questions.status_code == codes.created:
                                    # If we got "access_token" header in 201 status, we need to overwrite user object
                                    # and call again add_questions function.
                                    if "access-token" in response_for_adding_questions.headers:
                                        Config.logged_in_user_info.access_token = \
                                            response_for_adding_questions.headers["access-token"]
                                        add_questions(list_of_entries)
                                    # If we got 201 without "access-token" header we create message for user that
                                    # successfully added question.
                                    else:
                                        for element in list_of_entries:
                                            element.delete(0, END)
                                        messagebox.showinfo("Pomyślnie dodano pytanie",
                                                            "Twoje pytanie zostało pomyślnie dodane, dziękujemy!")
                                # If we got 401, our session has expired, or we have problem with access or refresh
                                # token.
                                elif response_for_adding_questions.status_code == codes.unauthorized:
                                    if "Your session has expired" in response_for_adding_questions.json():
                                        messagebox.showerror("Nie udalo sie dodać pytania.",
                                                             "Nie mogliśmy dodać pytania z powodu wygaśnięcia sesji."
                                                             " Zaloguj się ponownie.")
                                    else:
                                        messagebox.showerror("Nie udało sie dodać pytania.",
                                                             "Z powodu problemu z tokenem dostępu lub problemu z "
                                                             "odświeżeniem tokenu dostępu nie mogliśmy dodać pytania.")
                                # If we got 400, 404 or 500, creating other error message.
                                else:
                                    messagebox.showerror("Nie udało sie dodać pytania.",
                                                         "W chwili obecnej nie możemy dodać pytania, "
                                                         "gdyż wystąpił błąd.")
                            # Bad for user's entry: content, answer A, answer B, answer C, answer D, right answer, or
                            # difficulty.
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
