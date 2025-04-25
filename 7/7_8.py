sandwich_orders = ["big mac", "cheese", "doble cheese", "role", "sandwich"]
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"I made {current_sandwich}")
	finished_sandwiches.append(current_sandwich)
print(finished_sandwiches)
for i in finished_sandwiches:
	print(i)