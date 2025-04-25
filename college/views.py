from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Department, Program, Faculty, News, Event
from .forms import DepartmentForm, ProgramForm, FacultyForm, NewsForm, EventForm, ApplicationForm

# Home Page
def home(request):
    featured_news = News.objects.filter(is_featured=True)[:3]
    upcoming_events = Event.objects.filter(is_active=True).order_by('start_date')[:3]
    departments = Department.objects.all()
    
    context = {
        'featured_news': featured_news,
        'upcoming_events': upcoming_events,
        'departments': departments,
    }
    return render(request, 'college/home.html', context)

# Department CRUD
def department_list(request):
    departments = Department.objects.all()
    template = 'college/department_list.html'  # Use single template
    return render(request, template, {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    programs = Program.objects.filter(department=department, is_active=True)
    faculty = Faculty.objects.filter(department=department, is_active=True)
    
    context = {
        'department': department,
        'programs': programs,
        'faculty': faculty,
    }
    return render(request, 'college/department_detail.html', context)

@login_required
def department_create(request):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('department_list')
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department created successfully!')
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'college/department_form.html', {'form': form, 'title': 'Create Department'})

@login_required 
def department_update(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('department_list')
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department updated successfully!')
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'college/department_form.html', {'form': form, 'title': 'Update Department'})

@login_required
def department_delete(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('department_list')
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        messages.success(request, 'Department deleted successfully!')
        return redirect('department_list')
    return render(request, 'admin/department_confirm_delete.html', {'department': department})

# Program CRUD (similar pattern as Department)
def program_list(request):
    programs = Program.objects.filter(is_active=True)
    template = 'college/program_list.html'  # Simplify to use single template
    return render(request, template, {'programs': programs})

def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'college/program_detail.html', {'program': program})

@login_required
def program_create(request):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('program_list')
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program created successfully!')
            return redirect('program_list')
    else:
        form = ProgramForm()
    return render(request, 'college/program_form.html', {'form': form, 'title': 'Create Program'})

@login_required 
def program_update(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('program_list')
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program updated successfully!')
            return redirect('program_detail', pk=program.pk)
    else:
        form = ProgramForm(instance=program)
    return render(request, 'college/program_form.html', {'form': form, 'title': 'Update Program'})

@login_required
def program_delete(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('program_list')
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        program.delete()
        messages.success(request, 'Program deleted successfully!')
        return redirect('program_list')
    return render(request, 'college/program_confirm_delete.html', {'program': program})

# Faculty CRUD (similar pattern)
def faculty_list(request):
    faculty = Faculty.objects.filter(is_active=True)
    template = 'college/faculty_list.html'  # Use single template
    return render(request, template, {'faculty': faculty})

def faculty_detail(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    return render(request, 'college/faculty_detail.html', {'faculty': faculty})

@login_required
def faculty_create(request):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('faculty_list')
    if request.method == 'POST':
        form = FacultyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Faculty member added successfully!')
            return redirect('faculty_list')
    else:
        form = FacultyForm()
    return render(request, 'college/faculty_form.html', {'form': form, 'title': 'Add Faculty'})

@login_required 
def faculty_update(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('faculty_list')
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        form = FacultyForm(request.POST, request.FILES, instance=faculty)
        if form.is_valid():
            form.save()
            messages.success(request, 'Faculty member updated successfully!')
            return redirect('faculty_detail', pk=faculty.pk)
    else:
        form = FacultyForm(instance=faculty)
    return render(request, 'college/faculty_form.html', {'form': form, 'title': 'Update Faculty'})

@login_required
def faculty_delete(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('faculty_list')
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        faculty.delete()
        messages.success(request, 'Faculty member deleted successfully!')
        return redirect('faculty_list')
    return render(request, 'admin/faculty_confirm_delete.html', {'faculty': faculty})

# News CRUD
def news_list(request):
    news = News.objects.all().order_by('-publish_date')
    return render(request, 'college/news_list.html', {'news': news})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'college/news_detail.html', {'news': news})

@login_required
def news_create(request):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('news_list')
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'News created successfully!')
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'college/news_form.html', {'form': form, 'title': 'Create News'})

@login_required 
def news_update(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('news_list')
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request, 'News updated successfully!')
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm(instance=news)
    return render(request, 'college/news_form.html', {'form': form, 'title': 'Update News'})

@login_required
def news_delete(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('news_list')
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        messages.success(request, 'News deleted successfully!')
        return redirect('news_list')
    return render(request, 'admin/news_confirm_delete.html', {'news': news})

# Event CRUD
def event_list(request):
    events = Event.objects.filter(is_active=True).order_by('start_date')
    template = 'college/event_list.html'  # Use single template
    return render(request, template, {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'college/event_detail.html', {'event': event})

@login_required
def event_create(request):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('event_list')
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'admin/event_form.html', {'form': form, 'title': 'Create Event'})

@login_required 
def event_update(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('event_list')
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'admin/event_form.html', {'form': form, 'title': 'Update Event'})

@login_required
def event_delete(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('event_list')
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('event_list')
    return render(request, 'admin/event_confirm_delete.html', {'event': event})

def application_create(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('home')
    else:
        form = ApplicationForm()
    return render(request, 'college/application_form.html', {
        'form': form,
        'title': 'Apply for Admission'
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'college/login.html', {
        'form': form,
        'title': 'Login'
    })