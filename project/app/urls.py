from django.urls import path
from app import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='main'),
    path('<int:id>', views.show, name='show'),
]