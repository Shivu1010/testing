from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import AdmissionDetail
from django.contrib.auth.decorators import login_required
from .models import  UserProfile
from .forms import AdmissionDetailForm
from .forms import MarksForm
from .models import StudentMarks
 # Import your model here

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def admission_details(request):
    if request.method == 'POST':
        form = AdmissionDetailForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('view_admission_details')  # Redirect to the page that views the data
    else:
        form = AdmissionDetailForm()
    return render(request, 'management/admission_details.html', {'form': form})

def view_admission_details(request):
    # Retrieve all admission details from the database
    admission_details = AdmissionDetail.objects.all()
    return render(request, 'management/view_admission_details.html', {'admission_details': admission_details})

@login_required
def exam_section(request):
    return render(request, 'management/manage/exam_section.html')

@login_required
def marks_section(request):
    return render(request, 'management/manage/marks_section.html')

@login_required
def admission_updates(request):
    return render(request, 'management/admission_updates.html')

@login_required
def upload_myphotosign(request):
    return render(request, 'management/upload_myphotosign.html')

@login_required
def upload_documents(request):
    return render(request, 'management/upload_documents.html')
def submit_admission(request):
    if request.method == 'POST':
        form = AdmissionDetailForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            messages.success(request, "Successfully uploaded the data")  # Success message
            return redirect('view_admission_details')  # Redirect to another page after successful submission
    else:
        form = AdmissionDetailForm()

    return render(request, 'admission_detail.html', {'form': form})

def add_marks(request):
    if request.method == "POST":
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('view_marks')  # Redirect to view marks page after submission
    else:
        form = MarksForm()
    
    return render(request, 'management/manage/marks_section.html', {'form': form})

# View for displaying marks
def view_marks(request):
    marks = StudentMarks.objects.all()  # Fetch all the marks
    return render(request, 'management/manage/view_marks.html', {'marks': marks})

def edit_marks(request, pk):
    student_mark = get_object_or_404(StudentMarks, pk=pk)  # Get the student marks by ID (pk)
    
    if request.method == 'POST':
        form = MarksForm(request.POST, instance=student_mark)  # Prepopulate the form with existing data
        if form.is_valid():
            form.save()  # Save the updated data to the database
            return redirect('view_marks')  # Redirect to the view marks page after update
    else:
        form = MarksForm(instance=student_mark)  # Get the current marks in the form
    
    return render(request, 'management/manage/edit_marks.html', {'form': form})