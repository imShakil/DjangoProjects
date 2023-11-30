from django.urls import path
from django.contrib import admin
from feedback import views

urlpatterns = [
    path('feedback/', views.feedback_list),
    path('admin/', admin.site.urls),
    path('', views.feedback_index),
]
