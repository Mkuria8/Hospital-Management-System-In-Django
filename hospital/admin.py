from django.contrib import admin
from .models import Patient, Doctor, Gallery, Appointment

# ✅ Action to approve doctors
@admin.action(description="Approve selected doctors")
def approve_doctors(modeladmin, request, queryset):
    queryset.update(status=True)

# ✅ Action to approve patients
@admin.action(description="Approve selected patients")
def approve_patients(modeladmin, request, queryset):
    queryset.update(status=True)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'mobile', 'symptoms', 'assignedDoctorId', 'profile_pic', 'status']
    list_filter = ['status']
    actions = [approve_patients]  # ✅ Approve patients using `status`

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'mobile', 'department', 'profile_pic', 'status']
    list_filter = ['status']
    actions = [approve_doctors]  # ✅ Approve doctors using `status`

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['category', "images"]

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):  # ✅ Fixed incorrect class name
    list_display = ['patientId', "doctorId", 'patientName', 'doctorName', 'description', 'appointmentDate', 'status']
