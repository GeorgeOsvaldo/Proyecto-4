# Simulación de la Máquina de Galton en Python

Este proyecto implementa una **simulación de la Máquina de Galton**, también conocida como *Quincunce de Galton*, utilizando **Python** junto con las librerías **NumPy**, **Matplotlib** y **Random**.  

La Máquina de Galton es un dispositivo mecánico inventado por **Francis Galton** en el siglo XIX para ilustrar cómo los procesos aleatorios pueden dar lugar a una **distribución normal (curva de campana)**. Se trata de un excelente ejemplo del **Teorema Central del Límite**, donde múltiples decisiones binarias independientes tienden a producir una distribución gaussiana.

---

## Descripción del Proyecto

En esta simulación:

1. Se lanzan un número determinado de **bolas** desde la parte superior de la máquina.
2. Cada bola pasa por una serie de **niveles** con clavijas.  
   En cada nivel, la bola puede:
   - Ir a la **izquierda** con probabilidad del 50%.  
   - Ir a la **derecha** con probabilidad del 50%.
3. Tras atravesar todos los niveles, cada bola termina en un **contenedor** (casilla final).  
4. Al repetir este proceso para muchas bolas, la distribución resultante forma una **curva de campana** (distribución binomial aproximada a una normal).

---

## Requisitos

Antes de ejecutar el programa, instala las librerías necesarias:

```bash
pip install numpy matplotlib
