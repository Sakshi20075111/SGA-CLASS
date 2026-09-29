import requests
from bs4 import BeautifulSoup
import pandas as pd
#1. URL of our canteen webpage
url = "http://10.11.20.24:5001/menu"

# 2. get webpage
response = requests.get(url)

# 3. parse HTML
soup = BeautifulSoup(response.text, "html.parser")

#4. find all menu items
items = soup.find_all("li")

# 5. store extracted data
data = []
for item in items:
    text = item.text.strip()
    name,price = text.split(" .")
    data.append({ "item": name,"price": price})
    #6. convert to dataframe
    df = pd.dataframe(data)

    # 7. display data
    print(df)

    # 8. save to CSV
    df.to_csv("canteen_menu.csv", index=false)
    print("\nsaved to canteen_menu.csv")
