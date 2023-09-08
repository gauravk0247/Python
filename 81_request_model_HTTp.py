<<<<<<< HEAD
import requests
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)
print(r.status_code)

url = "www.something.com"
data = {
    "p1":4,
    "p2":9
}
=======
import requests
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)
print(r.status_code)

url = "www.something.com"
data = {
    "p1":4,
    "p2":9
}
>>>>>>> 8ad8ee1 (Add initial files)
r2 = requests.post(url=url, data=data)