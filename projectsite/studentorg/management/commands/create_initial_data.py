import random
from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize Faker once for the whole class
        self.fake = Faker('en_PH') 

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        self.create_organizations(10)
        self.create_students(50)
        self.create_membership(20)
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded all initial data.'))

    def create_organizations(self, count):
        colleges = list(College.objects.all())
        if not colleges:
            self.stdout.write(self.style.WARNING('No Colleges found. Skipping Org creation.'))
            return

        for _ in range(count):
            Organization.objects.create(
                name=f"{self.fake.catch_phrase()} Society".title(),
                college=random.choice(colleges),
                description=self.fake.paragraph(nb_sentences=3)
            )
        self.stdout.write(self.style.SUCCESS(f'Created {count} organizations.'))

    def create_students(self, count):
        programs = list(Program.objects.all())
        if not programs:
            self.stdout.write(self.style.WARNING('No Programs found. Skipping Student creation.'))
            return

        for _ in range(count):
            # Formats a typical PH Student ID: 2024-1-0001
            s_id = f"{random.randint(2020, 2025)}-{random.randint(1, 2)}-{random.randint(1000, 9999)}"
            
            Student.objects.create(
                student_id=s_id,
                last_name=self.fake.last_name(),
                first_name=self.fake.first_name(),
                middle_name=self.fake.last_name(),
                program=random.choice(programs)
            )
        self.stdout.write(self.style.SUCCESS(f'Created {count} students.'))

    def create_membership(self, count):
        students = list(Student.objects.all())
        orgs = list(Organization.objects.all())

        if not students or not orgs:
            return

        for _ in range(count):
            OrgMember.objects.get_or_create(
                student=random.choice(students),
                organization=random.choice(orgs),
                defaults={'date_joined': self.fake.date_between(start_date="-2y", end_date="today")}
            )
        self.stdout.write(self.style.SUCCESS(f'Created {count} memberships.'))