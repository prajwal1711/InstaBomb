#welcome to InstaBomb

from selenium import webdriver                                 #importing modules
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

print("Welcome to InstaBomb!")    #introduction
print("Two modes are available.")
print("1. Send the same text multiple times")
print("2. Send a paragraph (or a novel) word by word (this is real fun)")
print("Choose an option (1 or 2) : ")  #Two options given
opt=int(input())   #choose an option

if opt==1:         #if option 1 is chosen
    msg=input("Enter message: ")
    count=int(input("Enter count: "))
    print("Press any key to confirm")
#-------------------------------------------------------------------#
    driver.get("https://www.instagram.com/")    #open instagram (login needed)
    driver.maximize_window()                    #maximise the window
    print("Enter profile name: ")              #Entering profile name
    proname=input()                            #taking the input
    driver.get("https://www.instagram.com/{}/".format(proname))   #opening the entered profile

    driver.implicitly_wait(5)                  #wait

    target=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/button")               #searching for the message button
    target.click()

    driver.implicitly_wait(5)                 #wait

    msg_box=driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")      #finding the text area

    driver.implicitly_wait(5)                 #wait

    for index in range(count):                #loop for sending message multiple times
        msg_box.send_keys(msg)
        driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()    #clicking send button
#==================================== end of case 1 ============================================#
if opt==2:
    driver.get("https://www.instagram.com/")    #open instagram (login needed)
    driver.maximize_window()                    #maximise the window
    print("Enter profile name: ")              #Entering profile name
    proname=input()                            #taking the input
    driver.get("https://www.instagram.com/{}/".format(proname))   #opening the entered profile
    driver.implicitly_wait(5)                  #wait

    target=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/button")                       #searching for the message button
    target.click()

    driver.implicitly_wait(5)                 #wait

    msg_box=driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")      #finding the text area

    driver.implicitly_wait(5)                 #wait
    
    with open('sentence.txt','r') as f:
      for line in f:
        for word in line.split():
          msg_box.send_keys(word)
          driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
        
#============================== end of case 2 =================================================#

else:             #invalid option choosen
    print("Option not valid. Try again.")

#============================== end of case 3 =================================================#
    
print("Success")                          #end of program. YESSSSS


