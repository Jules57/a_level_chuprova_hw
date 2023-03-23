const medianNumber = 10
let star = '*'

for (let i = 0; i < medianNumber; i++) {
    let startFiller = ''
    for (let j = (medianNumber - 2 - i); j >= 0; j--) {
        startFiller += '-'
    }
    console.log(startFiller + star + startFiller)
    star += '**'
}
