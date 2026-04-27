# fetch_api.py
import requests

def fetch_data(url):
    # 1. Send the request (发送请求)
    response = requests.get(url)

    # 2. Check if the request was successful (检查请求是否成功)
    if response.status_code == 200:
        # 3. Parse the data as JSON (将数据解析为 JSON 格式)
        data = response.json()
        print("Data fetched successfully.")
        return data
    else:
        print(f"Failed to fetch. Error code: {response.status_code}")
        return None

if __name__ == "__main__":
    test_url = "https://api.github.com"
    fetch_data(test_url)
