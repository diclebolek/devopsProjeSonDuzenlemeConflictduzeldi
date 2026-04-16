from django.db import models


class FAQEntry(models.Model):
    question = models.CharField(max_length=400)
    answer = models.TextField()
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("sort_order", "id")
        verbose_name_plural = "FAQ entries"
