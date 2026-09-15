import requests


def check_connectivity(url: str = "https://api.github.com") -> None:
    response = requests.get(url, timeout=5)
    print(f"GET {url} -> {response.status_code}")
    print(f"Python dependency 'requests' resolved and working correctly.")


if __name__ == "__main__":
    check_connectivity()