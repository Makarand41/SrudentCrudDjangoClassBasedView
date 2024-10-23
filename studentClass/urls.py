from django.contrib import admin
from django.urls import path
from cbvapp import views  # Make sure 'cbvapp' is the correct app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.StudentListView.as_view(), name='student-list'),
path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('students/create/', views.StudentCreateView.as_view(), name='student-create'),
path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='student-update'),
path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student-delete'),

    # Add this line
]
