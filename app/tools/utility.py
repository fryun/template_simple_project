
import sys
import time
from art import text2art



def starting_text():
    text = "Created By: ArdiYP"
    Art=text2art("Remark Resize","big")
    print(Art)
    print_with_delay(text,0.1)
    print()
    print()


def print_with_delay(text, delay):
    for char in text:
        print(char, end="")
        time.sleep(delay)
        sys.stdout.flush()
    time.sleep(0.3)

    
def convert_seconds_to_time(seconds:int):
    """
    Mengubah format detik menjadi jam dengan format hh:mm:ss

    Args:
    seconds: Jumlah detik

    Returns:
    String yang berisi waktu dengan format hh:mm:ss
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return time_str