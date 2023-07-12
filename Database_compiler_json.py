import mysql.connector
from json import load

with open("pytanka.json", encoding="utf8") as json_file:
    questions = load(json_file)

query = """INSERT INTO questions(content, A, B, C, D, right_answer, difficulty) VALUES"""

for dictionary in questions:
    content = dictionary["tresc"]
    a = dictionary["odp"][0]
    b = dictionary["odp"][1]
    c = dictionary["odp"][2]
    d = dictionary["odp"][3]
    right_answer = dictionary["odp_poprawna"]
    difficulty = dictionary['trudnosc']

    if questions.index(dictionary) < (len(questions)-1):
        query += f""" (\"{content}\", \"{a}\", \"{b}\", \"{c}\", \"{d}\", \"{right_answer}\", {difficulty}),"""

    else:
        query += f""" (\"{content}\", \"{a}\", \"{b}\", \"{c}\", \"{d}\", \"{right_answer}\", {difficulty})"""

connection = mysql.connector.connect(host="127.0.0.1", user="root", password="User96",
                                     database="millionarie",
                                     auth_plugin="mysql_native_password")
cur = connection.cursor()
try:
    cur.execute(query)
    connection.commit()

except mysql.connector.Error as message:
    print(message)

else:
    print("Pomyślnie dodano pytania do bazy danych")

finally:
    connection.close()
    cur.close()
