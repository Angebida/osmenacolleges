from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    established_date = models.DateField()
    head_of_department = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='departments/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Program(models.Model):
    DEGREE_TYPES = [
        ('certificate', 'Certificate'),
        ('diploma', 'Diploma'),
        ('associate', 'Associate Degree'),
        ('bachelor', "Bachelor's Degree"),
        ('master', "Master's Degree"),
        ('doctorate', 'Doctorate'),
    ]
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    degree_type = models.CharField(max_length=20, choices=DEGREE_TYPES)
    duration_years = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)]
    )
    description = models.TextField()
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} ({self.get_degree_type_display()})"

class Faculty(models.Model):
    RANKS = [
        ('instructor', 'Instructor'),
        ('assistant', 'Assistant Professor'),
        ('associate', 'Associate Professor'),
        ('professor', 'Professor'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    rank = models.CharField(max_length=20, choices=RANKS)
    specialization = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    office_location = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to='faculty/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_rank_display()})"

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    
    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    registration_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class Application(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    
    # Personal Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    
    # Program Choice
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    start_term = models.CharField(max_length=20)
    
    # Additional Details
    current_address = models.TextField()
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.program}"