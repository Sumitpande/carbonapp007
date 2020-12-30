from django import forms

from .models import *
from allauth.account.forms import SignupForm

# class MyCustomSignupForm(SignupForm):
#     def __init__(self, *args, **kwargs):
#         super(MyCustomSignupForm, self).__init__(*args, **kwargs)
#         # self.fields['organization'] = forms.CharField(required=True)
#         for fieldname, field in self.fields.items():
#             field.widget.attrs.update({
#                 'class': 'red-border'
#             })
            
#     def save(self, request):
#         # organization = self.cleaned_data.pop('organization')
   
#         user = super(MyCustomSignupForm, self).save(request)

class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'red-border'
        })

        
    first_name = forms.CharField(max_length=30, label='First Name')

    last_name = forms.CharField(max_length=30, label='Last Name')


	
    def signup(self, request, user):

        user.first_name = self.cleaned_data['first_name']

        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

    


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text','image')
        widgets = {
          'text': forms.Textarea(attrs={'rows':3, 'cols':25}),
        }

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('image',)
        

class BioForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio',)
        widgets = {
          'bio': forms.Textarea(attrs={'rows':3, 'cols':25}),
        }
        