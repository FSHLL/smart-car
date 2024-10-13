from src.position import Position
from src.constants import Operators, Representations

def matrix_from_string(matrix_string):
    matrix = []
    for line in matrix_string.strip().split('\n'):
        row = list(map(int, line.split()))
        matrix.append(row)

    return matrix

def find_number_in_matrix(matrix, target):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == target:
                return Position(i, j)
    return None

def apply_operator(position, operator):
    if operator == Operators.UP:
        new_position = position.up()
    elif operator == Operators.DOWN:
        new_position = position.down()
    elif operator == Operators.LEFT:
        new_position = position.left()
    else:
        new_position = position.right()
    return new_position

def can_apply_operator(matrix, position, operator):
    new_position = apply_operator(position, operator)
    row = new_position.row
    col = new_position.col
    return (0 <= row < len(matrix)) and (0 <= col < len(matrix[0]) and matrix[row][col] != Representations.WALL)

def get_solution(solution_node, nodes):
        if not solution_node:
            return None

        chain = []
        current_id = solution_node.parent
        chain.append(solution_node.position)

        while current_id is not None:
            parent_node = next((node for node in nodes if node.id == current_id), None)
            if parent_node is None:
                break

            chain.append(parent_node.position)
            current_id = parent_node.parent

        return chain[::-1]

def get_parent_node(s_node, nodes):
    return next((node for node in nodes if node.id == s_node.parent), None)

def already_visited_in_branch(node, nodes, destination):
    solution = get_solution(node, nodes)
    for position in solution:
        if position.row == destination.row and position.col == destination.col:
            return True
    return False