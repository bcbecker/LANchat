# LANchat
This web chat app was built using Flask, Jinja, an SQLite3 database, and SocketIO. It will run locally, and by changing the environment variables, could run on LAN as well. A virtual environment is included as a method of providing necessary library access, but the requirements.txt file can be executed just the same.


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

## Creating .env file

For this server to run, you must create a .env file, setting the following paramters:
```bash
TESTING=False
DEBUG=True
SECRET_KEY=
SERVER=0.0.0.0
```
Set the secret key to whatever you'd like! Server is set to 0.0.0.0 for localhost.

## Running the Server

```bash
cd website
python main.py
```

## Viewing the website

Site can be found here: http://0.0.0.0:5000
(for localhost)


## Clearing Message History

To clear the message history, simply delete the `messages.db` file.
