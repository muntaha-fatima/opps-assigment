
# **** ____________________ Assigment 4______________***

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


print(TemperatureConverter.celsius_to_fahrenheit(0))     # Output: 32.0
print(TemperatureConverter.celsius_to_fahrenheit(100))   # Output: 212.0
