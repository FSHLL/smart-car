import src.helpers as helpers
from src.constants import Representations, RepresentationsCost, Operators
from src.node import Node
import time

def evaluate(matrix, operators):
    matrix = helpers.matrix_from_string(matrix)

    vehicle = helpers.find_number_in_matrix(matrix, Representations.VEHICLE)
    passenger = helpers.find_number_in_matrix(matrix, Representations.PASSENGER)
    destination = helpers.find_number_in_matrix(matrix, Representations.DESTINATION)

    current_destination = passenger
    visited_positions = {}

    tree = list()
    tail = list()
    depth = 0
    node_id = 1

    tail.append(Node(0, vehicle))
    tree.append(Node(0, vehicle))

    start = time.time()

    solution_node = None

    while len(tail) > 0:
        minimum_node = min(tail, key=lambda n: n.cost)
        vehicle_node = tail.pop(tail.index(minimum_node))
        vehicle_position = vehicle_node.position

        if vehicle_position.is_equal_to(current_destination):
            if current_destination.is_equal_to(passenger):
                current_destination = destination
                tail.clear()
            else:
                solution_node = vehicle_node
                break

        visited_positions[vehicle_position.key()] = 1

        for operator in operators:
            if helpers.can_apply_operator(matrix, vehicle_position, operator):
                new_vehicle_position = helpers.apply_operator(vehicle_position, operator)

                if new_vehicle_position.key() not in visited_positions:
                    tail.append(Node(node_id, new_vehicle_position, vehicle_node.id, cost=RepresentationsCost.get_cost(matrix, new_vehicle_position)))
                    tree.append(Node(node_id, new_vehicle_position, vehicle_node.id, cost=RepresentationsCost.get_cost(matrix, new_vehicle_position)))
                    node_id += 1
        depth += 1

    end = time.time()

    return {
        'steps': helpers.get_solution(solution_node, tree),
        'expandedNodes': node_id,
        'depth': depth,
        'time': ((end-start))
    }