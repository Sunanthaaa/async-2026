import asyncio
from time import ctime, perf_counter
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301019"

    print(f"{ctime()} | --- [Task 2] Practice using gather to wait for all group orders ---")

    start_time = perf_counter()

    t1 = asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice"))
    t2 = asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Wonton Noodles"))
    t3 = asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak"))

    results = await asyncio.gather(t1, t2, t3)

    for dish in results:
        print(f"{ctime()} | [Pickup] Shop: {dish['shop']} | Menu: {dish['menu']} is ready!")

    elapsed = perf_counter() - start_time
    print(f"{ctime()} | Total time: {elapsed:.2f} seconds (Equals to the slowest dish.)")

if __name__ == "__main__":
    asyncio.run(main())