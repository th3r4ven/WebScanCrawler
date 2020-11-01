#  Copyright (c) 2020.
#  This code was designed and created by TH3R4VEN, its use is encouraged for academic and professional purposes.
#  I am not responsible for improper or illegal uses
#  Follow me on GitHub: https://github.com/th3r4ven

import requests


def response(url):

    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL:
        pass
    except UnicodeError:
        pass
    except KeyboardInterrupt:
        exit()


def crawler(url):
    print("\n[+]\tSearching for sub domains on the target web site.......")
    print("-------------------------------------------------------------------------")

    with open("wordlist/subdomain_default.txt", "r") as wordlist_file:
        for line in wordlist_file:
            line = line.strip()
            url = url.split("/")[-1]
            test_url = "http://" + line + "." + url

            resp = response(test_url)
            if resp:
                print("[+]\tSub domain " + test_url + " returned status code " + str(resp.status_code))


