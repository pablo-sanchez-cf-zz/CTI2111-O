cookies = 10
hungry = True

while hungry == True:
    if cookies >= 1:
        print "You have eaten a cookie"
        cookies -= 1
        print "there are " + str(cookies) + " left"
    else:
        print "You've eaten all the cookies."
        break