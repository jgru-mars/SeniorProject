from django.db import models


# maybe be able to use what we have so we don't need to insert anything into ORM but instead just search.

class Building(models.Model):
    id = models.IntegerField(max_length=100, primary_key=True)
    name = models.CharField(max_length=30)


class Floor(models.Model):
    id = models.IntegerField(max_length=100, primary_key=True)
    name = models.CharField(max_length=30)
    floorimg = models.CharField(max_length=30)
    building = models.CharField(max_length=30)


class Classes(models.Model):
    id = models.IntegerField(max_length=100, primary_key=True)
    name = models.CharField(max_length=30)
    ClassShort = models.CharField(max_length=30)


class Rooms(models.Model):
    id = models.IntegerField(max_length=100, primary_key=True)
    floor = models.CharField(max_length=30)
    roomNumber = models.CharField(max_length=30)
    YOffset = models.CharField(max_length=30)
    XOffset = models.CharField(max_length=30)

class Schedule(models.Model):
    id = models.IntegerField(max_length=100, primary_key=True)
    classRoomID = models.ForeignKey(Rooms, null=True, on_delete=models.CASCADE)
    classesID = models.ForeignKey(Classes, null=True, on_delete=models.CASCADE)
    section = models.CharField(max_length=30)
    startTime = models.CharField(max_length=30)
    endTime = models.CharField(max_length=30)

    # this is where to select things I think
    def __str__(self):
        return self.headline
