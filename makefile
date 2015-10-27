###################################################################
# Installing ip2e                                                 #
###################################################################

PREFIX=/usr

install:
	cp ip2e-daemon.py $(PREFIX)/bin
	cp ip2e-config.py $(PREFIX)/bin
	cp ip2e-log.py $(PREFIX)/bin
	chmod +x $(PREFIX)/bin/ip2e-daemon.py
	chmod +x $(PREFIX)/bin/ip2e-config.py
	chmod +x $(PREFIX)/bin/ip2e-log.py
	
uninstall:
	rm $(PREFIX)/bin/ip2e-daemon.py
	rm $(PREFIX)/bin/ip2e-config.py
	rm $(PREFIX)/bin/ip2e-log.py

