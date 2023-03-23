let myArr = [10, 800, 11, 115, 50, 3450]
let myArr2 = ['ab', 'ac', 'db', 'cd', 'fd']

function myArraySort(arr, callback) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < (arr.length - i - 1); j++) {
            if (arr[j] < arr[j + 1]) {
                let temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            }
        }
    }
    return arr
}

console.log(myArraySort(myArr2))
console.log(myArr.sort( (a, b) => b - a))
