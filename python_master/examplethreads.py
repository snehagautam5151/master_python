import logging
import threading
import time 

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.basicConfig(format=format, level=logging.INFO, datefmt = "%H:%M:%S")
    logging.info("main   : before running thread")
    x = threading.Thread(target= thread_function,args= (1,))
    logging.info("main   : before running thread")
    x.start()
    logging.info("Main   : wait for the thread to finish")
    logging.info("Main   : all done")