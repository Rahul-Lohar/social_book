from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .models import OTP
from django.utils import timezone
from django.http import JsonResponse
from datetime import timedelta
from django.http import HttpResponse
from django.contrib.auth.models import User
import random


def generate_otp(user):
    otp = random.randint(100000, 999999) 
    otp_instance = OTP.objects.create(user=user, otp=otp, expires_at=timezone.now() + timedelta(minutes=5))
    return otp_instance
     

def send_otp_email(user, otp):
    send_mail(
                'Your verification code',
                f'Your verification code is {otp}',
                'rkv.luhar@gmail.com.com',
                [user.email],
                fail_silently=False,
            )


