### Scrapy
+ install :`pip install Scrapy`
+ `Detected a distutils installed project ('six') which we cannot uninstall. The metadata provided by distutils does not contain a list of files which have been installed, so pip does not know which files to uninstall.`
resolve :`pip install Scrapy --upgrade --ignore-installed six`
+ `ImportError: cannot import name xmlrpc_client`
resolve :
`sudo rm -rf /Library/Python/2.7/site-packages/six*`
`sudo rm -rf /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/six*`
`sudo pip install six`

+ Creating a project
`scrapy startproject tutorial`

###  Beautiful Soup
<http://cuiqingcai.com/1319.html>
<http://blog.csdn.net/watsy/article/details/14161201>
<http://www.crummy.com/software/BeautifulSoup/bs4/doc/>

 很多标签解析,跟jsoup有点像
 