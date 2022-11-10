<div align="center">
  <h2 align="center">Simple Votings</h2>
  <p align="center">Web service for online voting</p>
</div>


### About the project

The product is a website that provides users with the option to create votings and participate in them.

The project was developed by a small team of developers as part of an developers course.

##### Features:
* User accounts
* User's profile page
* Option to create a new voting and set it up
* 3 types of choice: multiple choice, checkboxes, binary choice
* Option to show/hide the vote number before voting's end
* Option of anonymous voting
* 3 states of votings: under creation, underway, ended
* Search of votings with its name or its author's login
* Different search filters
* Target OS – Linux, Windows 10

##### Technology stack:
* `Python 3.10`
* `Django 3.1.4`
* `SQLite 3.22`

### Usage

##### Project setting up
1. Clone the repository
    ```sh
    git clone https://github.com/Melyohin-AA/simple_votings.git
    ```
2. Create Python virtual environment
3. Activate the virtual environment
4. Install required packages
    ```sh
    pip install -r requirements.txt
    ```
5. Synchronize the database
    ```sh
    manage.py migrate
    ```

##### Starting server
1. Activate the virtual environment
2. Run server
    ```sh
    python manage.py runserver --insecure
    ```

### Demo

Youtube video:<br>
[![Demo](https://img.youtube.com/vi/uhkOR7ubrAA/0.jpg)](https://www.youtube.com/watch?v=uhkOR7ubrAA)
