from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("comments", views.comments,name='comments'),
    path('search/', views.search_view, name='search'),
    path("sortby/<str:key>/",views.sortby,name='sortby'),
    path('genre/<str:key>/',views.genre,name='drop'),
    path('movie/<str:key>/', views.all_blogs, name='key'),
]