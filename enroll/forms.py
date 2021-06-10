from django import forms
from .models import User,User2

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        widgets={
                'name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),}

                # 'sub':forms.TextInput(attrs={'class':'form-control'}),
class widgestform(forms.ModelForm):
    class Meta:
        model=User2
        fields=['name','email','password','sub','add'] 
        widgets={
                
                  'email':forms.EmailInput(attrs={'class':'form-control'}),
                   'add':forms.TextInput(attrs={'class':'form-control'}),
                }               
                


