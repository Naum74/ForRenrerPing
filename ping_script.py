import requests
import logging

def ping_endpoints():
    endpoints = [
        "https://probfire-chatbot.onrender.com",  # Замените на ваш фактический URL
        "https://probfire-chatbot.onrender.com"   # Замените на ваш фактический URL
    ]

    for url in endpoints:
        try:
            response = requests.get(url, timeout=30)
            logging.info(f"Pinged {url}. Status code: {response.status_code}")
        except Exception as e:
            logging.error(f"Error pinging {url}: {e}")

def main():
    logging.basicConfig(level=logging.INFO)
    ping_endpoints()

if __name__ == "__main__":
    main()
