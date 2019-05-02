from django import forms

class TailorForm(forms.Form):
    Age = forms.IntegerField(label='age')
    Size = forms.IntegerField(label='size')
    Bust = forms.ChoiceField(label='bust',
                            choices=[
                                ('30a','30a'),('32a','32a'),('34a','34a'),('36a','36a'),('38a','38a'),('40a','40a'),
                                ('30b','30b'),('32b','32b'),('34b','34b'),('36b','36b'),('38b','38b'),('40b','40b'),
                                ('30c','30c'),('32c','32c'),('34c','34c'),('36c','36c'),('38c','38c'),('40c','40c'),
                                ('30d','30d'),('32d','32d'),('34d','34d'),('36d','36d'),('38d','38d'),('40d','40d'),
                                ('30dd','30dd'),('32dd','32dd'),('34dd','34dd'),('36dd','36dd'),('38dd','38dd'),('40dd','40dd'),
                                ('30ddd','30ddd'),('32ddd','32ddd'),('34ddd','34ddd'),('36ddd','36ddd'),('38ddd','38ddd'),('40ddd','40ddd'),
                            ])
    Clothing_Type = forms.ChoiceField(label='clothingt',
                            choices=[
                                ("dress","dress"),
                                ("skirt","skirt")
                            ])
    Occasion = forms.ChoiceField(label='occasion',
                            choices=[
                                ("wedding","wedding"),
                                ("date","data"),
                                ("party","party"),
                                ("work","work"),
                                ("formal","formal"),
                                ("vacation","vacation")
                            ])
    def get_age(self):
        return self.cleaned_data.get('Age')
    def get_size(self):
        return self.cleaned_data.get('Size')
    def get_bust(self):
        return self.cleaned_data.get('Bust')
    def get_clothing_type(self):
        return self.cleaned_data.get('Clothing_Type')
    def get_occasion(self):
        return self.cleaned_data.get('Occasion')
