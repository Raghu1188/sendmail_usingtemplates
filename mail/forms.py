from django import forms

class Contactmail(forms.Form):
  Sender_id = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  Subject = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
  Message = forms.CharField(max_length=250,widget=forms.Textarea(attrs={'class': 'form-control'}))
  