#Program 3: The Event Loop (asyncio.run)
#Concept: Using the Event Loop to actually execute a Coroutine Object.
import asyncio

async def greet():
    print("Hello from the Event Loop!")

if __name__ == "__main__":
    coro_object = greet()

#asyncio.run() automatically creates an Event Loop,
#runs our coroutine object until it finishes, and shuts down the loop.
asyncio.run(coro_object)