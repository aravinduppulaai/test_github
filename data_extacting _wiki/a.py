
import time

def wait_seconds(seconds):
    print(f"Waiting for {seconds} seconds...")
    time.sleep(seconds)
    print("Done waiting!")

if __name__ == "__main__":
    wait_seconds(2)