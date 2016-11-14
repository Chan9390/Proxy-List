import requests
from time import sleep

proxylist = [
# Numbers
"http://5proxy.xyz",
"http://4everproxy.com",
"http://1freeproxy.pw",

# A
"http://anonymouse.org",
"http://americaproxy.info",
"http://www.anonymizer.com",

# B
"https://www.best-proxy.co.uk",
"http://bitswork.info",
"http://www.blewpass.com",
"http://brazilproxy.info",

# C
"http://canadaproxy.info",
"https://www.crazyproxy.org",
"http://caproxies.info",
"http://cantblockthis.org",
"http://www.clubredweb.com",

# D 
"http://dzhot.us",
"http://www.dontfilter.us",
"http://defilter.us",

# E 
"https://www.extremeproxy.us",
"https://www.englandproxy.co.uk",
"http://ecxs.asia",

# F 
"https://funproxy.net",
"http://fastusaproxy.com",
"http://fbproxies.info",
"http://fishproxy.com",
"http://fasttime.info",
"http://freeproxy.party",
"http://freeopenproxy.com",
"http://freeyoutube.net",
"http://freeproxyserver.uk",
"http://freeyouproxytube.com",
"http://f4fp.com",
"http://fishproxy.com",

# G 
"http://greatestfreeproxy.com",
"http://german-proxy.info",
"https://www.goproxy.asia",
"http://gizlenin.com",
"http://goproxy.asia",

# H 
"http://hostapp.eu",
"http://hidetheinternet.com",
"https://hideipproxy.com",
"http://hide.mx",
"http://hidingyour.info",
"https://www.hidemyass.com/proxy",
"https://hidemytraxproxy.ca",
"http://hiddendigital.info",

# I 
"http://interncloud.info",
"http://itproxy.work",

# J 
"http://justunblockit.com",
"http://jezuslovesthisproxy.info",
"http://justproxy.co.uk",

# K 
"http://krproxy.info",
"http://www.kproxysite.com",
"http://www.kproxy.com",

# L 
"http://londonproxy.eu",

# M 
"https://www.mehide.asia",
"http://ww11.myyoutubeunblocker.com",

# N 
"https://www.networkbypass.com",
"http://newipnow.com",
"http://ninjacloak.com",

# O 
"http://o-itc.be",
"https://onlinecollege1081.info",

# P 
"http://proxyinternet.info",
"https://www.proxypirate.co.uk",
"https://www.proxytube.info",
"http://proxy4freedom.com",
"http://proxys.pw",
"http://www.proxy-2014.com",
"http://proxy-2015.info",
"http://prointern.info",
"http://proxybrowse.info",
"http://proxy-internet.info",
"http://pkproxy.info",
"http://proxy.org",
"https://www.proxythis.info",
"http://www.phproxysite.com",
"https://www.proxysite.com",
"http://proxify.com/p",
"http://proxy2014.net",
"http://proxyo.info",
"https://proxyone.net",
"http://www.proxay.co.uk",
"http://pro-unblock.com",
"http://proxy4freedom.com",
"http://www.proxypower.co.uk",
"http://phproxy.co",
"http://proxys.pw",
"http://proxmecallmenames.com",
"https://proxylistpro.com",

# Q 
"http://www.quickproxy.co.uk",

# R 
"http://rexoss.com",
"http://rapidproxy.us",

# S 
"https://www.sslproxy.org.uk",
"http://surf-for-free.com",
"http://saoudiproxy.info",
"http://skinftw.com",
"http://sporium.org",
"http://suedeproxy.info",
"http://surfproxy.co",
"http://singaporeproxy.nu",
"http://stardollproxy.com",
"http://spedo.co",

# T 
"http://travelvpn.info",
"http://tiafun.com",
"https://proxy.toolur.com",
"http://toproxy.co",
"http://thebestproxy.info",

# U 
"http://www.unblockmyweb.com",
"http://unblockyoutubefree.net",
"https://www.unblocker.us",
"http://unblockyoutubeatschool.com",
"http://unblocker.us",
"http://usproxies.info",
"http://usproxy.nu",

# V 
"http://vpnbrowse.com",
"http://viewyoutube.net",
"http://vtunnel.com",
"http://www.vobas.com",

# W 
"http://webproxyfree.net",
"http://websurfproxy.me",
"http://workhost.eu",
"http://webproxy.net",
"http://workingproxy.net",

# X 
"http://xitenow.com",

# Y 
"http://youserver.nu",
"http://youliaoren.com",
"http://youtubeu.info",
"http://www.youtubeunblockproxy.com",
"http://youtubefreeproxy.net",

# Z
"http://zendproxy.com",
"http://www.zalmos.com",
"http://zacebookpk.com"]

for something in proxylist:
	try:
		response = requests.get(something)
		if "Access Denied" not in response.text:
			print "[+] "+something
	except requests.exceptions.ConnectionError:
		pass
	sleep(0.5)