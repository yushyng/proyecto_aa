import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

class Exploracion:
    def __init__(self):
         self.df_total = None

    def calcular_matriz_correlacion(self,df):
        # Filtrar solo las columnas numéricas
        df_numeric = df.df.select_dtypes(include='number')

        # Calcular la matriz de correlación
        correlation_matrix = df_numeric.corr()
        
        return correlation_matrix
    
    def resumen(self,df):
        """
        Imprime un resumen básico de los datos en el DataFrame.
        """
        print("Resumen del DataFrame:")
        print(df.info())
        print("\nDescripción estadística del DataFrame:")
        print(df.describe())
        print("\nModa de las variables categóricas")
        print(df.mode())

    def visualizar_columnas(self,df):
        """
        Muestra las columnas presentes en el DataFrame.
        """
        print("Columnas en el DataFrame:")
        print(df.columns)

    def mostrar_muestra(self, df,n=5):
        """
        Muestra una muestra de filas del DataFrame.
        """
        print(f"Muestra de {n} filas del DataFrame:")
        print(df.head(n))

    def calcular_coeficiente_contingencia(df, columna1, columna2):
        tabla_contingencia = pd.crosstab(df[columna1], df[columna2])
        c, p, dof, expected = chi2_contingency(tabla_contingencia)
        print("Coeficiente de contingencia (C de Pearson):", c)
        print("Valor p:", p)
        return tabla_contingencia
    
    def plot_boxplots(df, column1, column2, figsize=(10, 5)):
        fig, axs = plt.subplots(1, 2, figsize=figsize)  # 1 fila, 2 columnas

        # Boxplot de la primera columna
        df.boxplot(column=column1, ax=axs[0])
        axs[0].set_title(f'Boxplot de {column1}')

        # Boxplot de la segunda columna
        df.boxplot(column=column2, ax=axs[1])
        axs[1].set_title(f'Boxplot de {column2}')

        # Ajusta el diseño de los subplots
        plt.tight_layout()

        # Muestra los subplots
        plt.show()