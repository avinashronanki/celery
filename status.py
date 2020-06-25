from tasks import *
import time
result = check_status.delay()

while True:
    time.sleep(1)
    print(result.status)