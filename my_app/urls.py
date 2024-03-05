from django.urls import path
# from .views import user_form, many_fields_form, add_user, upload_image
from .views import hello # , HelloView, index, about, post_full, author_posts
# from .views import year_post, MonthPost, post_detail
# from .views import my_view
# from .views import TemplIf, view_for
from .views import total_in_db, total_in_view, total_in_template


urlpatterns = [
    path('', hello, name='hello'),
    # path('hello2/', HelloView.as_view(), name='hello2'),
    # path('posts/<int:year>/', year_post, name='year_post'),
    # path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    # path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    # path('', my_view, name='index'),
    # path('if/', TemplIf.as_view(), name='templ_if'),
    # path('for/', view_for, name='templ_for'),
    # path('index/', index, name='index'),
    # path('about/', about, name='about'),
    # path('author/<int:author_id>/', author_posts, name='author_posts'),
    # path('post/<int:post_id>/', post_full, name='post_full'),
    # path('user/add/', user_form, name='user_form'),
    # path('forms/', many_fields_form, name='many_fields_form'),
    # path('user/', add_user, name='add_user'),
    # path('upload/', upload_image, name='upload_image'),
    path('db/', total_in_db, name='db'),
    path('view/', total_in_view, name='view'),
    path('template/', total_in_template, name='template'),

]


