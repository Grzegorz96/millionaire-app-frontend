![logo](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/logo.png)

# MILLIONAIRE.app

MILLIONAIRE.app is my original creation, a desktop application version, serving as a clone of the popular TV game show "Who Wants to Be a Millionaire." Users can take on the role of a player and compete with other participants in a points-based ranking system. All data-related operations are conducted through a dedicated API interface and a database. Additionally, the program is designed in such a way that upon user login, a session is automatically created, lasting until logout, program exit, or automatic expiration, ensuring convenience and security in using the application through the use of JSON Web Tokens. This program is written and optimized for Windows.


## Description of the modules

The program consists of 6 modules, each of which plays a unique role in the functioning of the application. Below is a brief description of each module:

Backend_requests.py:
- The Backend_requests.py module is responsible for sending and receiving API requests. It serves as a connector to the backend, where validated data is sent to the server.

Config.py:
- The Config.py module contains global variables for the entire project. Enables the proper functioning of the program by providing global settings.

GUI.py:
- The GUI.py module is responsible for displaying graphics in the program. It initializes new graphic panels in the application and is the interface between the user and the program.

Functions.py:
- The Functions.py module serves as a connection between GUI.py and Backend_requests. Intercepts new access tokens and overwrites expired access tokens in the user object. Responsible for validating user-entered data. Decides what to do with the entered data and how to proceed with the data received from Backend_requests.py. Manages the logic of login, logout, and registration. Responsible for the game logic, sounds, and clock.

User_class.py:
- The User_class.py contains the user class, which is used to create an object that stores user data.

Main.py:
- The Main.py module is a executive file for all these modules. Acts as a connector between individual modules.


## Features

- Two-step login verification:
###### - Getting access token, refresh token and user id.
###### - Getting informations about user using tokens and id.
- User logout.
- Three-step registration verification:
###### - Checking if the user is not already in the database.
###### - Email confirmation by the user with an activation code.
###### - Placing validated user data in the database.
- Deleting account.
- JSON Web Token for user authentication.
- Sending emails with an activation number to the account.
- Adding your own questions by the user.
- Updating and displaying logged in user.
- Displaying scores of top players.
- Adding scores of top players.
- Automatic refresh of JWT access tokens.
- Download questions from the database and randomizing questions to the user, taking into account the current level.
- Sounds system.
- Random rejection of two incorrect answers. 
- System of points.
- Clock updating every second.
- Ending the game with a guaranteed amount during a wrong answer, arbitrarily withdrawing from the game or by answering all questions correctly.
- Validation of entered data.
- Handling response errors from the server.
- Dynamic display of the list of in-game amounts.
- Automatic replenishment of the question list when the questions run out.

## Technology used

**Client:** 
- Languages: Python
- Third Party Libraries: Tkinter, Pygame, requests

**Server:** 
- Languages: Python, SQL
- Third Party Libraries: Flask, PyJWT, mysql-connector-python, python-dotenv
- Hosting for API: www.pythonanywhere.com
- Hosting for MySQL database: www.pythonanywhere.com


## Installation

### To quickly launch the application on Windows:
- Download millionaire-app-frontend repository:
```bash
 git clone https://github.com/Grzegorz96/millionaire-app-frontend.git
```
- Enter the directory millionaire-app-frontend/millionaire_app_exe.
- If you want to move the Millionaire_app.exe file, do it together with the sounds and photos folders. You can also create a copy of the .exe file on your desktop.
- Run Millionaire_app.exe.

### For manually launching the application on the IDE:
#### Requirements:
##### Programs and libraries:
- Python 3.11.1
- IDE, for example Pycharm
- pygame 2.5.0
- requests 2.31.0
#### Instruction:
- Download millionaire-app-frontend repository:
```bash
 git clone https://github.com/Grzegorz96/millionaire-app-frontend.git
```
- Go to the millionaire-app-frontend directory.
- Open the millionaire-app-frontend on your IDE.
- Create virtual enviroment for the project (Windows):
```bash
 py -m venv venv
```
- Activate virtual enviroment (Windows):
```bash
 venv/Scripts/activate.bat
```
- Install required packages on your activated virtual enviroment:
```bash
 pip install -r requirements.txt
```
- or
```bash
 pip install pygame==2.5.0
 pip install requests==2.31.0
```
- Run Main.py on Windows:
```bash
 py .\Main.py
```
Program MILLIONAIRE.app connects to the enpoints on the cloud server, you don't need to create a local backend server.


## Lessons learned

During the creation of this project, I acquired the skill of integrating various programs and worked with different libraries and technologies. The necessity of independently implementing JWT tokens allowed me to capture newly returned access tokens in the frontend program, overwrite expired tokens in the user object, and repeat queries. I developed the logic for user login and registration, ensuring a secure execution of all processes. The login process consists of two steps: first, checking if the user exists in the database, and then, if so, retrieving their ID and creating a JWT token for them. The subsequent query involves obtaining information about this user using the identifier and access token. The registration process involves three steps: initially checking if the user does not already exist in the database, then verifying the authenticity of the provided email address by sending an email with activation number for address verification before registration, finally, if the user confirms the authenticity of the email address, it will be added to the database. I believe that implementing these functions was the most time-consuming, but it also taught me effective problem-solving. I learned how to connect with a dedicated API interface that conducts queries to the database and learned techniques for capturing and handling errors. Additionally, my skills in creating the logical structure of the program were enhanced, and I acquired knowledge about implementing graphic and sound files in the application.


## Features to be implemented

- The function of adding more questions from a .json file after prior validation. There is already such a function on the backend.
- The function of resetting the password to the account via a code sent to the e-mail.
- The function of restoring a deleted account via a code sent to an e-mail.
- Questions added should not go directly to the "questions" table, but first to a substitute table, and only after the administrator's verification should they be transferred to the main table.
- Loading of sound files into the global "sounds" dictionary when running Main.py. During operation, the program will use sounds stored in memory instead of reading them directly from the computer's path.


## Authors

[@Grzegorz96](https://www.github.com/Grzegorz96)


## Contact

E-mail: grzesstrzeszewski@gmail.com


## License

[MIT](https://github.com/Grzegorz96/millionaire-app-frontend/blob/master/LICENSE.md)


## Screnshoots
##### Screenshot of the user authorization panel
![authorization_panel](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/main_label.png)
##### Screenshot of the login and registration window
![login_register_windows](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/login_register_windows.png)
##### Screenshot of the window for entering the generated activation number from the e-mail
![activate_account](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/activate_account.png)
##### Screenshot of start panel after logged in
![logged_in](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/logged_in.png)
##### Screenshot of the add questions panel
![questions_page](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/questions_page.png)
##### Screenshot of the user panel
![user_page](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/user_page.png)
##### Screenshot of the game panel
![game](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/game.png)
##### Screenshot of the selected answer in the game
![seleced_answer](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/selected_answer.png)
##### Screenshot of selecting the correct answer in the game
![right_answer](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/right_answer.png)
##### Screenshot of using the 50/50 feature
![fiftyfifty](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/fiftyfifty.png)
##### Screenshot of choosing the wrong answer in the game
![wrong_answer](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/wrong_answer.png)
##### Screenshot of end game panel
![end panel](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/end_label.png)
##### Screenshot of the highscore list
![results](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/results.png)
##### Email sent from the email sender
![email_activation_number](https://raw.githubusercontent.com/Grzegorz96/millionaire-app-frontend/master/docs/readme-images/email_activation_number.png)
