from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    

class Region(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.name
    

class City(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete = models.SET_NULL , null=True, related_name='city')

    def __str__(self) -> str:
        return self.name

class Arena(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    parking = models.BooleanField(default=False)
    bathroom = models.BooleanField(default=False)
    seat = models.IntegerField()
    area = models.FloatField()
    time_open = models.TimeField()
    time_close = models.TimeField()
    repaired = models.DateField(null=True, blank=True)
    location = models.ForeignKey(City, on_delete = models.SET_NULL, null=True, related_name='arena')
    is_active = models.BooleanField(default=True)
    sport = models.ManyToManyField(Category)
                                   
    def __str__(self) -> str:
        return self.name
    

class Trener(models.Model):
    name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="treners/")
    about = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    arena = models.ForeignKey(Arena, on_delete = models.SET_NULL, null=True, related_name="arena")
    sport = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True, related_name="trener")

    def __str__(self) -> str:
        return self.name
    

class ImageArena(models.Model):
    arena = models.ForeignKey(Arena, related_name='images' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to="arena/")

    def __str__(self) -> str:
        return self.arena.name
    

class ImageSport(models.Model):
    sport = models.ForeignKey(Category, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="sport/")

    def __str__(self) -> str:
        return self.sport.name