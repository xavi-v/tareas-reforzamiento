from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length = 128)
    description = models.CharField(max_length = 256)

    options = [
        ["critico", "critico"],
    ["Medio", "Medio"],
    ["bajo","bajo"],
    ["opcional","opcional"]
    ]

    tags = models.CharField(max_length = 32, choices = options, default="Opcional")

    class Meta:

        permissions = [("revocar_tarea", "Revocar esta tarea")]
        verbose_name_plural = "Administrar Tarea"

    def __str__(self):
        return self.title 
