
# Titanic Survival Prediction – Project Activity Log

##  November 2026

### Activities Completed

1. Continued Titanic dataset analysis.
2. Calculated passenger survival counts and percentages.
3. Created survival distribution visualization.
4. Implemented a majority-class baseline prediction using NumPy.
5. Evaluated baseline accuracy using Scikit-learn's `accuracy_score()`.

### Results

| Metric | Result |
|---|---:|
| Total Records | 891 |
| Correct Predictions | 549 |
| Incorrect Predictions | 342 |
| Baseline Accuracy | 61.62% |

### Technical Observations

- The majority class is passenger non-survival (0).
- Predicting the majority class for every passenger produces 61.62% accuracy.
- This baseline will be used as a reference when evaluating trained classification models.

### Next Activity

Investigate passenger survival patterns based on gender and passenger class.

**Status:** In Progress

### Model Training – Logistic Regression

**Model:** Logistic Regression

**Dataset split:**
- Training records: 712
- Testing records: 179

**Initial results:**
- Training accuracy: 80.76%
- Testing accuracy: 79.89%
- Accuracy difference: 0.87 percentage points

**Initial observation:**

The Logistic Regression model achieved approximately 80% accuracy on the training and testing datasets. The small difference between the two accuracy values is encouraging and does not indicate obvious severe overfitting.

Further evaluation using the confusion matrix, precision, recall, and F1-score is required before drawing conclusions about model performance.

**Status:** Initial model training completed; detailed evaluation in progress.

##  Random Forest Classifier Evaluation

### Model Configuration

- Algorithm: Random Forest Classifier
- Number of trees: 100
- Random state: 42

### Accuracy Results

| Metric | Result |
|---|---:|
| Training Accuracy | 98.31% |
| Testing Accuracy | 80.45% |
| Accuracy Difference | 17.87 percentage points |

### Confusion Matrix

| Actual / Predicted | Not Survived (0) | Survived (1) |
|---|---:|---:|
| Not Survived (0) | 95 | 15 |
| Survived (1) | 20 | 49 |

### Classification Report

| Metric | Not Survived (0) | Survived (1) |
|---|---:|---:|
| Precision | 0.83 | 0.77 |
| Recall | 0.86 | 0.71 |
| F1-score | 0.84 | 0.74 |
| Support | 110 | 69 |

Overall accuracy: 0.80

### ROC-AUC Evaluation

ROC-AUC Score: 0.8356 (83.56%)

### Key Observations

1. The model achieved 80.45% testing accuracy.
2. Survivor recall improved to 71%, compared with 67% for Logistic Regression.
3. The survivor F1-score improved from 0.72 to 0.74.
4. The training accuracy of 98.31% is considerably higher than the testing accuracy, indicating possible overfitting.
5. ROC-AUC is slightly lower than the Logistic Regression result.

### Conclusion

Random Forest achieved slightly better testing accuracy and survivor recall than Logistic Regression. However, the large difference between training and testing accuracy suggests possible overfitting. Further hyperparameter tuning is required to improve generalization.
 
##  Random Forest Hyperparameter Tuning

### Configuration

| Parameter | Value |
|---|---:|
| n_estimators | 100 |
| max_depth | 5 |
| min_samples_split | 10 |
| min_samples_leaf | 4 |
| random_state | 42 |

### Results

| Metric | Original Random Forest | Tuned Random Forest |
|---|---:|---:|
| Training Accuracy | 98.31% | 84.83% |
| Testing Accuracy | 80.45% | 80.45% |
| Accuracy Gap | 17.87 percentage points | 4.38 percentage points |

### Observations

1. Limiting tree depth and increasing minimum sample requirements reduced model complexity.
2. Training accuracy decreased from 98.31% to 84.83%.
3. Testing accuracy remained unchanged at 80.45%.
4. The training-testing accuracy gap decreased significantly.
5. The tuned model shows improved generalization based on the smaller accuracy gap.

### Conclusion

Hyperparameter tuning substantially reduced the overfitting observed in the original Random Forest model without reducing testing accuracy. Further evaluation using the confusion matrix, classification report and ROC-AUC is required.

