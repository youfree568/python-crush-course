first_name = 'ada'
last_name = 'lovelace'
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
full_name2 = "{} {}".format(first_name, last_name)
print(full_name2.title())

