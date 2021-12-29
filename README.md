<div id="top"></div>

<h3 align="center">Currency Tracker</h3>

<div align="center">
    <p>
        A compact Django project built to keep track of a world currency (money) collection for my son.
    </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
<div id="about">

## About The Project

![Product Name Screen Shot][product-screenshot]

<p>
    My oldest son has recently acquired an interest in money from around the world and started building a collection. When it got beyond a collection of 30 different
    coins in various langauges, it became difficult for us to keep track of which coins came from where. So I built this compact project for my son to keep track
    of what currency he already has and what countries he still needs for his collection.
</p>

<p>
    On the home page, you can see a visual of the countries already in your collection as well as a table that displays a listing of the countries that you are missing
    from your collection.
</p>

<p align="right">(<a href="#top">back to top</a>)</p>
</div>
<div id="built-with">

### Built With

* [Django](https://www.djangoproject.com/)
* [Python](https://www.python.org/)
* [JQuery](https://jquery.com)

<p align="right">(<a href="#top">back to top</a>)</p>
</div>

# Currency Tracker
A world currency collection tracker app I made for my son.

Setup Instructions
===================
Instructions below are for setting up CurrencyTracker in a Linux Ubuntu environment.

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

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: currency/static/home.PNG
