#!/usr/bin/env python3
import sys
from collections import defaultdict
#for tracing teh current key that is being processed
currentK = None
# dictionary for holding the counts of the category for each key
counts = defaultdict(int)
# when a key is finshed processing result is prited
def flush(key, counts):
    result = ",".join([f"{k}:{v}" for k,v in counts.items()])
    print(f"{key}\t{result}")
# loop to process each line of mapper input 
for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    satisfaction_cat, c = value.split(",", 1)
    c = int(c)
    #if we are processing the same key add 1
    if currentK == key:
        counts[satisfaction_cat] += c
    #if not flush the results of the previous key
    else:
        if currentK:
            flush(currentK, counts)
        currentK = key
        # reset counts for the new key
        counts = defaultdict(int)
        counts[satisfaction_cat] = c
#when exiting the loop flush the results of the previous key
if currentK:
    flush(currentK, counts)
