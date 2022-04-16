from django.db import models

# Create your models here.
class Parishes(models.Model):
    name = models.CharField(max_length=100, default='', blank=False)
    street = models.CharField(max_length=100, default='', blank=False)
    city = models.CharField(max_length=100, default='', blank=False)
    state = models.CharField(max_length=100, default='', blank=False)
    zip = models.CharField(max_length=100, default='', blank=False)
    diocese = models.CharField(max_length=100, default='', blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Intentions(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    intention = models.TextField(max_length=250, default='', blank=False )
    category = models.CharField(max_length=100,  null=True, blank=True, default='')
    # requestor = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    requestor = models.CharField(max_length=100, default='', blank=False)
    requestor_email = models.EmailField(max_length=70, default='', blank=False)
    requestor_phone = models.CharField(max_length=70, default='', blank=False)
    donation_amount = models.CharField(max_length=70, default='', null=True, blank=True)
    status  = models.CharField(max_length=70, default='', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.intention

class Meetings(models.Model):
    intention = models.ForeignKey(Intentions, on_delete=models.CASCADE)
    day = models.CharField(max_length=100, default='', blank=False)
    time = models.CharField(max_length=100, default='', blank=False)
    parish = models.ForeignKey('Parishes', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return str(self.time)
