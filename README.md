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

![Home Page Screen Shot][home-screenshot]

<p>
    My oldest son has recently acquired an interest in money from around the world and started building a collection. When it got beyond a collection of 30 different
    coins in various langauges, it became difficult for us to keep track of which coins came from where. So I built this compact project for my son to keep track
    of what currency he already has and what countries he still needs for his collection.
</p>

<p>
    On the home page, you can see a visual representation of the countries already in your collection as well as a table that displays a listing of the countries 
    that you are missing from your collection.
</p>

</div>
<div id="built-with">

### Built With

* [Django](https://www.djangoproject.com/)
* [Python](https://www.python.org/)
* [JQuery](https://jquery.com)

<p align="right">(<a href="#top">back to top</a>)</p>
</div>

<!-- GETTING STARTED -->
<div id="getting-started">

## Getting Started

Below are instructions for setting up this project on your local machine. The shell commands below are written with Linux Ubuntu in mind. If you are using a different operating system, your instructions may vary.
</div>
<div id="prerequisites">

### Prerequisites

* [Python 3.6+](https://www.python.org/downloads/)
* Python 3.6+ virtual environment
  ```sh
  sudo apt install python3-venv
  ```
</div>
<div id="installation">
    
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kaido1224/currencytracker.git
   ```
2. Navigate to the project directory created.
   ```sh
   cd currencytracker
   ```
3. Setup Python virtual environment
   ```sh
    python3 -m venv ve
   ```
4. Activate the new virtual environment
    ```sh
    . ve/bin/activate
    ```
5. Update pip
   ```sh
    pip install -U pip
   ```
6. Install the requirements file
   ```sh
    pip install -r requirements.txt
   ```
7. If you didn't already have Postgres installed, follow the instructions below to set it up.
   ```sh
    sudo -u postgres createuser --superuser --createdb --pwprompt usernamehere
   ``` 
8. Create a database for CurrencyTracker in Postgres, assign it to your user.
   ```sh
    psql
    create database currency with owner usernamehere;
    \q
   ```
9. Create a secrets.py file under settings.
   ```sh
    sudo vim currency/settings/secrets.py
   ```

   Inside of the file, create a secrets dictionary similar to the below:
    ```py
    secrets_dict = {
        "SECRET_KEY": "DJANGOSECRETKEYHERE",
        "DB_USER": "YOURPOSTGRESUSERHERE",
        "DB_PASSWORD": "YOURPOSTGRESUSERPWHERE"
    }
   ```
    
   After that, save and exit.

10. Apply database migrations. If you want prepopulated data, access <i>myapp.0002_auto_20211210_0311.py</i> under myapp/migrations and uncomment out the
    book creation and currency bulk_create sections.
    ```sh
     ./manage.py migrate
    ```

11. Create a superuser to log into the project.
    ```sh
    ./manage.py createsuperuser
    ```

12. If done correctly, you should now be able to run CurrencyTracker in a development environment.
    ```sh
    ./manage.py runserver
    ```

13. In your browser, navigate to http://127.0.0.1:8000, you should see a login screen. Use the credentials you created in step 11 to login.

    ![Login Screen Shot][login-screenshot]

<p align="right">(<a href="#top">back to top</a>)</p>
</div>

<!-- USAGE EXAMPLES -->
<div id="usage">

## Usage

<p>This project currently has three main pages. The first, is the home page already discussed <a href="#about">above</a>. The other two pages, book management
and collection management, both contain similar sub pages and can be accessed in the left-hand navigation menu. A more detailed explanation of these two management pages, and their underlying models is described below.
</p>
    
#### Book Management

<p>Before you create entries into your collection, you must first create a book that you can assign your collection entries to. On the book management page you can view your existing collection books, add a new one, edit existing book details or delete books and their associated collections.</p>
    
![Book Management Page Screen Shot][book-management-screenshot]
    
<p>Below is a brief description of the fields associated to a book.</p>

| Field | Value | Description | Required? |
| ----------- | ----------- | ----------- | ----------- |
| Description | String, up to 100 characters | You can enter the title of the book here. Otherwise, if you are like my son, whose collection books don't have a title, enter a description of the book instead. | Yes |
| Pages | Integer | The number of pages in the book. At this time, this isn't used for anything. | No |
| Rows Per Page | Integer | The number of rows on a given page. At this time, this isn't used for anything. | No |
| Columns Per Row | Integer | The number of columns on a given row on a page. At this time, this isn't used for anything. | No |


#### Collection Management

<p>Once you've created a book for your collection, you can begin using the collection management page. On this page, similar to the book management page, you can view your existing collection entries, add a new one, or edit or delete existing entries.</p>
    
![Collection Management Page Screen Shot][collection-management-screenshot]
    
<p>Below is a brief description of the fields associated to a collection entry. Most of the fields are not required to allow you to fill in the information that 
    you know now and can fill in the rest of the information later.</p>
    
| Field | Value | Description | Required? |
| ----------- | ----------- | ----------- | ----------- |
| Book | Book ID |  The book the collection entry is located in. | Yes |
| Page | Integer | The page in the book the entry is located in. | No |
| Row | Integer | The row on the page the entry is located in. | No |
| Column | Integer | The column in the row the entry is located in. | No |
| Currency | String, up to 100 characters | The name of the currency, such as a Euro Cent or Peso. | No |
| Value | Decimal | The value of the currency. | No |
| Type | String, 4 characters. Should be either a bill or coin. | No |
| Country | String, 2 character ISO code for the country. | No |
    
<p>There are certain countries that share a currency with several other nations and are grouped together as a different "country". These special exceptions are shown below.
</p>
    
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[home-screenshot]: currency/static/images/home.png
[login-screenshot]: currency/static/images/login.png
[book-management-screenshot]: currency/static/images/book_management.png
[collection-management-screenshot]: currency/static/images/collection_management.png
