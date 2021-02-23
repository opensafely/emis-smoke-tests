import csv
import json

with open("output/input.csv") as f:
    reader = csv.reader(f)
    headers = next(reader)
    assert headers == [
        "registered",
        "has_died",
        "asthma_dx_today",
        "asthma_rx_today",
        "patient_id",
    ]

    asthma_dx_today = 0
    asthma_rx_today = 0

    for row in reader:
        if row[2] == "1":
            asthma_dx_today += 1
        if row[3] == "1":
            asthma_rx_today += 1

output = {"asthma_dx_today": asthma_dx_today, "asthma_rx_today": asthma_rx_today}

with open("output/counts.json", "w") as f:
    json.dump(output, f, indent=2)
