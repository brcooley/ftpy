FT.Py is an easy-to-use, powerful API for harnessing FTP from the command line or python programs

### Quick Start ###

    git clone https://github.com/brcooley/ftpy.git && cd ftpy

Then, from a python shell

    >>> import ft, os
    >>> ft.login("my_user:my_pass@ftp.myserver.tld")
    >>> ft.ls("-l")
	drwxr-xr-x    2 my_user    my_user          4096 Jul  3 21:08 about
	drwxr-xr-x    7 my_user    my_user          4096 Jul  3 21:08 assets
	-rw-r--r--    1 my_user    my_user          4859 Jul  5 08:36 index.html
	-rw-r--r--    1 my_user    my_user         36900 Jul  3 21:08 logo.png
	-rw-r--r--    1 my_user    my_user           986 Jul  5 08:36 maintenance.html
	>>> ft.cd("assets")
	>>> ft.ls()
	css  js  pdf
	>>> ft.upload("images")
	>>> ft.ls("images")
	bg.gif  headshot.jpg  pitch_graphic.gif
	>>> ft.mv("../logo.png","images/")
	>>> ft.cd("..")
	>>> ft.ls()
	about  assets  index.html  maintenance.html
	>>> ft.cd("about")
	>>> ft.ls()
	index.html
	>>> ft.download(".")
	>>> os.listdir()
	['about','beta','hugeDir','topSecret.txt','zebras.html']
	>>> os.listdir("about")
	['index.html']
	>>> ft.connections(5)
	>>> ft.upload("hugeDir","..")
	>>> ft.ls("..")
	about  assets  hugeDir  index.html  maintenance.html
	>>> ft.info()
	{'user': 'my_user', 'server': 'ftp.myserver.tld', 'connections': 5, 'passive': True, 'secure': False}
	>>> ft.secure()
	>>> ft.info('secure')
	{'secure': True}
	>>> ft.cmd(["mkdir",".topSecret"],["cd",".topSecret"],["upload","topSecret.txt"])
	>>> ft.ls("../.topSecret","-l")
	-rw-r-----    1 my_user    my_user           345 Jul  1 04:55 topSecret.txt
	>>> ft.logout()
	>>> ft.info()
	{'user': 'my_user', 'server': 'ftp.myserver.tld', 'connections': 0, 'passive': True, 'secure': True}

