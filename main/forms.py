from django.forms import ModelForm
from .models import Expense,Budget
from django.forms.widgets import TextInput,Select,NumberInput,DateInput


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields =['amount','merchant','category','payment_method','description']
        
        widgets = {
            'category':Select(attrs={'class': "block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6"}),
            'payment_method':Select(attrs={'class': "block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6"}),
            'merchant':TextInput(attrs={'class': "block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6",'placeholder':"Merchant"}),
            'description':TextInput(attrs={'class':"block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6",'placeholder':"Expense description"}),
            'amount':NumberInput(attrs={'class': "block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6",'min':0,'placeholder':"Amount"}),
                       
                       
            }
          
class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields =['amount','start_date','end_date','description','category']
        
        widgets = {
            'category':Select(attrs={'class': "block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6 mt-2"}),
            'start_date':DateInput(attrs={'class': "block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6 mt-2",'placeholder':"Merchant",'type':'date'}),
            'end_date':DateInput(attrs={'class': "block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6 mt-2",'placeholder':"Merchant",'type':'date'}),
            'description':TextInput(attrs={'class':"block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6 mt-2",'placeholder':"Budget description"}),
            'amount':NumberInput(attrs={'class': "block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6 mt-2",'min':0,'placeholder':"Amount"}),
                       
                       
            }
          