name = 'Eric'
print("Hello " + name + ", would you like to learn some Python today?")
print(f"Hello {name}, would you like to learn some Python today?")
hello = "Hello "
another = ', would you like to learn some Python today?'
message = "{}{}{}".format(hello, name, another)
print(message)