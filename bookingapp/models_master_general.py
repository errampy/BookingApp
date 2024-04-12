from django.db import models

class Country(models.Model):
    """
    Model representing the county
    """
    code = models.CharField(max_length=5, primary_key=True, help_text="Code of the country")    # Code of the country
    name = models.CharField(max_length=50, unique=True, help_text="Name of the country")    # Name of the country
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")    # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")      # Date and time of last update

    def __str__(self):
        return str(self.name)
class CountyOrState(models.Model):
    """
    Model representing the County / State
    """
    county = models.ForeignKey(Country, on_delete=models.CASCADE, help_text="Name of the country")  # Name of the country
    code = models.CharField(max_length=5, primary_key=True, help_text="Code of the country")    # Code of the Country / state
    name = models.CharField(max_length=50, unique=True, help_text="Name of the county/state")    # Name of the county / state
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")    # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")      # Date and time of last update

    def __str__(self):
        return str(self.name)
    
class City(models.Model): 
    """
    Model representing the city
    """
    country = models.ForeignKey(Country, on_delete=models.CASCADE, help_text="Name of the country")  # Name of the country
    county_or_state = models.ForeignKey(CountyOrState, on_delete=models.CASCADE, help_text="Name of the county or state")  # Name of the county or state
    code = models.CharField(max_length=5, primary_key=True, help_text="Code of the city")    # Code of the city
    name = models.CharField(max_length=50, unique=True, help_text="Name of the city")    # Name of the city
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")    # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")      # Date and time of last update

    def __str__(self):
        return str(self.name)