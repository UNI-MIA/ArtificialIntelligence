from flask import Blueprint
from rubick_solver import RubickSolver

controllers = Blueprint('controllers', __name__)

rubick_solver = RubickSolver()


def call_rubick(pattern: str) -> str:
    return rubick_solver.start_solve_rubick(pattern)
