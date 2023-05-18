# Sistema de gestión automatizado de tickets de alimentación

Programa empresarial de gestión para cesta ticket de alimentación, este es un modelo general y básico de lo que vendría siendo un sistema completo de tickets o incluso un sistema de nomina. Python como lenguaje principal y sqlite3 como base de datos para trabajar en local viene bien para cualquer institución que quiera llevar control sobre una parte de su nomina.

Para poner en marcha el proyecto solo debe de inicializar con el interprete de python el archivo app.py

```
python app.py
```

O si está en linux

```
python3 app.py
```

Aún se encuentra bajo construcción y actualizaciones constantes, pero las dependencias de este programa serán las siguientes

- tkinter
- sqlite3
- openpyxl
- reportlab

En caso de que se quiera utilizar, tanto el algoritmo de importación y la base de datos están pensadas para un modelo especifico de hoja de Excel. Se recomienda adaptar estos dos modulos a la necesidad del usurio, o en todo caso adaptar las hojas de Excel al algorithmo.