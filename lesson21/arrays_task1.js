const citiesAndCountries  = {
    'Kiev': 'Ukraine',
    'New York': 'USA',
    'Amsterdam': 'Netherlands',
    'Berlin': 'Germany',
    'Paris': 'France',
    'Lisbon': 'Portugal',
    'Vienna': 'Austria'
}

let result = []

for (let elem in citiesAndCountries) {
    let singleStr = ''
    singleStr = elem + ' is ' + citiesAndCountries[elem]
    result.push(singleStr)
}

console.log(result)
