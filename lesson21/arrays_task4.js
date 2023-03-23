let myArr = [19, 5, 42, 1,  2, 77]
let myNewArr = [10, 800, 3453000, 8010]
let myVeryNewArr = [12, 898, 899, 900]

function addTwoMinValues(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < (arr.length - i - 1); j++) {
            if (arr[j] > arr[j+1]) {
                let temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            }
        }
    }
    let firstElem = arr[0]
    let secondElem = arr[1]
    return firstElem + secondElem
}

console.log(addTwoMinValues(myArr))
console.log(addTwoMinValues(myNewArr))
console.log(addTwoMinValues(myVeryNewArr))
