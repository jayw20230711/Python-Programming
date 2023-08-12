"""
Bootstrap Aggregation (Bagging)

Bagging
Methods such as Decision Trees, can be prone to over fitting on the training set which can lead to wrong predictions on
new data.

Bootstrap Aggregation (bagging) is a ensembling method that attempts to resolve overfitting for classification or
regression problems. Bagging aims to improve the accuracy and performance of machine learning algorithms. It does this
by taking random subsets of an original dataset, with replacement, and fits either a classifier (for classification) or
regressor (for regression) to each subset. The predictions for each subset are then aggregated through majority vote
for classification or averaging for regression, increasing prediction accuracy.

Evaluating a Base Classifier
To see how bagging can improve model performance, we must start by evaluating how the base classifier performs on the
dataset. If you do not know what decision trees are review the lesson on decision trees before moving forward, as
bagging is an continuation of the concept.

We will be looking to identify different classes of wines found in Sklearn's wine dataset.

Let's start by importing the necessary modules.
"""
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

"""
Next we need to load in the data and store it into X (input features) and y (target). The parameter as_frame is set 
equal to True so we do not lose the feature names when loading the data. (sklearn version older than 0.23 must skip 
the as_frame argument as it is not supported)
"""
data = datasets.load_wine(as_frame=True)

X = data.data
print("printing X values :\n", X)
y = data.target
print("\nprinting y values :\n", y)

"""
In order to properly evaluate our model on unseen data, we need to split X and y into train and test sets. For 
information on splitting data, see the Train/Test lesson.
"""
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=22)

"""
With our data prepared, we can now instantiate a base classifier and fit it to the training data.
"""
dtree = DecisionTreeClassifier(random_state=22)
dtree.fit(X_train, y_train)

"""
We can now predict the class of wine the unseen test set and evaluate the model performance.
"""
y_pred = dtree.predict(X_test)

print("Train data accuracy :", accuracy_score(y_true=y_train, y_pred=dtree.predict(X_train)))
print("Test data accuracy :", accuracy_score(y_true=y_test, y_pred=y_pred))

"""
Result:

Train data accuracy: 1.0
Test data accuracy: 0.8222222222222222

The base classifier performs reasonably well on the dataset achieving 82% accuracy on the test dataset with the 
current parameters (Different results may occur if you do not have the random_state parameter set).

Now that we have a baseline accuracy for the test dataset, we can see how the Bagging Classifier out performs a single 
Decision Tree Classifier.

"""

"""
Creating a Bagging Classifier

For bagging we need to set the parameter n_estimators, this is the number of base classifiers that our model is going 
to aggregate together.


"""