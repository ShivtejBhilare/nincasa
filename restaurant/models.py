from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.name

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)  # New field for video URLs
    caption = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.caption if self.caption else "Carousel Image"