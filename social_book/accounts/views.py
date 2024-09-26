from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import UploadedFile
from .forms import UploadFileForm 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets                                                                                     # type: ignore
from rest_framework.permissions import IsAuthenticated                                                                   # type: ignore
from .serializers import UploadedFileSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes                              # type: ignore
from rest_framework.response import Response                                                                            # type: ignore
from .decorators import check_uploaded_files
from rest_framework.authentication import TokenAuthentication                                                           # type: ignore
from django.core.mail import send_mail
from django.http import HttpResponse         
from django.utils import timezone
from .models import OTP
from django.http import JsonResponse           
from django.core.mail import send_mail
from .utils import generate_otp, send_otp_email
from .decorators import csrf_exempt_view 
from django.contrib import messages
from django.contrib.auth import logout


@api_view(['GET', 'POST'])
def upload_books(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            UploadedFile.objects.create(user=request.user, file=uploaded_file)
            return Response({'message': 'File uploaded successfully'})
        return Response({'message': 'No file uploaded'})
    return Response({'message': 'Upload your books here.'})


@api_view(['GET'])
@check_uploaded_files
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@login_required
def my_books(request):
    uploaded_files = UploadedFile.objects.filter(user=request.user)
    if uploaded_files.exists():
        return render(request, 'accounts/my_books.html', {'uploaded_files': uploaded_files})
    else:
        return redirect('upload_books')


@api_view(['POST'])
def upload_file(request):
    user = request.user  
    uploaded_files = UploadedFile.objects.filter(user=user) 
    if uploaded_files.exists():
        serializer = UploadedFileSerializer(uploaded_files, many=True)
        return Response(serializer.data, status=200)
    else:
        return Response({'message': 'No files found.'})


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def authors_and_sellers(request):
    users = CustomUser.objects.filter(public_visibility=True)
    return render(request, 'authors_and_sellers.html', {'users': users})


def upload_books(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            return redirect('uploaded_files') 
    else:
        form = UploadFileForm()

    return render(request, 'upload_books.html', {'form': form})

@login_required
def uploaded_files(request):
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'uploaded_files.html', {'files': files})


class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UploadedFile.objects.filter(user=self.request.user)
    
    
def send_test_email(request):
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    from_email = 'rkv.luhar@gmail.com' 
    recipient_list = ['2020pgicsrahul62@poornima.org']  

    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse('Email sent successfully!')

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')
    

def custom_logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('/')


def send_otp_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            otp_instance = generate_otp(user)
            send_otp_email(user, otp_instance.otp)
            messages.success(request, 'OTP sent successfully!')
            return redirect('login')
        except CustomUser.DoesNotExist:
            messages.error(request, 'No account found with this email.')
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard/')  
        else:
            return JsonResponse({'error': 'Invalid credentials'})

    return render(request, 'accounts/login.html')


def verify_otp_view(request):
    if request.method == 'POST':
        otp_input = request.POST.get('otp')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(request, username=username, password=password)

            if user is not None: 
                otp_instance = OTP.objects.filter(user=user).latest('created_at')
                if otp_instance.otp == otp_input and not otp_instance.is_expired():
                    login(request, user)  
                    return redirect('dashboard') 

                else:
                    messages.error(request, 'Invalid or expired OTP')
                    return render(request, 'accounts/login.html')

            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'accounts/login.html')

        except CustomUser.DoesNotExist:
            messages.error(request, 'User not found')
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')






