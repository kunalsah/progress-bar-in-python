import time
from tqdm import tqdm

for i in tqdm(range(100), desc="Loading...", ascii=False, ncols=75):
	time.sleep(0.01)
print("complete.")