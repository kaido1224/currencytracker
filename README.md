# currencytracker
A world currency collection tracker app I made for my son.

Apollo Setup Instructions
===================
Instructions below are for setting up Apollo in a Linux Ubuntu environment.

Install a python virtual environment.
    
```sh
$ sudo apt install python3-venv
```

Next, clone the repository from github.

```sh
$ git clone https://github.com/kaido1224/currencytracker.git

$ cd currencytracker

# Setup virtual environment
$ python3 -m venv ve

# Activate new virtual environment
$ . ve/bin/activate

# Update pip
$ pip install -U pip

# Install everything necessary to run CurrencyTracker.
$ pip install -r requirements.txt
```

If you don't already have Postgres setup on your system, follow the instructions below to set it up.

```sh
$ sudo -u postgres createuser --superuser --createdb --pwprompt usernamehere
```

Create a database for CurrencyTracker in Postgres, assign it to your user.

```sh
$ psql
> create database currencytracker with owner usernamehere;
>\q
```

Create a secrets.py file under settings.
```sh
sudo vim currency/settings/secrets.py
```

Inside of the file, create a secrets dictionary similar to the below:
```python
secrets_dict = {
    "SECRET_KEY: "DJANGOSECRETKEYHERE",
    "DB_USER": "YOURPOSTGRESUSERHERE",
    "DB_PASSWORD: "YOURPOSTGRESUSERPWHERE"
}
```

After that, save and exit.

```sh
# Apply database models.
$ ./manage.py migrate

# Create a superuser to log into the project.
$ ./manage.py createsuperuser
```

If done correctly, you should now be able to run CurrencyTracker in a development environment.

```sh
$ ./manage.py runserver
```

In the browser, navigate to http://127.0.0.1:8000.
