import threading
import time


def work(num):
    print("Start %d work" %(num))
    results = 0
    for i in range(10000000 * num):
        results += i


def none_threading():
    for i in range(3):
        work(i)


def process_threading():
    threads = []
    for i in range(3):
        thread = threading.Thread(target=work, args=(i, ))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start = time.time()
    none_threading()
    print(time.time() - start)

    start = time.time()
    process_threading()
    print(time.time() - start)

# GIL 정책 때문에 속도 차이는 거의 나지 않는다.

# threading.active_count() = 현재 실행 중인 모든 스레드 개수
# threading.current_thread() = 현재 스레드 나타내기
# threading.main_thread() = 메인 스레드 구하기
# threading. enumerate() = 모든 스레드 열거하기