# Create your views here.

from django.http import JsonResponse
import logging
import logging.config
import sys
from sklearn.externals import joblib
import pandas as pd
import os
import json
#
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}

logging.config.dictConfig(LOGGING)

base_dir = os.path.realpath(os.path.dirname(__file__))

def handleRequest(request):

    if request.method == 'POST':

        regressor = joblib.load(base_dir + '/model.pkl')

        marital_status = request.POST.get('marital_status')
        gender = int(request.POST.get('gender'))
        age = int(request.POST.get('age'))
        occupation = int(request.POST.get('occupation'))
        city_category = int(request.POST.get('city_category'))
        stay_in_current_city_years = int(request.POST.get('stay_in_current_city_years'))
        product_category_1 = int(request.POST.get('product_category_1'))
        product_category_2 = int(request.POST.get('product_category_2'))
        product_category_3 = int(request.POST.get('product_category_3'))
        product_id = str(request.POST.get('product_id'))

        args = {"Marital_Status": [marital_status], "Gender": gender, "Age": [age], "Occupation": [occupation],
                "City_Category": city_category, "Stay_In_Current_City_Years": [stay_in_current_city_years],
                "product_category_1": [product_category_1], "product_category_2": [product_category_2],
                "product_category_3": [product_category_3], "product_id": product_id}

        data = pre_process(gender, age, occupation, city_category, stay_in_current_city_years, marital_status, product_id
                           , product_category_1, product_category_2, product_category_3)

        prediction = list(regressor.predict(data))
        jsn = {'prediction': prediction}

        return JsonResponse(jsn, safe=False)

    else:
        # jsn = {'Request': 'You have requested a POST request, this is the response'}
        jsn = {'Request': 'You have requested a GET request, this is the response'}
        return JsonResponse(jsn, safe=False)

def pre_process(Gender, Age, Occupation, City_Category, Stay_In_Current_City_Years,
                Marital_Status, Product_ID, Product_Category_1, Product_Category_2, Product_Category_3):

    Stay_In_Current_City_Years_0 = 0
    Stay_In_Current_City_Years_1 = 0
    Stay_In_Current_City_Years_2 = 0
    Stay_In_Current_City_Years_3 = 0
    Stay_In_Current_City_Years_4 = 0

    if Stay_In_Current_City_Years == 0:
        Stay_In_Current_City_Years_0 = 1
    elif Stay_In_Current_City_Years == 1:
        Stay_In_Current_City_Years_1 = 1
    elif Stay_In_Current_City_Years == 2:
        Stay_In_Current_City_Years_2 = 1
    elif Stay_In_Current_City_Years == 3:
        Stay_In_Current_City_Years_3 = 1
    else:
        Stay_In_Current_City_Years_4 = 1

    Age_Count = pd.read_csv(base_dir + '/Age_Count.csv', index_col=0)['0']
    Occupation_Count = pd.read_csv(base_dir + '/Occupation_Count.csv', index_col=0)['0']
    Product_Category_1_Count = pd.read_csv(base_dir + '/Product_Category_1_Count.csv', index_col=0)['0']
    Product_Category_2_Count = pd.read_csv(base_dir+'/Product_Category_2_Count.csv', index_col=0)['0']
    Product_Category_3_Count = pd.read_csv(base_dir+'/Product_Category_3_Count.csv', index_col=0)['0']
    Product_ID_Count = pd.read_csv(base_dir+'/Product_ID_Count.csv', index_col=0)['0']

    df = pd.DataFrame([[Gender, Age, Occupation, City_Category, Marital_Status,
                       Product_Category_1, Product_Category_2, Product_Category_3,
                       Stay_In_Current_City_Years_0, Stay_In_Current_City_Years_1,
                       Stay_In_Current_City_Years_2, Stay_In_Current_City_Years_3, Stay_In_Current_City_Years_4,
                       Age_Count[Age], Occupation_Count[Occupation],
                       Product_Category_1_Count[Product_Category_1], Product_Category_2_Count[Product_Category_2],
                       Product_Category_3_Count[Product_Category_3], Product_ID_Count[Product_ID]]],
                      columns=['Gender', 'Age', 'Occupation', 'City_Category', 'Marital_Status',
                               'Product_Category_1', 'Product_Category_2', 'Product_Category_3',
                               'Stay_In_Current_City_Years_0', 'Stay_In_Current_City_Years_1',
                               'Stay_In_Current_City_Years_2', 'Stay_In_Current_City_Years_3',
                               'Stay_In_Current_City_Years_4',
                               'Age_Count', 'Occupation_Count', 'Product_Category_1_Count', 'Product_Category_2_Count',
                               'Product_Category_3_Count', 'Product_ID_Count'])

    return df