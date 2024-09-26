from django.urls import path, include
from .views import register, authors_and_sellers, home
from .views import upload_books, uploaded_files, my_books
from django.conf import settings
from django.conf.urls.static import static
from .views import *
#from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('send-email/', send_test_email, name='send_email'),
    path('send-otp/', send_otp_view, name='send_otp_email'),
    path('verify-otp/', verify_otp_view, name='verify_otp'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('authors-and-sellers/', authors_and_sellers, name='authors_and_sellers'),
    path('upload-books/', upload_books, name='upload_books'),
    path('uploaded-files/', uploaded_files, name='uploaded_files'),
    path('auth/token/login/', login_view, name='login'),
    path('upload_books/', upload_books, name='upload_books'),
    path('uploaded-files/', uploaded_files, name='uploaded_files'),
    path('login/', login_view, name='login'),
    path('logout/', custom_logout_view, name='logout'),
    #path('my_books/', my_books, name='my_books'),


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
