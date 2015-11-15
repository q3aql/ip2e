#################################################################
# Installing ip2e                                               #
#################################################################

PREFIX=/usr

install:
	cp ip2e-daemon.py $(PREFIX)/bin
	cp ip2e-config.py $(PREFIX)/bin
	cp ip2e-log.py $(PREFIX)/bin
	cp desktop/ip2e.desktop $(PREFIX)/share/applications
	cp desktop/ip2e-config.desktop $(PREFIX)/share/applications
	cp icon/ip2e.png $(PREFIX)/share/icons	
	chmod +x $(PREFIX)/bin/ip2e-daemon.py
	chmod +x $(PREFIX)/bin/ip2e-config.py
	chmod +x $(PREFIX)/bin/ip2e-log.py
	chmod +x $(PREFIX)/share/applications/ip2e.desktop
	chmod +x $(PREFIX)/share/applications/ip2e-config.desktop
	
uninstall:
	rm $(PREFIX)/bin/ip2e-daemon.py
	rm $(PREFIX)/bin/ip2e-config.py
	rm $(PREFIX)/bin/ip2e-log.py
	rm $(PREFIX)/share/applications/ip2e.desktop
	rm $(PREFIX)/share/applications/ip2e-config.desktop
	rm $(PREFIX)/share/icons/ip2e.png	

