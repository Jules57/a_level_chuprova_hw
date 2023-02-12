class ChemicalElement:
    def __init__(self, melting_point, boiling_point):
        self.melting_point = melting_point
        self.boiling_point = boiling_point

    def convert_to_celsius(self, temperature: float, temp_scale: str) -> float:
        celsius_degrees = temperature
        temp_scale = temp_scale.lower()
        if temp_scale == 'f':
            celsius_degrees = (temperature - 32) * (5 / 9)
        elif temp_scale == 'k':
            celsius_degrees = temperature - 273.15
        return round(celsius_degrees, 2)

    def define_aggregate_state(self, temperature: float, temp_scale: str = 'c') -> str:
        temperature = self.convert_to_celsius(temperature, temp_scale)
        state = None
        if temperature < self.melting_point:
            state = 'solid'
        elif self.melting_point <= temperature < self.boiling_point:
            state = 'liquid'
        elif temperature >= self.boiling_point:
            state = 'gas'
        return state


if __name__ == '__main__':
    sulfur = ChemicalElement(115.2, 446.6)
    assert sulfur.define_aggregate_state(110) == 'solid'
    assert sulfur.define_aggregate_state(120) == 'liquid'
    assert sulfur.define_aggregate_state(450) == 'gas'
    assert sulfur.define_aggregate_state(500, 'f') == 'liquid'
    assert sulfur.convert_to_celsius(500, 'f') == 260
    assert sulfur.define_aggregate_state(300, 'k') == 'solid'
    assert sulfur.convert_to_celsius(300, 'k') == 26.85

    nitrogen = ChemicalElement(-210, -195.8)
    assert nitrogen.define_aggregate_state(-215) == 'solid'
    assert nitrogen.define_aggregate_state(-200) == 'liquid'
    assert nitrogen.define_aggregate_state(3) == 'gas'
    assert nitrogen.define_aggregate_state(400, 'f') == 'gas'
    assert nitrogen.convert_to_celsius(400, 'f') == 204.44
    assert nitrogen.define_aggregate_state(80, 'k') == 'gas'
    assert nitrogen.convert_to_celsius(80, 'k') == -193.15

    manganese = ChemicalElement(1246, 2061)
    assert manganese.define_aggregate_state(1217) == 'solid'
    assert manganese.define_aggregate_state(2019) == 'liquid'
    assert manganese.define_aggregate_state(2100) == 'gas'
    assert manganese.define_aggregate_state(600, 'f') == 'solid'
    assert manganese.convert_to_celsius(600, 'f') == 315.56
    assert manganese.define_aggregate_state(2400, 'k') == 'gas'
    assert manganese.convert_to_celsius(2400, 'k') == 2126.85

    iodine = ChemicalElement(113.7, 184.3)
    assert iodine.define_aggregate_state(98) == 'solid'
    assert iodine.define_aggregate_state(115) == 'liquid'
    assert iodine.define_aggregate_state(195) == 'gas'
    assert iodine.define_aggregate_state(370, 'f') == 'gas'
    assert iodine.convert_to_celsius(370, 'f') == 187.78
    assert iodine.define_aggregate_state(650, 'k') == 'gas'
    assert iodine.convert_to_celsius(650, 'k') == 376.85

