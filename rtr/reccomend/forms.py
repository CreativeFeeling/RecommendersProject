from django import forms

class TailorForm(forms.Form):
    Age = forms.IntegerField(label='age')
    Size = forms.IntegerField(label='size')
    Bust = forms.ChoiceField(label='bust',
                            choices=[
                                ('A','A30'),('A','A32'),('A','A34'),('A','A36'),('A','A38'),('A','A40'),
                                ('B','B30'),('B','B32'),('B','B34'),('B','B36'),('B','B38'),('B','B40'),
                                ('C','C30'),('C','C32'),('C','C34'),('C','C36'),('C','C38'),('C','C40'),
                                ('D','D30'),('D','D32'),('D','D34'),('D','D36'),('D','D38'),('D','D40'),
                                ('DD','DD30'),('DD','DD32'),('DD','DD34'),('DD','DD36'),('DD','DD38'),('DD','DD40'),
                                ('DDD','DDD30'),('DDD','DDD32'),('DDD','DDD34'),('DDD','DDD36'),('DDD','DDD38'),('DDD','DDD40'),
                            ])
    Clothing_Type = forms.ChoiceField(label='clothingt',
                            choices=[
                                ("dress","dress")
                            ])
    Occasion = forms.ChoiceField(label='occasion',
                            choices=[
                                ("N/A", "nothing specific"),
                                ("wedding","wedding"),
                                ("date","data"),
                                ("weekend","weekend")
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
