const sheetsInReamPaper = 500
const consumptionPerWeek = 1200
const weekAmount = 10

let totalConsumption = consumptionPerWeek * weekAmount
let reamOfPaper = 0
let additionalReam = totalConsumption % sheetsInReamPaper

if (additionalReam) {
    reamOfPaper = (totalConsumption - additionalReam) / sheetsInReamPaper + 1
}
else {
    reamOfPaper = totalConsumption / sheetsInReamPaper
}

console.log(reamOfPaper)
