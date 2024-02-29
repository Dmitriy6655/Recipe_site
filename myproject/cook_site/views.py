import logging


from django.http import HttpRequest, HttpResponse

from cook_site.models import Recipes, RecipesCategory, Image


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

logger = logging.getLogger(__name__)


# Регистрация пользователя
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'cook_site/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'cook_site/register.html', {'form': form})


# Вход пользователя

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'cook_site/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('posts')

        # form is not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'cook_site/login.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('login')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def get_recipes(request: HttpRequest):
    title = "List Recipes"
    recipes = Recipes.objects.all()
    recipescategory = RecipesCategory.objects.filter()

    if request.method == 'POST':
        rec_id = request.POST['number']
        recept = Recipes.objects.get(pk=rec_id)

        context = {
            'title': title,
            "recipes": recept,
            'recipescategory': recipescategory

        }
        return render(request, "cook_site/rec_list.html", context=context)


    else:
        context = {
            'title': title,
            "recipes": recipes,
            'recipescategory': recipescategory

        }
        return render(request, "cook_site/recipes.html", context=context)





def get_goods(request):
    title = 'Просмотр рецепта'

    if request.method == 'POST':
        rec_id = request.POST['number']
        recept = Recipes.objects.get(pk=rec_id)

        # print(f'type= {type(id_prod)}')
        # print(f'client_id= {client_id}')
        # amount = request.POST['amount']

        context = {
            'text': 'Клиент:',
            'title': title,
            'recept': recept

        }
        return render(request, "cook_site/rec_list.html", context=context)




def main(request):
    context = {
        'title': 'Главная страница',
        'goods': Recipes.objects.order_by('name', 'description')
    }
    logger.info(f'context: {context}')
    return render(request, 'cook_site/index.html', context)


def all_clients(request: HttpRequest) -> HttpResponse:
    # clients_with_order_counts = Client.objects.annotate(order_count=Count("order"))
    clients_with_order_counts = Recipes.objects.all()
    return render(
        request, "cook_site/index.html", context={"clients": clients_with_order_counts}
    )

