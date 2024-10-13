export const algorithms = {
    UNINFORMED_BREADTH_SEARCH: 0,
    UNINFORMED_UNIFORM_COST: 1,
    UNINFORMED_DEPTH_AVOIDING_CYCLES: 2,
    INFORMED_AVARA: 3,
    INFORMED_A: 4,
}

const names = {
    [algorithms.UNINFORMED_BREADTH_SEARCH]: 'No informada amplitud',
    [algorithms.UNINFORMED_UNIFORM_COST]: 'No informada costo uniforme',
    [algorithms.UNINFORMED_DEPTH_AVOIDING_CYCLES]: 'No informada profundidad evitando ciclos',
    [algorithms.INFORMED_AVARA]: 'Informada avara',
    [algorithms.INFORMED_A]: 'Informada A*'
}

export const getNameByAlgorithm = (algorithm) => {
    return names[algorithm] || '';
};