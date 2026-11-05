from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.25, random_state=42,
    stratify=iris.target
)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
print("\nConfusion matrix:\n", confusion_matrix(y_test, predictions))
print("\nClassification report:\n",
      classification_report(y_test, predictions, target_names=iris.target_names))
print("\nTree rules:\n", export_text(model, feature_names=list(iris.feature_names)))
