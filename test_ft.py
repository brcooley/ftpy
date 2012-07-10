from ft import *

#TEST INFO
USER = ""
PASS = ""
SERVER = ""


class test_HighLevelAPI(object):

	def setUp(self):
		login("USER"+":"+PASS+"@"+SERVER)

	def test_upload(self):
		#assert
		assertEquals(upload(self.testDir), FTP_SUCCESS)
		assertEquals()

	def test_2(self):
		assert False

	def tearDown(self):
		pass
