import threading
import queue
import time

# Define the number of items to be produced and consumed
NUM_ITEMS = 100000

# Shared queue between producer and consumer
buffer = queue.Queue()


def producer():
    # It loops the NUM_ITEMS and places integers into the queue.
    for i in range(NUM_ITEMS):
        buffer.put(i)  # Put item in the queue
    buffer.put(None)


def consumer():
    # It continuously takes items from the queue and processes them.
    while True:
        item = buffer.get()
        if item is None:
            break
        buffer.task_done()


def benchmark():
    # Function to measure the time taken for the producer-consumer execution. Records the start time and end time
    start_time = time.time()

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    end_time = time.time()
    print(f"Execution Time: {end_time - start_time:.4f} seconds")

# Runs the benchmark
if __name__ == "__main__":
    benchmark()
