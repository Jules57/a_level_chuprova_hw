const roomsOnFloor = 3
const floors = 9
const roomNumber = 467
const roomsPerPorch = roomsOnFloor * floors

let porchNumber = 0
let floorNumber = 0

porchNumber = (roomNumber + (roomsPerPorch - roomNumber % roomsPerPorch) % roomsPerPorch) / roomsPerPorch

let singlePorch = (roomNumber - 1) % roomsPerPorch + 1
floorNumber = (singlePorch + (roomsOnFloor - singlePorch % roomsOnFloor) % roomsOnFloor) / roomsOnFloor

console.log(porchNumber)
console.log(floorNumber)
