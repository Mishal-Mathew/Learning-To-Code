import threading
import time

def worker_function():
    print("Worker thread starting...")
    time.sleep(5)  # Simulate some work
    print("Worker thread finished.")

# Create a Thread object
my_thread = threading.Thread(target=worker_function)

# Start the thread
my_thread.start()

# Call join() to wait for the worker thread to finish
print("Main thread waiting for worker thread...")
my_thread.join() 
print("Main thread continues after worker thread completion.")