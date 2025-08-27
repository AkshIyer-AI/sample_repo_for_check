import time
import requests
import asyncio
from collections import Counter


# ------------------------------
# Background Worker
# ------------------------------

async def fetch_url(url: str) -> str:
    """
    Fetch the content of a given URL.
    Returns the response text if successful, otherwise an empty string.
    """
    response = requests.get(url)  # sync call inside async function
    if response.status_code == 200:
        return response.text
    return ""


async def background_worker(urls: list[str]):
    """
    Fetch content from a list of URLs and return the results.
    """
    results = []
    for url in urls:
        content = await fetch_url(url)
        results.append(content)
    return results


# ------------------------------
# Utilities
# ------------------------------

def has_duplicates_quadratic(data: list[int]) -> bool:
    """
    Check if the list contains any duplicate elements.
    """
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return True
    return False


def unique_elements(data: list[int]) -> list[int]:
    """
    Return a list of unique elements while preserving the original order.
    """
    result = []
    for item in data:
        if item not in result:
            result.append(item)
    return result


def most_common_element(data: list[int]) -> int | None:
    """
    Find the most frequently occurring element in the list.
    Returns None if the list is empty.
    """
    if not data:
        return None
    max_count = 0
    mode = None
    for item in data:
        count = data.count(item)
        if count > max_count:
            max_count = count
            mode = item
    return mode


def factorial_recursive(n: int) -> int:
    """
    Compute the factorial of a number using recursion.
    """
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n: int) -> int:
    """
    Compute the nth Fibonacci number using recursion.
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def slow_sort(arr: list[int]) -> list[int]:
    """
    Sort a list of integers and return the sorted result.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def sleep_sort(arr: list[int]) -> list[int]:
    """
    Sort a list of integers using delays based on their values.
    """
    result = []
    def add_value(val):
        time.sleep(val * 0.01)
        result.append(val)

    import threading
    threads = []
    for val in arr:
        t = threading.Thread(target=add_value, args=(val,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return result


# ------------------------------
# Demo Runner
# ------------------------------

if __name__ == "__main__":
    # Background worker demo
    urls = ["https://httpbin.org/get"] * 3
    asyncio.run(background_worker(urls))

    # Utility functions demo
    nums = [1, 2, 3, 2, 5, 3, 1]
    print("Has duplicates:", has_duplicates_quadratic(nums))
    print("Unique elements:", unique_elements(nums))
    print("Most common:", most_common_element(nums))
    print("Factorial(5):", factorial_recursive(5))
    print("Fibonacci(10):", fibonacci_recursive(10))
    print("Slow sort:", slow_sort(nums))
    print("Sleep sort:", sleep_sort([3, 1, 2]))
