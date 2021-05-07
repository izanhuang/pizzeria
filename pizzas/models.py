from django.db import models

# Create your models here.
class Pizza(models.Model):
    """The name of a pizza."""
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the Pizza Model."""
        return self.name

class Topping(models.Model):
    """The name of a pizza and its toppings."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Return a string representation of a Topping object."""
        if len(self.name) <= 50:
            return self.name
        else:
            return f"{self.name[:50]}..."
