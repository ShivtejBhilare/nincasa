from django.urls import path
from .views import home, booking, dashboard, menu, contact
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('booking/', booking, name='booking'),
    path('dashboard/', dashboard, name='dashboard'),
    path('menu/', menu, name='menu'),
    path('contact/', contact, name='contact'),
    path('login/', LoginView.as_view(template_name='restaurant/login.html'), name='login'),  # Login URL
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Logout URL
]