from django.views.generic.base import TemplateView
from django.http import JsonResponse
from GUI.forms import mlForm
from django.shortcuts import render
import requests
import json


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"


class Dashboard(TemplateView):
    template_name = 'dashboard.html'
    request_url = 'http://192.168.99.100:5002/api/'
    #request_url = 'http://127.0.0.1:8000/api/'

    def get(self, request):
        form = mlForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = mlForm(request.POST)

        if form.is_valid():
            marital_status = form.cleaned_data['marital_status']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            occupation = form.cleaned_data['occupation']
            city_category = form.cleaned_data['city_category']
            stay_in_current_city_years = form.cleaned_data['stay_in_current_city_years']
            product_category_1 = form.cleaned_data['product_category_1']
            product_category_2 = form.cleaned_data['product_category_2']
            product_category_3 = form.cleaned_data['product_category_3']
            product_id = form.cleaned_data['product_id']
            args = {'marital_status': marital_status, 'gender': gender, 'age': age, 'occupation': occupation,
                    'city_category': city_category, 'stay_in_current_city_years': stay_in_current_city_years,
                    'product_category_1': product_category_1, 'product_category_2': product_category_2,
                    'product_category_3': product_category_3, 'product_id': product_id
                    }

            try:
                response = requests.post(url=self.request_url, data=args)
                return render(request, self.template_name, {'result_text': response.json()['prediction'], 'ok': 'ok'})
            except:
                result_text = "Failed to fetch prediction"
                return render(request, self.template_name, {'result_text': result_text, 'notok': 'notok'})

        result_text = "Failed to fetch prediction"

        return render(request, self.template_name, {'result_text': result_text, 'notok': 'notok'})
