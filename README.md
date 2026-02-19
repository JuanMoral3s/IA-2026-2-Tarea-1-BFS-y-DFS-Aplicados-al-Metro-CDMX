# IA 2026-2 – Tarea 1

## BFS y DFS aplicados al Metro de la CDMX

Implementación de los algoritmos de búsqueda **Breadth-First Search (BFS)** y **Depth-First Search (DFS)** para encontrar rutas entre estaciones del sistema de Metro de la Ciudad de México.

---

## Lenguaje y versión

* Lenguaje: Python
* Versión: Python **3.14.3**

---

## Dependencias

El proyecto utiliza las siguientes librerías externas:

* networkx – Manejo y representación del grafo del sistema de Metro
* matplotlib – Visualización de rutas y del grafo 

### Instalación de dependencias

Instalar las librerías con pip:

```bash
pip install networkx matplotlib
```

## Cómo ejecutar el proyecto

1. Clona el repositorio:

```bash
git clone https://github.com/JuanMoral3s/IA-2026-2-Tarea-1-BFS-y-DFS-Aplicados-al-Metro-CDMX.git
```

2. Entra al directorio del proyecto:

```bash
cd IA-2026-2-Tarea-1-BFS-y-DFS-Aplicados-al-Metro-CDMX
```

3. Ejecuta el archivo principal:

```bash
python main.py
```

---

## Casos de prueba obligatorios

Los tres casos de prueba se encuentran definidos dentro del archivo `main.py` y se ejecutan automáticamente al correr el programa.

### Caso 1

Ruta desde:

* Observatorio → Ciudad Azteca

```python
pruebas("Observatorio","Ciudad Azteca")
```

---

### Caso 2

Ruta desde:

* Indios Verdes → Velodromo

```python
pruebas("Indios Verdes","Velodromo")
```

---

### Caso 3

Ruta desde:

* El Rosario → Tasqueña

```python
pruebas("El Rosario","Tasqueña")
```

---

## Prueba de completitud (opcional)

El archivo `main.py` incluye un bloque comentado que permite evaluar la completitud de los algoritmos ejecutando múltiples pruebas con estaciones aleatorias.

Este bloque realiza hasta **100,000 pruebas**, verificando que BFS y DFS encuentren una ruta cuando existe.

Para activarlo:

1. Descomenta el bloque dentro de `main.py`
2. Ejecuta nuevamente:

```bash
python main.py
```

El programa mostrará:

* `Cumple para #n pruebas` si todos los casos fueron exitosos
* `No cumple para #n pruebas` si alguna prueba falla

---

## Descripción general

* BFS encuentra la ruta con el menor número de estaciones (óptimo para costos uniformes).
* DFS explora en profundidad y encuentra una ruta válida, aunque no necesariamente la más corta.
* Ambos algoritmos operan sobre el grafo del sistema de Metro de la CDMX.

---

## Autor

Juan Pablo Vera Morales
Facultad de Ingeniería – UNAM
Ingeniería en Computación
