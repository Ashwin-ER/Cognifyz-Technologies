def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5 / 9


def temperature_converter():
    """Main temperature conversion program"""
    print("Temperature Converter")
    print("====================")

    while True:
        # Get conversion direction
        print("\nChoose conversion direction:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        # Exit condition
        if choice == '3':
            print("Thank you for using the Temperature Converter!")
            break

        # Validate choice
        if choice not in ['1', '2']:
            print("Invalid choice! Please select 1, 2, or 3.")
            continue

        # Get temperature input
        try:
            temp = float(input("Enter the temperature value: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        # Perform conversion based on choice
        if choice == '1':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {result:.2f}°F")
        else:
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {result:.2f}°C")

        # Ask if user wants to continue
        again = input("\nWould you like to convert another temperature? (y/n): ")
        if again.lower() != 'y':
            print("Thank you for using the Temperature Converter!")
            break


# Test cases
def run_tests():
    """Test the conversion functions"""
    print("Running test cases...")
    # Test Celsius to Fahrenheit
    assert round(celsius_to_fahrenheit(0), 2) == 32.00, "0°C should be 32°F"
    assert round(celsius_to_fahrenheit(100), 2) == 212.00, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert round(fahrenheit_to_celsius(32), 2) == 0.00, "32°F should be 0°C"
    assert round(fahrenheit_to_celsius(212), 2) == 100.00, "212°F should be 100°C"
    print("All test cases passed!")


# Run the program
if __name__ == "__main__":
    # Run tests first
    run_tests()
    print("\nStarting Temperature Converter...")
    temperature_converter()
