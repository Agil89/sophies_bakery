from django import forms
from main.models import Subscriber,Contact

class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = (
            'email',
        )

        widgets = {
            'email': forms.EmailInput(attrs={
                'class':'form-control w-100 py-4 col-md-10 rounded',
                'placeholder':'Напишите свою почту'
            })
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'phone',
            'subject',
            'message'
        )
        widgets = {
            'name':forms.TextInput(attrs={
                    'class':'form-control py-4',
                     'placeholder':'Ваще имя',
                }),
            'email':forms.TextInput(attrs={
                    'class':'form-control py-4',
                     'placeholder':'Ваша почта',
                }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control py-4 number-type',
                'placeholder': 'Ваш номер',
                'type' : 'number'
            }),
            'subject':forms.TextInput(attrs={
                    'class':'form-control py-4 theme-subject',
                     'placeholder':'Тема',
                }),
            'message':forms.Textarea(attrs={
                    'class':'form-control py-4',
                    'rows':7,
                    'cols':25,
                     'placeholder':'Письмо',
                    'style':'resize:off',
                }),
        }