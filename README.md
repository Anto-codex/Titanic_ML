# 🚢 Titanic Survival Prediction

### Machine Learning Classification Project

A machine learning project that predicts passenger survival on the Titanic using supervised classification algorithms. The project covers data understanding, exploratory data analysis, feature engineering, preprocessing, model training, evaluation, validation and an interactive Streamlit application.

---

## 📌 Project Overview

The objective is to develop a machine learning model that estimates whether a Titanic passenger survived based on passenger information such as gender, age, passenger class, ticket fare, embarkation port and family size.

**Problem Type:** Binary Classification

**Target Variable:** `Survived`

- `0` – Did Not Survive
- `1` – Survived

## 🎯 Project Objectives

- Perform exploratory data analysis.
- Identify important survival patterns.
- Handle missing values and categorical features.
- Build classification models.
- Compare model performance.
- Evaluate models using multiple metrics.
- Develop an interactive prediction application.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Model Persistence | Joblib |
| Application | Streamlit |
| Development | Jupyter Notebook, VS Code |

## 📂 Project Structure

```text
titanic/
│
├── data/
├── docs/
│   ├── 01_project_overview.md
│   ├── 02_dataset_documentation.md
│   ├── 03_eda_findings.md
│   └── 04_project_log.md
│
├── models/
│   └── logistic_regression_pipeline.pkl
│
├── notebook/
│   └── notebook.ipynb
│
├── output/
│
├── src/
│   ├── app.py
│   └── predict.py
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 📊 Exploratory Data Analysis

The training dataset contains 891 passenger records and 12 original columns.

Key observations:

- Female passengers had a higher survival rate than male passengers.
- First-class passengers had a higher survival rate than third-class passengers.
- Fare showed a positive association with survival.
- Age contained 177 missing values.
- Cabin contained 687 missing values.
- Family size showed different survival patterns across family groups.

Feature engineering was performed to derive `FamilySize` from `SibSp` and `Parch`.

## ⚙️ Data Preprocessing

The preprocessing workflow included:

1. Selecting relevant features.
2. Splitting the data into training and testing sets.
3. Handling missing numerical values using median imputation.
4. Handling missing categorical values using most-frequent imputation.
5. Standardizing numerical features.
6. Applying One-Hot Encoding to categorical features.
7. Combining transformations using Scikit-learn's ColumnTransformer and Pipeline.

### Selected Features

- Pclass
- Sex
- Age
- Fare
- Embarked
- FamilySize

The six selected input features were transformed into 11 model features.

## 🤖 Models Developed

Three model configurations were evaluated:

1. Logistic Regression
2. Random Forest Classifier
3. Tuned Random Forest Classifier

### Model Performance Comparison

| Model | Training Accuracy | Testing Accuracy | ROC-AUC |
|---|---:|---:|---:|
| Logistic Regression | 80.76% | 79.89% | 83.93% |
| Random Forest | 98.31% | 80.45% | 83.56% |
| Tuned Random Forest | 84.83% | 80.45% | 83.45% |

### Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC-AUC Curve

### Cross-Validation

Logistic Regression was additionally evaluated using Stratified 5-Fold Cross-Validation.

| Metric | Mean Score |
|---|---:|
| Accuracy | 80.20% |
| Precision | 76.75% |
| Recall | 69.61% |
| F1-score | 72.91% |
| ROC-AUC | 85.39% |

Logistic Regression was retained as the baseline candidate because of its relatively small training-testing accuracy gap and competitive ROC-AUC.

## 🎚️ Classification Threshold

A threshold experiment was performed to understand the trade-off between precision and recall.

The selected threshold for the prediction application is `0.30`.

The final prediction is classified as:

- Probability ≥ 0.30: Survived
- Probability < 0.30: Did Not Survive

## 🌐 Streamlit Application

The project includes an interactive Streamlit application that allows users to:

- Enter passenger information.
- Select passenger class and gender.
- Enter age, fare and family size.
- Select the embarkation port.
- Generate survival probability.
- View the predicted classification.
- Switch between dark and light themes.

### Run the Application

```bash
pip install -r requirements.txt
streamlit run src/app.py
```

Open the local URL provided by Streamlit, usually:

```text
http://localhost:8501
```

## 💾 Saved Model

The trained Logistic Regression pipeline is saved using Joblib.

```text
models/logistic_regression_pipeline.pkl
```

The saved artifact includes the preprocessing pipeline, trained classifier and selected classification threshold.

## 📖 Documentation

Detailed project documentation is available in the `docs/` directory.

- Project Overview
- Dataset Documentation
- EDA Findings
- Project Log

## ⚠️ Limitations

- Predictions are estimates based on historical training data.
- The dataset represents a specific historical passenger population.
- Model predictions do not establish causal relationships.
- Performance may vary on different datasets.
- The selected threshold changes the precision-recall trade-off.

## 👨‍💻 Author

**Anto Sanjay C**

Data Science | Machine Learning | Python

GitHub: [Anto-codex](https://github.com/Anto-codex)

LinkedIn: [Anto Sanjay](https://www.linkedin.com/in/anto-sanjay-543bb7255)

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

*Developed as a Machine Learning classification project using Python and Scikit-learn.*