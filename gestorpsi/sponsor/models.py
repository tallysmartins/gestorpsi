from django.db import models
from django.newforms import ModelForm
from django.contrib.contenttypes import generic
from gestorpsi.phone.models import Phone
from gestorpsi.person.models import Person
from gestorpsi.address.models import Country, City, Address



class Sponsor(models.Model):
    name = models.CharField('name',max_length=100)    
    companyID = models.CharField('companyID',max_length=100, null=True)
    healthRegion = models.CharField('healthRegion',max_length=10, null=True)
    bankBranch = models.CharField('bankBranch',max_length=10, null=True)
    account = models.CharField('account',max_length=15, null=True)
    taxWithHold = models.CharField('taxWithHold',max_length=20, null=True)
        
    phones = generic.GenericRelation(Phone, null=True)
    address = generic.GenericRelation(Address, null=True)        
    
                          
    def __unicode__(self):
        return self.name    
    
    class Admin:
        pass