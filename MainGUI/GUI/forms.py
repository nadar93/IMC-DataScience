from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

#added test comment for Jenkins

occupation_choices = [(1, 'Occupation 1'), (2, 'Occupation 2'), (3, 'Occupation 3'), (4, 'Occupation 4'),
                      (5, 'Occupation 5'), (6, 'Occupation 6'), (7, 'Occupation 7'), (8, 'Occupation 8'),
                      (9, 'Occupation 9'), (10, 'Occupation 10'), (11, 'Occupation 11'), (12, 'Occupation 12'),
                    (13, 'Occupation 13'), (14, 'Occupation 14'), (15, 'Occupation 15'), (16, 'Occupation 16'),
                      (17, 'Occupation 17'), (18, 'Occupation 18'), (19, 'Occupation 19'), (20, 'Occupation 20')]

age_choices = [(0, '0-17'), (1, '18-25'), (2, '26-35'), (3, '36-45'),
                                           (4, '46-50'), (5, '51-55'), (6, '55+')]

city_choices = [(0, 'City A'), (1, 'City B'), (2, 'City C')]
gender_choices = [(1, 'Female'), (0, 'Male')]

category_choice1 = [(1, 'Category 1'), (2, 'Category 2'), (3, 'Category 3'), (4, 'Category 4'),
                   (5, 'Category 5'), (6, 'Category 6'), (7, 'Category 7'), (8, 'Category 8'), (9, 'Category 9'),
                   (10, 'Category 10'), (11, 'Category 11'), (12, 'Category 12'), (13, 'Category 13'), (14, 'Category 14'),
                   (15, 'Category 15'), (16, 'Category 16'), (17, 'Category 17'), (18, 'Category 18')]

category_choice2 = [(0, 'Category 0'), (2, 'Category 2'), (3, 'Category 3'), (4, 'Category 4'),
                   (5, 'Category 5'), (6, 'Category 6'), (7, 'Category 7'), (8, 'Category 8'), (9, 'Category 9'),
                   (10, 'Category 10'), (11, 'Category 11'), (12, 'Category 12'), (13, 'Category 13'), (14, 'Category 14'),
                   (15, 'Category 15'), (16, 'Category 16'), (17, 'Category 17'), (18, 'Category 18')]

category_choice3 = [(0, 'Category 0'), (3, 'Category 3'), (4, 'Category 4'),
                   (5, 'Category 5'), (6, 'Category 6'), (7, 'Category 7'), (8, 'Category 8'), (9, 'Category 9'),
                   (10, 'Category 10'), (11, 'Category 11'), (12, 'Category 12'), (13, 'Category 13'), (14, 'Category 14'),
                   (15, 'Category 15'), (16, 'Category 16'), (17, 'Category 17'), (18, 'Category 18')]

marital_choises = [(0, 'Not Married'), (1, 'Married')]

class mlForm(forms.Form):

    age = forms.ChoiceField(choices=age_choices)
    city_category = forms.ChoiceField(choices=city_choices)
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect(), required=True)
    stay_in_current_city_years = forms.IntegerField()
    marital_status = forms.ChoiceField(choices=marital_choises, widget=forms.RadioSelect(), required=True)
    occupation = forms.ChoiceField(choices=occupation_choices)
    product_category_1 = forms.ChoiceField(choices=category_choice1)
    product_category_2 = forms.ChoiceField(choices=category_choice2)
    product_category_3 = forms.ChoiceField(choices=category_choice3)
    product_id = forms.CharField(required=True
                                 )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper


