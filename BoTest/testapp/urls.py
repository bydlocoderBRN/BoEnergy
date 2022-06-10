from django.urls import path
from . import views

urlpatterns = [
    path('quad', views.QuadroView.as_view()),
    path('colors/<int:num>', views.ColorsView.as_view())
]
