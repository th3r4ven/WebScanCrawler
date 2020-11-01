#  Copyright (c) 2020.
#  This code was designed and created by TH3R4VEN, its use is encouraged for academic and professional purposes.
#  I am not responsible for improper or illegal uses
#  Follow me on GitHub: https://github.com/th3r4ven

import requests


def validrequest(url):
    print("[+]\tSending requests to the page...")
    try:
        get_response = requests.get(url)

        if get_response.status_code == 200:
            downloader(url, get_response)
        else:
            print("[-]\tThe page is unavailable or the URL given is incorrect")

    except requests.exceptions.ConnectionError:
        print("[-]\tThe page is unavailable or the URL given is incorrect")
        pass


def downloader(url, get_response):
    print("[+]\tRequest successful with status code 200")
    print("[+]\tDownloading page...")
    file_name = url.split("/")[-1]
    file_name = "downloads/" + file_name.split(".")[0]

    with open(file_name + ".html", "wt") as out_file:
        out_file.write(get_response.text)
        print("[+]\tDownloaded successfully")



