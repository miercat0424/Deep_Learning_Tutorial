from tqdm import tqdm

import time

text  = ""
for char in tqdm(["a","b","c","d"]):
    # time.sleep(1)
    text = text + char


for i in tqdm(range(100)):
    time.sleep(0.1)