##  Tuned Random Forest Evaluation

### Classification Results

| Metric | Not Survived (0) | Survived (1) |
|---|---:|---:|
| Precision | 0.78 | 0.87 |
| Recall | 0.95 | 0.58 |
| F1-score | 0.86 | 0.70 |
| Support | 110 | 69 |

Overall testing accuracy: 80.45%

### Confusion Matrix

| Actual / Predicted | Not Survived (0) | Survived (1) |
|---|---:|---:|
| Not Survived (0) | 104 | 6 |
| Survived (1) | 29 | 40 |

### ROC-AUC

ROC-AUC Score: 0.8345 (83.45%)

### Key Observations

1. The tuned model correctly classified 144 out of 179 test passengers.
2. Survivor precision increased from 77% to 87% compared with the original Random Forest.
3. Survivor recall decreased from 71% to 58%.
4. False-positive predictions decreased from 15 to 6.
5. False-negative predictions increased from 20 to 29.
6. Testing accuracy remained at 80.45%.

### Conclusion

Hyperparameter tuning reduced the model's complexity and substantially reduced the training-testing accuracy gap. However, this came with a reduction in survivor recall. The tuned model is more precise when predicting survival but misses more actual survivors. Further experimentation is required to find a better balance between precision and recall.  

##  Model Performance Comparison

Three model experiments were conducted using the same training and testing split.

### Comparison Results

| Metric | Logistic Regression | Random Forest | Tuned Random Forest |
|---|---:|---:|---:|
| Training Accuracy | 80.76% | 98.31% | 84.83% |
| Testing Accuracy | 79.89% | 80.45% | 80.45% |
| ROC-AUC | 83.93% | 83.56% | 83.45% |
| Survivor Precision | 78% | 77% | 87% |
| Survivor Recall | 67% | 71% | 58% |
| Survivor F1-score | 72% | 74% | 70% |

### Findings

1. Logistic Regression achieved the highest ROC-AUC score.
2. Both Random Forest experiments achieved 80.45% testing accuracy.
3. Original Random Forest showed a substantial training-testing accuracy gap.
4. Hyperparameter tuning reduced this gap from 17.87 to 4.38 percentage points.
5. Original Random Forest achieved the highest survivor recall at 71%.
6. Tuned Random Forest achieved the highest survivor precision at 87%.

### Preliminary Model Selection

Logistic Regression is retained as a strong baseline candidate due to its consistent training and testing performance and highest ROC-AUC.

Random Forest and Tuned Random Forest are retained for further comparison.

Final model selection will be made after additional validation and experimentation.

## 1 Classification Threshold Experiment

### Objective

To investigate how changing the classification threshold affects the precision, recall and F1-score of the Logistic Regression model.

### Validation Results

| Threshold | Precision | Recall | F1-score |
|---:|---:|---:|---:|
| 0.3 | 0.667 | 0.800 | 0.727 |
| 0.4 | 0.684 | 0.709 | 0.696 |
| 0.5 | 0.720 | 0.655 | 0.686 |
| 0.6 | 0.773 | 0.618 | 0.687 |

### Key Observations

1. Threshold 0.3 achieved the highest recall of 80%.
2. Threshold 0.3 also achieved the highest F1-score of 0.727 among the tested thresholds.
3. Threshold 0.6 achieved the highest precision of approximately 77%.
4. Increasing the threshold generally reduced survivor recall and increased precision.
5. Lowering the threshold increased survivor detection but also increased false-positive predictions.

### Conclusion

A classification threshold of 0.3 provided the best F1-score and recall among the four tested thresholds on the validation dataset. This threshold is selected as a candidate for final testing.

The final decision will be evaluated on the previously untouched test dataset.

## Final Threshold Evaluation

### Objective

To evaluate the selected classification threshold of 0.3 on the previously untouched test dataset.

### Test Results

| Metric | Threshold 0.5 | Threshold 0.3 |
|---|---:|---:|
| Accuracy | 0.799 | 0.771 |
| Survivor Precision | 0.78 | 0.67 |
| Survivor Recall | 0.67 | 0.80 |
| Survivor F1-score | 0.72 | 0.73 |

