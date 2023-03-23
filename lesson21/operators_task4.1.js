const roomsOnFloor = 3
const floors = 9
const roomNumber = 467
const roomsPerPorch = roomsOnFloor * floors

let porchNumber = 0
let floorNumber = 0

if (roomNumber % roomsPerPorch) {
    porchNumber = (roomNumber - (roomNumber % roomsPerPorch)) / roomsPerPorch + 1
} else {
    porchNumber = roomNumber / roomsPerPorch
}

let singlePorch = roomNumber % roomsPerPorch

if (roomNumber <= roomsPerPorch && roomNumber % roomsOnFloor) {
    floorNumber = (roomNumber - roomNumber % roomsOnFloor) / roomsOnFloor + 1
} else if ( !(roomNumber % roomsPerPorch) && !(roomNumber % roomsOnFloor)) {
    floorNumber = roomNumber / porchNumber / roomsOnFloor
} else if (singlePorch % roomsOnFloor) {
    floorNumber = (singlePorch - singlePorch % roomsOnFloor) / roomsOnFloor + 1
} else {
    floorNumber = singlePorch / roomsOnFloor
}

console.log(porchNumber)
console.log(floorNumber)
