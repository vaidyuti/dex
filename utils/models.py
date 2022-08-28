from django.db import models


class BaseModel(models.Model):
    created_on = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True,
        editable=False,
    )
    updated_on = models.DateTimeField(
        blank=False,
        null=False,
        auto_now=True,
        editable=False,
    )
    deleted = models.BooleanField(
        blank=False,
        null=False,
        default=False,
        editable=False,
        help_text="Whether the record is deleted or not (soft-delete)",
    )

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    class Meta:
        abstract = True
