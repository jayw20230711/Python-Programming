"""
What is a confusion matrix?

It is a table that is used in classification problems to assess where errors in the model were made.

The rows represent the actual classes the outcomes should have been. While the columns represent the predictions we
have made. Using this table it is easy to see which predictions are wrong.

Creating a Confusion Matrix
Confusion matrices can be created by predictions made from a logistic regression.

For now, we will generate actual and predicted values by utilizing NumPy:
"""
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt  # Visualizing the display requires that we import pyplot from matplotlib

# Next we will need to generate the numbers for "actual" and "predicted" values
actual = np.random.binomial(1, 0.9, size=1000)
predicted = np.random.binomial(1, 0.9, size=1000)
# print(actual)
# print(predicted)

# Once metrics is imported we can use the confusion matrix function on our actual and predicted values
confusion_matrix = metrics.confusion_matrix(actual, predicted)
print("Confusion_matrix")
print(confusion_matrix)

# To create a more interpretable visual display we need to convert the table into a confusion matrix display.
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[False, True])

# Finally to display the plot we can use the functions plot() and show() from pyplot.
cm_display.plot()
plt.show()

"""
Results Explained
The Confusion Matrix created has four different quadrants:

True Negative (Top-Left Quadrant)
False Negative (Top-Right Quadrant)
False Positive (Bottom-Left Quadrant)
True Positive (Bottom-Right Quadrant)

Now that we have made a Confusion Matrix, we can calculate different measures to quantify the quality of the model. 
First, lets look at Accuracy.

Created Metrics
The matrix provides us with many useful metrics that help us to evaluate out classification model.

The different measures include: Accuracy, Precision, Sensitivity (Recall), Specificity, and 
the F-score, explained below.

Accuracy
Accuracy measures how often the model is correct.

How to Calculate
(True Positive + True Negative) / Total Predictions

"""
Accuracy = metrics.accuracy_score(actual, predicted)
print("Accuracy :")
print(Accuracy)

"""
Precision
Of the positives predicted, what percentage is truly positive?

How to Calculate
True Positive / (True Positive + False Positive)

Precision does not evaluate the correctly predicted negative cases:
"""
# actual = np.random.binomial(1, 0.9, size=1000)
# predicted = np.random.binomial(1, 0.9, size=1000)

Precision = metrics.precision_score(actual, predicted)
print("Precision :")
print(Precision)

"""
Sensitivity (Recall)
Of all the positive cases, what percentage are predicted positive?

Sensitivity (sometimes called Recall) measures how good the model is at predicting positives.

This means it looks at true positives and false negatives (which are positives that have been incorrectly 
predicted as negative).

How to Calculate
True Positive / (True Positive + False Negative)

Sensitivity is good at understanding how well the model predicts something is positive:
"""
Sensitivity_recall = metrics.recall_score(actual, predicted)
print("Sensitivity-recall :")
print(Sensitivity_recall)

"""
Specificity
How well the model is at predicting negative results?

Specificity is similar to sensitivity, but looks at it from the perspective of negative results.

How to Calculate
True Negative / (True Negative + False Positive)

Since it is just the opposite of Recall, we use the recall_score function, taking the opposite position label:
"""
Specificity = metrics.recall_score(actual, predicted, pos_label=0)
print("Specificity :")
print(Specificity)

"""
F-score
F-score is the "harmonic mean" of precision and sensitivity.

It considers both false positive and false negative cases and is good for imbalanced datasets.

How to Calculate
2 * ((Precision * Sensitivity) / (Precision + Sensitivity))

This score does not take into consideration the True Negative values:
"""
F1_score = metrics.f1_score(actual, predicted)
print("F1-score :")
print(F1_score)

"""
All calculations in one:
"""
# metrics
print({"Accuracy": Accuracy, "Precision": Precision, "Sensitivity_recall": Sensitivity_recall, "Specificity":
    Specificity, "F1_score": F1_score})
