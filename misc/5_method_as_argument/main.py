class Main:

	@staticmethod
	def foo(first_name, last_name, method):
		print(first_name)
		method(last_name)


	@staticmethod
	def bar(last_name):
		print(last_name)

	@staticmethod
	def main():
		first_name = "Saketh"
		last_name = "Katari"
		Main.foo(first_name, last_name, Main.bar)

Main.main()