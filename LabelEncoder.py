import pandas as pd
from sklearn import preprocessing


def get_output_schema():
	return pd.DataFrame({
        'Region Encoded':prep_int(),
        'Opportunity Result Encoded':prep_int(),
        'Opportunity Number':prep_int(),
        'Supplies Subgroup Encoded' : prep_int(),
        })


def encode(input):     
  le = preprocessing.LabelEncoder()
  return pd.DataFrame({
    'Opportunity Number' : input['Opportunity Number'],
    'Supplies Subgroup Encoded' : le.fit_transform(input['Supplies Subgroup']),
    'Region Encoded' : le.fit_transform(input['Region']),
    #'Route To Market Encoded' : le.fit_transform(input['Route To Market']),
    'Opportunity Result Encoded' : le.fit_transform(input['Opportunity Result']),
    #'Competitor Type Encoded' : le.fit_transform(input['Competitor Type']),
    #'Supplies Group Encoded' : le.fit_transform(input['Supplies Group']),
    })