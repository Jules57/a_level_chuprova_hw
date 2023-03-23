const sheetsInReamPaper = 500
const consumptionPerWeek = 1200
const weekAmount = 8

let totalConsumption = consumptionPerWeek * weekAmount
let reamOfPaper = 0

if (totalConsumption % sheetsInReamPaper > 0) {
    for (let i = 1; i < totalConsumption; i++) {
        totalConsumption -= sheetsInReamPaper
        reamOfPaper += 1
    }
}
else {
    reamOfPaper = totalConsumption / sheetsInReamPaper
}

console.log(reamOfPaper)
