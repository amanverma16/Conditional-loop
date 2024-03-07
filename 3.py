def convert_temperature():
    print("CHange Temperature")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        
        
        F=32+ (9*celsius) / 5
        print(F)
    elif choice == '2':
        Fahrenheit = float(input("Enter temperature in Fahrenheit"))    
        C = (5/9) * (Fahrenheit - 32)
        print(C)
    
    else: 
        print("Invalid input")
        
convert_temperature()
