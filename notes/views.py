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


# для шифрования
import random
import sympy
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
from sympy import isprime


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


# далее воспринимаем это как Боба - бэкенд


def generate_prime():
    flag = 1
    while flag!=0:
        num = random.randint(100, 1000)  # Задайте нужный диапазон для p
        num2=(num - 1) // 2
        if fermat_test(num)==True and fermat_test(num2)==True:
            flag=0
        else:
            flag=1
    return num


def fermat_test(n, k=10):
    if n <= 1:
        return False
    for _ in range(k):
        a = random.randint(1, n-1)
        if pow(a, n-1, n) != 1:
            return False
        return True


def primitive_root(p):
    primitive_roots = [i for i in range(2, p) if is_primitive_root(i, p)]
    return random.choice(primitive_roots)


def is_primitive_root(a, p):
    if a % p == 1:
        return False
    return all(pow(a, (p - 1) // i, p) != 1 for i in factorize(p - 1))


def factorize(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


p = generate_prime()
g = primitive_root(p)
b = random.randint(1, 100)
B = pow(g, b) % p  # Вычисление открытого ключа B


@csrf_exempt
def generate_params(request):
    # p = generate_prime()
    # g = primitive_root(p)
    # b = random.randint(1, 100)
    # B = pow(g, b, p)  # Вычисление открытого ключа B
    return JsonResponse({'p': p, 'g': g, 'b':b, 'B': B})

@csrf_exempt
def calculate_result(request):
    if request.method == 'POST':
        # Получаем значение A из тела запроса
        A = int(request.POST.get('A'))

        # Выполняем оставшиеся шаги алгоритма Диффи-Хеллмана на бекенде
        K = pow(A, b) % p  # где b - закрытый ключ бекенда, p - простое число

        # Отправляем общий секретный ключ обратно на фронтенд
        return JsonResponse({'result': K})
    else:
        # Возвращаем ошибку для запросов с методами, отличными от POST
        return JsonResponse({'error': 'Invalid request method'})
