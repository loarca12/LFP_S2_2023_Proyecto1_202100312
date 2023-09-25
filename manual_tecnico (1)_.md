UNIVERSIDAD DE SAN CARLOS DE GUATEMALA
  
LENGUAJES FORMALES Y DE PROGRAMACIÓN
  
SECCIÓN A+
  
  
#  <center> MANUAL TÉCNICO </center>
  
  
<center>Nombre: Giancarlo Adonay Cifuentes Loarca</center>
<center>Carné: 202100312</center>
<center>Ciudad de Guatemala, 24 de septiembre de 2023</center>
  
___
  
###  OBJETIVOS
  
* Brindar una aplicación que analiza archivos con extensiones .json del
cual se puede hacer un análisis léxico y generar un reporte.
* Conocer más acerca de los autómatas y gramáticas libres de contexto.
  
  
###  REQUISITOS DEL SISTEMA
  
* Windows 10,8,7 (x86 y x64)
* Procesador a 1.6 GHz o superior
* 1 GB (32 bits) o 2 GB (64 bits) de RAM (agregue 512 MB al host si se ejecuta en una máquina virtual)
    * 3 GB de espacio disponible en el disco duro
* Disco duro de 5400 RPM
* Tarjeta de vídeo compatible con DirectX 9 con resolución de pantalla de 1024 x 768 o más
  
####  DESCARGAR VISUAL STUDIO CODE
  
Link de descarga [Visual Studio Code](https://code.visualstudio.com/download "vscode")
  
####  DESCARGAR PYTHON
  
Link de descarga [Python](https://www.python.org/downloads/ "python") ver manual de instalación en la página Oficial
  
##  <center>CLASES Y MÉTODOS</center>
  
###  Archivo gui.py
  
#####  CLASES
  
```python
class ScrollText(tk.Frame):
class RedesignedApp(tk.Tk):
```
#####  MÉTODOS
  
```python
def __init__(self, master):
def get(self):
def insert(self):
def delete(self):
def __init__(self):
def view_errors(self):
def open_file(self):
def save_file(self):
def analyze_text(self): 
```
##  <center>CLASES Y MÉTODOS</center>
  
###  Archivo aritmeticas.py
  
#####  CLASES
  
```python
class ExpresionAritmetica:
```
#####  MÉTODOS
  
```python
def __init__(self, tipo, valor1, valor2, linea, columna)
def interpretar(self)
def __str__(self): 
```
  
##  <center>CLASES Y MÉTODOS</center>
  
###  Archivo expresion.py
  
#####  CLASES
  
```python
class Expresion:
```
#####  MÉTODOS
  
```python
def interpretar(self, contexto): 
```
  
##  <center>CLASES Y MÉTODOS</center>
  
###  Archivo trigonometricas.py
  
#####  CLASES
  
```python
class ExpresionTrigonometrica:
```
#####  MÉTODOS
  
```python
def __init__(self, tipo, valor, linea, columna):
def interpretar(self): 
```
  
##  <center>CLASES Y MÉTODOS</center>
  
###  Archivo Arbol.py
  
#####  CLASES
  
```python
class Arbol:
```
#####  MÉTODOS
  
```python
def __init__(self):
def agregarConfiguracion(self, confg):
def agregarNodo(self, valor):
def agregarArista(self, nodo1, nodo2):
def generarGrafica(self):
def obtenerUltimoNodo(self): 
```
  
##  <center>CLASES Y MÉTODOS</center>
  
###  Archivo analizador.py
  
#####  MÉTODOS
  
```python
def tokenize_string(input_str, i)
def tokenize_number(input_str, i)
def tokenize_input(input_str)
def get_instruccion()
def create_instructions()
def analizar(entrada)
def generar_reporte_errores(): 
```
##  <center>CARPETAS Y ARCHIVOS</center>
  
  
* dist
    * Diagraph.gv.pdf
* Expresiones
    * aritmeticas.py
    * expresion.py
    * trigonometricas.py
* Graficas
    * arbol.py
* Pruebas
    * archivos de prueba
* Archivo analizador.py
* Archivo gui.py
  