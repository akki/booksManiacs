from django.db import models

# Create your models here.


class Student_Year(models.Model):
    FIRST = '1st'
    SECOND = '2nd'
    THIRD = '3rd'
    FOURTH = '4th'
    YEAR_CHOICES = (
        (FIRST, 'First'),
        (SECOND, 'Second'),
        (THIRD, 'Third'),
        (FOURTH, 'Fourth'),
    )


class Hostel(models.Model):
	HOSTEL_CHOICES = (
		('clb','Cautley Bhawan'),
		('rkb','RadhaKrishnan Bhawan'),
		('rb','Rajeev Bhawan'),
		('rjb','Rajendra Bhawan'),
		# add all bhawans
	)


class Book(models.Model):
	name = models.CharField(max_length=100)
	author = models.CharField(max_length=40,primary_key=True)
	avail_count = models.IntegerField(default=0)
	price = models.IntegerField()
	imageLink = models.CharField(max_length=500,blank=True)
	def __unicode__(self):
		return self.name + " (" + self.author + ")"

class Profile(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=254,primary_key=True)
	password = models.CharField(max_length=32)
	mobile_number = models.CharField(max_length=10)
	room_number = models.CharField(max_length=10,blank=True)
	hostel = models.CharField(max_length=3,choices=Hostel.HOSTEL_CHOICES,blank=True)
	year = models.CharField(max_length=3,choices=Student_Year.YEAR_CHOICES,blank=True)
	enrollment_number = models.CharField(max_length=8,blank=True)
	synced_facebook = models.BooleanField(default=False)
	blocked = models.BooleanField(default=False)
	def __unicode__(self):
		return self.email

class Item(models.Model):
	ITEM_STATUS = (
		('0','no_request'),
		('1','request_to_buy'),
		('2','sold'),
	)
	name = 	models.ForeignKey(Book)
	edition = models.CharField(max_length=15)
	seller = models.ForeignKey(Profile)
	buy_request = models.CharField(max_length=1,choices=ITEM_STATUS,default='0')
	buyer = models.ForeignKey(Profile,related_name='+',blank=True, null=True)
	other_details = models.TextField(default='')
	def __unicode__(self):
		return str(self.id) + " " + self.name_id + " status:" + self.buy_request