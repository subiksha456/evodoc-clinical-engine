import time

cache_store = {}
TTL = 3600  # 1 hour

def generate_cache_key(data):
    meds = sorted(data.medications)
    current = sorted(data.patient_history.current_medications)

    return str(meds + current)

def get_cache(key):
    if key in cache_store:
        value, timestamp = cache_store[key]

        if time.time() - timestamp < TTL:
            return value
        else:
            del cache_store[key]

    return None

def set_cache(key, value):
    cache_store[key] = (value, time.time())