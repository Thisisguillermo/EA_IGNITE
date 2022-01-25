#! python3 -v

import os
import webbrowser

answer = ""


def save_the_urls():
    Used_URLS = input("What URL(s) do you want to use? : ")
    print("This is what you are going to use: " + Used_URLS)
    print("URL(s) have been saved in the file called: 'URL.txt' \n")
    with open('URL.txt', 'w',) as file:
        urls = file.write(Used_URLS)
        return


def read_the_saved_urls():
    with open('URL.txt', 'r',) as readfile:
        all_urls = readfile.read().split(' ')
        for each_url in all_urls:
            print(each_url)
            webbrowser.open_new_tab(each_url.strip())


while answer != "0":
    user_selection = input(
        "Please choose a number: \n (1) To (re)configure the URLS \n (2) Run the program \n").lower().strip()
    if user_selection == "1":
        save_the_urls()

    elif user_selection == "2":
        read_the_saved_urls()
        break
    else:
        read_the_saved_urls()
        break