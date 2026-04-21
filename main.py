from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue
import threading

class ThreadPoolManager:
    def __init__(self, max_workers):
        self.max_workers = max_workers
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.queue = Queue()

    def submit_task(self, func, *args, **kwargs):
        self.queue.put((func, args, kwargs))

    def start(self):
        threading.Thread(target=self.process_queue).start()

    def process_queue(self):
        while True:
            task = self.queue.get()
            if task is None:
                break
            func, args, kwargs = task
            self.executor.submit(func, *args, **kwargs)
            self.queue.task_done()

    def shutdown(self):
        self.queue.put(None)
        self.executor.shutdown(wait=True)

def example_task(x, y):
    print(f"Task {x} + {y} = {x + y}")

manager = ThreadPoolManager(5)
manager.submit_task(example_task, 1, 2)
manager.submit_task(example_task, 3, 4)
manager.submit_task(example_task, 5, 6)
manager.start()
manager.shutdown()
```

Kodda quyidagilar mavjud:

- `ThreadPoolManager` klassi yaratildi, u quyidagilar ni o'z ichiga oladi:
  - `max_workers` - threadlar soni
  - `executor` - `ThreadPoolExecutor` obyekti
  - `queue` - `Queue` obyekti
- `submit_task` metodi - vazifani qo'shish uchun metod
- `start` metodi - threadni boshlash uchun metod
- `process_queue` metodi - vazifalarni qayta ishlash uchun metod
- `shutdown` metodi - threadni to'xtatish uchun metod
- `example_task` funktsiyasi - misol vazifa funktsiyasi
- `manager` obyekti - `ThreadPoolManager` obyekti
- `submit_task` metodi orqali vazifalar qo'shildi
- `start` metodi orqali thread boshlandi
- `shutdown` metodi orqali thread to'xtatildi
