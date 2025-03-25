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

from django.utils.html import format_html

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['get_user_name', 'address', 'mobile', 'symptoms', 'assignedDoctorId', 'get_profile_pic', 'status']
    list_filter = ['status']
    actions = [approve_patients]

    def get_user_name(self, obj):
        if obj.user:  # Check if user exists
            return f"{obj.user.first_name} {obj.user.last_name}"
        return "No User Assigned"
    get_user_name.short_description = 'User'

    def get_profile_pic(self, obj):
        if obj.profile_pic:  # Check if there's a profile picture
            return format_html('<img src="{}" width="50" height="50" />', obj.profile_pic.url)
        return "No Image"
    get_profile_pic.short_description = 'Profile Picture'
  # ✅ Approve patients using `status`

from django.utils.html import format_html

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['get_user_name', 'address', 'mobile', 'department', 'get_profile_pic', 'status']
    list_filter = ['status']
    actions = [approve_doctors]

    def get_user_name(self, obj):
        if obj.user:  # Check if user exists
            return f"{obj.user.first_name} {obj.user.last_name}"
        return "No User Assigned"
    get_user_name.short_description = 'User'

    def get_profile_pic(self, obj):
        if obj.profile_pic:  # Check if there's a profile picture
            return format_html('<img src="{}" width="50" height="50" />', obj.profile_pic.url)
        return "No Image"
    get_profile_pic.short_description = 'Profile Picture'
  # ✅ Approve doctors using `status`

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['category', "images"]

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):  # ✅ Fixed incorrect class name
    list_display = ['patientId', "doctorId", 'patientName', 'doctorName', 'description', 'appointmentDate', 'status']
