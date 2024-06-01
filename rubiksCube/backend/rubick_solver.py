import json
import os.path
import time

from cube import RubiksCube
from solver import IDA_star, build_heuristic_db


class RubickSolver:
    MAX_MOVES = 5
    NEW_HEURISTICS = False
    HEURISTIC_FILE = 'heuristic.json'
    h_db = None

    def __init__(self):
        print("Cargando Base de Datos Heuristica...")
        start_time = time.time()
        cube = RubiksCube(n=3)
        if os.path.exists(self.HEURISTIC_FILE):
            with open(self.HEURISTIC_FILE) as f:
                self.h_db = json.load(f)
        else:
            self.h_db = None

        if self.h_db is None or self.NEW_HEURISTICS is True:
            actions = [(r, n, d) for r in ['h', 'v', 's'] for d in [0, 1] for n in range(cube.n)]
            self.h_db = build_heuristic_db(
                cube.stringify(),
                actions,
                max_moves=self.MAX_MOVES,
                heuristic=self.h_db
            )

            with open(self.HEURISTIC_FILE, 'w', encoding='utf-8') as f:
                json.dump(
                    self.h_db,
                    f,
                    ensure_ascii=False,
                    indent=4
                )
        elapsed_time = time.time() - start_time
        cube.reset()
        print("Tiempo de Carga Base de Datos: " + str(elapsed_time) + " seg.")
    def start_solve_rubick(self, pattern):
        print("Iniciando cube solver....")
        start_time = time.time()
        print("input: ", pattern)
        cube = RubiksCube(n=3, state=pattern)
        cube.show()
        data1 = cube.show2()
        print('-----------')

        #data2 = cube.show2()
        #cube.show()
        print('----------')
        #--------------------------------
        solver = IDA_star(self.h_db)
        moves = solver.run(cube.stringify())
        print(moves)

        for m in moves:
            if m[0] == 'h':
                cube.horizontal_twist(m[1], m[2])

            elif m[0] == 'v':
                cube.vertical_twist(m[1], m[2])

            elif m[0] == 's':
                cube.side_twist(m[1], m[2])

        cube.show()
        data3 = cube.show2()
        elapsed_time = time.time() - start_time
        print("Tiempo en resolver el cubo: " + str(elapsed_time) + " seg.")
        return {"d1": data1, "d3": data3, "move": moves, "time": elapsed_time}
