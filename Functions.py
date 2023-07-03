import mysql.connector
import Config
from random import choice


def download_questions():
    connection = mysql.connector.connect(host="127.0.0.1", user="root", password="User96",
                                         database="millionarie",
                                         auth_plugin="mysql_native_password")
    cur = connection.cursor(dictionary=True)
    try:
        query = """SELECT content, A, B, C, D, right_answer, difficulty FROM questions"""
        cur.execute(query)

    except mysql.connector.Error as message:
        print(message)

    else:
        Config.list_of_questions = cur.fetchall()

    finally:
        connection.close()
        cur.close()


def draw_question():
    list_of_questions_for_current_difficulty = []
    for question in Config.list_of_questions:
        if question["difficulty"] == Config.current_question_number:
            list_of_questions_for_current_difficulty.append(question)
    question = choice(list_of_questions_for_current_difficulty)
    # Removing drawn question from list of all questions
    Config.list_of_questions.remove(question)

    return question


def check_answer(question, selected_answer, init_game_label, root, answer_button, list_of_buttons, init_end_label,
                 end_game_button, fifty_fifty_button):
    def checking():
        if selected_answer == question["right_answer"]:
            Config.current_question_number += 1
            answer_button.config(bg="green")

            if Config.current_question_number == 2:
                Config.guaranteed_amount = 1000
                root.after(3000, init_game_label, root)
            elif Config.current_question_number == 7:
                Config.guaranteed_amount = 40000
                root.after(3000, init_game_label, root)
            elif Config.current_question_number == 12:
                Config.guaranteed_amount = 1000000
                current_won = Config.guaranteed_amount
                root.after(3000, init_end_label, root, current_won)

            else:
                root.after(3000, init_game_label, root)
        else:
            # setting right button on green light
            for obj in list_of_buttons:
                if question["right_answer"] == obj[1]:
                    obj[0].config(bg="green")
            # setting selected button on red light
            answer_button.config(bg="red")

            current_won = Config.guaranteed_amount
            root.after(3000, init_end_label, root, current_won)

    # setting state buttons on disabled
    for obj in list_of_buttons:
        obj[0]["state"] = ["disabled"]
    end_game_button["state"] = ["disabled"]
    fifty_fifty_button["state"] = ["disabled"]


    # config color of selected button on yellow
    answer_button.config(bg="yellow")
    # checking after 3s
    root.after(3000, checking)


def fifty_fifty(question, list_of_buttons, fifty_fifty_button):
    Config.is_fifty_fifty_available = False
    fifty_fifty_button["state"] = ["disabled"]
    fifty_fifty_button.config(bg="#473a3a")
    wrong_answers = ["A", "B", "C", "D"]
    wrong_answers.remove(question["right_answer"])
    drawn_answer = choice(wrong_answers)
    wrong_answers.remove(drawn_answer)

    for button in list_of_buttons:
        if button[1] in wrong_answers:
            button[0]["state"] = ["disabled"]
            button[0]["text"] = ""
