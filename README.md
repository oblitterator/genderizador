# API de Predicción de Género por Nombre

Esta es una API simple construida con Flask que permite predecir el género asociado a un nombre dado principalmente para el idioma español. Utiliza un modelo de aprendizaje automático previamente entrenado para realizar estas predicciones y es particularmente performante con nombres compuestos.

## Requisitos

Asegúrate de tener instalado Python y las siguientes bibliotecas:

- Flask
- joblib
- pandas

Puedes instalar las dependencias usando el siguiente comando:

```
pip install Flask joblib pandas
```

## Uso
1. Clona este repositorio a tu máquina local:

```
git clone https://github.com/TuUsuario/tu-repositorio.git
cd tu-repositorio
```
2. Coloca el archivo modelo_nombre_sexo.pkl (modelo previamente entrenado) y vectorizador_nombre_sexo.pkl (vectorizador asociado) en la misma carpeta que el archivo app.py.

3. Inicia el servidor Flask:

```
python app.py
```

La aplicación se ejecutará en modo de depuración, lo que te permitirá ver mensajes de registro en la consola.

Realiza solicitudes de predicción usando cURL o cualquier cliente API. Envía una solicitud POST al endpoint /predict con un cuerpo JSON que contenga el campo "nombre". Por ejemplo:

```
curl -X POST -H "Content-Type: application/json" -d '{"nombre": "Juan"}' http://127.0.0.1:5000/predict
```

Obtendrás una respuesta JSON con el nombre y la predicción del género asociado.

## Ejemplo de Respuesta
```

{
  "nombre": "Maria del Carmen",
  "sexo": "F"
}

```

## Cómo funciona
El servidor Flask carga el modelo de predicción y el vectorizador cuando se inicia. Cuando se realiza una solicitud POST al endpoint /predict con un nombre, la API realiza las siguientes acciones:

Verifica que el campo "nombre" esté presente en el cuerpo de la solicitud. Si no lo está, devuelve un mensaje de error.

Vectoriza el nombre utilizando el vectorizador cargado.

Realiza una predicción utilizando el modelo cargado.

Devuelve una respuesta JSON que contiene el nombre y la predicción de género.

## Notas
Este es un ejemplo básico con fines educativos y de demostración.
Asegúrate de tener los archivos modelo_nombre_sexo.pkl y vectorizador_nombre_sexo.pkl en la misma carpeta que app.py para que la carga del modelo funcione correctamente en la aplicación.
Ten en cuenta que la precisión de las predicciones depende de la calidad y cantidad de los datos utilizados para entrenar el modelo original.
