import json

from config import DATA_DIR
OK = DATA_DIR.joinpath('orders.json')


with open(OK) as f:
    result = json.load(f)
    print(result)
exit()