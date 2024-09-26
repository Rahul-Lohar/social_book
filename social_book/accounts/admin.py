from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  
from .models import UploadedFile
from .models import OTP

admin.site.register(CustomUser, UserAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'uploaded_at') 
    search_fields = ('user__username', 'file')
    list_filter = ('uploaded_at',)
    ordering = ('-uploaded_at',)
    

@admin.register(OTP)
class OTPLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp', 'created_at', 'expires_at')