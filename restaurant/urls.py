from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.menuView.as_view()),
    path('booking/', views.bookingView.as_view()),
]
