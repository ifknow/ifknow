# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re

blogUrl = 'https://gongshiyong.online/'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Safari/537.36'} 

def addIntro(f):
	txt = '''  
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=xindoo&show_icons=true&theme=graywhite"/>
</p>
<p align="center"> 新❤技术博主，CSDN认证博客专家 </p>  
<p align="center"> 现为某公司Java后端开发工程师，擅长 挖坑 踩坑 填坑 背锅经验 🐶   </p>  
<p align="center"> 专注于Java，	 </p>  
''' 
	f.write(txt)

def addProjectInfo(f):
	txt ='''
### 开源项目  

   
[查看更多](https://gongshiyong.online/)	 
	''' 
	f.write(txt) 


def addBlogInfo(f):  
	http = urllib3.PoolManager(num_pools=5, headers = headers)
	resp = http.request('GET', blogUrl)
	resp_tree = etree.HTML(resp.data.decode("utf-8"))
	html_data = resp_tree.xpath(".//div[@class='article-item-box csdn-tracking-statistics']/h4") 
	f.write("\n### 我的博客\n")
	cnt = 0
	for i in html_data: 
		if cnt >= 5:
			break
		title = i.xpath('./a/text()')[1].strip()
		url = i.xpath('./a/@href')[0] 
		item = '- [%s](%s)\n' % (title, url)
		f.write(item)
		cnt = cnt + 1
	f.write('\n[查看更多](https://gongshiyong.online/)\n')


if __name__=='__main__':
	f = open('README.md', 'w+')
	addIntro(f)
	f.write('<table align="center"><tr>\n')
	f.write('<td valign="top" width="50%">\n')
	addProjectInfo(f)
	f.write('\n</td>\n')
	f.write('<td valign="top" width="50%">\n')
	addBlogInfo(f)
	f.write('\n</td>\n')
	f.write('</tr></table>\n')
	f.close
