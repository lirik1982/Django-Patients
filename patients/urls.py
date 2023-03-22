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

    path('patient/<str:patient_id>', views.patient, name='patient'),

]
