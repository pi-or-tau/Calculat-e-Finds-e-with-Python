import math
import decimal
import sys


def ask_user(boolean):
    if (boolean == True):                                                    #If True: Time n should be increased; If False: Decimal Places
        response = int(input("How many times should n be increased? "))
        if (response > 0):
            n = response
            return n
        else:
            print ("Wrong value: Only the natural numbers accepted.")
            sys.exit()
    elif (boolean == False):
        response = int(input("How many decimal places should be calculated? "))
        if (response > 0):
            e = response
            return e
        else:
            print ("Wrong value: Only the natural numbers accepted.")
            sys.exit()

def main():
    number_trials = ask_user(True)
    decimal_places = ask_user(False)
    n = 0
    e = 0
    old_percentage = None
    decimal.getcontext().prec = decimal_places
    while(n <= number_trials):
        e += (decimal.Decimal(1)/(math.factorial(n)))
        percentage = int(((float(n)/number_trials)*100))
        if (percentage != old_percentage):
            print percentage,"%"
            old_percentage = percentage    
        n += 1
    print "Changing to string."
    e_string = str(e)
    print "Writing to file."
    with open("C:\Users\Collin\Desktop\e_python2.txt","w") as f:
        f.write(e_string)
    f.close()
    print "Done!"
    
main()