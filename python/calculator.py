
import re


def sum(a,b):

    return float(a)+float(b)

def check_for_number(givennumber):
    num_format = re.compile("(\d+(?:\.\d+)?)")
    isnumber = re.match(num_format,givennumber)
    
    if isnumber:
        return givennumber
    else:
        raise "Error: Entered input is not a valid digit"

def ask_user():
    x = input("Enter first number:")
    check_for_number(x)

    y = input ("Enter second number:")
    check_for_number(y)
    return x,y


# --==Main==--

from optparse import OptionParser

parser = OptionParser()

parser.add_option('-o', type='choice', choices=['add', 'sub', 'mul', 'div'])

options, args = parser.parse_args()

print('Operation to be performed:', options.o)
    
if options.o == 'add':
    a,b = ask_user()
    print("RESULT: ",sum(a,b))

    
