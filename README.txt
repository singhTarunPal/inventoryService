# Inventory Service

Its a webservice based on Django and SQLite

*Design*
 - ITs a Microservice with Django and SQLite 

 
*API - Book Inventory*
 - GET http://127.0.0.1:8000/api/bookInventory/
 - GET http://127.0.0.1:8000/api/bookInventory/CSE110

 - POST http://127.0.0.1:8000/api/bookInventory/
  -- {
  --     "book_number": "CSE121",
  --     "count": 12
  -- }

 - PUT http://127.0.0.1:8000/api/bookInventory/
  -- {
  --     "book_number": "CSE121",
  --     "count": 12
  -- }

References:
 - C:\_PROJECTS\_GITHUB\inventoryService\inventory-service\Scripts>activate
 - (inventory-service) C:\_PROJECTS\_GITHUB\inventorymicroservicePRJ>python manage.py runserver
