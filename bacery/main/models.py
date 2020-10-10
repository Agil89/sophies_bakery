from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Contact(models.Model):
    #information
    name = models.CharField('Name',max_length=40)
    email = models.EmailField('Email',max_length=40)
    phone = models.CharField('Phone number',max_length=15)
    subject = models.CharField('Subject',max_length=255)
    message = models.TextField('Message')

    # moderation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'{self.name} subject:{self.subject}'

    def get_email(self):
        return self.email

class ContactInfo(models.Model):
    #information
    fullname = models.CharField('Fullname',max_length=60)
    email = models.CharField('Email',max_length=40)
    phone_number = models.CharField('Phone Number',max_length=20)
    location = models.CharField('Our location',max_length=100)

    class Meta:
        verbose_name = 'Our Contact'
        verbose_name_plural = 'Our Contacts'

    def __str__(self):
        return self.fullname

class AboutProject(models.Model):
    #information
    project_devops = models.CharField('Fullname',max_length=60)
    key_words = models.CharField('Key words',max_length=500)
    title = models.CharField('Title',max_length=60)
    faq_icon = models.ImageField('Faq icon',upload_to='images')
    logo = models.ImageField('Logo',upload_to='images')
    description = models.TextField('Description')

    #moderation
    project_developing_start_time = models.DateField()
    project_developing_finish_time = models.DateField()

class Subscriber(models.Model):
    email = models.EmailField('Email',max_length=30,unique=True)
    is_active = models.BooleanField('is active',default=True)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email