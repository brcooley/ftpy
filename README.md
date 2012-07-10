FT.Py is an easy-to-use, powerful API for harnessing FTP from python programs

### Quick Start ###

    git clone https://github.com/brcooley/ftpy.git && cd ftpy

Then, from a python shell

    >>> import ftpy, os
    >>> ftpy.login("my_user:my_pass@ftp.myserver.tld")
    >>> ftpy.ls("-l")
	drwxr-xr-x    2 my_user    my_user          4096 Jul  3 21:08 about
	drwxr-xr-x    7 my_user    my_user          4096 Jul  3 21:08 assets
	-rw-r--r--    1 my_user    my_user          4859 Jul  5 08:36 index.html
	-rw-r--r--    1 my_user    my_user         36900 Jul  3 21:08 logo.png
	-rw-r--r--    1 my_user    my_user           986 Jul  5 08:36 maintenance.html
	>>> ftpy.cd("assets")
	>>> ftpy.ls()
	css  js  pdf
	>>> ftpy.upload("images")
	>>> ftpy.ls("images")
	bg.gif  headshot.jpg  pitch_graphic.gif
	>>> ftpy.mv("../logo.png","images/")
	>>> ftpy.cd("..")
	>>> ftpy.ls()
	about  assets  index.html  maintenance.html
	>>> ftpy.cd("about")
	>>> ftpy.ls()
	index.html
	>>> ftpy.download(".")
	>>> os.listdir()
	['about','beta','hugeDir','topSecret.txt','zebras.html']
	>>> os.listdir("about")
	['index.html']
	>>> ftpy.connections(5)
	>>> ftpy.upload("hugeDir","..")
	>>> ftpy.ls("..")
	about  assets  hugeDir  index.html  maintenance.html
	>>> ftpy.info()
	{'user': 'my_user', 'server': 'ftp.myserver.tld', 'connections': 5, 'passive': True, 'secure': False}
	>>> ftpy.secure()
	>>> ftpy.info('secure')
	{'secure': True}
	>>> ftpy.cmd(["mkdir",".topSecret"],["cd",".topSecret"],["upload","topSecret.txt"])
	>>> ftpy.ls("../.topSecret","-l")
	-rw-r-----    1 my_user    my_user           345 Jul  1 04:55 topSecret.txt
	>>> ftpy.logout()
	>>> ftpy.info()
	{'user': 'my_user', 'server': 'ftp.myserver.tld', 'connections': 0, 'passive': True, 'secure': True}

