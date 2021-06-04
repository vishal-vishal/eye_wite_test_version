import time
from selenium import webdriver
import os

# User Input data
file_name = input("Enter file which is content URLs : ")
dir_name = input("Enter directory name where is store the files : ")

# Create Directory
try:
    os.system(f"mkdir {dir_name}")
except:
    print("Directory is already exist and it overwrite the directory content")

# Store the urls is list
urls = []

# Open file
file_data = open(file_name, 'r')

# Read the Directory content
for i in file_data:
    urls.append(i)

# Print message on the screen
print(f"Screenshots store on the {dir_name}.")
print(f"It maybe takes {(len(urls)*30)/60} minutes.")
print("It is running.......................")

# Takes Screenshots
counter = 0
for url in urls:
    counter += 1
    t = time.time()
    driver = webdriver.Chrome("C:/Users/Asus/chromedriver.exe")
    driver.set_page_load_timeout(30)
    try:
        driver.get(url)
        time.sleep(1)
        pic_name = f"{dir_name}/{url.replace('/','').replace(':','_').rstrip()}-v34sdf543.png"
        print(pic_name)
        time.sleep(1)
        driver.save_screenshot(pic_name)
        driver.close()
    except:
        print(f"Time Out Error is occurred in {url}")
        driver.close()
    # print(f"{counter} ==> {url} ==> TimeTakse {time.time() - t }")

print("It successfully completed")