#使用 time 模块来实现秒表功能
import time
print("Enter:start,ctrl+c:stop.")
while True:
	input("Please click Enter:")
	start=time.time()
	try:
		while True:
			print("timing:" ,round(time.time() - start,1),"s")
			time.sleep(1)
	except KeyboardInterrupt:
		print("stop")
		end = time.time()
		print("The total time is:",round(end-start,2),"s")
		break