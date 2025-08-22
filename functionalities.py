import os
import json
import math
import statistics
import requests
from typing import List, Dict, Any, Optional


def read_json_file(filepath: str) -> Dict[str, Any]:
    """Read JSON from a file and return a dictionary."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json_file(filepath: str, data: Dict[str, Any]) -> None:
    """Write a dictionary as JSON into a file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def calculate_statistics(numbers: List[float]) -> Dict[str, float]:
    """Return basic statistics for a list of numbers."""
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    return {
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
        "stdev": statistics.stdev(numbers) if len(numbers) > 1 else 0.0,
        "min": min(numbers),
        "max": max(numbers),
    }


def factorial(n: int) -> int:
    """Compute factorial of n recursively."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return 1 if n <= 1 else n * factorial(n - 1)


def fetch_github_user(username: str) -> Optional[Dict[str, Any]]:
    """Fetch a GitHub user's public info using GitHub API."""
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None


class DataProcessor:
    """A class to handle data processing tasks."""

    def __init__(self, name: str):
        self.name = name
        self.data: List[float] = []

    def load_data(self, numbers: List[float]) -> None:
        """Load numeric data into the processor."""
        if not all(isinstance(n, (int, float)) for n in numbers):
            raise TypeError("All elements must be int or float")
        self.data = numbers

    def normalize_data(self) -> List[float]:
        """Normalize data between 0 and 1."""
        if not self.data:
            raise ValueError("No data loaded")
        min_val, max_val = min(self.data), max(self.data)
        if min_val == max_val:
            return [0.5 for _ in self.data]
        return [(x - min_val) / (max_val - min_val) for x in self.data]

    def get_stats(self) -> Dict[str, float]:
        """Return statistics of the loaded data."""
        return calculate_statistics(self.data)

    def save_to_file(self, filepath: str) -> None:
        """Save the current data to a JSON file."""
        write_json_file(filepath, {"name": self.name, "data": self.data})


# ------------------- Example usage -------------------
if __name__ == "__main__":
    # Factorial demo
    print("Factorial of 5:", factorial(5))

    # GitHub API demo
    user_info = fetch_github_user("torvalds")
    if user_info:
        print("GitHub User:", user_info["login"], "| Public repos:", user_info["public_repos"])

    # Data processing demo
    processor = DataProcessor("SampleData")
    processor.load_data([10, 20, 30, 40, 50])
    print("Normalized data:", processor.normalize_data())
    print("Statistics:", processor.get_stats())

    # Save to file
    processor.save_to_file("output.json")
    print("Data saved to output.json")
