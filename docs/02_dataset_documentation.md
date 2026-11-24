# Titanic Survival Prediction – Dataset Documentation

## 1. Dataset Introduction

The Titanic dataset contains historical passenger information from the Titanic disaster.

The dataset provides passenger-related attributes such as age, gender, passenger class, ticket fare, family information, cabin details, and survival status.

This dataset is used to investigate patterns associated with passenger survival and develop a supervised Machine Learning classification model.

## 2. Dataset Files

The project contains three CSV files:

| File Name | Description |
|---|---|
| train.csv | Contains passenger information and survival labels for model training. |
| test.csv | Contains passenger information without survival labels for prediction. |
| gender_submission.csv | Provides sample survival predictions for the test dataset. |

## 3. Training Dataset Overview

The training dataset was loaded using Pandas.

| Parameter | Value |
|---|---|
| File Name | train.csv |
| Total Rows | 891 |
| Total Columns | 12 |
| Target Column | Survived |
| File Format | CSV |
| Duplicate Records | 0 |

## 4. Feature Description

The training dataset contains the following features:

| Feature | Data Type | Description |
|---|---|---|
| PassengerId | Integer | Unique identifier assigned to each passenger. |
| Survived | Integer | Target variable indicating passenger survival. |
| Pclass | Integer | Passenger ticket class (1st, 2nd or 3rd). |
| Name | String | Passenger's full name and title. |
| Sex | String | Passenger gender. |
| Age | Float | Passenger age in years. |
| SibSp | Integer | Number of siblings or spouses aboard. |
| Parch | Integer | Number of parents or children aboard. |
| Ticket | String | Passenger ticket identification number. |
| Fare | Float | Passenger ticket fare. |
| Cabin | String | Passenger cabin identification. |
| Embarked | String | Port where the passenger boarded. |

## 5. Data Type Distribution

Based on the initial dataset inspection:

| Data Type | Number of Columns |
|---|---:|
| Integer (int64) | 5 |
| Float (float64) | 2 |
| String (str) | 5 |
| Total | 12 |

The dataset contains both numerical and categorical features.

## 6. Missing Value Analysis

The following missing values were identified during the initial inspection:

| Feature | Missing Records | Missing Percentage |
|---|---:|---:|
| Age | 177 | 19.87% |
| Cabin | 687 | 77.10% |
| Embarked | 2 | 0.22% |
| Other Columns | 0 | 0% |

### Observations

**Age:**
- Contains 177 missing records.
- Approximately 19.87% of age information is unavailable.
- Requires an appropriate imputation strategy.

**Cabin:**
- Contains 687 missing records.
- Approximately 77.10% of cabin information is unavailable.
- Requires further investigation to determine its usefulness.

**Embarked:**
- Contains only 2 missing records.
- Missing values can potentially be handled using the most frequent category.

No missing values were identified in the target variable.

## 7. Statistical Summary

The following statistical observations were obtained from the numerical features:

| Feature | Mean | Median |
|---|---:|---:|
| Age | 29.70 | 28.00 |
| Fare | 32.20 | 14.45 |
| SibSp | 0.52 | 0.00 |
| Parch | 0.38 | 0.00 |

### Initial Observations

- The average passenger age is approximately 29.70 years.
- The median passenger age is 28 years.
- The average ticket fare is higher than its median, suggesting a potentially right-skewed distribution.
- The median values of SibSp and Parch are zero, indicating that at least half of the passengers had no siblings/spouses or parents/children aboard, respectively.

## 8. Target Variable Description

The target feature is `Survived`.

| Value | Meaning |
|---|---|
| 0 | Passenger did not survive |
| 1 | Passenger survived |

The target variable contains no missing values.

Initial survival distribution:

- Survival rate: approximately 38.38%.
- Non-survival rate: approximately 61.62%.

Further analysis will be performed during Exploratory Data Analysis.

## 9. Data Quality Assessment

The initial dataset inspection identified the following:

1. The training dataset contains 891 passenger records.
2. No duplicate rows were identified.
3. Missing values are present in Age, Cabin and Embarked.
4. Both numerical and categorical features are available.
5. The target variable is complete.
6. Some columns may require feature engineering or further evaluation before model development.

## 10. Potential Data Preprocessing Requirements

The following preprocessing activities are planned:

- Handle missing values in Age.
- Investigate missing values in Cabin and determine whether the feature should be retained or transformed.
- Handle missing values in Embarked.
- Encode categorical features such as Sex and Embarked.
- Investigate the usefulness of Name, Ticket and PassengerId.
- Examine outliers and feature distributions.
- Perform feature engineering where appropriate.
- Prepare numerical features for model training.

These are proposed activities and will be finalized after further analysis.

## 11. Dataset Limitations

- A considerable percentage of Cabin information is unavailable.
- Some passenger records have incomplete age information.
- The dataset represents a specific historical event.
- Certain features may contain limited predictive information.
- The training dataset is relatively small compared with datasets used in large-scale production Machine Learning systems.

## 12. Conclusion

The initial dataset inspection confirms that the Titanic training dataset is suitable for a binary classification problem.

However, missing values, categorical variables and feature relevance must be investigated before model development.

The next stage is Exploratory Data Analysis (EDA), where relationships between passenger characteristics and survival outcomes will be examined.

## 13. Current Status

**Completed:** Dataset loading and initial inspection.

**Pending:** Detailed feature analysis, visualization and preprocessing.

**Next Stage:** Exploratory Data Analysis (EDA).