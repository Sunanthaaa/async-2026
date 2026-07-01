#Program 4: The await Keyword
#Concept: Pausing a coroutine to let another operation finish using await.
import asyncio
from time import ctime

async def main():
    print(f"{ctime()} -> Task Started")

#'await' tells the Event Loop: "I am waiting for this non-blocking sleep.
#You can go check and run other tasks if available."
    await asyncio.sleep(1)

print(f"{ctime()} -> Task Finished")

if __name__ == "__main__":
    asyncio.run(main())