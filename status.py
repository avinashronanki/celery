from tasks import *
import time
result = check_status.delay()

while True:
    time.sleep(2)
    print(result.status)