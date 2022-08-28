from django.db import models
from utils.models import BaseModel


class Prosumer(BaseModel, models.Model):
    """
    Model of a peer in a vaidyuti based network.
    """

    location = models.CharField(
        max_length=255,
        blank=False,
        verbose_name="latitude_longitude",
        help_text="The coordinated of the prosumer",
    )
