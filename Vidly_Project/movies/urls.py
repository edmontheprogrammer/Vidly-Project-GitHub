from django.urls import path
from . import views

# movies/ --> root url or home page of the
# 'movies' app
# movies/1/details

app_name = 'movies'
urlpatterns = [
    # mapping the 'urls' to view 'functions()'
    # located in the views.py file
    # '' repersents home page of the 'movies' app
    # 'views.index' is passing 'index' as a reference
    # not calling it as a method
    # 'name=index' is a keyword argument
    # 'name=index' is giving the url mapping/endpoint
    # a simple name, 'index'
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
    # movies/1


]
