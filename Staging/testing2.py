class StackSem(object):
	stack_ = []
	def __getitem__(self, arg):
		return self.stack_[arg]
	def append(self, element):
		self.stack_.append(element)
	def pop(self):
		if len(self.stack_) != 0:
			return self.stack_.pop()
		else:
			return None

StackSem = StackSem()
print(StackSem.pop())
StackSem.append(1)
StackSem.append(2)
print(StackSem[-1])
print(StackSem[0])
print(StackSem.pop())
print(StackSem.pop())
print(StackSem.pop())

	