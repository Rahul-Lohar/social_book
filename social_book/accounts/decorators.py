from django.shortcuts import redirect
from .models import UploadedFile 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def check_uploaded_files(view_func):
    def _wrapped_view(request, *args, **kwargs):
        has_files = UploadedFile.objects.filter(user=request.user).exists()
        if has_files:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('upload_books')  
    return _wrapped_view


def csrf_exempt_view(view_func):
    return csrf_exempt(view_func)
