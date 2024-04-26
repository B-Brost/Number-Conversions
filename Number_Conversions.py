"""
Number_Conversions.py
Brianna Brost
4/13/2023
This program converts numbers between decimal, binary, and hexadecimal. It also converts numbers between any base between 2 and 16.
"""
import math
def binToDecList(bin):
    # changes binary to decimal - did all this work to code for this so might as well use it, though had to edit it like crazy so who even knows if it was worth it. also it is 4:20AM as I code this after 12 hours of classes, so please excuse the extraneous comments :)
    # size so that last num is power of 0
    size = len(bin)-1
    dec = 0
    # makes the digits from string to ints 
    for dig in bin:
        digit=chartoHex(dig)
        # puts the 1s in the correct thousands/hundreds/etc place, 0 just is zero
        point=digit*(10**(size))
        # no power if num is 0 but makes correct if 1
        curPow = digit*size
        # another safeguard against 0 digit and putting 2 to the corect power
        dec += (digit * 2**curPow)
        # decrease size
        size-=1
    # return final value
    return dec


def decToBinList(d):
    # changes dec to binary numbers because holy moly ones and 
    bin = ''
    # sets max digit to zero cuz noone likes logs
    numDigits = 8
    for pos in range(numDigits, 0, -1):
        # have to do pos-1 because you need to start with 2**7 and end with 0
        curPow = 2**(pos-1)
        # while dec is more than the power it adds a 1 then takes away from dec
        if d>=curPow:
            bin+='1'
            d -= curPow
        else:
            # if dec not more than power then it adds a 0
            bin+='0'
    # take away all the extra beginning 0s
    for digit in bin:
        if bin[0]=='0':
            bin=bin[1:]
# returns final binary #####3
    return bin

def baseToDec(baseNum, base):
    # changes special bases to decimal
    # special case for base2 because no thanks otherwise
    if base==2:
        return binToDecList(baseNum)
    else:
        # gets num so that last place is 0
        num_dig=len(baseNum)-1
        dec=0
        for dig in baseNum:
            # change digits to ints
            digit=chartoHex(dig)
            # gets the number to add to final
            point=digit*(base**num_dig)
            # minus 1 to keep in the loop 
            num_dig-=1
            # adds the point to the eventual final answer
            dec+=point
    # returns the decimal value
        return dec
    

def decToBase(dec, base):
    # goes to the special case for 2 because idek how i would make it work for 2 along with the veeeerrry different rest of them
    if base==2:
        return decToBinList(dec)
    else:
        # setting variables
        bas = []
        decimal=dec
        str_bas=''
        while dec>base:
            # keeps dividing and inserting remainder to beginning of list to make the special base num
            dec=dec//base
            # calcs the remainer which is what is the actual number in the base case
            rem=decimal-base*dec
            # inserts it at the beginning
            bas.insert(0,rem)
            decimal=dec
        # have to insert the final remainder which is the very first num 
        bas.insert(0,dec)
        if base==16:
            # changes the nums over 9 to letters but only checks if base is 16 cuz thats the only one that uses letters so no need to waste time by doing the other ones
            # turning everything into str_bas just to make it consistant
            for digit in range(len(bas)):
                str_bas+=f"{(hextoChar(bas[digit]))}"
        else:
            for digit in range(len(bas)):
                str_bas+=f"{bas[digit]}"
        # returning the string answer
        return str_bas


def chartoHex(char):
# uses .lower to check all letters and uses index +10 to turn them into numbers
# uses index of the numbers to make sure the numbers are not strings and returns the numbers
    letters=['a','b','c','d','e','f']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    hex=''
    for i in range(len(char)):
        # allows both upper and lower case letters to be used
        element=char.lower()
        if element in letters:
            # number corresponding to letter is the index+10
            num=10+letters.index(char.lower())
            # this is the hex number
            hex=num
# if number just turn the string number into int number using index from the numbers list
        elif element in numbers:
            hex=numbers.index(char)
        else:
            # no crazy symbols
            raise ValueError("Only input digits and letters")  
    return hex

def hextoChar(hex):
# changes numbers over 10 to appropriate letters and turns numbers under 10 to strings and returns the character 
    letters=['A','B','C','D','E','F']
    char='' 
    # if less than 9 returns string number
    if hex<9:
        char=f"{hex}"
    elif hex>=10 and hex<=15:
        # if 10+ uses index of letter+10 turned into a string and returned
        index=hex-10
        char=f"{letters[index]}"
    else:
        raise ValueError("Only input digits and letters and no num over 15")  
    return char


# testing dec and base conversions
print(decToBase(25, 2))  # returns "11001"
print(decToBase(243, 16)) # returns "F3"
print(baseToDec("11001", 2)) # returns 25
print(baseToDec("F3", 16)) # returns 243
print(baseToDec("f3", 16)) # returns 243

# tests to see if chartoHex and hextoChar work
print(chartoHex("5")) # returns 5
print(chartoHex("B")) # returns 11
print(chartoHex("c")) # returns 12
print(hextoChar(5)) # returns "5"
print(hextoChar(15)) # returns "F"
