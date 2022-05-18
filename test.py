import json
import csv
d = {"one":1, "two":2}

with open('test.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(d)

# with open('test.txt', 'r') as f:
#     dict = json.loads(f.read())
#     print(dict)