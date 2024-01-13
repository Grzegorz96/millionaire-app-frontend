![logo frontend](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/1b1610c8-d435-47a3-92be-df9ce009fef5)
# MILLIONAIRE.app

MILLIONAIRE.app is my original project, a clone of the popular millionaires game show. The program allows users to take on the role of a millionaire player and compete with other players in the score ranking, thanks to the system of points. All operations using data in this application are performed through the proprietary API and database at pythonanywhere hosting. This program is written and optimized for Windows.  


## Description of the modules

The program consists of 6 modules and each of them is responsible for something else. The Backend_requests.py module is responsible for sending and receiving API requests, Config.py contains global variables for the entire project, GUI.py is responsible for displaying graphics in the program. The Functions.py module is the link between the GUI and Backend_requests and is used to perform various functions, this module catches the new access tokens returned and overwrites the expired access tokens with them in the user object, it is also responsible for validating the data entered by the user. Decides what to do with the entered data and what to do with the received data from Backend_requests.py. It also takes care of all login/logout and registration logic. Responsible for game logic, sounds and clock. This is a very important module in the whole program. User_class.py contains the user's class and the last Main.py is the executive file for all these modules.


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
- Install required packages on your virtual enviroment:
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
Program MILLIONAIRE.app connects to the enpoints on the cloud server, you don't need to create a local server.


## Lessons Learned

While creating this project, I learned how to combine many programs. I've worked on different libraries with different technologies. I had to implement JWT tokens myself so that the frontend program could catch the returned new access tokens, overwrite the expired one in the user object and repeat the query again. I created user login and registration logic so that all processes are safe for the user. Logging in consists of 2 steps, the first is to check whether the given user is in the database, then if so, downloading his id and creating a JWT for him, the next query is a request for information about this user, using the ID and access token. Registration consists of 3 steps, the first is to check if the given user is not already in the database, the next is to check if the given email really belongs to the user by sending the user an e-mail to verify the e-mail address before registration, the last step is to place the user in the database. I think implementing these functions took me the most time but also learned a lot how to solve problems. I learned to connect with the proprietary API that performs queries on the database and how to catch bugs and handle them. I increased my skills in creating program logic. I gained knowledge about the implementation of graphic and sound files in the application. 


## Features to be implemented

- The function of adding more questions from a .json file after prior validation. There is already such a function on the backend.
- The function of resetting the password to the account via a code sent to the e-mail.
- The function of restoring a deleted account via a code sent to an e-mail.
- Questions added should not go directly to the "questions" table, but first to a substitute table, and only after the administrator's verification should they be transferred to the main table.
- Loading of sound files into the global "sounds" dictionary when running Main.py. During operation, the program will use sounds stored in memory instead of reading them directly from the computer's path.


## Authors

- [@Grzegorz96](https://www.github.com/Grzegorz96)


## Contact

E-mail: grzesstrzeszewski@gmail.com


## License

[MIT](https://github.com/Grzegorz96/millionaire-app-frontend/blob/master/LICENSE.md)


## Screnshoots
##### Screenshot of the user authorization panel
![apka](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/a1fe5e2d-9e49-4e17-bfb3-f1ed88d97cec)
##### Screenshot of the login and registration window
![apka z oknami](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/58ccf70d-99da-4838-be5c-1840164cb002)
##### Screenshot of the window for entering the generated activation number from the e-mail
![aktywacja](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/2004f0e4-f070-441e-81fa-6a02ced31fa6)
##### Screenshot of start panel after logged in
![apka logged in](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/9cdef175-761b-45c3-bf20-4fd9bc7f26a1)
##### Screenshot of the add questions panel
![pytania](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/161bd253-1113-4a90-a6b9-8469a4cc9100)
##### Screenshot of the user panel
![uzytkownik](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/40a62b7b-5231-4fc8-8fa2-cb5da70a3269)
##### Screenshot of the game panel
![gra](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/d2adaff7-aa17-405a-ab40-4e8cc9db2f06)
##### Screenshot of the selected answer in the game
![seleced](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/788f5fd3-4cb6-435c-b2db-738f7622ec61)
##### Screenshot of selecting the correct answer in the game
![right](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/d12a189b-9126-47f6-829e-32d667f68e51)
##### Screenshot of using the 50/50 feature
![5050](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/e9cbb604-fbfb-4970-86de-57d331ec3bdf)
##### Screenshot of choosing the wrong answer in the game
![falilure](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/a7094e29-b1b2-4030-81fd-c3d911a2f272)
##### Screenshot of end game panel
![end panel](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/62011be5-f93a-448e-84e6-276d6ad7e8bc)
##### Screenshot of the highscore list
![apka z wynikami](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/b07055e6-c47f-4e70-af77-8828d4a2b2fb)
##### Email sent from the email sender
![email](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/5b353fd9-2afc-4918-9471-5cda04d8b7f2)
