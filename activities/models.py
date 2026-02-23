"""Database models for activity records and type choices."""

from django.db import models

class ActivityType(models.TextChoices):
    """Enumerated activity type values supported by the app."""
    EDUCATION = 'education', 'Education'
    RECREATIONAL = 'recreational', 'Recreational'
    SOCIAL = 'social', 'Social'
    DIY = 'diy', 'DIY'
    CHARITY = 'charity', 'Charity'
    COOKING = 'cooking', 'Cooking'
    RELAXATION = 'relaxation', 'Relaxation'
    MUSIC = 'music', 'Music'
    BUSYWORK = 'busywork', 'Busywork'

class Activity(models.Model):
    """Persisted activity returned by the external API."""
    id = models.IntegerField(primary_key=True)
    activity = models.CharField(max_length=255)
    type = models.CharField(max_length=64, choices=ActivityType.choices, db_index=True)
    participants = models.PositiveSmallIntegerField(db_index=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, db_index=True)
    accessibility = models.CharField(max_length=64, db_index=True)
    link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        """Return a readable label for admin and shell output."""
        return f"{self.activity} ({self.type})"
