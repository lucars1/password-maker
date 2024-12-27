import pyautogui
import time
Times = 0
cool = []
while Times < 100:
    pos = pyautogui.position()
    #print(pos)
    cool.append(pos[0])
    cool.append(pos[1])
    time.sleep(0.02)
    Times += 1
    
chicken_cokco = cool[0] * cool[2]
if chicken_cokco > 50000:
    chicken_cokco = chicken_cokco * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

chicken_str = str(chicken_cokco)

if cool[10] < 1000:
    chicken_str = chicken_str + '!*~)'
if chicken_cokco > 1000000:
    chicken_str = chicken_str + '(!)$'
if cool[19] > 500:
    chicken_str = chicken_str + '(Ili'
if cool[19] < 500:
    chicken_str = chicken_str + '%^*'
else:
    chicken_str = chicken_str + '!(@'

if cool[100] != cool[98]:
    randomvar =+ cool[77] / cool[1]
    Ba = chicken_str
    randomvarstr = str(randomvar)
    chicken_str = Ba + randomvarstr

print('here is the password:', chicken_str)
print('password is:', len(chicken_str), "digits long")