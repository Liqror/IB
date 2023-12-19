# notes/urls.py
from django.urls import path
from .views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView

app_name = 'notes'

urlpatterns = [
    path('list/', NoteListView.as_view(), name='note-list'),
    path('create/', NoteCreateView.as_view(), name='note-create'),
    path('<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]
