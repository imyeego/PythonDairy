import webbrowser as web
import time

i = 0
while i < 10:
	web.open_new_tab("http://www.baidu.com")
	time.sleep(5)
	i = i + 1;