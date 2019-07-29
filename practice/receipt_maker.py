arc_description = (
	"Aerospace and Robotic Connections (ARC) supplies simple-smart solutions"
	" to the new age of technology in outer space travel.\n"
	)

nav_software_description = (
	"ARC's proprietary space navigation software. Price includes installation" 
	" and integration.\n"
	)
nav_software_price = 25000.00

weather_software_description = (
	"ARC's proprietary software for space weather readings and forcasts. Price"
	" includes integration, installation.\n"
	)
weather_software_price = 39000.00

com_secure_description = (
	"ARC's proprietary software package for securing communication in space."
	" Price includes installation and integration.\n"
	)
com_secure_price = 13000.00

sales_tax = 0.085


customer_one_shopcart = ""
customer_one_total = 0


customer_one_shopcart += nav_software_description
customer_one_total += nav_software_price

customer_one_shopcart +=  com_secure_description
customer_one_total += com_secure_price

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer Pne Items:")
print(customer_one_shopcart)
print("Customer One Total:")
print(customer_one_total)