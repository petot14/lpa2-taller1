# Pruebas Unitarias con `pytest`

![commits](https://badgen.net/github/commits/UR-CC/lpa2-taller1?icon=github) 
![last_commit](https://img.shields.io/github/last-commit/UR-CC/lpa2-taller1)

- ver [badgen](https://badgen.net/) o [shields](https://shields.io/) para otros tipos de _badges_

## Autor

- [@estudiante](https://www.github.com/estudiante)

## Descripción del Proyecto

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ut quam dolor. Quisque elementum est sed massa gravida convallis. Donec volutpat turpis eget lectus feugiat congue. Morbi rutrum auctor eleifend. Etiam iaculis libero tellus, vel aliquet erat tempor sed. Duis efficitur quam vel sapien luctus, sed semper lacus mollis. Suspendisse non nunc eleifend, aliquet elit eget, condimentum augue.

Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus vel nibh fringilla, porta elit vel, consequat libero. Nulla et libero ac nulla ultricies sollicitudin. Sed viverra non nulla id convallis. Morbi vel varius lacus, in maximus nunc. Praesent sed semper diam. Pellentesque vehicula nulla augue, ut porta dolor consequat at.

## Documentación

### Requerimientos del Sistema para Cálculo de Ingredientes

**REQ-01**: Entrada de datos

El sistema debe permitir al usuario ingresar la cantidad de porciones deseadas, validando que el número sea un valor positivo (mayor o igual a cero) y que sea múltiplo de 4. En caso de que el valor ingresado no cumpla con estas condiciones, el sistema debe mostrar un mensaje informativo solicitando al usuario que ingrese un múltiplo de 4 y repetir el proceso de entrada hasta que se proporcione un valor válido.

**REQ-02**: Cálculo de ingredientes

El sistema debe calcular con precisión la cantidad necesaria de cada ingrediente basándose en la cantidad de porciones especificada, utilizando la siguiente proporción base para 8 porciones:

- 450 gramos de arroz
- 2 litros de leche
- 200 gramos de azúcar
- 400 gramos de leche condensada

El sistema debe verificar nuevamente que la cantidad de porciones sea un valor positivo y múltiplo de 4 antes de realizar los cálculos. Si no cumple con estas condiciones, todos los ingredientes deben establecerse en cero.

**REQ-03**: Presentación de resultados

El sistema debe mostrar al usuario un resumen detallado de los ingredientes necesarios para la cantidad de porciones especificada, incluyendo:

- La cantidad de porciones seleccionada
- La cantidad de arroz en gramos
- La cantidad de leche en litros
- La cantidad de azúcar en gramos
- La cantidad de leche condensada en gramos

Cada cantidad debe estar claramente etiquetada con su unidad de medida correspondiente.

## Instalación

Morbi quam lectus, tempus sit amet mi non, facilisis dignissim erat. Aenean tortor libero, rhoncus eu eleifend ut, volutpat id nisi. Ut porta eros at ante rutrum pharetra. Integer nec nulla dictum, vestibulum ligula id, hendrerit ex. Morbi eget tortor metus.

1. Clonar el proyecto
```bash
git clone https://github.com/UR-CC/lpa2-taller1.git
```

2. Crear y activar entorno virtual
```bash
cd lpa2-taller1
python -m venv venv
venv/bin/activate
```

3. Instalar librerías y dependencias
```bash
pip install -r requirements.txt
```
    
## Ejecución

Maecenas sed lorem at arcu varius mollis. Sed eleifend nulla ut blandit interdum. Donec sollicitudin nunc at orci facilisis dignissim. Donec at arcu luctus, commodo magna eget, blandit leo.

1. Ingresar al proyecto

```bash
cd lpa2-taller1
```

2. Ejecutar el programa

```bash
python main.py
```

3. Ejecutar las pruebas

```bash
pytest
```

