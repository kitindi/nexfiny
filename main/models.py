from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256, null=True)

class Expense(models.Model):
    
    EXPENSE_CATEGORY = (('Education', 'Education'),('Groceries', 'Groceries'),('Transportation', 'Transportation'),('Utilities', 'Utilities'),('Fixed expenses', 'Fixed expenses'),("Shopping", 'Shopping'))
    PAYMENT_METHOD = (('Cash', 'Cash'),('Credit card', 'Credit card'),('Debit card', 'Debit card'),('Bank transfer', 'Bank transfer'),('Mobile money', 'Mobile money'))
    amount = models.IntegerField(null=True)
    merchant = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, choices=EXPENSE_CATEGORY, null=True)
    date = models.DateField(default =now)
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD, null=True)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.category+ " " +"  payed to  " + " "+ self.merchant + " through "+ " " + self.payment_method 
    
    
    class Meta:
        ordering=["-date"]


class Income(models.Model):
    pass


class Budget(models.Model):
    BUDGET_CATEGORY = (('Education', 'Education'),('Groceries', 'Groceries'),('Transportation', 'Transportation'),('Utilities', 'Utilities'),('Fixed expenses', 'Fixed expenses'),('Savings contributions', 'Savings contributions'),("Shopping", 'Shopping'))
    
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    date_created = models.DateTimeField(null=True,default =now)
    amount = models.IntegerField(null=True)
    category = models.CharField(max_length=255, null=True, choices = BUDGET_CATEGORY)
    description = models.TextField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   
    
    def __str__(self):
        return self.category
    

