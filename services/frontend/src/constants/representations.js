export const representations = {
    lightTraffic: 0,
    wall: 1,
    vehicle: 2,
    mediumTraffic: 3,
    heavyTraffic: 4,
    passenger: 5,
    destination: 6,
}

const colors = {
    [representations.lightTraffic]: '#ffffff', // Blanco
    [representations.wall]: '#8b8b8b',         // Gris
    [representations.vehicle]: '#0000ff',      // Azul
    [representations.mediumTraffic]: '#d0f0c0', // Verde claro
    [representations.heavyTraffic]: '#ff0000',  // Rojo
    [representations.passenger]: '#ffa500',     // Naranja
    [representations.destination]: '#ff00ff',   // Magenta
};

export const getColorByRepresentation = (representation) => {
    return colors[representation] || '#ffffff';
};