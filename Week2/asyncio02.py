# Program 3: The Event Loop (asyncio.run)
# Concept: Using the Event Loop to actually execute a Coroutine Object.
import asyncio

async def greet():
    print("Hello!")

# Calling the coroutine function creates a "Coroutine Object".
coro_object = greet()

# Notice that "Hello!" is NOT printed yet!
print(type(coro_object)) # Output: <class 'coroutine'>

#To prevent Python from throwing a warning, we must close or run it. I
#We will learn how to run it in the next file.
coro_object.close()
