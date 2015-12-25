from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
	street = models.CharField('Street Name', max_length=70)
	state = models.CharField('State', max_length=10)
	city = models.CharField('City', max_length=20)
	country = models.CharField('Country', max_length=20)
	postal = models.CharField('Postal Code', max_length=10)

	#Django admin plural name reference
	class Meta:
		verbose_name_plural = 'Addresses'

	def __str__(self):
		return self.city + ', ' + self.country


class Company(models.Model):
	name = models.CharField('Company Name', max_length=30) # Company Name

	#toString() - String representation of the class
	def __str__(self):
		return self.name

	#Django admin plural name reference
	class Meta:
		verbose_name_plural = 'Companies'

class School(models.Model):
	name = models.CharField('School Name', max_length=50, primary_key=True)
	city = models.CharField('City', max_length=40)
	country = models.CharField('Country', max_length=40)


	#toString() - String representation of the class
	def __str__(self):
		return self.name

class Education(models.Model):
	school = models.ForeignKey(School)
	start_date = models.DateField('Started')
	end_date = models.DateField('Ended')
	relevant_courses = models.TextField('Relevant Course Work', blank=True)
	major = models.TextField('Major', blank=True)
	minor = models.TextField('Minor', blank=True)
	type = models.CharField('Type', max_length=5) # Bachelors/Masters/Doctorate
	present = models.BooleanField('Present') # Am I Currently at this School?

	class Meta:
		ordering = ('-start_date',)

	#toString() - String representation of the class
	def __str__(self):
		return self.type + " - " + self.school.name

class Experience(models.Model):
	start_date = models.DateField('Started')
	end_date = models.DateField('Ended')
	present = models.BooleanField('Present') # Am I currently working here?
	job_duty = models.TextField('Job Duty')
	company = models.ForeignKey(Company)
	role = models.CharField('Role', max_length=50)

	class Meta:
		ordering = ('start_date',)

	#toString() - String representation of the class
	def __str__(self):
		return self.company.name + " - " + self.role



class Skill(models.Model):
	name = models.CharField('Skill Name', max_length=30)
	description = models.TextField('Skill Description')

	def __str__(self):
		return self.name


class SchoolProject(models.Model):
	name = models.CharField('Project Name', max_length=30)
	description = models.TextField('Project Description')

	def __str__(self):
		return self.name


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	phone = models.CharField('Phone Number', max_length=20)
	profession = models.CharField('Profession', max_length=40) # Professional Title to the work you do
	address = models.ForeignKey(Address, default='')
	skill = models.ManyToManyField(Skill)
	experiences = models.ManyToManyField(Experience)
	education = models.ManyToManyField(Education)
	projects = models.ManyToManyField(SchoolProject)
	linkedin = models.CharField('LinkedIn', max_length=80)
	github = models.CharField('GitHub', max_length=40)

	def __str__(self):
		return self.user.first_name + ' profile'