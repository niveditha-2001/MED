from django import forms
from registrationapp.models import registration

class rgform(forms.ModelForm):
    class Meta:
        model=registration
        fields=['username','last_name','first_name','mob','password','email']
    def clean(self):
        user=self.cleaned_data['username']
        # if not(user[0].isupper()) and not(len(user)>=6):
        if not(user[0].isupper()) or not(len(user)>=6):
            raise ValueError('username should be 6 chars and first char is uppercase')
        mob=self.cleaned_data['mob']
        if str(mob)[0] not in ['6','7','8','9'] or len(str(mob))!=10:
            raise ValueError('mobile num contains 10 digits and starting with 6789')
        
    
    


    # def clean_mob(self):
    #     mob=self.cleaned_data['mob']
    #     if str(mob)[0] not in ['6','7','8','9'] or len(str(mob))!=10:
    #         raise ValueError('mobile num contains 10 digits and starting with (6,7,8,9)')
    #     return mob
    # def clean_pas(self):
    #     pas=self.cleaned_data['pas']
    #     if '0'<=pas<='9' 
    
    