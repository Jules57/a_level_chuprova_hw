let arr = [10, 800, 3453000, 8010]
console.log(arr.slice(1, 3))


function mySlice(arr, start, end) {
    start = start < 0 ? arr.length + start : start
    if (end === undefined) {
        end = arr.length
    } else {
        end = end < 0 ? arr.length + end : end
    }

    let finalList = []
    for (start; start < end; start++ ) {
        finalList.push(arr[start])
    }
    return finalList
}

console.log(mySlice(arr, 1, 3))
