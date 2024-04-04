from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Expense, Budget
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ExpenseForm,BudgetForm
from django.core.paginator import Paginator
import datetime
from django.http import JsonResponse
import json
from django.db.models import Sum
import datetime
# Create your views here.

@login_required(login_url='login')
def dashboard_view(request):
    expenses = Expense.objects.filter(owner=request.user)
    budgets = Budget.objects.filter(owner=request.user)
    lables = ['Education','Groceries','Transportation','Utilities','Fixed expenses',"Shopping"]
    lables_budgets = []
    
    # for a pie chart
    expenses_data =[] 
    
    # for a bar chart
    mothly_expenses_bar = []
    
    # for a bar chart
    monthly_savings = []
    
    total_expenses =0
    total_mothly_budget = 0
   
    expense_percentages = []
    savings_amount = 0
    
    # pagination for expense listings
    paginator = Paginator(expenses,4)
    page_number = request.GET.get('page')
    page_object = Paginator.get_page(paginator,page_number)

# calculate the category besed expenses amount for the current month
    today = datetime.datetime.now()
    for category in lables:
        total = 0
        for expense in expenses:
            if category == expense.category  and expense.date.month == today.month :
                total += expense.amount
        expenses_data.append(total) 
   
# calculate total mothly expense for the current month
    today = datetime.datetime.now()
    for expense in expenses:
            if expense.category != 'Savings contributions' and expense.date.month == today.month:
                total_expenses += expense.amount
                                                  
        

# calculate total mothly savings for the current month
    today = datetime.datetime.now()
    for budget in budgets:
        if budget.date_created.month == today.month:
                total_mothly_budget += budget.amount           
        
        

# generate a monthly total expenses for each month 

    for month in range(1,13):
        total = 0
        for expense in expenses:
            if expense.date.month == month:
                total += round(expense.amount,0)
            
        mothly_expenses_bar.append(total)
 
                
# generate a monthly savings for each month 

    for month in range(1,13):
        total = 0
        for budget in budgets:
            if budget.date_created.month == month and budget.category == "Savings contributions":
                total += round(budget.amount,0)
            
        monthly_savings.append(total)
    
# calculate % of expense to the current month budget 

    edu_percentage = 0
    edu_budget = 0
    gro_percentage = 0
    gro_budget = 0
    trans_percentage = 0
    trans_budget = 0
    util_percentage =0
    util_budget =0
    fixed_percentage =0
    fixed_budget =0
    shop_percentage =0
    shop_budget =0
    for budget in budgets: 
        if budget.category == "Education" and budget.date_created.month == today.month:
            edu_percentage = (expenses_data[0]/budget.amount)*100
            edu_budget = budget.amount
        if budget.category == "Groceries" and budget.date_created.month == today.month:
            gro_percentage = (expenses_data[1]/budget.amount)*100
            gro_budget = budget.amount
    
        if budget.category == "Transportation" and budget.date_created.month == today.month:
            trans_percentage = (expenses_data[2]/budget.amount)*100
            trans_budget = budget.amount
    
        if budget.category == "Utilities" and budget.date_created.month == today.month:
            util_percentage = (expenses_data[3]/budget.amount)*100
            util_budget = budget.amount
    
        if budget.category == "Utilities" and budget.date_created.month == today.month:
            util_percentage = (expenses_data[3]/budget.amount)*100
            util_budget = budget.amount
    
        if budget.category == "Fixed expenses" and budget.date_created.month == today.month:
            fixed_percentage = (expenses_data[4]/budget.amount)*100
            fixed_budget = budget.amount
            
        if budget.category == "Shopping" and budget.date_created.month == today.month:
            shop_percentage = (expenses_data[5]/budget.amount)*100
            shop_budget = budget.amount
    
        
                
                
    
    balance = total_mothly_budget - total_expenses- savings_amount          
    context = {"expenses":page_object,"labels":lables,"data":expenses_data,"expenses_data":mothly_expenses_bar,"savings_data":monthly_savings, "total_expenses":total_expenses,"total_budget":total_mothly_budget, 'balance':balance,"edu_percent":edu_percentage,'edu_budget':edu_budget,'gro_percentage':gro_percentage,'gro_budget':gro_budget,'trans_percent':trans_percentage,'trans_budget':trans_budget,'util_percentage':util_percentage,'util_budget':util_budget, 'fixed_percentage':fixed_percentage,'fixed_budget':fixed_budget, 'shop_percentage':shop_percentage,'shop_budget':shop_budget, 'today':today}
    return render(request, 'main/dashboard.html', context)




