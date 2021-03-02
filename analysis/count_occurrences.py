import csv
import json

with open("output/input.csv") as f:
    reader = csv.reader(f)
    headers = next(reader)

    asthma_dx_ix = headers.index("asthma_dx_today")
    asthma_rx_ix = headers.index("asthma_rx_today")

    asthma_dx_today = 0
    asthma_rx_today = 0

    for row in reader:
        if row[asthma_dx_ix] == "1":
            asthma_dx_today += 1
        if row[asthma_rx_ix] == "1":
            asthma_rx_today += 1

output = {"asthma_dx_today": asthma_dx_today, "asthma_rx_today": asthma_rx_today}

with open("output/counts.json", "w") as f:
    json.dump(output, f, indent=2)
