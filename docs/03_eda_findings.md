 ### Experiment 1: Survival Distribution

**Objective:** Understand the distribution of passengers who survived and did not survive the Titanic disaster.

**Methodology:**

- Used `value_counts()` to calculate passenger counts.
- Used `value_counts(normalize=True)` to calculate percentages.
- Used Seaborn Countplot to visualize survival distribution.

**Results:**

| Survival Status | Passenger Count | Percentage |
|---|---:|---:|
| Survived (1) | 342 | 38.38% |
| Not Survived (0) | 549 | 61.62% |
| Total | 891 | 100% |

**Key Findings:**

1. Out of 891 passengers, 342 survived.
2. A total of 549 passengers did not survive.
3. The non-survivor group exceeds the survivor group by 207 passengers.
4. The target variable shows moderate class imbalance.

**Machine Learning Implication:**

A baseline model predicting the majority class would achieve approximately 61.62% accuracy. Therefore, accuracy alone will not be sufficient to evaluate the final classification model.

**Conclusion:**

The initial analysis indicates that passenger survival was not evenly distributed. Further investigation is required to identify the passenger characteristics associated with survival.

**Status:** Completed.

### Experiment 2: Gender vs Survival Analysis

**Objective:** Investigate the relationship between passenger gender and survival outcomes.

**Methodology:**

- Used Pandas `groupby()` to group passengers by gender and survival status.
- Used `value_counts` through grouped aggregation to calculate survival counts.
- Calculated gender-wise survival rates using the mean of the binary target variable.
- Used Seaborn barplot for visualization.

**Results:**

| Gender | Did Not Survive | Survived | Total |
|---|---:|---:|---:|
| Female | 81 | 233 | 314 |
| Male | 468 | 109 | 577 |

**Survival Rates:**

| Gender | Survival Rate |
|---|---:|
| Female | 74.20% |
| Male | 18.89% |

**Key Findings:**

1. Female passengers had a significantly higher survival rate than male passengers.
2. Approximately 74.20% of female passengers survived.
3. Approximately 18.89% of male passengers survived.
4. The observed survival-rate difference was approximately 55.31 percentage points.

**Machine Learning Implication:**

The Sex feature appears to have strong predictive potential and should be considered during feature selection and model development.

**Conclusion:**

The analysis identifies a strong association between passenger gender and survival outcomes in the Titanic training dataset.

**Status:** Completed.

### Experiment 3: Passenger Class vs Survival

**Objective:** Investigate the relationship between passenger ticket class and survival outcomes.

**Methodology:**

- Grouped passengers using `Pclass` and `Survived`.
- Calculated survival counts using Pandas `groupby()` and `unstack()`.
- Calculated survival percentages using the mean of the binary target variable.
- Visualized survival rates using Seaborn barplot.

**Results:**

| Passenger Class | Did Not Survive | Survived | Total |
|---|---:|---:|---:|
| 1st Class | 80 | 136 | 216 |
| 2nd Class | 97 | 87 | 184 |
| 3rd Class | 372 | 119 | 491 |

**Survival Rates:**

| Passenger Class | Survival Rate |
|---|---:|
| 1st Class | 62.96% |
| 2nd Class | 47.28% |
| 3rd Class | 24.24% |

**Key Findings:**

1. First-class passengers recorded the highest survival rate.
2. Third-class passengers recorded the lowest survival rate.
3. Survival rates decreased across the three passenger classes.
4. Passenger class shows a strong association with survival outcomes.

**Machine Learning Implication:**

Pclass is a potentially important predictive feature and should be retained for further investigation and model development.

**Conclusion:**

The analysis indicates that passenger ticket class was associated with survival outcomes in the Titanic dataset.

**Status:** Completed.

### Experiment 4: Age Distribution Analysis

**Objective:** Understand the age distribution of Titanic passengers and identify patterns in passenger age.

**Methodology:**

- Used `sns.histplot()` to visualize the age distribution.
- Used 30 histogram bins to examine passenger age frequencies.
- Enabled KDE (Kernel Density Estimation) to understand the distribution pattern.
- Used `describe()` to calculate statistical summaries.

**Statistical Results:**

| Statistic | Value |
|---|---:|
| Count | 714 |
| Mean | 29.70 |
| Standard Deviation | 14.53 |
| Minimum | 0.42 |
| 25th Percentile | 20.125 |
| Median | 28.00 |
| 75th Percentile | 38.00 |
| Maximum | 80.00 |

**Key Findings:**

