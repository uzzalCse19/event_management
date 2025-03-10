

from django import forms
from .models import Event, Participant, Category

class StyledFormMixin:
    def add_common_attrs(self,field):
        field.widget.attrs.update({
            'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300'

        })
        return field
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            self.add_common_attrs(field)



class EventForm(StyledFormMixin,forms.ModelForm):
    class Meta:
        model=Event
        fields=['name','description','date','time','location','category']
        widgets= {
           'date':forms.DateInput(attrs={'type': 'date'}),
           'time': forms.TimeInput(attrs={'type': 'time'}),
        }


class CategoryForm(StyledFormMixin,forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','description']

class ParticipantForm(StyledFormMixin,forms.ModelForm):
    class Meta:
        model=Participant
        fields=['name','email','events']










# # class EventForm(forms.ModelForm):
# # #     class Meta:
# # #         model = Event
# # #         fields = ['name', 'description', 'date', 'time', 'location', 'category']
# # #         widgets = {
# # #            'date':forms.SelectDateWidget,
# # #            'time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}), 
# # #         }


# # from django import forms
# # from .models import Event,Category

# # class EventForm(forms.ModelForm):
# #     class Meta:
# #         model = Event
# #         fields = ['name', 'description', 'date', 'time', 'location', 'category']
# #         widgets = {
# #             'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300'}),
# #             'description': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300'}),
# #             'date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300'}),
# #             'time': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300'}),
# #             'location': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300'}),
# #             'category': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300'}),
# #         }


# # class CategoryForm(forms.ModelForm):
# #     class Meta:
# #         model = Category
# #         fields = ['name', 'description']

# # # forms.py

# # class ParticipantForm(forms.ModelForm):
# #     class Meta:
# #         model = Participant
# #         fields = ['name', 'email', 'events']