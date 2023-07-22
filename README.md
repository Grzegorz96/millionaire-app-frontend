![logo frontend](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/1b1610c8-d435-47a3-92be-df9ce009fef5)
# MILLIONAIRE.app

MILLIONAIRE.app is my original project, a clone of the popular millionaires game show. The program allows users to join the community and compete with each other, thanks to the system of points received after the end of the game. All operations using data in this application are performed through the API and database at pythonanywhere hosting. This program is written and optimized for windows.  


## Description of the modules

The program consists of 6 modules and each of them is responsible for something else. The Backend_requests.py module is responsible for sending and receiving API requests, Config.py contains global variables for the entire project, GUI.py is responsible for displaying graphics in the program. The Functions.py module is the link between the GUI and Backend_requests and is used to perform various functions, this module catches the new access tokens returned and overwrites the expired access tokens with them in the user object, it is also responsible for validating the data entered by the user. Decides what to do with the entered data and what to do with the received data from Backend_requests.py. It also takes care of all login/logout and registration logic. Responsible for game logic, sounds and clock. This is a very important module in the whole program. User_class.py contains the user's class and the last Main.py is the executive file for all these modules.


## Features

- Two-step login verification
- Log out
- Three-step registration verification
- Deleting account
- JSON Web Token for user authentication.
- Sending emails with an activation number to the account.
- Adding your own questions by the user.
- Updating and displaying logged in user.
- Displaying top players.
- Adding top players.
- Automatic refresh of JWT access tokens.
- Download questions from the database and randomizing questions to the user, taking into account the current level.
- Sounds system.
- 50/50 function.
- Ending the game with a guaranteed amount during a wrong answer, arbitrarily withdrawing from the game or by answering all questions correctly.


## Technology used

**Client:** 
- Languages: Python
- Third Party Libraries: Tkinter, Pygame, requests

**Server:** 
- Languages: Python, SQL
- Third Party Libraries: Flask, PyJWT, mysql-connector-python, python-dotenv


## Installation

### To quickly launch the application on windows:
- Download millionaire-app-frontend repository:
```bash
 git clone https://github.com/Grzegorz96/millionaire-app-frontend.git
```
- Enter the directory millionaire-app-frontend/exe_millionaire_app.
- Run Millionaire_app.exe.

### For manually launching the application on the IDE:
#### Requirements:
- Python 3.11
- pygame 2.5.0
- requests 2.31.0
#### Instruction:
- Download millionaire-app-frontend repository:
```bash
 git clone https://github.com/Grzegorz96/millionaire-app-frontend.git
```
- Open the millionaire-app-frontend on your IDE.
- Install required packages on your venv:

```bash
  pip install pygame
  pip install requests 
```
- Run Main.py:
```bash
 py .\Main.py
```
Program MILLIONAIRE.app connects to the enpoints on the cloud server, you don't need to create a local server.


## Lessons Learned

While creating this project, I learned how to combine many programs. I've worked on different libraries with different technologies. I had to implement JWT tokens myself so that the frontend program could catch the returned new access tokens, overwrite the expired one in the user object and repeat the query again. I created user login and registration logic so that all processes are safe for the user. Logging in consists of 2 steps, the first is to check whether the given user is in the database, then if so, downloading his id and creating a JWT for him, the next query is a request for information about this user, using the ID and access token. Registration consists of 3 steps, the first is to check if the given user is not already in the database, the next is to check if the given email really belongs to the user by sending the user an e-mail to verify the e-mail address before registration, the last step is to place the user in the database. I think implementing these functions took me the most time but also learned a lot how to solve problems. I learned to connect with the proprietary API that performs queries on the database. It also took me a long time to catch most of the bugs and handle them. I increased my skills in creating program logic. I gained knowledge about the implementation of graphic and sound files in the application. 


## Features to be implemented

- The function of adding more questions from a .json file after prior validation. There is already such a function on the backend.
- The function of resetting the password to the account via a code sent to the e-mail.
- The function of restoring a deleted account via a code sent to an e-mail.


## Authors

- [@Grzegorz96](https://www.github.com/Grzegorz96)


## Contact

E-mail: grzesstrzeszewski@gmail.com


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Screnshoots
##### Screenshot of the user authorization panel
##### Screenshot of the login and registration window
![apka](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/a1fe5e2d-9e49-4e17-bfb3-f1ed88d97cec)
![apka z oknami](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/58ccf70d-99da-4838-be5c-1840164cb002)
##### Screenshot of the highscore list
##### Screenshot of the add questions panel
![apka z wynikami](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/b07055e6-c47f-4e70-af77-8828d4a2b2fb)
![pytania](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/161bd253-1113-4a90-a6b9-8469a4cc9100)
##### Screenshot of end game panel
##### Screenshot of the game panel
![end panel](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/62011be5-f93a-448e-84e6-276d6ad7e8bc)
![gra](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/d2adaff7-aa17-405a-ab40-4e8cc9db2f06)
##### Screenshot of the window for entering the generated activation number from the e-mail
##### Screenshot of the panel for changing user data
![aktywacja](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/2004f0e4-f070-441e-81fa-6a02ced31fa6)
![uzytkownik](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/40a62b7b-5231-4fc8-8fa2-cb5da70a3269)
##### Email sent from the email sender
![email](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/5b353fd9-2afc-4918-9471-5cda04d8b7f2)
