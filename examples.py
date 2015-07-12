# import the psypy modules, psySI for SI units and psyIP for IP units.
import psySI as SI

# The main function to be used is the state function.

# psySI.state(p1, p1val, p2, p2val, P)

# p1 - A string that is a valid state property. Valid state properties are:
#      DBT   - Dry bulb temperature
#      H     - Specific enthalpy
#      RH    - Relative humidity
#      V     - Specific volume
#      W     - Humidity ratio
#      WBT   - Wet bulb temperature

# p1val - A numeric that is in base units of which ever property that is given.
#         Valid base SI units are (with IP units in parenthesis):
#         DBT   - Kelvins (degrees Rankine)
#         H     - KiloJoules per kilogram (British thermal unit per pound mass)
#         RH    - decimal number, not a percentage (same as SI)
#         V     - cubic meters per kilogram (cubic feet per pound mass)
#         W     - kilogram per kilogram (pounds mass per pound mass)
#         WBT   - Kelvins (degrees Rankine)

# p2 - A string that is a valid state property but must not be the same as p1

# p2val - A numeric that is in base units of which ever property that is given.

# P - A numeric that is the atmospheric pressure in Pascals of SI units or
#     pounds per square inch for IP units.

# The state function returns a list of all state property values in the
# following order:
#                 Dry bulb temperature (DBT)
#                 Specific enthalpy (H)
#                 Relative humidity (RH)
#                 Specific volume (V)
#                 Humidity ratio (W)
#                 Wet bulb temperature (WBT)

# Example - For a dry bulb temperature of 300 Kelvin and a relative humidity
#           of 0.32 (i.e. 32%) at standard atompspheric pressure, the other
#           state properties can be calculated by the following.
S=SI.state("DBT",300,"RH",0.32,101325)
print("The dry bulb temperature is ", S[0])
print("The specific enthalpy is ", S[1])
print("The relative humidity is ", S[2])
print("The specific volume is ", S[3])
print("The humidity ratio is ", S[4])
print("The wet bulb temperature is ", S[5])
# All calculated values are in base SI units as listed above.
