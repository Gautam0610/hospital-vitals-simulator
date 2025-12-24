import random
import time
from datetime import datetime, timedelta

class FaultInjector:
    def __init__(self, missing_field_prob=0.1, delay_prob=0.1, max_delay=5, out_of_order_prob=0.1):
        self.missing_field_prob = missing_field_prob
        self.delay_prob = delay_prob
        self.max_delay = max_delay
        self.out_of_order_prob = out_of_order_prob
        self.last_timestamp = datetime.now()

    def inject_missing_field(self, data):
        new_data = data.copy()
        for key in data.keys():
            if random.random() < self.missing_field_prob:
                del new_data[key]
        return new_data

    def inject_delay(self):
        if random.random() < self.delay_prob:
            delay = random.uniform(0, self.max_delay)
            time.sleep(delay)

    def inject_out_of_order_timestamp(self):
        if random.random() < self.out_of_order_prob:
            # Introduce a timestamp that is earlier than the last one
            delta = timedelta(seconds=random.uniform(1, 10))  
            new_timestamp = self.last_timestamp - delta
            return new_timestamp
        else:
            self.last_timestamp = datetime.now()
            return self.last_timestamp

    def maybe_inject_faults(self, data):
        self.inject_delay()
        corrupted_data = self.inject_missing_field(data)
        timestamp = self.inject_out_of_order_timestamp()
        return corrupted_data, timestamp