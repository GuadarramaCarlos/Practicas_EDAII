# 📚 Proyecto Final: Sistema de Recomendación y Análisis de Libros

## **Proyecto Final – Estructuras de Datos Avanzados II (2026-1)**

---

## Objetivo General del Proyecto

[cite_start]Desarrollar un **ecosistema modular** que permita explorar, buscar, analizar y recomendar libros a partir del Book Recommendation Dataset (`Books.csv`, `Ratings.csv`, `Users.csv`)[cite: 3]. [cite_start]Esto se logra aplicando las estructuras de datos y algoritmos estudiados en EDA II[cite: 3]. [cite_start]El sistema unificado se conforma integrando todos los módulos implementados por los equipos[cite: 6].

---

## Estructura de Carpetas y Módulos

El proyecto está organizado en carpetas individuales para cada uno de los siete módulos implementados:

* **`01_ordenamientos_comparativos`**: Ordenamiento de libros (Quick Sort, Merge Sort, Heap Sort)[cite: 20].
* **`02_ordenamientos_no_comparativos`**: Ordenamiento de usuarios y ratings (Counting Sort, Radix Sort)[cite: 37, 38].
* **`03_busquedas`**: Búsquedas de usuarios, libros y ratings (Hashing, Búsqueda Binaria, Centinela)[cite: 54, 55].
* **`04_arboles_binarios`**: Inserción y búsqueda de nuevos libros (BST, AVL, Red-Black)[cite: 71, 72].
* **`05_arboles_n_arios`**: Inserción y búsqueda de nuevos usuarios (Árboles B y B+)[cite: 90, 91].
* **`06_grafos_no_ponderados`**: Recorridos para encontrar islas y caminos (BFS, DFS)[cite: 110, 111].
* **`07_grafos_ponderados`**: Recorridos para encontrar caminos más cortos (Dijkstra)[cite: 137, 138].

---

## Orden Sugerido de Ejecución

[cite_start]Es crucial seguir este orden para que los módulos dependientes puedan acceder a los archivos intermedios (`.pkl`) generados por los módulos previos[cite: 166].

1.  **Ordenamientos Comparativos** (Módulo 1)
2.  **Ordenamientos No Comparativos** (Módulo 2)
3.  **Búsquedas** (Módulo 3)
4.  **Árboles Binarios de Búsqueda** (Módulo 4)
5.  **Árboles N-arios de Búsqueda** (Módulo 5)
6.  **Grafos No Ponderados** (Módulo 6)
7.  **Grafos Ponderados** (Módulo 7)

---

## Comunicación y Archivos Intermedios

[cite_start]La comunicación se basa en la generación y consumo de archivos intermedios, principalmente en formato `.pkl`, y la escritura de logs compartidos[cite: 166, 168].

| Módulo Generador | Archivos Generados (Ejemplos) | Módulo(s) Utilizador(es) |
| :--- | :--- | :--- |
| **1. Ordenamientos Comparativos** | `books-by-isbn.pkl` [cite: 27] | **3. [cite_start]Búsquedas** (Para crear tabla hash y buscar libros por ISBN)[cite: 58, 62]. |
| **2. Ordenamientos No Comparativos** | `ratings-by-user-id.pkl` [cite: 48] | **3. [cite_start]Búsquedas** (Para búsqueda binaria de ratings)[cite: 59, 64]. |
| **3. Búsquedas** | Archivo `.pkl` con la **Tabla Hash** [cite: 69] | Ninguno listado directamente. |
| **4. Árboles Binarios** | `*-tree.pkl`, `sorted-data.csv` [cite: 86] | Ninguno listado directamente. |
| **5. Árboles N-arios** | `*-tree.pkl`, `sorted-data.csv` [cite: 104] | Ninguno listado directamente. |
| **Logs Compartidos** | **`logs.log`** (JSON format) [cite: 168] | [cite_start]Todos los módulos escriben en él[cite: 36, 53, 70, 89, 108, 135, 163]. |

---
