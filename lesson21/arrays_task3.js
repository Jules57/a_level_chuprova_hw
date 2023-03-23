const weekDays = {
    en: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    it: ['Lunedi', 'Martedi', 'Mercoledi', 'Giovedi', 'Venerdi', 'Sabato', 'Domenica']
}

function getDayName(language, day) {
    // let language = 'en'
    // let day = 7
    return weekDays[language][day-1]
}

console.log(getDayName('it', 5))
