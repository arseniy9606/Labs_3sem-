import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print(f"time: {end - self.start:.4f}")


@contextmanager
def cm_timer_2():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"time: {end - start:.4f}")


if __name__ == '__main__':
    from time import sleep

    print("Тест cm_timer_1:")
    with cm_timer_1():
        sleep(1.2)

    print("Тест cm_timer_2:")
    with cm_timer_2():
        sleep(0.8)
