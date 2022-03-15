# LANchat
LANchat was designed as a lightweight, self-contained chat room for a wireless local area network. In particular, it was designed to run on a Raspberry Pi serving to WLAN. LANchat uses SocketIO to host a real-time updating session for users to message each other. And, in case you want to view the message history, there's a feature for that too!

This project is not currently live.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Improvements](#improvements)


## General Information
LANchat is a straightforward and self-contained chat server, designed to be downloaded by the end user and configured on their own device. While this may sound daunting for some, the purpose of doing so is to not rely on any outside resources, which keeps the footprint and maintenance to a minimum, while still giving you the benefit of a private chat server. Users can message back and forth in real-time, and since it's only on your local network, there's no need to worry about unwanted visitors to your chatroom (that is, if your network is properly secured).

The overall goal for this project was to build something small and usable, while learning a new skill. I like projects that require me to learn as I go, and the skills I acquire throughout help me to expand my horizon as a developer. I had not written much JavaScript before diving into this project, and afterword, I feel much more confident in using asynchronous JavaScript and jQuery. I took a more 'JavaScript-centric' (client-side rendering) approach to the functions I would normally handle server-side. This was done to become more comfortable with client-side rendering, fetching data from a backend API rather than relying on server-side rendering to reload pages.


## Technologies Used
- Flask, a micro-framework
    - SocketIO for bi-directional communication
    - Jinja2 templating engine
- Local SQLite3 database
- Bootstrap CSS
- JavaScript, jQuery


## Features
- User sign in with name only to enter chat
- Full message thread, organized by time sent
- User message history, organized by time sent
- Session messages for users entering/leaving


## Setup
Ensure python 3.9 is installed.

Install requirements:
```bash
pip install -r requirements.txt
```

Or, access virtual environment:
```bash
pip install pipenv
pipenv shell
```

### Creating .env file
For this server to run, you must create a .env file within the package, setting the following parameters:
```bash
TESTING=
DEBUG=
SECRET_KEY=
SERVER=0.0.0.0
```
Set the secret key to whatever you'd like! Server is set to 0.0.0.0.

### Running the Server
```bash
python run.py
```

### Viewing the website
Site can be found here: http://0.0.0.0:5000
(for localhost)

### Clearing Message History
To clear the message history, simply delete the `messages.db` file.


## Improvements
Improvements:
- Upgrade the testing suite, maybe using Selenium for functional testing
- Create a web-facing version that has numerous chatrooms
    - Oauth, Cloud DB
- End to end encryption

To Do:
- Data transfer limit
