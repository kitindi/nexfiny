from django.forms import ModelForm
from .models import Profile
from django.forms.widgets import TextInput,NumberInput,FileInput, Textarea


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields =['phone_number','full_name','image','bio','location']
        
        widgets = {
            'location':TextInput(attrs={'class': "block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6 mt-2",'placeholder':'Dar es Salaam, Tanzania'}),
            'phone_number':TextInput(attrs={'class': "block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6 mt-2"}),
            'full_name':TextInput(attrs={'class': "block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6 mt-2",'placeholder':'John Smith'}),
            'bio':Textarea(attrs={'class': "block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6 mt-2",'rows':3,'cols':4,'placeholder':'What are you doing for a living ?'}),
            'image':FileInput(attrs={'class': "block w-full rounded-md border-0 p-2.5 text-gray-900  ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6 mt-2"}),
                       
                       
            }