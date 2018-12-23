import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.externals import joblib

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Join Train and Test Dataset
train['source']='train'
test['source']='test'
data = pd.concat([train,test], ignore_index = True, sort = False)

# Fill null data
data['Product_Category_2']= \
data['Product_Category_2'].fillna(0.0).astype('float')
data['Product_Category_3']= \
data['Product_Category_3'].fillna(0.0).astype('float')

# We delete rows where Product_Category_1 = 19 and 20 because the amount of these data is very small and doesn't exist in the test dataset
condition = data.index[(data.Product_Category_1.isin([19,20])) & (data.source == 'train')]
data = data.drop(condition)

# Turn gender binary
gender_dict = {'F':0, 'M':1}
data['Gender'] = data['Gender'].apply(lambda line: gender_dict[line])

# Giving Age Numerical values
age_dict = {'0-17':0, '18-25':1, '26-35':2, '36-45':3, '46-50':4, '51-55':5, '55+':6}
data['Age'] = data['Age'].apply(lambda line: age_dict[line])

city_dict = {'A':0, 'B':1, 'C':2}
data['City_Category'] = data['City_Category'].apply(lambda line: city_dict[line])

le = LabelEncoder()
# New variable for outlet
data['Stay_In_Current_City_Years'] = le.fit_transform(data['Stay_In_Current_City_Years'])
    
# Dummy Variables
data = pd.get_dummies(data, columns=['Stay_In_Current_City_Years'])


# feature representing the count of each user
def getCountVar(compute_df, count_df, var_name):
    grouped_df = count_df.groupby(var_name)
    count_dict = {}
    count_list = []
    for name, group in grouped_df:
        count_dict[name] = group.shape[0]

    for index,row in compute_df.iterrows():
        name = row[var_name]
        count_list.append(count_dict.get(name, 0))
    return count_list, count_dict

# data[“User_ID_Count”] = getCountVar(data, data, “User_ID”)
data['Age_Count'], Age_Count = getCountVar(data, data, 'Age')
data['Occupation_Count'], Occupation_Count = getCountVar(data, data, 'Occupation')
data['Product_Category_1_Count'], Product_Category_1_Count = getCountVar(data, data,'Product_Category_1')
data['Product_Category_2_Count'], Product_Category_2_Count = getCountVar(data, data, 'Product_Category_2')
data['Product_Category_3_Count'], Product_Category_3_Count = getCountVar(data, data,'Product_Category_3')
data['Product_ID_Count'], Product_ID_Count = getCountVar(data, data, 'Product_ID')

# write counts
pd.DataFrame(pd.Series(Age_Count)).to_csv('Age_Count.csv')
pd.DataFrame(pd.Series(Occupation_Count)).to_csv('Occupation_Count.csv')
pd.DataFrame(pd.Series(Product_Category_1_Count)).to_csv('Product_Category_1_Count.csv')
pd.DataFrame(pd.Series(Product_Category_2_Count)).to_csv('Product_Category_2_Count.csv')
pd.DataFrame(pd.Series(Product_Category_3_Count)).to_csv('Product_Category_3_Count.csv')
pd.DataFrame(pd.Series(Product_ID_Count)).to_csv('Product_ID_Count.csv')

# Divide into test and train
train = data.loc[data['source']=='train']
test = data.loc[data['source']=='test']

# Drop 'source'  columns:
test.drop(['source'],axis=1,inplace=True)
train.drop(['source'],axis=1,inplace=True)

# Define target and ID columns
target = 'Purchase'
IDcol = ['User_ID','Product_ID']
def modelfit(alg, dtrain, dtest, predictors, target, IDcol, filename):
    # Fit the algorithm on the data
    alg.fit(dtrain[predictors], dtrain[target])
        
    # Predict training set
    dtrain_predictions = alg.predict(dtrain[predictors])
    # Perform cross-validation
    cv_score = model_selection.cross_val_score(alg, dtrain[predictors],(dtrain[target]) , cv=20, scoring='neg_mean_squared_error')
    cv_score = np.sqrt(np.abs(cv_score))
    
    # Print model report
    print('\nModel Report')
    print('RMSE : %.4g' % np.sqrt(mean_squared_error((dtrain[target]).values, dtrain_predictions)))
    print('R2 : %.4g' % r2_score((dtrain[target]).values,dtrain_predictions))
    print('CV Score : Mean - %.4g | Std - %.4g | Min - %.4g | Max - %.4g' % (np.mean(cv_score),np.std(cv_score),np.min(cv_score),np.max(cv_score)))
    
    # Predict on testing data
    dtest[target] = alg.predict(dtest[predictors])
    
    # Export submission file
    IDcol.append(target)
    submission = pd.DataFrame({ x: dtest[x] for x in IDcol})
    submission.to_csv(filename, index=False)


predictors = train.columns.drop(['Purchase','Product_ID','User_ID'])

regressor = RandomForestRegressor(n_estimators = 10, random_state = 0) 
modelfit(regressor, train, test, predictors, target, IDcol, 'Pridiction.csv')

#save model
joblib.dump(regressor, 'rfr.pkl')
