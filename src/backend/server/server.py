import threading
import concurrent
from util import chatgpt

#import flask
num_threads = 4

#handle request from frond-end
def handleRequest():
    pass

#threading
def generateSchedule():
    pass

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = [executor.submit(chatgpt.generateSchedule, "say hello")]
        
        for future in concurrent.futures.as_completed(results):
            result = future.result()
            print(result)