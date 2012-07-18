import ftpy
import os
import shutil
from nose import tools as nt

#TEST INFO
USER = ""
PASS = ""
SERVER = ""

TEST_DIR = ".test_files"


class test_HighLevelAPI(object):

	def setUp(self):
		ftpy.login("USER"+":"+PASS+"@"+SERVER)

	def test_upload(self):
		# DEPENDENCY - ls()
		nt.assert_equal(ftpy.upload(TEST_DIR), ftpy.FTP_SUCCESS)
		nt.assert_in(TEST_DIR, ftpy.ls())
		nt.assert_equal(ftpy.ls(TEST_DIR).split(), os.listdir())

	def test_download(self):
		# DEPENDENCY - ls()
		shutil.rmtree(TEST_DIR)
		nt.assert_equal(ftpy.download(TEST_DIR), ftpy.FTP_SUCCESS)
		nt.assert_in(TEST_DIR, os.listdir())
		nt.assert_equal(os.listdir(TEST_DIR), ftpy.ls(TEST_DIR))

	def test_connections(self):
		# DEPENDENCY - 	
		

	def tearDown(self):
		ftpy.logout()
