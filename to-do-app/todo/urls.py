from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('todopage/', views.todo, name='todo'),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:srno>', views.delete_todo, name='delete_todo'),
    path('signout/', views.signout, name='signout'),
]
