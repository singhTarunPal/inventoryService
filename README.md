# Inventory Service

*Description:* Its a webservice to manage the inventory of books

*Author:* Tarun Pal Singh

*Design:* ITs a Microservice with Django and SQLite 
 
## Setting up env
 - InstallPython 	 
 - Create virtualenv for windows
 	- py -m venv project-name
 - Activate virualenv for windows
 	- venv\Scripts\activate
 - Install Django on the enviroment
 	- py -m pip install Django
 - Upgrading PIP
 	- python -m pip install --upgrade pip

## Running Service
- >activate
- >python manage.py runserver

## API
 - GET http://127.0.0.1:8000/api/bookInventory/
   - Get all the inventory
   - Sample Response: [{  "book_number": "2", "count": 15  },    {   "book_number": "3",  "count": 10 }]

 - GET http://127.0.0.1:8000/api/bookInventory/2
   - Get all the inventory(count) of a particular book
   - Sample Response: [    {        "book_number": "1",        "count": 13    }]

 - POST 
    - http://127.0.0.1:8000/api/bookInventory/
   - creates an inventory(add a row)
      - { "book_number": "1",     "count": 10 }

 - PUT 
    - http://127.0.0.1:8000/api/bookInventory/
   - update an inventory(update a row)
      - { "book_number": "1",     "count": 12 }

References:

