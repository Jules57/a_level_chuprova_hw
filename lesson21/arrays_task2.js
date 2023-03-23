function getArray() {
    let amount = 12
    let finalList = []

    let singleList = []
    for (let i = 1; i <= amount; i++) {
        singleList[i-1] = i
    }

    let newList = []
    for (let i = 0; i < singleList.length; i++) {
        if (singleList[i] % 3 === 0) {
            newList.push(singleList[i])
            finalList.push(newList)
            newList = []
        }
        else {
            newList.push(singleList[i])
        }
    }
    return finalList
}

console.log(getArray())
