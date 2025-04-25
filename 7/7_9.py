sandwich_orders = ["pastorami", "big mac", "cheese",
 "doble cheese", "pastorami", "role", "sandwich", "pastorami"]

print("I'm sorry, our cafe is run out pastorami")

while "pastorami" in sandwich_orders:
	sandwich_orders.remove("pastorami")
print("But we have:")
for sandwich in sandwich_orders:
	print(f"\t{sandwich}")