### Confusion Matrix – Threshold 0.3

| Actual / Predicted | Not Survived (0) | Survived (1) |
|---|---:|---:|
| Not Survived (0) | 83 | 27 |
| Survived (1) | 14 | 55 |

### Key Observations

1. Survivor recall increased from approximately 67% to 80%.
2. The number of correctly identified survivors increased from 46 to 55.
3. False negatives decreased from 23 to 14.
4. False positives increased from 13 to 27.
5. Overall accuracy decreased from 79.89% to 77.09%.
6. Survivor F1-score improved slightly from approximately 0.72 to 0.73.

### Conclusion

The threshold of 0.3 improved survivor detection on the test dataset, achieving 80% recall. However, this improvement came with reduced precision and overall accuracy.

The threshold of 0.3 was selected based on validation results and is retained as a candidate operating threshold for the final model.

## Stratified 5-Fold Cross-Validation

### Objective

To evaluate the consistency and generalization performance of the Logistic Regression model across multiple training and validation splits.

### Configuration

- Algorithm: Logistic Regression
- Validation method: Stratified 5-Fold Cross-Validation
- Number of folds: 5
- Shuffle: True
- Random state: 42
- Evaluation metric: Accuracy

### Results

| Fold | Accuracy |
|---|---:|
| Fold 1 | 79.72% |
| Fold 2 | 79.72% |
| Fold 3 | 80.99% |
| Fold 4 | 78.17% |
| Fold 5 | 82.39% |

**Mean CV Accuracy:** 80.20%

**Standard Deviation:** 1.42 percentage points

### Key Observations

1. The mean cross-validation accuracy was approximately 80.20%.
2. The standard deviation was approximately 1.42 percentage points.
3. The validation scores remained relatively close across all five folds.
4. The mean cross-validation accuracy was close to the independent test accuracy of 79.89%.

### Conclusion

The Logistic Regression model demonstrated reasonably consistent accuracy across the five validation folds. The cross-validation results support retaining Logistic Regression as a strong baseline candidate for the Titanic Survival Prediction project.


## Multi-Metric Cross-Validation

### Objective

To evaluate Logistic Regression using multiple performance metrics across five stratified validation folds.

### Evaluation Results

| Metric | Mean Score | Standard Deviation |
|---|---:|---:|
| Accuracy | 80.20% | 1.42% |
| Precision | 76.75% | 2.87% |
| Recall | 69.61% | 3.65% |
| F1-score | 72.91% | 2.12% |
| ROC-AUC | 85.39% | 2.18% |

### Key Observations

1. The model achieved a mean accuracy of approximately 80.20%.
2. Mean precision was approximately 76.75%.
3. Mean recall was approximately 69.61%.
4. Mean F1-score was approximately 72.91%.
5. Mean ROC-AUC was approximately 85.39%.
6. The standard deviations indicate relatively consistent results across the five folds.

### Conclusion

Multi-metric cross-validation indicates that Logistic Regression provides reasonably consistent classification performance. Its mean ROC-AUC of 85.39% demonstrates good ability to distinguish between the two classes across validation folds.

The model remains a strong baseline candidate for final model selection.


## Prediction Testing Using the Saved Model

### Objective

To verify that the saved machine learning pipeline can process a new passenger record and generate a survival prediction.

### Input Passenger Details

| Feature | Value |
|---|---|
| Pclass | 1 |
| Sex | Female |
| Age | 25 |
| Fare | 80 |
| Embarked | C |
| FamilySize | 2 |

### Prediction Results

- Survival Probability: 0.9506 (95.06%)
- Classification Threshold: 0.30
- Predicted Class: 1
- Prediction: Survived

### Observation

The saved preprocessing and Logistic Regression pipeline successfully processed the new passenger record and generated a survival probability. Since the predicted probability exceeded the selected threshold of 0.30, the passenger was classified as survived.

### Conclusion

The saved machine learning pipeline was successfully loaded and tested with a new passenger record. This confirms that the pipeline can be reused for future predictions without manually repeating preprocessing.






