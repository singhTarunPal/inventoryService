from django.db import models

class BookInventory(models.Model):
   book_number = models.CharField(max_length=20)
   count = models.IntegerField()
   added_on = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
       return self.inventory_id