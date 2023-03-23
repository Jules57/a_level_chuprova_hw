const medianNumber = 8
let filler = '-'
let star = '*'

for (let i = 1; i <= medianNumber; i++) {
    console.log(
        filler.repeat(medianNumber - i) +
        star.repeat(i * 2 - 1) +
        filler.repeat(medianNumber - i))
}
