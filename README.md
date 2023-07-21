![logo frontend](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/1b1610c8-d435-47a3-92be-df9ce009fef5)
# MILLIONAIRE.app

Millionaire.app is my original project, a clone of the popular millionaires game show. The program allows users to join the community and compete with each other, thanks to the system of points received after the end of the game. All operations using data in this application are performed through the API and database at pythonanywhere hosting. This program is written and optimized for windows.


## Features

- Login/ Logout.
- Register/ Deleting account.
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

**Client:** Python, Tkinter, Pygame.mixer, requests

**Server:** Python, Flask, SQL (MySQL)


## Installation

### To quickly launch the application on windows:
- Make new directory on your computer.
- Download millionaire-app-frontend repository:
```bash
 git clone https://github.com/Grzegorz96/millionaire-app-frontend.git
```
- Enter the directory exe_millionaire_app.
- Run Millionaire_app.exe.

### For manually launching the application on the IDE:
#### Requirements:
- Python 3.11
- pygame 2.5.0
- requests 2.31.0
#### Instruction:
- Make new directory on your computer.
- Download millionaire-app-frontend repository:
```bash
 git clone https://github.com/Grzegorz96/millionaire-app-frontend.git
```
- Open the "Frontend" on your IDE.
- Install required packages on your venv:

```bash
  pip install pygame
  pip install requests 
```
- Run Main.py:
```bash
 py .\Main.py
```
Program Millionaire.app connects to the enpoints on the cloud server, you don't need to create a local server.


## Lessons Learned

While creating this project, I learned how to combine many programs. I've worked on different libraries with different technologies. I had to implement JWT tokens myself so that the frontend program could catch the returned new access tokens, overwrite the expired one in the user object and repeat the query again. I created user login and registration logic so that all processes are safe for the user. Another challenge was the implementation of the e-mail sender to confirm the user's e-mail before registering. I learned to connect with the proprietary API that performs queries on the database. It also took me a long time to catch most of the bugs and handle them. I also increased my skills in creating program logic. I gained knowledge about the implementation of graphic and sound files in the application.


## Authors

- [@Grzegorz96](https://www.github.com/Grzegorz96)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Screnshoots

![apka](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/a1fe5e2d-9e49-4e17-bfb3-f1ed88d97cec)
![apka z oknami](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/58ccf70d-99da-4838-be5c-1840164cb002)

![apka z wynikami](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/b07055e6-c47f-4e70-af77-8828d4a2b2fb)

![email](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/5b353fd9-2afc-4918-9471-5cda04d8b7f2)

![pytania](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/161bd253-1113-4a90-a6b9-8469a4cc9100)

![end panel](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/62011be5-f93a-448e-84e6-276d6ad7e8bc)

![gra](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/d2adaff7-aa17-405a-ab40-4e8cc9db2f06)

![aktywacja](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/2004f0e4-f070-441e-81fa-6a02ced31fa6)

![uzytkownik](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/40a62b7b-5231-4fc8-8fa2-cb5da70a3269)
















