from django.urls import path

from users.views import UserUpdateView

urlpatterns = [
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]