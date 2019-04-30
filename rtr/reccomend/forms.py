from django import forms

class TailorForm(forms.Form):
    Age = forms.IntegerField(label='age')
    Size = forms.IntegerField(label='size')
    Bust = forms.IntegerField(label='bust')
    Clothing_Type = forms.ChoiceField(label='clothingt',choices=[("dress","dress")])
    Occasion = forms.ChoiceField(label='occasion',choices=[("N/A", "nothing specific"),("wedding","wedding"),("date","data"),("weekend","weekend")])
