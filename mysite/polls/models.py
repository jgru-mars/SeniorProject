from django.db import models


# maybe be able to use what we have so we don't need to insert anything into ORM but instead just search.

class Building(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)


class Floor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    floorimg = models.CharField(max_length=30)
    building = models.ForeignKey(Building, null=True, on_delete=models.CASCADE)


class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    ClassShort = models.CharField(max_length=30)


class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    floor = models.ForeignKey(Floor, null=True, on_delete=models.CASCADE)
    roomNumber = models.CharField(max_length=30)
    YOffset = models.CharField(max_length=30)
    XOffset = models.CharField(max_length=30)


class Schedule(models.Model):
    id = models.IntegerField(primary_key=True)
    classRoomID = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)
    classesID = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)
    section = models.CharField(max_length=30)
    startTime = models.CharField(max_length=30)
    endTime = models.CharField(max_length=30)

    # this is where to select things I think
    def __str__(self):
        return self.headline
