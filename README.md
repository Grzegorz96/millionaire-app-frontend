![logo frontend](https://github.com/Grzegorz96/millionaire-app-frontend/assets/129303867/1b1610c8-d435-47a3-92be-df9ce009fef5)
# MILLIONAIRE.app

Millionaire.app is my original project, a clone of the popular millionaires game show. The program allows users to join the community and compete with each other, thanks to the system of points received after the end of the game. All operations using data in this application are performed through the API and database at pythonanywhere hosting. 


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
