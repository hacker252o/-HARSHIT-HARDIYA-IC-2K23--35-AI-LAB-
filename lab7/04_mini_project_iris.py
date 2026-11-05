# Mini project: classify Iris flowers and report model performance.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=7,
    stratify=iris.target
)

model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5)
)
model.fit(X_train, y_train)
predicted = model.predict(X_test)

print("Mini Project: Iris Flower Classification")
print("Number of training rows:", len(X_train))
print("Number of testing rows:", len(X_test))
print("Accuracy:", accuracy_score(y_test, predicted))
print(classification_report(y_test, predicted,
                            target_names=iris.target_names))
