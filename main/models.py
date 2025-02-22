from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics/')
    bio = models.TextField()
    cv_file = models.FileField(upload_to='cv_files/', null=True, blank=True)
    job_title = models.CharField(max_length=100, default="Urban Management and Development Specialist")

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company} ({self.start_date} - {self.end_date})"

from django.db import models

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)  # New field for location
    

    def __str__(self):
        return f"{self.degree} at {self.institution}"
from django.db import models

class Project(models.Model):
    PROJECT_TYPES = [
        ('pdf', 'Projects PDFs'),
        ('inspection', 'Property Inspection Projects'),
    ]

    type = models.CharField(max_length=20, choices=PROJECT_TYPES, default='pdf')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='projects/pdfs/', blank=True, null=True)  # For Projects PDFs
    description = models.TextField(blank=True, null=True)  # For Property Inspection Projects

    def __str__(self):
        return self.title



class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)  # Ensure this field exists

    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    name = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reply by {self.name}'
