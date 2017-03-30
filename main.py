from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
import glob
import os
import random
import time

class ProgramX(App):

	def build(self):

		listOfPics, listOfData = self.loadData()

		self.userPics, self.userData, self.computerPics, self.computerData = self.allocateCards(listOfPics, listOfData)

		self.f = FloatLayout()

		self.b1 = Button(text='', font_size=20, background_color=[0, 0, 0, 0.5], \
				pos_hint={'center_x': 0.5, 'center_y': 0.485}, size_hint=(0.75,0.08))
		self.b2 = Button(text='', font_size=20,  background_color=[0, 0, 0, 0.5], \
				pos_hint={'center_x': 0.5, 'center_y': 0.405}, size_hint=(0.75,0.08))
		self.b3 = Button(text='', font_size=20,  background_color=[0, 0, 0, 0.5], \
				pos_hint={'center_x': 0.5, 'center_y': 0.325}, size_hint=(0.75,0.08))
		self.b4 = Button(text='', font_size=20,  background_color=[0, 0, 0, 0.5], \
				pos_hint={'center_x': 0.5, 'center_y': 0.245}, size_hint=(0.75,0.08))
		self.b5 = Button(text='', font_size=20,  background_color=[0, 0, 0, 0.5], \
				pos_hint={'center_x': 0.5, 'center_y': 0.165}, size_hint=(0.75,0.08))

		self.iCard = Image(source=self.userPics[0], allow_stretch=True, keep_ratio=False, \
				pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(1.0,1.0))
		self.labl = Label(text='', font_size=65, color=[1, 1, 1, 1], \
				pos_hint={'center_x': 0.5, 'center_y': 0.85}, size_hint=(None,None))

		self.b1.bind(on_press=self.selectOption)
		self.b2.bind(on_press=self.selectOption)
		self.b3.bind(on_press=self.selectOption)
		self.b4.bind(on_press=self.selectOption)
		self.b5.bind(on_press=self.selectOption)

		self.f.add_widget(self.iCard)
		self.f.add_widget(self.b1)
		self.f.add_widget(self.b2)
		self.f.add_widget(self.b3)		
		self.f.add_widget(self.b4)
		self.f.add_widget(self.b5)
		self.f.add_widget(self.labl)

		return self.f

	def loadData(self):

		os.chdir('imgs')
		listOfPics = []
		listOfNames = []
		for fl in glob.glob('*.jpg'):
			listOfPics.append(fl)
			listOfNames.append(fl.strip().split('.')[0])
		
		os.chdir('../data')
		listOfData = []
		for currName in listOfNames:
			power = 0
			co2 = 0
			cost = 0
			employee = 0
			footprint = 0
			with open(currName+'.txt') as dataFile:
				for line in dataFile:
					if line.strip().split('=')[0] == 'power':
						power = int(float(line.strip().split('=')[1]))
					if line.strip().split('=')[0] == 'co2':
						co2 = int(float(line.strip().split('=')[1]))
					if line.strip().split('=')[0] == 'cost':
						cost = int(float(line.strip().split('=')[1]))
					if line.strip().split('=')[0] == 'employee':
						employee = int(float(line.strip().split('=')[1]))
					if line.strip().split('=')[0] == 'footprint':
						footprint = int(float(line.strip().split('=')[1]))
			listOfData.append([power, co2, cost, employee, footprint])

		os.chdir('../imgs')				

		return listOfPics, listOfData

	def allocateCards(self, listOfPics, listOfData):

		allIDs = range(len(listOfPics))
		userPicIDs = random.sample(allIDs,len(listOfPics)/2)
		computerPicIDs = []
		for aID in allIDs:
			if not aID in userPicIDs:
				computerPicIDs.append(aID)
		
		userPics = [listOfPics[x] for x in userPicIDs]
		userData = [listOfData[x] for x in userPicIDs]
		computerPics = [listOfPics[x] for x in computerPicIDs]
		computerData = [listOfData[x] for x in computerPicIDs]		
		
		return userPics, userData, computerPics, computerData
		

	def selectOption(self, instance):
		if instance == self.b1:
			if self.userData[0][0] >= self.computerData[0][0]:
				userWinsNow = 1
			else:
				userWinsNow = 0		
		elif instance == self.b2:
			if self.userData[0][1] >= self.computerData[0][1]:
				userWinsNow = 1
			else:
				userWinsNow = 0		
		elif instance == self.b3:
			if self.userData[0][2] >= self.computerData[0][2]:
				userWinsNow = 1
			else:
				userWinsNow = 0		
		elif instance == self.b4:
			if self.userData[0][3] >= self.computerData[0][3]:
				userWinsNow = 1
			else:
				userWinsNow = 0		
		elif instance == self.b5:
			if self.userData[0][4] >= self.computerData[0][4]:
				userWinsNow = 1
			else:
				userWinsNow = 0

		if userWinsNow == 1:
			self.labl.text = 'User wins!'
			self.iCard.source = self.computerPics[0]
			#Clock.schedule_once(function, time)
			self.userData.append(self.userData[0])
			self.userData.append(self.computerData[0])
			self.userData = self.userData[1:]
			self.computerData = self.computerData[1:]
			self.userPics.append(self.userPics[0])
			self.userPics.append(self.computerPics[0])
			self.userPics = self.userPics[1:]
			self.computerPics = self.computerPics[1:]
		else:
			self.labl.text = 'Computer wins!'
			self.iCard.source = self.computerPics[0]
			#Clock.schedule_once(function, time)
			self.computerData.append(self.computerData[0])
			self.computerData.append(self.userData[0])
			self.userData = self.userData[1:]
			self.computerData = self.computerData[1:]
			self.computerPics.append(self.computerPics[0])
			self.computerPics.append(self.userPics[0])
			self.userPics = self.userPics[1:]
			self.computerPics = self.computerPics[1:]

		if len(self.userPics) == 0:
			self.labl.text = 'Computer wins the game!'
			return -1
		if len(self.computerPics) == 0:
			self.labl.text = 'You win the game!'
			return 1

		self.iCard.source = self.userPics[0]
		return 0

	def useless(self, foo):
		time.sleep(1)

if __name__ == "__main__":
	ProgramX().run()
