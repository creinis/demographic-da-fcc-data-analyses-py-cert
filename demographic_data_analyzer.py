import pandas as pd

def calculate_demographic_data(print_data=True):
    
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset?
    # This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    
    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
      (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education = df[df['education'].isin(
      ['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = round(
      (higher_education[higher_education['salary'] == '>50K'].shape[0] /
       higher_education.shape[0]) * 100, 1)
    
    # What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = round(
      (lower_education[lower_education['salary'] == '>50K'].shape[0] /
       lower_education.shape[0]) * 100, 1)
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    
    
    
    return {
      'race_count': race_count,
      'average_age_men': average_age_men,
      'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
    }





