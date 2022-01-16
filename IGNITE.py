import os
import webbrowser
import pdb

Used_URLS = input("What URL(s) do you want to use? : ")
print("This is what you are going to use: " + Used_URLS)
print("URL(s) have been saved in the file called: 'URL.txt'")

with open('URL.txt', 'w') as file:
    urls = file.write(Used_URLS)

with open('URL.txt', 'r') as readfile:
    # print(readfile.read())
    all_urls = readfile.read().split(' ')
    for each_url in all_urls:
        print(each_url)
        webbrowser.open_new_tab(each_url.strip())
