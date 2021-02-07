from django.db import models

# Create your models here.
class Chart(models.Model):
    PIE = 'PIE'
    CHART_TYPE_OPTS = [
        (PIE, 'Pie'),
    ]

    b64_encoded = models.TextField()
    chart_type = models.CharField(max_length=3, choices=CHART_TYPE_OPTS)
    chart_desc = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.chart_type, self.chart_desc)
    
