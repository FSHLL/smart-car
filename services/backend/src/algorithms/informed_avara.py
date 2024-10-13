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
    visited_positions = {}

    tree = list()
    tail = list()
    depth = 0
    node_id = 1

    tail.append(Node(0, vehicle))
    tree.append(Node(0, vehicle))

    start = time.time()

    solution_node = None

    can_back = False

    while len(tail) > 0:
        minimum_node = min(tail, key=lambda n: n.cost)
        vehicle_node = tail.pop(tail.index(minimum_node))
        vehicle_position = vehicle_node.position

        if vehicle_position.is_equal_to(current_destination):
            if current_destination.is_equal_to(passenger):
                current_destination = destination
                tail.clear()
                visited_positions = {}
                can_back = True
            else:
                solution_node = vehicle_node
                break

        if vehicle_position.key() in visited_positions:
            visited_positions[vehicle_position.key()] += 1
            if visited_positions[vehicle_position.key()] >= 1000:
                return {
                    'steps': [],
                    'expandedNodes': node_id,
                    'cost': None,
                    'depth': depth,
                    'time': ((time.time()-start))
                }
        else:
            visited_positions[vehicle_position.key()] = 1

        for operator in operators:
            if helpers.can_apply_operator(matrix, vehicle_position, operator):
                new_vehicle_position = helpers.apply_operator(vehicle_position, operator)
                parent_node = helpers.get_parent_node(vehicle_node, tree)

                if can_back or not parent_node or not new_vehicle_position.is_equal_to(parent_node.position):
                    cost = helpers.manhattan_distance(new_vehicle_position, passenger) + helpers.manhattan_distance(passenger, destination)
                    tail.append(Node(node_id, new_vehicle_position, vehicle_node.id, cost=cost+vehicle_node.cost))
                    tree.append(Node(node_id, new_vehicle_position, vehicle_node.id, cost=cost+vehicle_node.cost))
                    node_id += 1
                    can_back = False

        depth += 1

    end = time.time()

    return {
        'steps': helpers.get_solution(solution_node, tree),
        'tree': tree,
        'expandedNodes': node_id,
        'cost': solution_node.cost,
        'depth': depth,
        'time': ((end-start))
    }