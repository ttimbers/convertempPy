def fahr_to_celsius(temp):
    """
    Convert Fahrenheit to Celsius.

    Parameters
    ----------
    temp : int or double
        The temperature in Fahrenheit.

    Returns
    -------
    double
        The temperature in Celsius.

    Examples
    --------
    >>> from convertempPy import convertempPy as tmp
    >>> tmp.fahr_to_celsius(32)
    0
    """
    return (temp - 32) * (5 / 9)


def celsius_to_kelvin(temp):
    """
    Convert Celsius to Kelvin.

    Parameters
    ----------
    temp : int or double
        The temperature in Celsius.

    Returns
    -------
    double
        The temperature in Kelvin.

    Examples
    --------
    >>> from convertempPy import convertempPy as tmp
    >>> tmp.celsius_to_kelvin(-273.15)
    0
    """
    return temp + 273.15


def kelvin_to_celsius(temp):
    """
    Convert Kelvin to Celsius.

    Parameters
    ----------
    temp : int or double
        The temperature in Kelvin.

    Returns
    -------
    double
        The temperature in Celsius.

    Examples
    --------
    >>> from convertempPy import convertempPy as tmp
    >>> tmp.kelvin_to_celsius(273.15)
    0
    """
    return temp - 273.15


def celsius_to_fahr(temp):
    """
    Convert Celsius to Fahrenheit.

    Parameters
    ----------
    temp : int or double
        The temperature in Celsius.

    Returns
    -------
    double
        The temperature in Fahrenheit.

    Examples
    --------
    >>> from convertempPy import convertempPy as tmp
    >>> tmp.celsius_to_fahr(0)
    32
    """
    return temp * 9 / 5 + 32


def kelvin_to_fahr(temp):
    """
    Convert Kelvin to Fahrenheit.

    Parameters
    ----------
    temp : int or double
        The temperature in Kelvin.

    Returns
    -------
    double
        The temperature in Fahrenheit.

    Examples
    --------
    >>> from convertempPy import convertempPy as tmp
    >>> tmp.kelvin_to_fahr(273.15)
    32
    """
    temp_c = kelvin_to_celsius(temp)
    return celsius_to_fahr(temp_c)


def fahr_to_kelvin(temp):
    """
    Convert Fahrenheit to Kelvin.

    Parameters
    ----------
    temp : int or double
        The temperature in Fahrenheit.

    Returns
    -------
    double
        The temperature in Kelvin.

    Examples
    --------
    >>> from convertempPy import convertempPy as tmp
    >>> tmp.fahr_to_kelvin(32)
    273.15
    """
    temp_c = fahr_to_celsius(temp)
    return celsius_to_kelvin(temp_c)
