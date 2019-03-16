from django.db import models
from core.enums import PublishStatusEnum
from core.models import TimeStampModel


class FrontCarousel(TimeStampModel):
    title = models.CharField(max_length=50)
    student_type = models.CharField(
        max_length=10, choices=PublishStatusEnum.choices())

    def __str__(self):
        return self.title
