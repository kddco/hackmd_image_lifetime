import requests

def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Successful request for {url}")
    except requests.exceptions.RequestException as e:
        print(f"Failed request for {url}: {e}")
        with open("error.txt", "a+") as error_file:
            error_file.write(url + "\n")

def process_image_urls(file_path):
    with open(file_path, "r") as file:
        for line in file:
            url = line.strip()
            make_request(url)

file_path = "imgurl.txt"
process_image_urls(file_path)
