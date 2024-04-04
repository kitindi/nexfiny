from django.urls import path
from . import views
from user_profile.views import *


urlpatterns = [
    path("", views.dashboard_view, name='dashboard'),
    path("expenses/", views.all_expenses, name='all-expenses'),
    path("expenses/add/", views.add_expenses, name='add-expense'),
    path("expenses/edit/<int:pk>", views.edit_expenses, name='edit-expense'),
    path("expenses/delete/<int:pk>", views.delete_expenses, name='delete-expense'),
    path("expenses_summary/", views.expense_category_summary, name='expense-summary'),
    path("budget/", views.budget, name='budget'),
    path("budget/add/", views.add_budget, name='add_budget'),
    path("budget/edit/<int:pk>", views.edit_budget, name='edit-budget'),
    path("profile/", profile_view, name='profile'),
]
