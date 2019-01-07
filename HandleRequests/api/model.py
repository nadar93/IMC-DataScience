import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score, ShuffleSplit

train = pd.read_csv('train.csv')
test  = pd.read_csv('test.csv')

# Join Train and Test Dataset
train['source']='train'
test['source'] ='test'
data = pd.concat([train,test], ignore_index = True, sort = False)

# Fill null data with 0
data['Product_Category_2'].fillna(0,inplace=True)
data['Product_Category_3'].fillna(0,inplace=True)

# Drop rows where Product_Category_1 = 19 and 20 
# because the amount of these data is very small and doesn't exist in the test dataset
condition = data.index[(data.Product_Category_1.isin([19,20])) & (data.source == 'train')]
data = data.drop(condition)

# Gender to binary
gender_dict = {'F':0, 'M':1}
data['Gender'] = data['Gender'].apply(lambda line: gender_dict[line])

# Age to numerical
age_dict = {'0-17':0, '18-25':1, '26-35':2, '36-45':3, '46-50':4, '51-55':5, '55+':6}
data['Age'] = data['Age'].apply(lambda line: age_dict[line])

# City to numerical
city_dict = {'A':0, 'B':1, 'C':2}
data['City_Category'] = data['City_Category'].apply(lambda line: city_dict[line])
    
# Stay_In_Current_City_Years to numerical
years_dict = {'0':0, '1':1, '2':2, '3':3, '4+':4}
data['Stay_In_Current_City_Years'] = data['Stay_In_Current_City_Years'].apply(lambda line: years_dict[line])

# Feature representing the count of each label
def getCount(data, column):
    count_dict = {}
    grouped_df = data.groupby(column)
    for name, group in grouped_df:
        count_dict[name] = group.shape[0]

    count_list = []
    for val in data[column]:
        count_list.append(count_dict.get(val, 0))

    return count_list, count_dict


data['Age_Count'], Age_Count = getCount(data,'Age')
data['Occupation_Count'], Occupation_Count = getCount(data, 'Occupation')
data['Product_Category_1_Count'], Product_Category_1_Count = getCount(data,'Product_Category_1')
data['Product_Category_2_Count'], Product_Category_2_Count = getCount(data,'Product_Category_2')
data['Product_Category_3_Count'], Product_Category_3_Count = getCount(data,'Product_Category_3')
data['Product_ID_Count'], Product_ID_Count = getCount(data,'Product_ID')
data['Stay_In_Current_City_Years_Count'], Stay_In_Current_City_Years_Count = getCount(data,'Stay_In_Current_City_Years')

pd.DataFrame(pd.Series(Age_Count)).to_csv('Age_Count.csv')
pd.DataFrame(pd.Series(Occupation_Count)).to_csv('Occupation_Count.csv')
pd.DataFrame(pd.Series(Product_Category_1_Count)).to_csv('Product_Category_1_Count.csv')
pd.DataFrame(pd.Series(Product_Category_2_Count)).to_csv('Product_Category_2_Count.csv')
pd.DataFrame(pd.Series(Product_Category_3_Count)).to_csv('Product_Category_3_Count.csv')
pd.DataFrame(pd.Series(Product_ID_Count)).to_csv('Product_ID_Count.csv')
pd.DataFrame(pd.Series(Stay_In_Current_City_Years_Count)).to_csv('Stay_In_Current_City_Years_Count.csv')

# Divide into test and train
train = data.loc[data['source']=='train'].copy()
test  = data.loc[data['source']=='test' ].copy()

# Drop unnecessary columns
train.drop(columns = ['source'],inplace=True)
test.drop( columns = ['source'],inplace=True)


# Define target 
target = 'Purchase'
features = train.columns.drop(['Product_ID','User_ID','Purchase'])
output = ['User_ID','Product_ID','Purchase']

def modelfit(model, train, test, features, target, output, filename):

    # Cross-Validation
    cv = ShuffleSplit(n_splits=3,test_size=0.02)
    cv_score = cross_val_score(model, train[features],(train[target]) , cv=cv, scoring='r2')
    
    # Model report
    print('\nModel Report')
    print('R2 : %.4g' % cv_score.mean())
    
    if 0.8 <= cv_score.mean():
        # Fit the algorithm on the data
        model.fit(train[features], train[target])

        # Prediction
        test[target] = model.predict(test[features])

        # Export submission file
        submission = pd.DataFrame({x: test[x] for x in output})
        submission.to_csv(filename, index=False)
        
        #save model
        joblib.dump(model, 'rfr.pkl')

model = RandomForestRegressor(n_estimators = 100,min_samples_leaf = 30,n_jobs = 3)
modelfit(model, train, test, features, target, output, 'Prediction.csv')