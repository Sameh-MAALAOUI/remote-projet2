import logging
import os
from redis import Redisimport requests
import time

og = logging.getLogger(__name__)
redis = Redis("redis")

def get_random_bytes():
    r = requests.get("http://rng/32")
    return r.content

def hash_bytes(data):
    r = requests.post("http://hasher/", data=data,headers={"Content-Type": "application/octet-stream"})
    hex_hash = r.text
    return hex_hash

def work_loop(interval=1):
    deadline = 0
    loops_done = 0
    while True:
        if time.time() > deadline:
            log.info("{} units of work done, updating hash counter".format(loops_done))
            redis.incrby("hashes", loops_done)
            loops_done = 0
            deadline = time.time() + interval
        work_once()
        loops_done += 1

def work_once():
    log.debug("Doing one unit of work")