import re

def match(pattern, string):
	g = re.finditer(pattern, string)
	result=[]
	for m in g:
		result.append(m.group())
	return result

def getip(string): # ip addr
	p1='((2(5[0-5]|[0-4][0-9]))|[0-1]?[0-9]{1,2})'
	pattern = p1+'\.'+p1+'\.'+p1+'\.'+p1
	return match(pattern, string)

def gettime(string): # time stamp
	ptntime='\d\d:\d\d:\d\d \+\d\d\d\d'
	pattern = '\[\d\d/[A-Z][a-z][a-z]/((20)|(19))\d\d:'+ptntime+'\]'#"18/Sep/2013:06:..........."
	return match(pattern, string)
	
def geturl(string): # ip addr
	pattern = '(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?'
	return match(pattern, string)

# GET:
# - ip addr
# - time stamp
# - url (like http://...)
if __name__ == '__main__':
	log='day2/regexp/raw_log.txt'
	file=open(log, 'r')
	string=file.read()
	#print(string)
	ipaddrs=getip(string)
	#print(ipaddrs)
	timestamps=gettime(string)
	#print(timestamps)
	urls=geturl(string)
	#print(urls)

	print("IP address:")
	for _ in ipaddrs:
		print('\t'+_)
	print()
	print("timestamps:")
	for _ in timestamps:
		print('\t'+_)
	print()
	print("urls:")
	for _ in urls:
		print('\t'+_)
