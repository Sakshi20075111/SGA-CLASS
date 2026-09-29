import requests
SERVER = "HTTP://127.0.0.1:5000"

# 1. Get latest menu 
response = requests.get(SERVER+"/menu")
menu = response.json()
print("latest menu:")
print(menu)

# 2. place an order 
order= { "item": "poha", "quantity": 2}
response = requests.post(
    SERVER +"/order",
    json=order
)
result =response.json()
print("order result:")
print(result)