from django import forms
from .models import Department, Program, Faculty, News, Event, Application

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'established_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'head_of_department': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., +63 912 345 6789'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'degree_type': forms.Select(attrs={'class': 'form-select'}),
            'duration_years': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '6'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tuition_fee': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'rank': forms.Select(attrs={'class': 'form-select'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., +63 912 345 6789'}),
            'office_location': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'start_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'placeholder': 'YYYY-MM-DD HH:MM'
            }),
            'end_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'placeholder': 'YYYY-MM-DD HH:MM'
            }),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'organizer': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'registration_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        }

class ApplicationForm(forms.ModelForm):
    start_term = forms.ChoiceField(
        choices=[
            ('2024-1', 'First Semester 2024'),
            ('2024-2', 'Second Semester 2024'),
            ('2025-1', 'First Semester 2025'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add error class if field has errors
        for field in self.fields:
            css_class = 'form-control'
            if isinstance(self.fields[field].widget, forms.Select):
                css_class = 'form-select'
            elif isinstance(self.fields[field].widget, forms.CheckboxInput):
                css_class = 'form-check-input'
                
            self.fields[field].widget.attrs.update({
                'class': css_class + ' is-invalid' if field in self.errors else css_class
            })
    
    class Meta:
        model = Application
        exclude = ['status']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+63 912 345 6789'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'program': forms.Select(attrs={'class': 'form-select'}),
            'start_term': forms.Select(attrs={'class': 'form-select'}),
            'current_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }