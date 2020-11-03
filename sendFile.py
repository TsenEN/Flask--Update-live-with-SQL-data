import requests 
seeds = [
	{'seedID': 9527 ,'x' : 111.111 ,'y' : 111.22222 ,'z' : 22222.222 , 'n' : 22.2222222, 'e' : '' ,'battery' : 22 , 'status' : 1},
	
	{'seedID': 7789 ,'x' : 223 ,'y' : 1.235 ,'z' : 2.99 , 'n' : 23.2222222, 'e' : 23.1111111,'battery' : 33 , 'status' : 1}
	
	]
r = requests.post('http://0.0.0.0:1000/',json = seeds)
print(r.text)