# Call methods from other modules

from maths import Calculator
from timezones import timezones

calc=Calculator()
print("Addition:",calc.add(10,5))
print("Subtraction:",calc.subtract(10,5))

tz=timezones()
tz.display_timezones()