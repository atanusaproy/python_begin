# Multiprocessing in Pythonf


from multiprocessing import Process
import os
import threading

def task():
    print(f"Process {os.getpid()} is running")


if __name__ == "__main__":
    processes = []
    for i in range(10):
        p = Process(target=task)
        processes.append(p)
        p.start() # Start the child process
    for p in processes:
        p.join() # Wait for all processes to complete
    print("All processes are done")


# Multithreading in Python
threading.Thread(target=task)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("All threads are done")


