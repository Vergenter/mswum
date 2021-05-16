import time

class Timer:
    def __init__(self):
        self.time = 0
        self.start_time = None

    def start(self):
        if self.start_time is not None:
            raise Exception("Timer is running. Use stop() to stop it.")

        self.start_time = time.perf_counter()
    
    def stop(self):
        if self.start_time is None:
            raise Exception("Timer is not running. Use start() to start it.")
        
        stop = time.perf_counter()
        self.time = stop - self.start_time
        self.start_time = None
        self.print()

    def print(self):
        print(f"Elapsed time: {self.time:0.4f} seconds.")