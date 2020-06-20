from django.db import models

# Create your models here.
class Awardee(models.Model):
    # Recipient data
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=1, blank=True)
    last_name = models.CharField(max_length=50)

    # Award data
    award = models.CharField(max_length=5)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    presentation_date = models.DateField(null=True)
    

    def __str__(self):
        if self.middle_initial:
            name = f'{self.last_name}, {self.first_name} {self.middle_initial}.'
        else:
            name = f'{self.last_name}, {self.first_name}'
        
        return f'{name} - {self.award}'
