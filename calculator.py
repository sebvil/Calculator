# to do: figure out how to evaluate/ignore keyboard input
# organize classes and objects better
# add exponents
# fix (-) sign
# edit style




import Tkinter
#import PIL
from operations import operations

class Number_Key(Tkinter.Button):
	def __init__(self, master, num, textbox):
		self.textbox =textbox
		Tkinter.Button.__init__(self, master,
						text = str(num),
						activebackground = "red",
						activeforeground = "blue",
						bd =2,
						bg = "green",
						fg = "black",
						font = "Arial",
						height = 1,
						width = 1,
						highlightcolor = "yellow",
						command = lambda x=self: self.select(str(num)))

	def select(self, text):
		print self.textbox.values
		if text in ["+", "-", "*", "/"]:
			if self.textbox.len_values() == 0:
				print self.textbox.get()
				self.textbox.add_value(self.textbox.get())
				self.textbox.add_value(text)
			elif self.textbox.values[-1] in ["+", "-", "*", "/", ")", "("]:
				if self.textbox.values[-1] != ")":
					last_operand = self.textbox.values[-1]
					i = self.textbox.get().rfind(last_operand)				
					last_num = self.textbox.get()[i+1:]				
					self.textbox.add_value(last_num)
				self.textbox.add_value(text)
			else:
				val = self.textbox.get()
				#self.textbox.delete(0, len(val))
				self.textbox.add_value(text)
			self.textbox.insert(Tkinter.END, text)
		elif text == "(":
			if len(self.textbox.values) == 0:
				self.textbox.add_value(text)
				self.textbox.insert(Tkinter.END, text)
			else:
				last_operand = str(self.textbox.values[-1])
				i = self.textbox.get().rfind(last_operand)				
				last_num = self.textbox.get()[i+1:]
				if last_num == "":
					self.textbox.add_value(text)
					self.textbox.insert(Tkinter.END, text)
				elif len(self.textbox.values) == 1:
					self.textbox.add_value("*")
					self.textbox.add_value(text)
					self.textbox.insert(Tkinter.END, text)
				else:
					self.textbox.add_value(last_num)
					self.textbox.add_value("*")
					self.textbox.add_value(text)
					self.textbox.insert(Tkinter.END, text)
					
		elif text == ")":
			last_operand = self.textbox.values[-1]
			i = self.textbox.get().rfind(last_operand)				
			last_num = self.textbox.get()[i+1:]	
			self.textbox.insert(Tkinter.END, text)			
			self.textbox.add_value(last_num)	
			self.textbox.add_value(text)
		elif self.textbox.len_values() == 1 and self.textbox.values[0] != "(":
			length =len(self.textbox.get())
			self.textbox.values = []
			self.textbox.delete(0, length)
			self.select(text)
		elif text == "C":
			length =len(self.textbox.get())
			self.textbox.delete(0, length)
		elif text == "DEL":
			self.textbox.delete(len(self.textbox.get())-1, Tkinter.END)
		elif text == "=":
			last_operand = self.textbox.values[-1]
			if last_operand != ")":
				i = self.textbox.get().rfind(last_operand)				
				last_num = self.textbox.get()[i+1:]				
				self.textbox.add_value(last_num)
			self.textbox.compute()
		elif text == "(-)":
			text = self.textbox.get()
			if len(text) > 0 and text[0] == "-":
				self.textbox.delete(0)
			else:
				self.textbox.insert(0, "-")
		elif text == "AC":
			length =len(self.textbox.get())
			self.textbox.delete(0, length)
			self.textbox.values = []
		else:
			self.textbox.insert(Tkinter.END, text)
top = Tkinter.Tk()



text = ""

class Calc_Entry(object):
	def __init__(self, master):
			self.text = ""
			self.values = []	
			self.entry = Tkinter.Entry(top, bg ="lightblue",
				font="Arial",
				fg = "black",
				justify = "right",
				selectbackground="blue",
				selectforeground="white",
				width = 20,
				textvariable = self.text)
	def place(self, x, y):
		self.entry.place(x= x, y= y)
	
	def insert(self, index, text):
		self.entry.insert(index, text)

	def get(self):
		return self.entry.get()

	def delete(self, sindex, eindex):
		self.entry.delete(sindex,eindex)

	def add_value(self, val):
		if val in ["+", "-", "*", "/", "(", ")"]:
			self.values.append(val)
		else:
			print val
			self.values.append(float(val))
			print self.values

		#self.delete(0, len(val))
	def len_values(self):
		return len(self.values)
	
	def compute(self):
		num = operations(self.values)
		print self.values
		
		self.values = [num]
		print num
		self.delete(0,len(self.get()))
		self.insert(0, str(num))
			
buttons = {}

entry = Calc_Entry(top)
show_input = Tkinter.Text(top, bg = "lightblue",
			font = "Arial",
			width = 20,
			height = 1,
			state="disabled")

for i in range(0,10):
	b = Number_Key(top, i, entry)
	buttons[i] = b

buttons["DEL"] = Number_Key(top, "DEL", entry)
buttons["C"] = Number_Key(top, "C", entry)
buttons["+"] = Number_Key(top, "+", entry)
buttons["-"] = Number_Key(top, "-", entry)
buttons["*"] = Number_Key(top, "*", entry)
buttons["="] = Number_Key(top, "=", entry)
buttons["/"] = Number_Key(top, "/", entry)
buttons["."] = Number_Key(top, ".", entry)
buttons["(-)"] = Number_Key(top, "(-)", entry)
buttons["AC"] = Number_Key(top, "AC", entry)
buttons["("] = Number_Key(top, "(", entry)
buttons[")"] = Number_Key(top, ")", entry)

for i in range(0,3):
	for j in range(0,3):
		buttons[3*i+j+1].place(x=35 * (j+1), y= 35*(i+2))

entry.place(x=35,y=35)


buttons[0].place(x=35, y=175)
buttons["DEL"].place(x=140, y = 70)
buttons["C"].place(x=140, y = 105)
buttons["+"].place(x=140, y = 140)
buttons["-"].place(x=140, y = 175)
buttons["="].place(x=105, y = 175)
buttons["*"].place(x = 175, y =140)
buttons["/"].place(x = 175, y =175)
buttons["."].place(x= 70, y =175)
buttons["(-)"].place(x=210, y =175) 
buttons["AC"].place(x= 175, y=70)
buttons["("].place(x = 175, y =105)
buttons[")"].place(x = 210, y =70)
top.mainloop()
