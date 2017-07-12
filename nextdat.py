print("Input a year:")
yr = input()
print("Input a month:")
mon = input()
print("Input a day:")
day = input()
nxday = day+1 
if(mon == [1,3,5,7,8,10,12] and day == 31):
	nxmon = mon+1
	nxday = 1
elif(mon == 2 and day == 28):
	nxmon = mon+1
	nxday = 1
else: 
	if(day == 30):
		nxmon = mon +1
		nxday = 1
	else:
		nxmon = mon
if(day == 31 and mon == 12):
	nxyr = yr +1
	nxmon = 1
	nxday = 1
else:
	nxyr = yr
print('The next date is [yyyy-mm-dd] '+str(nxyr)+'-'+str(nxmon)+'-'+str(nxday))