from django.db import models


class Banks(models.Model):
    name = models.CharField(max_length=49)

    class Meta:
        verbose_name_plural = "Banks"

    def __str__(self):
        return self.name


class Branches(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank_id = models.ForeignKey(Banks, on_delete=models.CASCADE, related_name="bank_branches")
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    class Meta:
        verbose_name_plural = "Branches"
    
    def __str__(self):
        return self.ifsc
