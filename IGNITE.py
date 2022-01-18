import os
import webbrowser


def new_or_old():
    Question_xtxt_exists = input(
        "Do you want to configure new URLS? (y/n) default = n: ").lower().strip()

    if Question_xtxt_exists == "y":
        Used_URLS = input("What URL(s) do you want to use? : ")
        print("This is what you are going to use: " + Used_URLS)
        print("URL(s) have been saved in the file called: 'URL.txt'")
        with open('URL.txt', 'w') as file:
            urls = file.write(Used_URLS)
            return True

    elif Question_xtxt_exists[0] == "n":
        with open('URL.txt', 'r') as readfile:
            all_urls = readfile.read().split(' ')
            for each_url in all_urls:
                print(each_url)
                webbrowser.open_new_tab(each_url.strip())
            return False


new_or_old()
