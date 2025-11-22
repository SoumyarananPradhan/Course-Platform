from django.db import models


class Access_Requirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email_required","Email_Required"

class Publish_Status(models.TextChoices):
    PUBLISHED = "publish", "Published"
    COMMING_SOON = "soon","Coming Soon"
    DRAFT = "draft", "Draft"

def handle_upload(instance, filename):
    return f"{filename}"

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    access = models.CharField(max_length=15, choices=Access_Requirement.choices,
    default=Access_Requirement.EMAIL_REQUIRED)
    status = models.CharField(max_length=10, choices=Publish_Status.choices,
    default=Publish_Status.DRAFT)

@property
def is_published(self):
    return self.status == Publish_Status.PUBLISHED