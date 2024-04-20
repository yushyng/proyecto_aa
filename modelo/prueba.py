import os
import mlflow
import mlflow.sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
import pprint

# Cargar los datos
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el modelo
model = RandomForestClassifier()

# Definir los hiperparámetros a ajustar
param_dist = {"max_depth": [3, None],
              "n_estimators": range(10, 200),
              "max_features": range(1, 4),
              "min_samples_split": range(2, 11),
              "bootstrap": [True, False],
              "criterion": ["gini", "entropy"]}

# Definir la validación cruzada
cv = KFold(n_splits=5, shuffle=True, random_state=42)

# Definir la búsqueda aleatoria
random_search = RandomizedSearchCV(model, param_distributions=param_dist, cv=cv, n_iter=10)

# Creamos (o elegimos nuestro experimento)
mlflow.set_experiment("Random search")

with mlflow.start_run():
    # Realizar la búsqueda de hiperparámetros
    random_search.fit(X_train, y_train)

    # Obtener los resultados de la búsqueda
    results = random_search.cv_results_

    # Iterar sobre cada modelo evaluado
    for i in range(len(results['params'])):
        with mlflow.start_run(nested=True):
            params = results['params'][i]
            mean_test_score = results['mean_test_score'][i]
            std_test_score = results['std_test_score'][i]

            # Loguear hiperparámetros
            mlflow.log_params(params)
            mlflow.log_metric("mean_test_score", mean_test_score)
            mlflow.log_metric("std_test_score", std_test_score)
            model_iteration = random_search.estimator.fit(X_train, y_train)
            mlflow.sklearn.log_model(model_iteration, f"Model_Iteration_{i+1}")



           

    # Registrar el mejor modelo en MLFlow
    # mlflow.sklearn.log_model(random_search.best_estimator_, "best_model")

    # # Obtener los mejores hiperparámetros y la puntuación
    # best_params = random_search.best_params_
    # best_score = random_search.best_score_
    # mlflow.log_params(best_params)
    # mlflow.log_metric("best_mean_test_score", best_score)

    