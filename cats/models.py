from django.db import models

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()

    def __str__(self):
        if self.weight > 10:
            description = "big chungus"
        elif self.name == "Albert":
            description = "wispy boo boo"
        elif self.name == "Maple":
            description = "fluffy loaf"
        else:
            description = "boring cat"
        return f"{self.name} the {description}."
