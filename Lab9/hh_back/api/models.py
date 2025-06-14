from django.db import models


class Companies(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class Vacancies(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return self.name
