import random
start = input("請決定隨機數字範圍開始值:")
end = input("請決定隨機數字範圍結束值:")
start=int(start)
end=int(end)
r = random.randint(start, end)
count = 0
while True:
	count+=1
	num = input("請猜數字:")
	num=int(num)
	
	num = int(num)
	if num == r:
		print("你猜對了")
		print("這是你猜的第", count, "次")
		break
	elif num >r :
		print("你猜得太大囉")
	elif num < r:
		print("你猜得太小囉")
	print("這是你猜的第", count, "次")