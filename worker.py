#utf-8
#python 2.7.10
#Daniel Sifton



if loopset == True:

	for url in cycle(urls):

		browser = WebDriver('firefox', reuse_browser=True)

		browser.maximize_window()

		browser.get(url[0])

		time.sleep(delayfinal)

		self.SetStatusText(str(count) +  "/" + str(num_lines) + "/" + "Infinite loop")
		
		count += 1
		
		wx.Yield()

elif loopset == False:

	for url in urls:

		browser = WebDriver('firefox', reuse_browser=True)

		browser.maximize_window()

		browser.get(url[0])

		time.sleep(delayfinal)

		browser.quit()

		self.SetStatusText(str(count) +  "/" + str(num_lines) + "/" + "Normal loop")
		
		count += 1
		
		wx.Yield()



else:
		self.SetStatusText("oops!")


