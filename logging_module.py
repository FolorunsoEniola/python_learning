import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
format=' %(asctime)s -  %(levelname)s -  %(message)s')
 
# let's you specify what details you want to see and how you want those details be displayed
# the filename lets you write to a file directly instead of showing the debug messages on the screen
# The level is to show the level of logging messgae we want to see,.Debug,.info,.warning,.critical are all levels of logging messages
# the format specifies how the log messages will be displayed, including a timestamp, the level of the message, and the actual message itself.
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(4))
logging.debug('End of program')
#the logging module showed what was going on in the program, with a timestamp and the word DEBUG indicating the level of the log message.
logging.disable(logging.CRITICAL) # This will disable the logging for all levels from critical to debug.
#it's better to be at the top of code as a comment and then uncomment when you want to call it
