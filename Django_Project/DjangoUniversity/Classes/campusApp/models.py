from django.db import models


# Create model of University Campus
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)

    # Create model manager
    object = models.Manager()

    # Have the browser show University Campus when chosen on admin page
    class Meta:
        verbose_name_plural = "University Campus"
