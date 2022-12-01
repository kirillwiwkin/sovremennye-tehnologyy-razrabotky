import requests

url = "https://api.github.com/repos/kubernetes/kubernetes"

data = requests.get(url).json()

keys = ['company', 'created_at', 'email', 'id', 'name', 'url']
filtered_data = {k: data[k] if k in data else None for k in keys}

with open("filtered_data.txt", "w") as f:
    f.write(str(filtered_data))
