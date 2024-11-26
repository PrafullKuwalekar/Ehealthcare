import requests
import subprocess
import os

def download_file_from_github(url, save_path):
    # Send a GET request to download the file
    response = requests.get(url)
    
    if response.status_code == 200:
        # Write the content to a file
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully and saved to {save_path}")
    else:
        print(f"Failed to download file. HTTP Status code: {response.status_code}")

def open_in_idle(file_path):
    # Open the downloaded file in IDLE
    subprocess.run(['python', '-m', 'idlelib.idle', file_path])

# Example Usage
github_file_url = "https://github.com/PrafullKuwalekar/Ehealthcare/blob/main/PYTHON.docx"  # Replace with actual file URL
save_path = os.path.join(os.getcwd(), "downloaded_file.py")  # Save in the current working directory

download_file_from_github(github_file_url, save_path)
open_in_idle(save_path)
