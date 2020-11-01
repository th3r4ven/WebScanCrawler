#  Copyright (c) 2020.
#  This code was designed and created by TH3R4VEN, its use is encouraged for academic and professional purposes.
#  I am not responsible for improper or illegal uses
#  Follow me on GitHub: https://github.com/th3r4ven

from sd_crawler import response


def file_scanner(url):
    print("\n[+]\tSearching for files and directories on the target web site.......")
    print("-------------------------------------------------------------------------------------------")

    with open("wordlist/files_dic_default.txt", "r") as wordlist_file:
        for line in wordlist_file:
            line = line.strip()
            test_url = url + "/" + line

            resp = response(test_url)
            if resp or resp.status_code == 403:
                print("[+]\tFile/Directory " + test_url + " returned status code " + str(resp.status_code))
