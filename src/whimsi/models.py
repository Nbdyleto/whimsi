from django.db import models

class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField(null=True, blank=True)
    parking_lots = models.PositiveIntegerField(null=True, blank=True, default=0)
    area_sqm = models.PositiveIntegerField()
    STATUS_CHOICES = (
        ('For Sale', 'For Sale'),
        ('For Rent', 'For Rent'),
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class PropertyAddress(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    street_address = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=8) # CEP

    def __str__(self):
        return f'{self.property.title} - {self.postal_code}, {self.street_address}, {self.neighborhood}, {self.city}'
    
class PropertyImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)

class PropertyFeature(models.Model):
    feature_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=255)

class HighlightedProperty(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    highlight_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.property.title