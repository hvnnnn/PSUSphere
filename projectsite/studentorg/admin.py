from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'college', 'created_at')
    list_filter = ('college',)
    search_fields = ('name',)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'college', 'created_at')
    list_filter = ('college',)
    search_fields = ('name', 'description')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "last_name", "first_name", "middle_name", "program")
    list_filter = ("program", "program__college")
    search_fields = ("last_name", "first_name", "student_id")
    ordering = ("last_name", "first_name")

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization", "date_joined")
    list_filter = ("organization", "date_joined")
    search_fields = ("student__last_name", "student__first_name", "organization__name")
    
    # Performance boost: fetches related data in one SQL JOIN
    list_select_related = ('student', 'student__program', 'organization')

    @admin.display(description='Program', ordering='student__program')
    def get_member_program(self, obj):
        return obj.student.program if obj.student else "No Program"