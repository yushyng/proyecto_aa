import pandas as pd
import matplotlib.pyplot as plt


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

    # Otros métodos de exploración de datos pueden ir aquí

if __name__ == "__main__":
    # Ejemplo de uso de la clase Exploracion
    # Crear un DataFrame de ejemplo
    datos = {
        "Nombre": ["Juan", "María", "Carlos", "Laura", "Ana"],
        "Edad": [25, 30, 35, 40, 45],
        "Género": ["M", "F", "M", "F", "F"],
        "Puntuación": [80, 90, 85, 88, 92]
    }
    df = pd.DataFrame(datos)

    # Crear una instancia de la clase Exploracion y explorar el DataFrame
    explorador = Exploracion(df)
    explorador.resumen()
    explorador.visualizar_columnas()
    explorador.mostrar_muestra()


# Datos
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [10, 20, 15, 25, 30]

# Crear el gráfico de barras
plt.bar(categorias, valores)

# Añadir etiquetas y título
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de barras')

# Mostrar el gráfico
plt.show()
