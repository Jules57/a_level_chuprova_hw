let myArr = [10, 800, 3453000, 8010]

function myArrayFilter (arr, callback) {
    
    let filteredArray = []
    for (let i = 0; i < arr.length; i++) {
        if (callback(arr[i])) {
            filteredArray.push(arr[i])
        }
    }
    return filteredArray
}


console.log(myArrayFilter(myArr, el => el < 1000))
console.log(myArrayFilter(myArr))
