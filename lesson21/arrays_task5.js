let myArr = [0, 0, 0, 1]   // 1
let myArr2 = [0, 0, 1, 0]  // 2
let myArr3 = [0, 1, 0, 1]  // 5
let myArr4 = [1, 0, 0, 1]  // 9
let myArr5 = [0, 1, 1, 0]  // 6
let myArr6 = [1, 1, 1, 1]  // 15
let myArr7 = [1, 0, 1, 1]  // 11
let myArr8 = [1, 0, 0, 0, 1]  // 17
let myArr9 = [1, 1, 1, 0, 0, 1]  // 57

const multiplier = 2

function getDecimalNumber(arr) {
    let value = 0
    for (let i = 0; i < arr.length; i++) {
        if (arr[arr.length-i-1] === 1) {
            value = value + multiplier ** i
        }
    }
    return value
}

console.log(getDecimalNumber(myArr))
console.log(getDecimalNumber(myArr2))
console.log(getDecimalNumber(myArr3))
console.log(getDecimalNumber(myArr4))
console.log(getDecimalNumber(myArr5))
console.log(getDecimalNumber(myArr6))
console.log(getDecimalNumber(myArr7))
console.log(getDecimalNumber(myArr8))
console.log(getDecimalNumber(myArr9))
