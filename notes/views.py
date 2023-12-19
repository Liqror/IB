# notes / views.py

from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'note_list.html'
    context_object_name = 'notes'
    ordering = ['-id']

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('notes:note-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('notes:note-list')


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'note_confirm_delete.html'
    success_url = reverse_lazy('notes:note-list')


class RegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy('login'))  # Перенаправление на страницу логина
        return render(request, self.template_name, {'form': form})
