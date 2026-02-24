from django.db import models

# Create your models here.
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class College(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Program(BaseModel):
    name = models.CharField(max_length=150)
    college = models.ForeignKey(
        College, 
        on_delete=models.CASCADE, 
        related_name="programs"
    )

    def __str__(self):
        return self.name

class Organization(BaseModel):
    name = models.CharField(max_length=250)
    college = models.ForeignKey(
        College, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="organizations"
    )
    description = models.TextField(max_length=500)  # Changed to TextField for better UI handling

    def __str__(self):
        return self.name

class Student(BaseModel):
    student_id = models.CharField(max_length=15, unique=True)
    last_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25, blank=True, null=True)
    program = models.ForeignKey(
        Program, 
        on_delete=models.CASCADE, 
        related_name="students"
    )

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class OrgMember(BaseModel):
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE, 
        related_name="memberships"
    )
    organization = models.ForeignKey(
        Organization, 
        on_delete=models.CASCADE, 
        related_name="members"
    )
    date_joined = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.organization}"