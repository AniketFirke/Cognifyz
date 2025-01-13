def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    return (celsius * 9/5) + 32

def temperature_converter():
    print("Temperature Converter")
    print("1. Convert Fahrenheit to Celsius")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Exit")

    while True:
        choice = input("Choose the conversion direction (1/2/3): ")

        if choice == '1':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C\n")
        elif choice == '2':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F\n")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    temperature_converter()
