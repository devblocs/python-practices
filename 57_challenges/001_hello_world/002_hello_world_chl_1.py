def get_user_input()-> str:
    return input("What is your name? ")

def print_message()-> None:
    print(f"Hello, {get_user_input()}, Nice to meet you!")

print_message()