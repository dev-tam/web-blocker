import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "fb.com", "www.chess.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 1) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          16):
        print("Working hours...")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass  # dont do anything if already added
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Fun hours...")
    time.sleep(5)
