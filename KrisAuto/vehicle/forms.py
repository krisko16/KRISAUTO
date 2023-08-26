from django import forms

from .models import Vehicle

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('category', 'make', 'model', 'power_hp', 'year', 'price', 'image', 'description',)

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'make': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'model': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'power_hp': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'year': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('make', 'model', 'power_hp', 'year', 'price', 'image', 'description',)

        widgets = {
            'make': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'model': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'power_hp': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'year': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            })
        }
