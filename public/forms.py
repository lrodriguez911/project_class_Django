from django import forms

class ContactForm(forms.Form):
    TYPE_CONSULT =(
        ('', '-Select-'),
        (1, 'Inscription'),
        (2, 'Support'),
        (3, 'Be Teacher'),
    )
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='email', max_length=100)
    issue = forms.CharField(label='Issue')
    message = forms.CharField(label='Message')
    type_consult = forms.ChoiceField(label='Type Consult', choices=TYPE_CONSULT, initial=2, widget=forms.Select)
    subscribe = forms.BooleanField(label='Subscribe', required=False)