1. The average passenger age was approximately 29.70 years.
2. The median passenger age was 28 years.
3. Most passengers were concentrated between approximately 18 and 35 years.
4. The distribution shows a longer tail towards older ages, suggesting right skewness.
5. The minimum recorded age was 0.42 years, indicating the presence of infants.
6. Only 714 out of 891 records contained valid age information.

**Data Quality Observation:**

A total of 177 Age values are missing, representing approximately 19.87% of the training dataset.

**Machine Learning Implication:**

Age may contain useful predictive information. Further analysis is required to investigate its relationship with passenger survival before selecting an appropriate missing-value treatment strategy.

**Conclusion:**

The age distribution indicates that most passengers were young adults, with fewer passengers in older age groups. The missing Age values require further investigation during preprocessing.

**Status:** Completed.

### Experiment 5: Age vs Survival Analysis

**Objective:** Investigate the relationship between passenger age and survival outcomes.

**Methodology:**

- Used Pandas `groupby()` to calculate average age by survival status.
- Used Seaborn `histplot()` with KDE to compare age distributions.
- Used Seaborn `boxplot()` to compare age distributions and identify potential outliers.

**Statistical Results:**

| Survival Status | Average Age |
|---|---:|
| Did Not Survive (0) | 30.63 |
| Survived (1) | 28.34 |

**Key Findings:**

1. The average age of passengers who did not survive was approximately 30.63 years.
2. The average age of passengers who survived was approximately 28.34 years.
3. The difference in average age between the two groups was approximately 2.28 years.
4. Both groups showed considerable overlap in their age distributions.
5. The boxplot indicated potential older-age outliers in both survival groups.
6. The survivor histogram showed a visible concentration of young children.

**Machine Learning Implication:**

Age may contain predictive information. However, the observed difference in average age is relatively small, and further investigation is required to understand its relationship with survival.

**Conclusion:**

The analysis indicates that passengers who survived were slightly younger on average than passengers who did not survive. Age should be retained for further investigation during feature selection and model development.

**Status:** Completed.

### Experiment 6: Fare Distribution Analysis

**Objective:** Understand the distribution of passenger ticket fares and identify potential extreme values.

**Methodology:**

- Used `describe()` to generate statistical summaries.
- Used `sns.histplot()` with KDE to visualize fare distribution.
- Used `sns.boxplot()` to investigate potential outliers.
- Used `skew()` to measure distribution asymmetry.

**Statistical Results:**

| Statistic | Value |
|---|---:|
| Count | 891 |
| Mean | 32.20 |
| Standard Deviation | 49.69 |
| Minimum | 0.00 |
| 25th Percentile | 7.91 |
| Median | 14.45 |
| 75th Percentile | 31.00 |
| Maximum | 512.33 |
| Skewness | 4.7873 |

**Key Findings:**

1. The average ticket fare was approximately 32.20.
2. The median ticket fare was approximately 14.45.
3. The maximum recorded fare was approximately 512.33.
4. The histogram shows a concentration of passengers paying relatively low fares.
5. The distribution is strongly positively skewed, with a skewness value of 4.7873.
6. The boxplot identifies several potential high-fare outliers.
7. Using the 1.5 × IQR rule, the upper outlier boundary is approximately 65.63.

**Machine Learning Implication:**

Fare may contain useful information for survival prediction. Its highly skewed distribution and extreme values should be considered during preprocessing.

A logarithmic transformation may be investigated during feature engineering.

**Conclusion:**

The ticket fare distribution is strongly concentrated towards lower values, with a smaller number of passengers paying considerably higher fares. Further analysis will investigate whether fare is associated with survival outcomes.

**Status:** Completed

### Experiment 7: Fare vs Survival Analysis

**Objective:** Investigate the relationship between passenger ticket fare and survival outcomes.

**Methodology:**

- Used Pandas `groupby()` to calculate average fare by survival status.
- Calculated median fare for both survival groups.
- Used Seaborn `boxplot()` to compare fare distributions.
- Applied `pd.qcut()` to divide passengers into four fare groups.
- Calculated survival percentages for each fare group.

**Statistical Results:**

| Survival Status | Average Fare | Median Fare |
|---|---:|---:|
| Did Not Survive (0) | 22.12 | 10.50 |
| Survived (1) | 48.40 | 26.00 |

**Survival Rate by Fare Group:**

| Fare Group | Survival Rate |
|---|---:|
| Group 1 (0–7.91) | 19.73% |
| Group 2 (7.91–14.454) | 30.36% |
| Group 3 (14.454–31) | 45.50% |
| Group 4 (31–512.329) | 58.11% |

