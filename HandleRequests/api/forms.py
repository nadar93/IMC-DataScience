from django import forms

class mlForm(forms.Form):
    marital_status = forms.BooleanField(help_text="Married?")
    gender = forms.ChoiceField(choices=[('female', 'Female'), ('male', 'Male')], widget=forms.RadioSelect())
    age = forms.IntegerField(required=False)
    occupation = forms.IntegerField()
    city_category = forms.CharField()
    stay_in_current_city_years = forms.IntegerField()
    product_category_1 = forms.IntegerField()
    product_category_2 = forms.IntegerField()
    product_category_3 = forms.IntegerField()
    purchase = forms.IntegerField()