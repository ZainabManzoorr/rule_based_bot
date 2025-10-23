bot_name : str = "ChatGPT"
print(f"Hello, I\'m {bot_name}! How can I assist you today?")

while True:
    user_input = input("You: ").lower()
    if user_input in ["hi", "hello"]:
        print(f"{bot_name}: Hello! How can I help you?")
    elif user_input in ["bye", "exit"]:
        print(f"{bot_name}: Goodbye! Have a great day!")
    elif user_input in ["+", "add"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"{bot_name}: The sum is {num1 + num2}")
        except ValueError:
            print(f"{bot_name}: Please enter valid numbers.")
    elif user_input in ["-", "subtract"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"{bot_name}: The difference is {num1 - num2}")
        except ValueError:
            print(f"{bot_name}: Please enter valid numbers.")
    elif user_input in ["*", "multiply"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"{bot_name}: The product is {num1 * num2}")
        except ValueError:
            print(f"{bot_name}: Please enter valid numbers.")
    elif user_input in ["/", "divide"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                print(f"{bot_name}: Cannot divide by zero.")
            else:
                print(f"{bot_name}: The quotient is {num1 / num2}")
        except ValueError:
            print(f"{bot_name}: Please enter valid numbers.")
    else:
        print(f"{bot_name}: I'm sorry, I didn't understand that. Can you please rephrase?")
        