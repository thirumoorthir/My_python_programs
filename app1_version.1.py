#!/usr/bin/python
# This is an simple python program to read content in an file and compute it and stores result.
import decimal
def amount_hand():
        print "The amount in your hand is %d" %balance
def write():
        f = open('balance1','w')  #program open's balance file and write data output to it .
        f.write('%d' %balance)
        f.close()
        
while True:
    choice = raw_input("What you want to do\n 1.For add amount \n 2.For subtract\n 3.For print balance \n 4.For exit this program \n Enter your choice:")
    f = open('balance1','r')
    num_lines = sum(1 for line in open('balance1'))
    print "There are %d number of lines in balance file"%num_lines
    balance=f.read()
    balance = int (balance)
    if choice == '1':
        amount = raw_input("Enter amount to add:")
        descrb = raw_input("Enter description for that income:")
        amount = int (amount)
        balance = amount + balance
        write()
        amount_hand()
    elif choice == '2':
        amount = raw_input ( "Enter amount to subtract:")
        descrb1 = raw_input("Enter description for that expence:")
        amount = float (amount)
        balance = balance - amount
        write()
        amount_hand()
    elif choice =='3':
        amount_hand()
    elif choice =='4':
            break

