
while True:
    try:
        print("Choose the operation you want to perform:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Square")
        print("7. Factorial")
        print("8. Trigonometric functions: sin, cos, tan (input in degrees)")
        print("9. Logarithm (base 10) and natural logarithm (ln)")
        print("10. Calculate Pi to a specific number of decimal places")
        print("11. Exit program")
        print("--------------------------------------------------")
        print("Choose the operation you want to perform:")
        print("--------------------------------------------------")
        import math 
        import sys
        user_input = input("Input your choice (1-11): ")
        if user_input == "1":
            num1 = float(input("Input first value:"))
            num2 = float(input("Input second value:"))
            result = num1 + num2
            print(f"Result: {result}")   
        elif user_input == "2":
            num1 = float(input("Input first value:"))
            num2 = float(input("Input second value:"))
            result = num1 - num2
            print(f"Result: {result}")   
        elif user_input == "3":
            num1 = float(input("Input first value:"))
            num2 = float(input("Input second value:"))
            result = num1 * num2
            print(f"Result: {result}")
        elif user_input == "4":
            num1 = float(input("Input first value:"))
            num2 = float(input("Input second value:"))
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"Result: {result}")
        elif user_input == "5":
            num1 = float(input("Input base: "))
            num2 = float(input("Input exponent: "))
            result = num1 ** num2
            print(f"Result: {result}")
        elif user_input == "6":
            num1 = float(input("Input value: "))
            result = num1 ** 2
            print(f"Result: {result}")
        elif user_input == "7":
            num1 = int(input("Input value: "))
            if num1 < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                result = 1
                for i in range(1, num1 + 1):
                    result *= i
                print(f"Factorial {num1} is: {result}")
        elif user_input == "8":
            angle = float(input("Input angle in degrees: "))
            radians = math.radians(angle)
            sin_value = math.sin(radians)
            cos_value = math.cos(radians)
            tan_value = math.tan(radians)
            print(f"sin({angle}) = {sin_value}")
            print(f"cos({angle}) = {cos_value}")
            print(f"tan({angle}) = {tan_value}")
        elif user_input == "9":
            num1 = float(input("Input value for logarithm (base 10): "))
            if num1 <= 0:
                print("Logarithm is not defined for negative numbers.")
            else:
                log_value = math.log10(num1)
                ln_value = math.log(num1)
                print(f"log10({num1}) = {log_value}")
                print(f"ln({num1}) = {ln_value}")
        elif user_input == "10":
            decimal_places = int(input("Input number of decimal places for Pi: "))
            pi_value = round(math.pi, decimal_places)
            print(f"Pi to {decimal_places} decimal places is: {pi_value}")
        elif user_input == "11":
            print("Exiting program.")
            sys.exit()
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\n--------------------------------------------------\n")
        continue