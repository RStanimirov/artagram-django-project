# artagram-django-project
This is the Django website I made for the SoftUni Python Web module

This project targets an audience of conceptual artists, designers and visual art enthusiasts in general. Accordingly, the name of the web application - Artagram - explicitly directs the user's attention to the topic of Art. *Note that this project is in its early stage of development and some of the features, including its name, could be changed at a later stage.

## Key concepts and functionalities:

- **- User authentication and authorization** - extending the Django User by applying the One-To-One Link With a User Model (Profile). Some additionl functionalities added on top of the built-in User class.

- **- Dynamic art blog** with the possibility of commenting and evaluating a given art post by all registered users.

- **- Protection against unauthorized changes** to the content of the posts � only the author of a given post could change the content or delete the entire post. Otherwise, a 403 Forbidden is loaded.

- **- Post's author has the full set of CRUD operations.** They can edit the post, add comments, and delete it entirely.

- **- Artagram rank system** - a special feature in this website is the implemented user rank system. When the users get registered, they start at the entry level - "Apprentice". The more posts they publish, the faster they climb on the rank ladder of Artagram and are endowed with the relevant badges. 

- **- Responsive design** - when rendering the site on tablets and smartphones, the navigation automatically collapses into a button, the site content is arranged vertically section by section.

- **- Search bar** for finding key-words in the content of the posts - available only for registered users.

- **- Pagination** - one of the reasons to use CBV for the page view is the built-in pagination they provide.

- **- Automatic image resizing algorithm** to save storage space. Width and height of images are resized to max. 600 pixels, which allows for extreme economy of uploaded images.

- **- Password reset** - implemented through Django's built-in PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView. An smtp server is setup and tested for succesfully receiving password change emails.

- **- Customized admin section of the site** - the models are displayed not only in the form of a list, but now also in tabular form with set fields, and where applicable, with customized filters and keyword search.

- **- Dark theme** - the website is set to comply with the client's custom browser theme.

### Technologies used:

- Backend: Django Web Framework
- Frontend: HTML5, CSS (Bootstrap4, Crispy Forms, Custom CSS), JavaScript
- Database: PostgreSQL

### How to setup and test this app:

 - Download the code and unzip it
 - Open the unzipped directory with an IDE such as Pycharm or Visual Studio Code
 - Create a virtual environment (optional but recommended)
 - Add a secret key of your choice in the settings.py (e.g. SECRET_KEY = 'TestApp1234567890')
 - Database: if you want to use SQLite, just uncomment the sqlite3 database code in settings.py; otherwise, in order to use PostgreSQL, you have to setup you own database name, username, password, host, and port. 
 - Email backend: just to test the app, you normally do not need the EMAIL_BACKEND info (at the bottom of the settings.py), so you can comment it out. However, if you want to be able to send emails through the site's contact form and keep the password reset functionality, you have to setup your own backend info, smtp server, host and password.
 - Install the dependencies by running "pip install -r requirements.txt" in yoiur IDE's terminal.
 - Finally, migrate the model data to the database by running "python manage.py migrate"


Co. Artagram Django Project 2022

