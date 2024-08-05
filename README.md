# Demographic Data Analyzer

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
<img src="https://pandas.pydata.org/static/img/pandas_white.svg" width="175" height="175" alt="Pandas" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Demographic Data Analyzer application, follow the instructions in the Setup section below.

## Project Structure

- `demographic_data_analyzer.py`: Contains the implementation of the `calculate_demographic_data` function that performs the demographic analysis.
- `main.py`: Used for development and testing the `calculate_demographic_data` function.

## Setup

### Prerequisites

- Python 3 installed
- Pandas installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/demographic-da-fcc-data-analyses-py-cert.git
   cd demographic-data-analyzer-fcc-data-analysis-py-cert
   ```

2. Run the Demographic Data Analyzer script:
   ```bash
   python3 main.py
   ```

## Demographic Data Analyzer

### Functionality

The Demographic Data Analyzer computes various statistics from a demographic dataset. The dataset contains information extracted from the 1994 Census database.

### calculate_demographic_data Function

#### Parameters

- `print_data` (default `True`): If set to `True`, prints the results to the console.

#### Returns

- A dictionary with the calculated demographic statistics.

### Practical Use Case

This analyzer is useful for extracting and computing demographic statistics from a large dataset, providing insights into the population's characteristics.

### Benefits

- **Data Analysis:** Quickly compute essential demographic statistics using Pandas.
- **Python Standard Library:** Utilizes Pandas for efficient data manipulation and analysis.

## How to Use

1. Call the `calculate_demographic_data` function with the `print_data` parameter set to `True` or `False`.
2. The function will return a dictionary with the calculated statistics.

### Example Usage

```python
import demographic_data_analyzer

result = demographic_data_analyzer.calculate_demographic_data(print_data=True)
print(result)
```

### Example Output

```plaintext
Number of each race:
 White                 27816
Black                  3124
Asian-Pac-Islander     1039
Amer-Indian-Eskimo      311
Other                   271
Name: race, dtype: int64
Average age of men: 39.4
Percentage with Bachelors degrees: 16.4%
Min work time: 1 hours/week
Percentage of rich among those who work fewest hours: 10.0%
Top occupations in India: Prof-specialty
{
  'race_count': race_count,
  'average_age_men': average_age_men,
  'percentage_bachelors': percentage_bachelors,
  'higher_education_rich': higher_education_rich,
  'lower_education_rich': lower_education_rich,
  'min_work_hours': min_work_hours,
  'rich_percentage': rich_percentage,
  'highest_earning_country': highest_earning_country,
  'highest_earning_country_percentage': highest_earning_country_percentage,
  'top_IN_occupation': top_IN_occupation
}
```

### Additional Information

- **Dataset:** Extracted from the 1994 Census database.
- **Comprehensive Statistics:** Computes various demographic statistics for thorough analysis.

---
#### This is a FreeCodeCamp Challenge for Data Analysis with Python Projects Certification.
<p align="center">
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" width="250" height="75" alt="freeCodeCamp" style="margin: 0 15px; opacity: 0.6" />
</p>
