from time import sleep, ctime, time
import threading

def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1)

    print(f"{ctime()} | Coffee ready for {customer_name}!")
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1)

    print(f"{ctime()} | LCD: Done for customer {customer_name}.")


def main():
    queue = ['A', 'B', 'C']
    threads = []

    print(f"{ctime()} | === Multi-threading Coffee Machine ===")

    start_time = time()

    # สร้าง thread สำหรับแต่ละลูกค้า
    for customer in queue:
        t = threading.Thread(target=make_coffee, args=(customer,))
        threads.append(t)
        t.start()

    # รอทุก thread ทำงานเสร็จ
    for t in threads:
        t.join()

    duration = time() - start_time

    print(f"{ctime()} | Total time: {duration:.2f} seconds")


if __name__ == "__main__":
    main()