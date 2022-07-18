#==============================================================================
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
# ================== HackerRank =======================================


def timeConversion(s):
    # Write your code here
    h, m, s = s.split(":")
    print(h, m, s)
    if (s[2:4] == "AM"):
        print("Am condition")
        if(int(h) <= 12):
            print("------")
            if (int(h) == 12):
                if (int(m)>= 1):
                    H = int(h)-12
                    print(str(H)+":"+m+":"+s[0:2]) 
                else:
                    H = int(h)-12
                    print(str(H)+":"+m+":"+s[0:2])
            elif(int(h)>12):
                print(str(h)+":"+m+":"+s[0:2])
                    
    elif (s[2:4] == "PM"):
        print ("pm condition"+h)
        if(int(h)<=12):
            print('-----')
            if (int(h) == 12):
               print(str(h)+":"+m+":"+s[0:2])
                    
            else:
                H = int(h)+12
                print (str(H)+":"+m+":"+s[0:2])



timeConversion('12:00:00AM')