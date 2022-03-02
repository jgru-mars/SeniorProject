from django.db import models
# maybe be able to use what we have so we don't need to insert anything into ORM but instead just search.


class Floor(models.Model):
    floorID = models.IntegerField(max_length=100)
    name = models.CharField(max_length=30)
    floorImg = models.ImageField(upload_to = "mysite/carrollFloorPlans/")


class Classes(models.Model):
    classesID = models.IntegerField(max_length=100)
    ClassName = models.CharField(max_length=30)
    ClassShort = models.CharField(max_length=30)


class ClassRoom(models.Model):
    classRoomID = models.IntegerField(max_length=100)
    ClassRoom = models.CharField(max_length=30)
    coordinatesY = models.CharField(max_length=30)
    coordinatesX = models.CharField(max_length=30)


class Buildings(models.Model):
    buildingID = models.IntegerField(max_length=100)
    BuildingName = models.CharField(max_length=30)


class Schedule(models.Model):
    scheduleID = models.IntegerField(max_length=100)
    section = models.CharField(max_length=30)
    startTime = models.CharField(max_length=30)
    endTime = models.CharField(max_length=30)


    # this is where to select things I think
    def __str__(self):
        return self.section
