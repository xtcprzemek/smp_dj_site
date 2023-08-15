#from django.shortcuts import render
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView, 
    DetailView,
    )
# Create your views here.

from .models import Note

class NoteListView(ListView):
    model = Note
    template_name ="notes_list.html"
    