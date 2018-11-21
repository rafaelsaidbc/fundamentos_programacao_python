import webbrowser
import time

breaks = 1
print("This program started on..." + time.ctime())
while breaks <= 3:
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=HaKIJrBENBU")
    breaks += 1
