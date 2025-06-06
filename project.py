import numpy as np
import pandas as pd
import seaborn as sns
import os

# Listing Out the Files 
print(os.listdir('stack-overflow-developer-survey-2020'))

# Reading the CSV Files

survey_raw_df = pd.read_csv('stack-overflow-developer-survey-2020/survey_results_public.csv')

print("Data Set for public:\n", survey_raw_df, "\n")

# print(survey_raw_df.columns, "\n")

schema_raw_df = pd.read_csv('stack-overflow-developer-survey-2020/survey_results_schema.csv', index_col='Column')

schema_series = schema_raw_df.QuestionText

print(schema_series, "\n")  # we just need the Questions now, this would make a pandas SERIES which has 'Column' as index and coresponding QuestionText as Value 

print(schema_series['YearsCodePro'], "\n") 

# Data Preparation & Cleaning 
  # we will limit our survey analysis to the following areas:
  # 1) Demographics of the survey respondents & the Global programming community
  # 2) Distribution of programming skills, experiencing and preferences 
  # 3) Employment-related information, preferences, opinion
  
selected_columns = [ # Demographics
                    'Country', 'Age', 'Gender', 'EdLevel', 'UndergradMajor',
                    
                    # programming Experience 
                    'Hobbyist', 
                    'Age1stCode',
                    'YearsCode',
                    'YearsCodePro',
                    'LanguageWorkedWith',
                    'LanguageDesireNextYear',
                    'NEWLearn', 
                    'NEWStuck', 
                    
                    # Employment
                    'Employment', 'DevType', 
                    'WorkWeekHrs', 'JobSat',
                    'JobFactors',  'NEWOvertime', 'NEWEdImpt'
                    ]

# print("\n", len(selected_columns))
# print("\n", survey_raw_df.columns, "\n")

survey_df = survey_raw_df[selected_columns].copy()

schema = schema_series[selected_columns]  # The Key-Value paired SERIES when passed with the selected_column gives the Index as the same, and the Question corresponding to it.  

print("Data Frame with All new columns\n", survey_df, "\n", "This is the Schema we have:\n", schema, "\n")

print(survey_df.info(), "\n")

# While Working with more number of Datas, most of the Data type will be of type OBJECT. There would be no problem to work with the String Data Type, but we have to convert all the numbers associated column to numeric Data type for our analyisis purpose. 




















