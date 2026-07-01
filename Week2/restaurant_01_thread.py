from time import sleep, ctime, time
import threading
# 1. Front desk greeting process, synchronous, one person at a time
def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

# 2. Individual customer workflow, to be taken separately in their own thread
def customer_private_workflow(customer):
    # Take Order
    print(f"{ctime()} [Thread-{customer}] Taking Order ...")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Taking Order ...Done!")

    # Do Cooking
    print(f"{ctime()} [Thread-{customer}] Cooking Spaghetti ...")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Cooking Spaghetti ...Done!")

    # Manage Bar
    print(f"{ctime()} [Thread-{customer}] Manage Bar for Drinks ...")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Manage Bar for Drinks ...Done!")

    print(f"{ctime()} [Thread-{customer}] All served!")

if __name__ == "__main__":

    customers = ['A', 'B', 'C']

    start_time = time()

    # PHASE 1: Greet customers one by one synchronously
    for customer in customers:
        greet_diners(customer)

    print(f"\n{ctime()} All customers greeted. Splitting into threads...\n")

    # PHASE 2: Assign each customer to perform a separate workflow
    customer_threads = []

    for customer in customers:
        # Create a thread for each customer
        t = threading.Thread(
            target=customer_private_workflow,
            args=(customer,)
        )

        customer_threads.append(t)
        t.start()  # Allows them to start working together

    # Wait for all threads to finish
    for t in customer_threads:
        t.join()

    duration = time() - start_time

    print(f"\n{ctime()} Finished Entire Restaurant Operation in "f"{duration:.2f} seconds.")