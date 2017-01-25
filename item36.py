"""
Python 2.7.13
Georgia Barnes
item 36
"""

import math

#list
asciiList = ['0 = NUL','1 = SOH','2 = STX','3 = ETX','4 = EOT','5 = ENA','6 = ACK','7 = BEL','8 = BS','9 = TAB',
         '10 = LF','11 = VT','12 = FF','13 = CR','14 = SO','15 = SI','16 = DLE','17 = DC1','18 = DC2','19 = DC3','20 = DC4',
         '21 = NAK','22 = SYN','23 = ETB','24 = CAN','25 = EM','26 = SUB','27 = ESC','28 = FS','29 = GS','30 = RS',
         '31 = US','32 = (space)','33 = !','34 = "','35 = #','36 = $','37 = %','38 = &','39 = \'','40 = (',
         '41 = )','42 = *','43 = +','44 = ,','45 = =','46 = .','47 = /','48 = 0','49 = 1','50 = 2',
         '51 = 3','52 = 4','53 = 5','54 = 6','55 = 7','56 = 8','57 = 9','58 = :','59 = ;','60 = <',
         '61 = =','62 = >','63 = ?','64 = @','65 = A','66 = B','67 = C','68 = D','69 = E','70 = F',
         '71 = G','72 = H','73 = I','74 = J','75 = K','76 = L','77 = M','78 = N','79 = O','80 = P',
         '81 = Q','82 = R','83 = S','84 = T','85 = U','86 = V','87 = W','88 = X','89 = Y','90 = Z',
         '91 = [','92 = \\','93 = ]','94 = ^','95 = _',"96 = '",'97 = a','98 = b','99 = c','100 = d',
         '101 = e','102 = f','103 = g','104 = h','105 = i','106 = j','107 = k','108 = l','109 = m','110 = n',
         '111 = o','112 = p','113 = q','114 = r','115 = s','116 = t','117 = u','118 = v','119 = w','120 = x',
         '121 = y','122 = z','123 = {','124 = |','125 = }','126 = ~','127 = DEL']

#tuple
answerKey = [(1,2),(2,1),(3,288)]
answers = [2,1,288]

#assign int to variable
def start(name=""):
    stop = True
    #use of while loop
    while stop:
        #assign string to variable
        name = raw_input("\nWhat is your name?").capitalize()
        if name != "":
            #use of .format()
            print ("\nWelcome, {}!").format(name)
            choices(name)
            stop = False
        return name

def choices(name):
    print ("\nWhat would you like to do, {}?".format(name))
    choice = raw_input("a. Math! \nb. Find out if you can do math! \nc.See the ASCII VALUES! \nd.Tell me your secrets! \n(a/b/c/d) :").lower()
    #if/elif/else        
    if choice == 'a':
        calculator(name)
    elif choice == 'b':
        mathTest(name)
    elif choice == 'c':
        ascii(name)
    elif choice =='d':
        secrets(name)
    else:
        print ("\nI'm sorry, I don't understand that command...")

def calculator(name):
    #float variables
    value1 = float(raw_input("\nGive me a number: "))
    value2 = float(raw_input ("\nGive me another number: "))
    operator = raw_input("\nWhat should I do with these numbers? \na.add \nb.subtract \nc.multiply \nd.divide \n(a/b/c/d) :").lower()
    if operator == 'a':
            # +
            value3 = value1 + value2
            print ("\n {} + {} = {} ".format(value1,value2,value3))
    elif operator =='b':
            # -
            value3 = (value1 - value2)
            print ("\n {} - {} = {} ".format(value1,value2,value3))
    elif operator == 'c':
            # *
            value3 = (value1 * value2)
            print ("\n {} * {} = {} ".format(value1,value2,value3))
    elif operator == 'd':
            # / and %
            value3 = math.floor(value1 / value2)
            print ("\n {} / {} = {} , Remainder: {}".format(value1,value2,value3,(value1 % value2)))
    else:
            print "Please enter a , b, c, or d."
    choice = raw_input("\nWhould you like to a. Do more math or b. return to the main menu? \n(a/b) :")
    if choice == 'a':
            calculator(name)
    else:
            choices(name)

def mathTest(name):
    answer0 = int(raw_input("\nWhat is 1 + 1? :"))
    answer1 = int(raw_input("\nWhat is 3 - 2? :"))
    answer2 = int(raw_input("\nWhat is 48/2(9+3)? "))
    #logial operators
    if (answer0 == answers[0]) and (answer1 == answers[1]) and (answer2 == answers[2]):
        print ("\nCongratulations {}, you can do math!".format(name))
        mathAnswers(name)
    elif (answer0 == answers[0]) or (answer1 == answers[1]) or (answer2 == answers[2]):
        print("\nSo close! You don't quite know math yet...")
        mathAnswers(name)
    else:
        print("\nYikes, you need to brush up on your math.")
        mathAnswers(name)       

def mathAnswers(name):
    print "\nThe correct answers were: "
    #for loop to print tuple
    for a,b in answerKey:
        print "Answer", a,':',b
    out = raw_input("\nEnter 'm' to return to the menu ").lower()
    if out =='m':
        choices(name)
    else:
        choices(name)
    

def ascii(name):
    #for loop to print list
    for i in asciiList:
        print i
    out = raw_input("\nEnter 'm' to return to the menu ").lower()
    if out =='m':
        choices(name)
    else:
        choices(name)

#return string variabe
def secrets(name,secret=""):
    secret = raw_input("\nWhat's your secret? I promise I won't tell anyone... ")
    tellSecret(name,secret)
    return secret

#print returned variable to shell
def tellSecret(name, secret):
    out = raw_input ("\nHey, World! Guess what? {} said \"{}\" \nI'm sorry, that secret was so juicy, I couldn't help myself. \nPress 'm' to return to the menu ".format(name,secret))
    if out =='m':
        choices(name)
    else:
        choices(name)

if __name__== "__main__":
    start()
