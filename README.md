# Crawl
Python webcrawler to automate events

This tool assumes you have the Selenium/Python3 enviroment installed already. 

- Just a Simple, Lightweight automated webcrawler.

#Tutorial

1.  Download ./chromedriver.sh to disered path of tool.
	Copy & Paste this in your terminal to download the latest chromedriver, this will download the lastest release and automatically extract zip.
		
		LATEST_VERSION=$(curl -s 
		https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && 
		wget -O /tmp/chromedriver.zip 
		https://chromedriver.storage.googleapis.com/$LATEST_VERSION/chromedriver_linux64.zip
 		&& sudo unzip /tmp/chromedriver.zip chromedriver -d 
		/usr/local/bin/;

1.  Download the User-Agents.txt file into this tools directory.
	
2.  Place path to "User-Agents.txt in this field. 
		f_name = open('User-Agents.txt', 'r')

3.  Place target website in between the " ". 
		web.get("http://www.websitehere.com")		

4.  Place website title in between the " ".
		assert "Web Title" in web.title

5.  Place the 'Xpath' to be clicked on/used between the ' '. 
		element = web.find_element_by_xpath('')



#How To Use

Just run the script with python3 .chromedriver.sh ./Crawl.py


#Thats It. =] 

This is my first script in python, so be easy on me! XP


#Disclaimer 

This tool is for education purposes only and is no way intended to do harm or perform illegal activities. 
