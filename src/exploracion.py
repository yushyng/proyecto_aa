import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno


class Exploracion:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def resumen(self):
        """
        Imprime un resumen básico de los datos en el DataFrame.
        """
        print("Resumen del DataFrame:")
        print(self.dataframe.info())
        print("\nDescripción estadística del DataFrame:")
        print(self.dataframe.describe())
        print("\nModa de las variables categóricas")
        print(self.dataframe.mode())

    def visualizar_columnas(self):
        """
        Muestra las columnas presentes en el DataFrame.
        """
        print("Columnas en el DataFrame:")
        print(self.dataframe.columns)

    def mostrar_muestra(self, n=5):
        """
        Muestra una muestra de filas del DataFrame.
        """
        print(f"Muestra de {n} filas del DataFrame:")
        print(self.dataframe.head(n))


    def matriz_correlacion(self):
        """
        Muestra la matriz de correlación para las variables numéricas
        """
        correlacion = self.dataframe.corr()
        print(correlacion)

        # Visualizarla
        # Mapa de calor de la matriz de correlación
        sns.heatmap(correlacion, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Matriz de Correlación')
        plt.show()


    def plot_missing_matrix(self):
        """Genera el gráfico de matriz de ausencia"""
        msno.matrix(self.dataframe)

# Seguir probando nuevos métodos