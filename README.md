# OCR-Projet8
Créez une plateforme pour amateurs de Nutella

## Prerequisites
* Download this repository
* You must have python3 installed on your computer, otherwise you can follow the guides on python's website https://www.python.org/downloads/
* Set your current directory in the project:
```cd path/to/folder/downloaded```
* run on your console/terminal the following command:
```pip3 install -r requirements.txt```
* deploy on heroku

## Environment variables
You need to export following variables to your environment:

    * EMAIL_PASSWORD : Password of the email used to send mails
    * SECRET_KEY : Django's secret key
    * SQL_PASSWORD : Password used to connect to postgres' database


## Commands

* You must populate the database using "python manage.py populate_database True"
* You can empty the database using "python manage.py empty_database True"

## Program design
* directory _build : directory containing generated documentation
* directory accounts : directory containing account / authenticatation related files
* directory catalog : directory containing product / favorite / database related files
* directory ocrProjet8 : directory containing main application related files
* directory scrapping : directory containing openfoodfact data scrapping related files
* directory search : directory containing search engine related files
* directory source : directory containing base files for creating documentation
* directory staticfiles : directory containing staticfiles

## Tests
Tests are divided in 3 categories:
* units: inside each modules
* features: inside ocrProjet8/tests/feature
* integration: inside ocProjet8/tests/integration

Tests are run using "python manage.py test"

## Author
**Mehdi Bichari** - [GitHub Repo](https://github.com/Kaik-a/)

## Acknowledgements
I want to make a special thank to Julien Jacquelinet who helped me all along this project and all the openclassrooms community !
