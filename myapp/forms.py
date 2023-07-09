from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de Tarea", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label="Descripción", max_length=1000, required=True, widget=forms.Textarea(attrs={'class': 'input'})
    )


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Titulo de Proyecto", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label="Descripción", max_length=1000, required=True, widget=forms.TextInput(attrs={'class': 'input'})
    )
