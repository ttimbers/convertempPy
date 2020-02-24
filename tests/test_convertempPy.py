from convertempPy import convertempPy as tmp


def test_fahr_to_celsius():
    assert tmp.fahr_to_celsius(32) == 0


def test_celsius_to_kelvin():
    assert tmp.celsius_to_kelvin(-273.15) == 0


def test_kelvin_to_celsius():
    assert tmp.kelvin_to_celsius(273.15) == 0


def test_celsius_to_fahr():
    assert tmp.celsius_to_fahr(0) == 32


def test_kelvin_to_fahr():
    assert tmp.kelvin_to_fahr(273.15) == 32


def fahr_to_kelvin():
    assert tmp.fahr_to_celsius(32) == 273.15
