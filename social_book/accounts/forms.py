from django import forms
from .models import CustomUser
from .models import UploadedFile



class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'public_visibility', 'birth_year', 'address']
    

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['title', 'description', 'visibility', 'cost', 'year_published', 'file']
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if not (file.name.endswith('.pdf') or file.name.endswith('.jpeg') or file.name.endswith('.jpg') or file.name.endswith('.png')):
                raise forms.ValidationError("Only PDF, JPEG and PNG files are allowed.")
        return file
    
    