@login_required(login_url='login')
def all_expenses(request):
    all_expenses = Expense.objects.filter(owner=request.user)
    
    # adding pagination
    paginator = Paginator(all_expenses,5)
    page_number = request.GET.get('page')
    page_object = Paginator.get_page(paginator,page_number)
    context ={"expenses": page_object}
    return render(request, 'main/expenses.html', context)


@login_required(login_url='login')
def add_expenses(request):
    
    form = ExpenseForm()
    context ={"form": form}
    
    if request.method == 'GET':
        return render(request, 'main/add_expense.html', context)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        
        if form.is_valid():
            data = form.save(commit=False)
            data.owner = request.user
            data.save()
            
            return redirect("all-expenses")
        
        

@login_required(login_url='login')
def edit_expenses(request,pk):
    expense = Expense.objects.get(id=pk)
    form = ExpenseForm(instance=expense)
    context ={"form": form}
    
    if request.method == 'GET':
        return render(request, 'main/edit_expense.html', context)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        
        if form.is_valid():
            data = form.save(commit=False)
            data.owner = request.user
            data.save()
            
            return redirect("all-expenses")
        
    

@login_required(login_url='login')
def delete_expenses(request,pk):
     expense = Expense.objects.get(id=pk)
     expense.delete()
     
     return redirect("all-expenses")
 
 
@login_required(login_url='login') 
def expense_category_summary(request):
    today_date = datetime.date.today()
    three_moths_ago = today_date - datetime.timedelta(days=30*6)
    expenses = Expense.objects.filter(owner= request.user, dat__gte=three_moths_ago, date_lte=today_date)
    
    final_rep ={}
    
    def get_category(expense):
        return expense.category
    
    category_list= list(set(map(get_category,expenses)))
    
    def get_category_amount(category):
        amount =0
        filtered_by_category =expenses.filter(category=category)
        for item in filtered_by_category:
            amount += item.amount
        return amount
    
    for x in expenses:
        for y in category_list:
            final_rep[y] = get_category_amount(y)
    
    return JsonResponse({'expense_category_data': final_rep}, safe=False)
    
@login_required(login_url='login') 
def budget(request):
    budgets =Budget.objects.filter(owner=request.user)
    show =[]
    
    today = datetime.datetime.now()
    for budget in budgets:
        if budget.date_created.month == today.month:
            show.append(budget)
                
                
    context = {"budgets": show, 'today':today}
    return render(request, 'main/budget.html', context)

@login_required(login_url='login') 
def add_budget(request):
    budgets =Budget.objects.filter(owner=request.user)
    existing_categories = []
    for budget in budgets:
        existing_categories.append(budget.category)
    form = BudgetForm()
    context = {'form': form}
    if request.method == 'GET':
        return render(request, 'main/add_budget.html', context)
    
    if request.method == 'POST':
        
        category_value = request.POST['category']
        if category_value in existing_categories:
            messages.success(request,"The budget category already exists")
            return render(request, 'main/add_budget.html', context)
        else:
            form = BudgetForm(request.POST)
            if form.is_valid():
                data = form.save(commit=False)
                data.owner = request.user
                data.save()
                
                return redirect("budget")
        
@login_required(login_url='login')   
def edit_budget(request,pk):
    budget = Budget.objects.get(id=pk)
    form = BudgetForm(instance=budget)
    context ={"form": form}
    
    if request.method == 'GET':
        return render(request, 'main/edit_budget.html', context)
    
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        
        if form.is_valid():           
            data = form.save(commit=False)
            data.owner = request.user
            data.save()    
    return redirect("budget")
      