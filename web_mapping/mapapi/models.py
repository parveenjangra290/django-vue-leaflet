"""
    Define model data.
"""
from django.db import models
from django_countries.fields import CountryField

COUNTRY_CHOICES = (
    ('IN', 'India'),
    ()
)
STATE_CHOICES = (
    ('KA', 'Karnataka'),('AP', 'Andhra Pradesh'), 
    ('KL', 'Kerala'),('TN', 'Tamil Nadu'),
    ('MH', 'Maharashtra'),('UP', 'Uttar Pradesh'),
    ('GA', 'Goa'), ('GJ', 'Gujarat'),
    ('RJ', 'Rajasthan'),('HP', 'Himachal Pradesh'),
    ('TG', 'Telangana'),('AR', 'Arunachal Pradesh'),
    ('AS', 'Assam'), ('BR', 'Bihar'),('CH', 'Chandigarh'),
    ('CT', 'Chhattisgarh'),('HR', 'Haryana'),
    ('JH', 'Jharkhand'),('MP', 'Madhya Pradesh'), 
    ('MN', 'Manipur'),('ML', 'Meghalaya'),
    ('MZ', 'Mizoram'), ('NL', 'Nagaland'),
    ('OR', 'Odisha'), ('PB', 'Punjab'),
    ('SK', 'Sikkim'), ('TR', 'Tripura'),
    ('UT', 'Uttarakhand'),('WB', 'West Bengal'),
    ('AN', 'Andaman and Nicobar Islands'),
    ('DH', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('DL', 'Delhi'), ('JK', 'Jammu and Kashmir'),
    ('LD', 'Lakshadweep'), ('LA', 'Ladakh'), ('PY', 'Puducherry')
)

class Farmer(models.Model):
    """ Class to store Farmer data. """

    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    village = models.CharField(max_length=250)
    block_tahsil = models.CharField(max_length=250)
    district = models.CharField(max_length=250)
    state = models.CharField(choices=STATE_CHOICES, null=False, max_length=20)
    country = CountryField(blank_label="(select country)", default="IN")
    latitude = models.FloatField()
    longitude = models.FloatField()
    amount = models.FloatField()
    remarks = models.CharField(max_length=250)
    uid = models.CharField(max_length=250)
    gp = models.CharField(max_length=250)
    year = models.CharField(max_length=250)
    
    class Meta:
        db_table = 'farmer'
    
    def __str__(self):
        """
            Change display name of Model Instance
        """
        return self.name

