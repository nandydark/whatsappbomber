#!/usr/bin/python3

##### Whatsapp Ddoser by NandyDark #####

from selenium import webdriver
import time
import sys
import os

###########################

os.system("clear")

###########################
print ("                                                                                                 ")
print ("  █▀▀▄ █▀▀█ █▀▀▄ █▀▀▄ █░░█ █▀▀▄ █▀▀█ █▀▀█ █░█                                                    ")
print ("  █░░█ █▄▄█ █░░█ █░░█ █▄▄█ █░░█ █▄▄█ █▄▄▀ █▀▄                                                    ")
print ("  ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀░ ▄▄▄█ ▀▀▀░ ▀░░▀ ▀░▀▀ ▀░▀                                                    ")
print ("                                                                                                 ")
print ("IF YOU WILL COPY MY CODE WITHOUT GIVING CREDITS THEN YOU ARE THE BIGGEST GAY ON THIS UNIVERSE  \n")

time.sleep(2)

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

name = input("\n Enter Target Name: ")

time.sleep(1)

msg = input("\n Enter Your Message: ")

time.sleep(1)

count = int(input("\n Enter Number of Messages: "))

time.sleep(1)

os.system("clear")

input(" Press Enter To Continue")

time.sleep(1)

os.system("clear")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name("_3u328")

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name("_3M-N-")
    button.click()
