from machine import Pin
from time import sleep
led = Pin('LED', Pin.OUT)

timeunit = 0.12

dit = timeunit
dah = timeunit*3
cspace = timeunit*3
wspace = timeunit*7

alphaturple = (".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..")
numberturple = ("-----",".----","..---","...---","....-",".....","-....","--...","---..","----.")

stringtoconvert = "Hello world"
def sendchar(morse): #function declaration
    print (c + " " + morse)
    for x in morse:
        led.value(1)
        if x == ".":
            sleep(dit)
        elif x == "-":
            sleep(dah)
        led.value(0)
        sleep(dit)

print(stringtoconvert)
ucstring = stringtoconvert.upper() #convert to uppercase
print(ucstring)
print("Sending Message...")
sleep(2)
for c in ucstring: #iterate through our uppcase string
    charascii = ord(c) #obtain ascii code of char
    if 65 <= charascii <= 90: #work with Alphas
        thechar = alphaturple[charascii-65] #'cos A = ascii 65, get letter from turple
        sendchar(thechar) #run function
        sleep(cspace) #space between characters
    if 48 <= charascii <= 57: #work with Numbers
        thechar = numberturple[charascii-48] #'cos 0 = ascii 48
        sendchar(thechar) #run function
        sleep(cspace) #space between characters
    if charascii == 32: #if space
        print(" ")
        sleep(wspace) #space between words
print("Message Sent.")