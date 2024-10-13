class Representations:
    LIGHT_TRAFFIC = 0
    WALL = 1
    VEHICLE = 2
    MEDIUM_TRAFFIC = 3
    HEAVY_TRAFFIC = 4
    PASSENGER = 5
    DESTINATION = 6

class RepresentationsCost:
    COSTS = {
        Representations.LIGHT_TRAFFIC: 1,
        Representations.MEDIUM_TRAFFIC: 4,
        Representations.HEAVY_TRAFFIC: 7,
        Representations.PASSENGER: 1,
        Representations.DESTINATION: 1,
        Representations.VEHICLE: 1,
    }

    @classmethod
    def get_cost(cls, matrix, position):
        # print(cls.COSTS.get(matrix[position.row][position.col], None))
        return cls.COSTS.get(matrix[position.row][position.col], None)

class Operators:
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

    @classmethod
    def get_all_operators(cls):
        return [cls.UP, cls.DOWN, cls.LEFT, cls.RIGHT]

class Algorithms:
    UNINFORMED_BREADTH_SEARCH = 0
    UNINFORMED_UNIFORM_COST = 1
    UNINFORMED_DEPTH_AVOIDING_CYCLES = 2
    INFORMED_AVARA = 3
    INFORMED_A = 4