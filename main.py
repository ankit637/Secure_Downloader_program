import hashlib
from pytube import YouTube
import sys

def generate_md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

# Example usage
user_hash = "447d2c8dc25efbc493788a322f1a00e7"
passwd_hash = "827ccb0eea8a706c4c34a16891f84e7b"

print('''
        Welcome To Youtube Automation Downloader
        Rules:
              You have to Login To Use This Feature
              Credentials: https://github.com/ankit637/Secure-Coding/blob/main/create-user.py
        Usage:
              Write Multiple or Single Youtube Videos URLs as you want in "urls.txt"
              Method: URLs in "urls.txt" file should be line-by-line
        Commands:
                 pip install -r requirements.txt
                 python main.py
''')

log_user_hash = input("Enter The Username:")[:5]
user_md5_hash = generate_md5_hash(log_user_hash)

pass_user_hash = input("Enter The Password:")[:5]
passwd_md5_hash = generate_md5_hash(pass_user_hash)


# Check if the entered MD5 hash values match the stored ones
if user_hash == user_md5_hash and passwd_md5_hash == passwd_hash:
    print("Correct! You are a root-user & Starting Youtube Automation Downloader")
    def download_video(link, index):
        try:
            youtube_object = YouTube(link)
            video_stream = youtube_object.streams.get_highest_resolution()

            print(f"Downloading video {index}: {youtube_object.title}")

            video_stream.download(filename=f'{youtube_object.title}.mp4')
            print(f"\nVideo {index} Downloaded successfully!")
        except Exception as e:
            print(f"\nAn error has occurred for video {index}: {e}")


    if __name__ == "__main__":

        #    file_path = input("Enter the path to the file containing video URLs: ")

        try:
            with open('urls.txt', 'r') as file:
                video_urls = file.read().splitlines()

            if not video_urls:
                print("No video URLs found in the file.")
            else:
                for i, url in enumerate(video_urls, start=1):
                    download_video(url, i)
        except FileNotFoundError:
            print("File not found. Please provide a valid file path.")
        except Exception as e:
            print(f"An error occurred: {e}")
else:
    print("Wrong! You are not a root-user")

# print(user_md5_hash)
