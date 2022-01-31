from django import forms
from django.core import validators

# # Optional check for something in the field, but must change in the form
# def check_for_s(value):
#     if value[0].lower() != 's':
#         raise forms.ValidationError("Name should start with letter 's'")
# # the name in the form must show the validator like this:
# # class FormName(forms.Form):
# #     name = forms.CharField(validators=[check_for_s])



class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again.')
    text = forms.CharField(widget=forms.Textarea)
    # 
    # botcatcher = forms.CharField(
    #     required=False,
    #     widget=forms.HiddenInput,
    #     validators=[validators.MaxLengthValidator(0)]
    # )
    
    # #This is a manual validator for a botcathcer but djanog has a buitin one which will be used instead,
    # First you should import it: from django.core import validators
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher

    def clean(self):
        all_clean_data =  super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("Email addresses don't match, please try again.")
