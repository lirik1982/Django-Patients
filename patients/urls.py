from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.frontend, name='frontend'),
    path('login/', include('django.contrib.auth.urls')),

# ----------------BACKEND--------------------
    path('backend/', views.backend, name='backend'),
# url in brawser        func in views    url inside template.html

    path('add_patient/', views.add_patient, name='add_patient'),
    path('edit_patient/', views.edit_patient, name='edit_patient'),


    path('patient/<str:patient_id>', views.patient, name='patient'),
    path('delete_patient/<str:patient_id>', views.delete_patient, name='delete_patient'),

]
