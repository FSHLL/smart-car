import src.helpers as helpers
from src.constants import Representations
from src.node import Node
import time

def evaluate(matrix, operators):
    matrix = helpers.matrix_from_string(matrix)

    vehicle = helpers.find_number_in_matrix(matrix, Representations.VEHICLE)
    passenger = helpers.find_number_in_matrix(matrix, Representations.PASSENGER)
    destination = helpers.find_number_in_matrix(matrix, Representations.DESTINATION)

    current_destination = passenger

    tree = list()
    tail = list()
    node_id = 1

    tail.append(Node(0, vehicle))
    tree.append(Node(0, vehicle))

    start = time.time()

    solution_node = None

    while len(tail) > 0:
        vehicle_node = tail.pop(0)
        vehicle_position = vehicle_node.position

        if vehicle_position.is_equal_to(current_destination):
            if current_destination.is_equal_to(passenger):
                current_destination = destination
                tail.clear()
            else:
                solution_node = vehicle_node
                break

        for operator in operators:
            if helpers.can_apply_operator(matrix, vehicle_position, operator):
                new_vehicle_position = helpers.apply_operator(vehicle_position, operator)
                if not helpers.already_visited_in_branch(vehicle_node, tree, new_vehicle_position):
                    tail.append(Node(node_id, new_vehicle_position, vehicle_node.id, depth=vehicle_node.depth+1))
                    tree.append(Node(node_id, new_vehicle_position, vehicle_node.id, depth=vehicle_node.depth+1))
                    node_id += 1

    end = time.time()

    return {
        'steps': helpers.get_solution(solution_node, tree),
        'expandedNodes': node_id,
        'depth': helpers.get_max_depth(tree),
        'time': ((end-start))
    }