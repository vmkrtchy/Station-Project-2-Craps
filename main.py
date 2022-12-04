from functools import partial
from random import randint
from tkinter import *

class Game:
	def __init__(self):
		self.main = Label(root, text='Project 2 ',font = ("Helvetica", "30"))
		self.main.pack()
		self.goal = 0
		self.newGoal = Label(root, text=f'Your new goal is: {self.goal}')
		self.newGoal.pack()
		self.button = Button(root, text='Play',padx = 10, pady = 5, command=partial(self.start, self.goal, randint(1, 6), randint(1, 6)))
		self.button.pack()


		self.exit = Button(root,padx = 10, pady = 5, text='Exit Game', command=self.quit)
		self.restartB = Button(root,padx = 10, pady = 5, text="Restart", command=self.restart)
		self.restartB.pack()
		self.exit.pack()

	def quit(self):
		root.destroy()
		exit()

	def restart(self):
		self.main.pack_forget()
		self.goal = 0
		self.newGoal.pack_forget()
		self.button.pack_forget()
		self.exit.pack_forget()
		self.restartB.pack_forget()
		self.__init__()

	def start(self, goal=0, nam1=0, nam2=0):
		nam1 = randint(1, 6)
		nam2 = randint(1, 6)
		self.sum = nam1 + nam2
		if self.goal != 0:
			if self.sum == 7:
				self.main.config(text=f'You Lose: {self.sum}')
				self.button.pack_forget()
				return
			elif self.sum == self.goal:
				self.main.config(text=f'You Win: {self.goal}')
				self.button.pack_forget()
				return
			else:
				self.main.config(text=f'The sum of numbers is: {self.sum}')
		else:
			if self.sum in [7, 11]:
				self.main.config(text=f'You Win {self.sum}')
				self.button.pack_forget()
				return
			elif self.sum in [2, 3, 12]:
				self.main.config(text=f'You Lose {self.sum}')
				self.button.pack_forget()
				return
			elif self.sum in [4, 5, 6, 8, 9, 10]:
				self.goal = self.sum
				self.newGoal.config(text=f'You new goal is: {self.goal}')

if __name__ == '__main__':
	root = Tk()
	root.geometry("400x400")

	root.resizable(width = False, height = False)
	Game()
	root.mainloop()


