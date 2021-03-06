from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('todos/', views.todos_index, name='index'),
    path('todos/<int:todo_id>/', views.todos_detail, name='todos_detail'),
    path('todos/create/', views.TodoCreate.as_view(), name='todos_create'),
    path('todos/<int:pk>/update/', views.TodoUpdate.as_view(), name='todos_update'),
    path('todos/<int:pk>/delete/', views.TodoDelete.as_view(), name='todos_delete'),
    path('accounts/signup/', views.signup, name='signup'),



    path('notes/', views.notes_index, name='notes_index'),
    path('notes/<int:note_id>/', views.notes_detail, name='notes_detail'),
    path('notes/create/', views.NoteCreate.as_view(), name='notes_create'),
    path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='notes_update'),
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='notes_delete'),

    path('todos/<int:todo_id>/add_photo/', views.add_photo, name='add_photo'),
    

]