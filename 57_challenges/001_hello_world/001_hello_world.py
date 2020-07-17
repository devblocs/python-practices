def get_user_input()-> str:
    return input("What is your name? ")

def print_message()-> None:
    name = get_user_input()
    print(f"Hello, {name}, Nice to meet you!")

print_message()