**Key Findings:**

1. Passengers who survived paid a higher average ticket fare.
2. The median fare among survivors was 26.00 compared with 10.50 among non-survivors.
3. The highest fare group recorded a survival rate of approximately 58.11%.
4. The lowest fare group recorded a survival rate of approximately 19.73%.
5. Survival rates increased across the four fare groups.
6. Potential fare outliers were observed in both survival groups.

**Machine Learning Implication:**

Fare appears to be a potentially useful predictive feature. Its relationship with passenger class should also be investigated to understand overlapping information.

**Conclusion:**

The analysis indicates a positive association between ticket fare and passenger survival. Passengers in higher fare groups demonstrated higher observed survival rates. Further investigation is required before determining the independent predictive contribution of Fare.

**Status:** Completed.

## EXPERIEMENT  8 : TRAVEL GROUP COMPARISON

Passengers were categorized into two groups using the engineered FamilySize feature.

- Alone: FamilySize = 1
- With Family: FamilySize greater than 1

**Results:**

| Travel Group | Survival Rate |
| ------------ | ------------: |
| With Family  |        50.56% |
| Alone        |        30.35% |

**Key Findings:**

1. Passengers travelling with family recorded a higher survival rate than passengers travelling alone.
2. The survival-rate difference was approximately 20.21 percentage points.
3. FamilySize may provide useful predictive information for the classification model.

**Conclusion:**

The analysis indicates an association between travelling with family and passenger survival. FamilySize will be considered as an engineered feature during model development.

**Status:** Completed.

### Experiment 9: Embarkation Port vs Survival

**Objective:** Investigate the relationship between passenger embarkation port and survival outcomes.

**Methodology:**

- Used `value_counts()` to examine passenger distribution across embarkation ports.
- Used `isnull().sum()` to identify missing embarkation values.
- Used Pandas `groupby()` to calculate survival counts by embarkation port.
- Calculated survival percentages using the mean of the binary target variable.
- Used Seaborn barplot to visualize survival rates.

**Passenger Distribution:**

| Port | Location | Passenger Count |
|---|---|---:|
| C | Cherbourg | 168 |
| Q | Queenstown | 77 |
| S | Southampton | 644 |

**Survival Counts:**

| Port | Did Not Survive | Survived |
|---|---:|---:|
| C | 75 | 93 |
| Q | 47 | 30 |
| S | 427 | 217 |

**Missing Values:**

- Embarked contains 2 missing values.
- Missing percentage: approximately 0.22%.

**Survival Rates:**

| Port | Survival Rate |
|---|---:|
| C | 55.36% |
| Q | 38.96% |
| S | 33.70% |

**Key Findings:**

1. Southampton had the highest passenger count.
2. Cherbourg recorded the highest observed survival rate.
3. Queenstown recorded a survival rate of approximately 38.96%.
4. Southampton recorded a survival rate of approximately 33.70%.
5. Two missing embarkation values were identified.

**Machine Learning Implication:**

Embarked may contain useful categorical information for survival prediction. Missing values will require appropriate treatment during preprocessing.

**Conclusion:**

The analysis indicates differences in survival rates across embarkation ports. Cherbourg recorded the highest observed survival rate among the three ports.

**Status:** Count analysis completed. Visualization and percentage verification pending.

### Experiment 10: Correlation Analysis

**Objective:** Identify linear relationships between numerical features and understand their association with the target variable, Survived.

**Methodology:**

- Selected numerical columns using `select_dtypes()`.
- Calculated Pearson correlation coefficients using `corr()`.
- Visualized relationships using Seaborn `heatmap()`.
- Examined individual feature correlations with the target variable.

**Correlation with Survival:**

| Feature | Correlation |
|---|---:|
| Pclass | -0.3385 |
| Fare | 0.2573 |
| Parch | 0.0816 |
| Age | -0.0772 |
| SibSp | -0.0353 |
| FamilySize | 0.0166 |
| PassengerId | -0.0050 |

**Additional Feature Relationships:**

| Feature Pair | Correlation |
|---|---:|
| SibSp and FamilySize | 0.8907 |
| Parch and FamilySize | 0.7831 |
| Pclass and Fare | -0.5495 |

**Key Findings:**

