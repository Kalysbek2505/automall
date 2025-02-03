from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.service.name} ({self.date})"

class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.rating}/5)"
    
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')

class Contact(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


    def __str__(self):
        return f'{self.full_name} - {self.phone_number}'
