# 4
import json

with open("data.json") as f:
    data = json.load(f)

filtered_data = list(filter(
    lambda d: d['client_id'] == 62602 and d['category'] == "page", 
    data["events_data"])
    )

print(len(filtered_data))