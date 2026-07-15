# foodcourt_03_wait_first.py

import asyncio
from time import ctime, perf_counter
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301019"

    print(f"{ctime()} | --- [Task 3] Practice using wait (FIRST_COMPLETED) ---")

    start_time = perf_counter()

    # สั่งอาหาร 3 ร้านพร้อมกัน
    t1 = asyncio.create_task(
        send_order_to_kitchen(
            MY_STUDENT_ID,
            "hainanese_chicken",
            "Chicken Rice Thigh"
        )
    )

    t2 = asyncio.create_task(
        send_order_to_kitchen(
            MY_STUDENT_ID,
            "noodle",
            "Wonton Noodles"
        )
    )

    t3 = asyncio.create_task(
        send_order_to_kitchen(
            MY_STUDENT_ID,
            "steak",
            "Sizzling Steak"
        )
    )

    # รอจนกว่าจะมีงานแรกเสร็จ
    done, pending = await asyncio.wait(
        {t1, t2, t3},
        return_when=asyncio.FIRST_COMPLETED
    )

    # แสดงงานที่เสร็จก่อน
    for task in done:
        result = task.result()
        print(
            f"{ctime()} | Winner served first! "
            f"Shop: {result['shop']} | Menu: {result['menu']}"
        )

    # ยกเลิกงานที่เหลือ
    print(f"{ctime()} | Cleaning up: Canceling {len(pending)} remaining pending orders...")

    for task in pending:
        task.cancel()

    elapsed = perf_counter() - start_time
    print(f"{ctime()} | Total waiting time for the first dish: {elapsed:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())