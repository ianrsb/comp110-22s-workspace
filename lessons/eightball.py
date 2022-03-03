"""An oracle that predcits the future."""

from random import randint

input("Ask a yes/no question: ")

response: int = randint(0, 3)

if response == 0:
    print("Most definetely")
elif response == 1:
    print("Highly likely")
elif response == 2:
    print("Ask Again later")
elif response == 3:
    print("No way, not a chance")