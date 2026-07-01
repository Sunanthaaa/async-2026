import asyncio
from time import ctime, time
import time as t

# 1. Front desk greeting process
def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    t.sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

# 2. Individual customer workflow
async def customer_private_workflow(customer):

    print(f"{ctime()} [Async-{customer}] Taking Order ...")
    await asyncio.sleep(1)
    print(f"{ctime()} [Async-{customer}] Taking Order ...Done!")

    print(f"{ctime()} [Async-{customer}] Cooking Spaghetti ...")
    await asyncio.sleep(1)
    print(f"{ctime()} [Async-{customer}] Cooking Spaghetti ...Done!")

    print(f"{ctime()} [Async-{customer}] Manage Bar for Drinks ...")
    await asyncio.sleep(1)
    print(f"{ctime()} [Async-{customer}] Manage Bar for Drinks ...Done!")

    print(f"{ctime()} [Async-{customer}] All served!")

async def main():

    customers = ['A', 'B', 'C']

    start_time = time()

    # PHASE 1 : Greeting
    for customer in customers:
        greet_diners(customer)

    print(f"\n{ctime()} All customers greeted. Splitting into async tasks...\n")

    tasks = []

    for customer in customers:
        tasks.append(
            asyncio.create_task(
                customer_private_workflow(customer)
            )
        )

    await asyncio.gather(*tasks)

    duration = time() - start_time

    print(f"\n{ctime()} Finished Entire Restaurant Operation "f"in {duration:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())