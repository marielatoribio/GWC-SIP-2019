# --- Define your functions below! ---
def greetingfunc():
    print("GREETINGS!")
    greetingfunc()
def addfunc(num1, num2):
    num1 = input("enter number 1")
    num2 = input("enter number 2")
    print("I will add 2 numbers")
    qnswer = num1 + num2
    print(f"the anwer is {answer}")
def respondtouser(useranswer):
    if(useranswer == "good"):
        print("I'm happy to hear. I'm good too.")
    if(useranswer == "bad"):
        print("I'm sorry, how can I help?")

# --- Put your main program below! ---
def main():

    num1 = int(input("enter number 1: "))
    num2 = int(input("enter number 2: "))
# DON'T TOUCH! Setup code that runs your main() function.
user_input = input ("How are you today?")
respondtouser(user_input)
if __name__ == "__main__":
  main()
addfunc(num1, num2)
