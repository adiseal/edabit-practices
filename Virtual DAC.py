def V_DAC(value):
    # Define the reference voltage
    reference_voltage = 5.00

    # Calculate the analog voltage level
    voltage = (value / 1023) * reference_voltage

    # Return the voltage rounded to two decimal places
    return round(voltage, 2)
