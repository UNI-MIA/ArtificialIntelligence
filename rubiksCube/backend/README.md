# Implementación del Algoritmo de Korf para la Solución Óptima del Cubo Rubik
```
Alejos Yarasca Fiorella Andrea (fiorella.alejos@yahoo.com)
Llana Chavez Walter Rodolfo (walter.wr7@gmail.com)
Luna Jaramillo Juan Marcos (jmlunaj@pucp.edu.pe)
Medina Rodríguez Henry (hmedinar@uni.pe)
Salazar Vega Edwin Martín (edwin@iartificial.io)
```

```
MIA-103 Fundamentos de Inteligencia Artificial  - Maestría en Inteligencia Artificial - 2024-I
Facultad de Ingeniería Industrial y Sistemas  -  Universidad Nacional de Ingeniería
```

## Description

```
cube = RubiksCube(
    state="rrrwrwrgryrywwwwrwbrbggggggwowyyyyyygygbbbbbbooobooooo"
)
```

```
MAX_MOVES = 5 #max amount of moves when building heuristics map
NEW_HEURISTICS = False #control for overwritting heuristics
HEURISTIC_FILE = 'heuristic.json' #file that the heuristics are saved in or need to be saved in
```

# Launch Instructions
step 1: open your console <br>
step 2: create a virutal enviroment <br>
step 3: type the following command: <br>
```
pip install -r requirements.txt
```
step 4: type the following command:
```
cd <app directory>
```
step 5: type the following command:
```
python3 main.py
```
step 6: type in the action you wish to perform
