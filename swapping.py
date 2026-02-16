# A simple program to swap two numbers in a single line

a = 10
b = 20

print("a = ", a, "\nb = ", b)
print("\nSwapping in a single line...\n")

a = (a + b) - (b := a)

print("\nSwapped...\n")
print("a = ", a, "\nb = ", b)
