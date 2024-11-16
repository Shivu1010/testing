from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('admission-details/', views.admission_details, name='admission_details'),
    path('exam-section/', views.exam_section, name='exam_section'), 
    path('marks-section/',views.marks_section, name='marks_section'),
    path('admission-updates/',views.admission_updates, name='admission_updates'),
    path('upload-myphotosign/',views.upload_myphotosign, name='upload_myphotosign'),
    path('upload-documents/',views.upload_documents, name='upload_documents'),
    path('view-admission-details/', views.view_admission_details, name='view_admission_details'),
    path('admission/', views.submit_admission, name='submit_admission'),
    path('add_marks/', views.add_marks, name='add_marks'),  # For submitting marks
    path('view_marks/', views.view_marks, name='view_marks'),
    path('edit_marks/<int:pk>/', views.edit_marks, name='edit_marks'), 
    
]
