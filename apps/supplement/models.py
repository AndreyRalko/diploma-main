from django.db import models

# Create your models here.
class Faculties(models.Model):
    FacultyID = models.IntegerField(db_column="FacultyID", primary_key=True
    )
    facultyNameKZ = models.CharField(db_column="facultyNameKZ", max_length=150)
    facultyNameEN = models.CharField(db_column="facultyNameEN", max_length=150)
    facultyNameRU = models.CharField(db_column="facultyNameRU", max_length=150)

    class Meta:
        managed = False
        db_table = "faculties"

class Cafedras(models.Model):
    cafedraID = models.IntegerField(db_column="cafedraID", primary_key=True)
    cafedraNameRU = models.CharField(db_column="cafedraNameRU", max_length=150)
    cafedraNameKZ = models.CharField(db_column="cafedraNameKZ", max_length=150)
    cafedraNameEN = models.CharField(db_column="cafedraNameEN", max_length=150)
    FacultyID = models.IntegerField(db_column="FacultyID")

    class Meta:
        managed = False
        db_table = "cafedras"

class Groups(models.Model):
    groupID = models.IntegerField(db_column="groupID", primary_key=True)
    name = models.CharField(db_column="name", max_length=150)

class Common_Info(models.Model):
    groupID = models.IntegerField(db_column="groupID", primary_key=True)
    name = models.CharField(db_column="name", max_length=150)
    #base = models.CharField(db_column="base", max_length=150)
    specializationID = models.IntegerField(db_column="specializationID")
    nameru = models.CharField(db_column="nameru", max_length=150)
    namekz = models.CharField(db_column="namekz", max_length=150)
    nameen = models.CharField(db_column="nameen", max_length=150)
    specializationCode = models.CharField(db_column="specializationCode", max_length=150)

class Student_Info(models.Model):
    StudentID = models.IntegerField(db_column="StudentID", primary_key=True)
    lastname = models.CharField(db_column="lastname", max_length=150)
    firstname = models.CharField(db_column="firstname", max_length=150)
    patronymic = models.CharField(db_column="patronymic", max_length=150)
    lastname_en = models.CharField(db_column="lastname_en", max_length=150)
    firstname_en = models.CharField(db_column="firstname_en", max_length=150)
    BirthDate = models.DateField(db_column="BirthDate", max_length=150)
    seriyaAttestata = models.CharField(db_column="seriyaAttestata", max_length=150)
    nomerAttestata = models.CharField(db_column="nomerAttestata", max_length=150)
    dataVydachiAttestata = models.DateField(db_column="dataVydachiAttestata", max_length=150)
    enterexamsen = models.CharField(db_column="enterexamsen", max_length=150)
    StartDate = models.DateField(db_column="nameru", max_length=150)