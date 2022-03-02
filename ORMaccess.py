from django.db import models
# maybe be able to use what we have so we don't need to insert anything into ORM but instead just search.


class Floor(models.Model):
    name = models.CharField(max_length=30)
    floorImg = models.ImageField(upload_to = "mysite/carrollFloorPlans/")


class Classes(models.Model):
    ClassName = models.CharField(max_length=30)
    ClassShort = models.CharField(max_length=30)


class ClassRoom(models.Model):
    ClassRoom = models.CharField(max_length=30)
    coordinatesY = models.CharField(max_length=30)
    coordinatesX = models.CharField(max_length=30)


class Buildings(models.Model):
    BuildingName = models.CharField(max_length=30)


class Schedule(models.Model):
    section = models.CharField(max_length=30)
    startTime = models.CharField(max_length=30)
    endTime = models.CharField(max_length=30)


    # this is where to select things I think
    def __str__(self):
        return self.section
