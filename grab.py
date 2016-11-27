import grab

start_url = 'http://kinogo.club'

g = grab.Grab(log_file='out.html')
g.go(start_url)

g.xpath_text('//span[@class="leftblok_contener2"]')