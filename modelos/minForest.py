# import mlflow
# import mlflow.sklearn
# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split, RandomizedSearchCV
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# # Cargar datos
# data = pd.read_csv('./2/data/datos_predecir_min.csv')
# # Eliminamos las categoricas
# columnas=['name','EventStartTime', 'SalesStartTIme', 'SalesEndTime', 'nameArtist', 'VenueName', 
#           'VenueCity', 'VenueState','Generos_combinados']

# data.drop(columnas, axis=1, inplace=True)

# RANDOM_STATE = 83 #fijamos la semilla

# # Dividir datos en conjuntos de entrenamiento y prueba
# X = data.drop(columns=['min_price'])
# y = data['min_price']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM_STATE)


# # Hiperparámetros
# param_grid = {
#     'n_estimators': [int(x) for x in np.linspace(start=100, stop=1000, num=10)],
#     'max_features': ['log2', 'sqrt', None],
#     'max_depth': [int(x) for x in np.linspace(10, 110, num=11)],
#     # 'min_samples_split': [2, 5, 10],
#     # 'min_samples_leaf': [1, 2, 4],
#     # 'bootstrap': [True, False]
# }

# # Inicializar el modelo 
# rf = RandomForestRegressor()
# # Inicializar RandomizedSearchCV
# random_search = RandomizedSearchCV(estimator=rf, param_distributions=param_grid, n_iter=200, cv=5, verbose=2, random_state=RANDOM_STATE, n_jobs=-1)
# # Entrenar modelo con búsqueda aleatoria
# random_search.fit(X_train, y_train)


# # Obtener el mejor modelo de la búsqueda aleatoria
# best_model = random_search.best_estimator_

# # Predicciones con el mejor modelo
# y_pred = best_model.predict(X_test)

# # Calcular métricas
# mae = mean_absolute_error(y_test, y_pred)
# mse = mean_squared_error(y_test, y_pred)
# rmse = np.sqrt(mse)
# r2 = r2_score(y_test, y_pred)

# mlflow.set_experiment("Random search MinPrice")

# # Iniciar una nueva ejecución en MLflow
# with mlflow.start_run(run_name='0.1'):

#     # Log de parámetros
#     mlflow.log_params(random_search.best_params_)
#     # Log de métricas
#     mlflow.log_metrics({
#         "MAE": mae,
#         "MSE": mse,
#         "RMSE": rmse,
#         "R2": r2
#     })

#     # Log del modelo
#     mlflow.sklearn.log_model(best_model, "random_forest_regressor_model")

import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Cargar datos
data = pd.read_csv('./2/data/datos_predecir_min.csv')
# Eliminar las columnas categóricas
columnas=['name','EventStartTime', 'SalesStartTIme', 'SalesEndTime', 'nameArtist', 'VenueName', 
          'VenueCity', 'VenueState','Generos_combinados']
data.drop(columnas, axis=1, inplace=True)

RANDOM_STATE = 83 # Fijar la semilla

# Dividir datos en conjuntos de entrenamiento y prueba
X = data.drop(columns=['min_price'])
y = data['min_price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM_STATE)

# Hiperparámetros
param_grid = {
    'n_estimators': [int(x) for x in np.linspace(start=100, stop=1000, num=10)],
    'max_features': ['log2', 'sqrt', None],
    'max_depth': [int(x) for x in np.linspace(10, 110, num=11)],
}

# Inicializar el modelo 
rf = RandomForestRegressor()
# Inicializar RandomizedSearchCV
random_search = RandomizedSearchCV(estimator=rf, param_distributions=param_grid, n_iter=200, cv=5, verbose=2, random_state=RANDOM_STATE, n_jobs=-1)
# Entrenar modelo con búsqueda aleatoria
random_search.fit(X_train, y_train)

# Obtener el mejor modelo de la búsqueda aleatoria
best_model = random_search.best_estimator_

# Predicciones con el mejor modelo
y_pred_train = best_model.predict(X_train)
y_pred_test = best_model.predict(X_test)

# Calcular métricas
train_mae = mean_absolute_error(y_train, y_pred_train)
train_mse = mean_squared_error(y_train, y_pred_train)
train_rmse = np.sqrt(train_mse)
train_r2 = r2_score(y_train, y_pred_train)

mae = mean_absolute_error(y_test, y_pred_test)
mse = mean_squared_error(y_test, y_pred_test)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_test)

mlflow.set_experiment("Random search MinPrice")

# Iniciar una nueva ejecución en MLflow
with mlflow.start_run(run_name='0.1'):

    # Log de parámetros
    mlflow.log_params(random_search.best_params_)
    # Log de métricas
    mlflow.log_metrics({
        "MAE_train": train_mae,
        "MSE_train": train_mse,
        "RMSE_train": train_rmse,
        "R2_train": train_r2,
        "MAE_test": mae,
        "MSE_test": mse,
        "RMSE_test": rmse,
        "R2_test": r2
    })

    # Log del modelo
    mlflow.sklearn.log_model(best_model, "random_forest_regressor_model")

    # Visualización de las métricas
    metric_names = ['MAE', 'MSE', 'RMSE', 'R2']
    train_metrics = [train_mae, train_mse, train_rmse, train_r2]
    test_metrics = [mae, mse, rmse, r2]

    fig, ax = plt.subplots(figsize=(10, 6))
    bar_width = 0.35
    index = np.arange(len(metric_names))

    bar1 = ax.bar(index, train_metrics, bar_width, label='Train')
    bar2 = ax.bar(index + bar_width, test_metrics, bar_width, label='Test')

    ax.set_xlabel('Metrics')
    ax.set_ylabel('Values')
    ax.set_title('Comparison of Metrics between Train and Test sets')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(metric_names)
    ax.legend()

    plt.show()
