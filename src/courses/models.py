from django.db import models


class Access_Requirement(model.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email_required","Email_Required"

class Publish_Status(model.TextChoices):
    PUBLISHED = "publish", "Published"
    COMMING_SOON = "soon","Coming Soon"
    DRAFT = "draft", "Draft"

class Course(model.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    # image = 
    access = model.CharField(max_length=10, choices=Access_Requirement.choices,
    default=Access_Requirement.DRAFT)
    status = model.CharField(max_length=10, choices=Publish_Status.choices,
    default=Publish_Status.DRAFT)

@property
def is_published(self):
    return self.status == Publish_Status.PUBLISHED