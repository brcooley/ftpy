supported = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
new_fns = {}

def new_cmd(name):
	def _make_cmd(*args):
		return cmd([name] + list(args))
	return _make_cmd

def cmd(*args):
	for arg in args:
		print(arg)

for fn in supported:
	locals()[fn] = new_cmd(fn)

abc=new_cmd('abc')

def __import__(name,globals=new_fns,locals={},fromlist=[]):
	pass



