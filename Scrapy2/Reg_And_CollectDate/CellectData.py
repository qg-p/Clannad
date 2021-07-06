 #encoding = utf-8
import requests
import re
import time
import os

def find_content(url):
	#print(url)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50',
	}
	while 1:
			response_2=requests.get(url,headers=headers)
			if '503 Service Temporarily Unavailable' not in response_2.text:
				break
			else:
				print('漏数据了，3 秒之后继续爬')
				sleep(3)
	response_2.encoding='UTF-8'
	response = str(response_2.text)
	reg_questions = '<title>每日新闻播报（(.*)） - Chinadaily.com.cn</title>'
	reg_answers = '>&gt;(.*?)<'
	questions = re.findall(reg_questions,response)
	answers = re.findall(reg_answers, response)
	#print(answers)
	question = questions[0]
	if len(answers) != 0:
		answer = ";".join(answers)
		with open ('C:/Users/dell/Desktop/Clannad/chatbot1/training_data/MyData.txt','a+',encoding="UTF-8") as f:#C:\Users\dell\Desktop\Clannad\chatbot1\training_data
			f.write('What happened in ' + question+'?'+'\n')
			f.write(answer+'\n')
			f.write('Good!'+'\n')
	

def find_html(html_url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50',
	}
	while 1:
			response_2=requests.get(html_url,headers=headers)
			if '503 Service Temporarily Unavailable' not in response_2.text:
				break
			else:
				print('漏数据了，3 秒之后继续爬')
				sleep(3)
	response_2.encoding='UTF-8'
	response = str(response_2.text)
	reg_url = 'href=\"(.*)\"><img'
	web_url = re.findall(reg_url, response)
	for i in web_url:
		find_content('https:'+i)


for i in range(1,11):#1,11
	total_url = 'https://language.chinadaily.com.cn/audio_cd/page_'+str(i)+'.html'
	find_html(total_url)
	#print(total_url)