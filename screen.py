import pyautogui,time
delay=int(input('DELAY time: '))
with open('g.txt','r') as f:
	data = f.read().strip()
count=int(data)+1
print(delay,'s')
path=f'screen{count}.jpg'
time.sleep(delay)
print("SCREEN!")
pyautogui.screenshot('img\\'+path)
with open('g.txt','w') as f:
	f.write(str(count))