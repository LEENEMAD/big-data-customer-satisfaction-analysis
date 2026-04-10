#!/usr/bin/env python3
import sys, csv, io

for line in sys.stdin:
    #reader
    r = next(csv.reader(io.StringIO(line)))
    # skip header
    if r and r[0].strip().lower() == "order_id":
        continue
    # get values with padding if needed
    order_id, delay, items, price, freight, satisfaction = (r + [""]*6)[:6]
    # Normalize satisfaction label where its all in lowercase and without spaces
    satisfaction = (satisfaction or "").strip().lower()
    # keep only 3 valid labels other than that save as "unknown"
    if satisfaction in ["not satisfied", "satisfied", "extremely satisfied"]:
        satisfaction_cat = satisfaction
    else:
        satisfaction_cat = "unknown"
    # emit 4 aspects delay, items, price, freight 
    # each key is (aspect, value) and each value is
    print(f"Delay category: ,{delay or 'Unknown'}\t{satisfaction_cat},1")
    print(f"Items bin: ,{items or 'Unknown'}\t{satisfaction_cat},1")
    print(f"Price bin: ,{price or 'Unknown'}\t{satisfaction_cat},1")
    print(f"Freight bin: ,{freight or 'Unknown'}\t{satisfaction_cat},1")
