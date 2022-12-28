# 4

import csv

with open("StudentsPerformance 14.csv") as f:
    reader = csv.DictReader(f, skipinitialspace=True)
    data = [r for r in reader]

filteredData = list(
    filter(
        lambda x: x["race/ethnicity"] == "group C" and x["test preparation course"] == "completed",
        data,
    )
)

print(filteredData)
