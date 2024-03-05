# from django.views import View
# from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse


# from django.views.generic import TemplateView
#
# from my_app.models import Author, Post
#
#
def hello(request):
    return HttpResponse("Hello World from function!")


#
#
# class HelloView(View):
#     def get(self, request):
#         return HttpResponse("Hello World from class!")
#
#
# def year_post(request, year):
#     text = ""
#     ...  # формируем статьи за год
#     return HttpResponse(f"Posts from {year}<br>{text}")
#
#
# class MonthPost(View):
#     def get(self, request, year, month):
#         text = ""
#         ...  # формируем статьи за год и месяц
#         return HttpResponse(f"Posts from {month} / {year} <br> {text}")
#
#
# def post_detail(request, year, month, slug):
#     ...  # Формируем статьи за год и месяц по идентификатору. Пока обойдёмся без запросов к базе данных
#     post = {
#         "year": year,
#         "month": month,
#         "slug": slug,
#         "title": "Кто быстрее создаёт списки в Python, list() или []",
#         "content": "В процессе написания очередной программы задумался над тем, "
#                    "какой способ создания списков в Python работает быстрее..."
#     }
#     return JsonResponse(post, json_dumps_params={'ensure_ascii': False})
#
#
# def my_view(request):
#     context = {"name": "John"}
#     return render(request, "my_app/my_template.html", context)
#
#
# class TemplIf(TemplateView):
#     template_name = "my_app/templ_if.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['message'] = "Привет, мир!"
#         context['number'] = 5
#         return context
#
#
# def view_for(request):
#     my_list = ['apple', 'banana', 'orange']
#     my_dict = {
#         'каждый': 'красный',
#         'охотник': 'оранжевый',
#         'желает': 'жёлтый',
#         'знать': 'зелёный',
#         'где': 'голубой',
#         'сидит': 'синий',
#         'фазан': 'фиолетовый',
#     }
#     context = {'my_list': my_list, 'my_dict': my_dict}
#     return render(request, 'my_app/templ_for.html', context)
#
#
# def index(request):
#     return render(request, "my_app/index.html")
#
#
# def about(request):
#     return render(request, "my_app/about.html")
#
#
# def author_posts(request, author_id):
#     author = get_object_or_404(Author, pk=author_id)
#     posts = Post.objects.filter(author=author).order_by('-id')[:5]
#     return render(request, 'my_app/author_posts.html', {'author': author, 'posts': posts})
#
#
# def post_full(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     return render(request, 'my_app/post_full.html', {'post': post})
#

# import logging
# from django.shortcuts import render
# from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget, ImageForm
# from .models import User
# from django.core.files.storage import FileSystemStorage

# logger = logging.getLogger(__name__)
#
#
# def user_form(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             age = form.cleaned_data['age']
#             # Делаем что-то с данными
#             logger.info(f'Получили {name=}, {email=}, {age=}.')
#     else:
#         form = UserForm()
#     return render(request, 'my_app/user_form.html', {'form': form})
#
#
# def many_fields_form(request):
#     if request.method == 'POST':
#         form = ManyFieldsFormWidget(request.POST)
#         if form.is_valid():
#             # Делаем что-то с данными
#             logger.info(f'Получили {form.cleaned_data=}.')
#     else:
#         form = ManyFieldsFormWidget()
#     return render(request, 'my_app/many_fields_form.html', {'form': form})
#
#
# def add_user(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         message = 'Ошибка в данных'
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             age = form.cleaned_data['age']
#             logger.info(f'Получили {name=}, {email=}, {age=}.')
#             user = User(name=name, email=email, age=age)
#             user.save()
#             message = 'Пользователь сохранён'
#     else:
#         form = UserForm()
#         message = 'Заполните форму'
#     return render(request, 'my_app/user_form.html', {'form': form, 'message': message})
#
#
# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.cleaned_data['image']
#             fs = FileSystemStorage()
#             fs.save(image.name, image)
#     else:
#         form = ImageForm()
#     return render(request, 'my_app/upload_image.html', {'form': form})


from django.shortcuts import render
from django.db.models import Sum
from my_app.models import Product


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'my_app/total_count.html', context)


def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 'my_app/total_count.html', context)


def total_in_template(request):
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'my_app/total_count.html', context)