1. Pclass has the strongest absolute linear correlation with survival among the numerical features.
2. Fare shows a positive association with survival.
3. Age has a very weak negative linear correlation with survival.
4. FamilySize has a near-zero linear correlation with survival despite showing different survival rates across individual family-size groups.
5. SibSp and Parch are strongly correlated with FamilySize because it is an engineered combination of these features.
6. Pclass and Fare show a moderate negative correlation.

**Machine Learning Implication:**

Pclass and Fare may provide useful predictive information. However, correlation alone cannot determine feature importance or predictive performance.

Nonlinear relationships and categorical features should also be investigated during model development.

**Conclusion:**

The correlation analysis identified several relationships between numerical features. Pclass and Fare showed the strongest absolute correlations with survival, while FamilySize demonstrated why nonlinear patterns should also be considered.

**Limitation:**

This analysis uses Pearson correlation and covers numerical features only. Correlation does not imply causation.

**Status:** Completed.

### Experiment 11: Missing Values and Outlier Investigation

**Objective:** Identify missing data, duplicate records, potential numerical outliers and dataset structure.

**Methodology:**

- Used `isnull().sum()` to identify missing values.
- Calculated missing percentages for each feature.
- Used `duplicated().sum()` to identify duplicate records.
- Applied the Interquartile Range (IQR) method to investigate potential outliers.
- Used `shape` and `dtypes` to inspect dataset dimensions and data types.

**Missing Value Analysis:**

| Feature | Missing Count | Missing Percentage |
|---|---:|---:|
| Age | 177 | 19.87% |
| Cabin | 687 | 77.10% |
| Embarked | 2 | 0.22% |
| Other Features | 0 | 0% |

**Duplicate Record Analysis:**

- Total duplicate records: 0.
- No fully duplicated rows were identified.

**Potential Outlier Analysis:**

| Feature | Potential Outliers |
|---|---:|
| Age | 11 |
| Fare | 116 |
| SibSp | 46 |
| Parch | 213 |

**Important Observations:**

1. Age contains 177 missing values.
2. Cabin has the highest missing percentage at approximately 77.10%.
3. Embarked contains only two missing values.
4. No duplicate records were identified.
5. Fare contains several potential high-value outliers.
6. Parch has a highly concentrated distribution at zero, resulting in an IQR of zero. Consequently, positive values are flagged by the IQR rule and should not automatically be considered erroneous.

**Dataset Structure:**

- Original training records: 891.
- Original features: 12.
- Current dataset dimensions: 891 rows × 15 columns.
- Additional engineered features: FareGroup, FamilySize and TravelGroup.

**Machine Learning Implication:**

The dataset requires missing-value treatment, categorical encoding and appropriate feature preparation before model training.

Potential outliers must be investigated rather than automatically removed. Valid passenger and family information should be preserved.

**Conclusion:**

The final data-quality investigation identified missing values in Age, Cabin and Embarked, with no duplicate records. Several numerical features contain potential outliers that require careful consideration during preprocessing.

**Status:** Completed.

# 05 – Model Evaluation

## 1. Model Details

- Algorithm: Logistic Regression
- Training records: 712
- Testing records: 179
- Features used: Pclass, Sex, Age, Fare, Embarked, FamilySize

## 2. Model Accuracy

| Metric | Result |
|---|---:|
| Training Accuracy | 80.76% |
| Testing Accuracy | 79.89% |
| Accuracy Difference | 0.87 percentage points |

## 3. Confusion Matrix

| Actual / Predicted | Not Survived (0) | Survived (1) |
|---|---:|---:|
| Not Survived (0) | 97 | 13 |
| Survived (1) | 23 | 46 |

## 4. Classification Report

| Metric | Not Survived (0) | Survived (1) |
|---|---:|---:|
| Precision | 0.81 | 0.78 |
| Recall | 0.88 | 0.67 |
| F1-score | 0.84 | 0.72 |
| Support | 110 | 69 |

Overall accuracy: 0.80

## 5. Key Observations

1. The model correctly classified 143 out of 179 test passengers.
2. It correctly identified 97 passengers who did not survive.
3. It correctly identified 46 passengers who survived.
4. Survivor recall is 67%, meaning 23 actual survivors were missed.
5. The training and testing accuracy values are close, with no obvious indication of severe overfitting based on accuracy alone.
6. Testing accuracy is higher than the majority-class baseline of approximately 61.62%.

## 6. Conclusion

The Logistic Regression model achieved approximately 79.89% testing accuracy. It performed better at identifying non-survivors than survivors.

Further model evaluation and improvement are required, particularly to improve survivor recall while maintaining a reasonable balance between precision and recall.
