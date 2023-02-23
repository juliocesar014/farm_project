from django.db import models

# Create your models here.

class Owner(models.Model):
    CPF = "CPF"
    CNPJ = "CNPJ"
    
    DOCUMENT_TYPE_CHOICES = (
        (CPF, "CPF"),
        (CNPJ, "CNPJ"),
    )
    
    name = models.CharField(max_length=255, help_text="Name of the owner (Ex. João)", verbose_name=u"Name")
    document = models.CharField(max_length=255, help_text="Document of the owner (Ex. 12345678900)", verbose_name=u"Document")
    document_type = models.CharField(max_length=10, choices=DOCUMENT_TYPE_CHOICES, default=CPF, verbose_name=u"Document Type", help_text="Document type of the owner (Ex. CPF)", blank=False)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=u"Creation Date", help_text="Creation date of the owner", editable=False)
    last_modification_date = models.DateTimeField(auto_now=True, verbose_name=u"Last Modification Date", help_text="Last modification date of the owner")
    is_active = models.BooleanField(default=True, verbose_name=u"Is Active", help_text="Is the owner active?")
    
    def __str__(self):
        return self.name
    
    
    def __int__(self):
        return self.id
    
    
    def get_class_name(self):
        return "owner"
    
    
class Farm(models.Model):
    
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, verbose_name="Who is the owner of the farm?", help_text="Who is the owner of the farm?")
    
    name = models.CharField(max_length=255, help_text="Name of the farm (Ex. Fazenda São João)", verbose_name=u"Name", blank=False)
    geometry = models.IntegerField(help_text="Geometry of the farm (Ex. 1)", verbose_name=u"Geometry", null=True, blank=True)
    area = models.FloatField(help_text="Area of the farm (Ex. 1000)", verbose_name=u"Area", null=True, blank=True)
    centro_id = models.IntegerField(help_text="Centro ID of the farm (Ex. 1)", verbose_name=u"Centro ID", null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=u"Creation Date", help_text="Creation date of the farm", editable=False)
    last_modification_date = models.DateTimeField(auto_now=True, verbose_name=u"Last Modification Date", help_text="Last modification date of the farm")
    is_active = models.BooleanField(default=True, verbose_name=u"Is Active", help_text="Is the farm active?")
    municipio = models.CharField(max_length=255, help_text="Municipio of the farm (Ex. São Paulo)", verbose_name=u"Municipio", blank=False)
    estado = models.CharField(max_length=255, help_text="Estado of the farm (Ex. São Paulo)", verbose_name=u"Estado", blank=False)

    
    
    def __str__(self):
        return self.name
    
    
    def __int__(self):
        return self.id