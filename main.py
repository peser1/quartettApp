from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

class ProgramX(App):

	def build(self):

		self.f = FloatLayout()

		self.bPower = Button(text='', font_size=20, background_color=[0, 0, 0, 0], \
				pos_hint={'center_x': 0.5, 'center_y': 0.485}, size_hint=(0.75,0.08))
		self.bCO2 = Button(text='', font_size=20,  background_color=[0, 0, 0, 0], \
				pos_hint={'center_x': 0.5, 'center_y': 0.405}, size_hint=(0.75,0.08))
		self.bCost = Button(text='', font_size=20,  background_color=[0, 0, 0, 0], \
				pos_hint={'center_x': 0.5, 'center_y': 0.325}, size_hint=(0.75,0.08))
		self.bEmployee = Button(text='', font_size=20,  background_color=[0, 0, 0, 0], \
				pos_hint={'center_x': 0.5, 'center_y': 0.245}, size_hint=(0.75,0.08))
		self.bFootprint = Button(text='', font_size=20,  background_color=[0, 0, 0, 0], \
				pos_hint={'center_x': 0.5, 'center_y': 0.165}, size_hint=(0.75,0.08))

		self.iCard = Image(source='Hydro1.jpg', pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(1.0,1.0))
		self.labl = Label(text='', font_size=65, color=[1, 1, 1, 1], \
				pos_hint={'center_x': 0.5, 'center_y': 0.85}, size_hint=(None,None))

		self.bPower.bind(on_press=self.selectOption)
		self.bCO2.bind(on_press=self.selectOption)
		self.bCost.bind(on_press=self.selectOption)
		self.bEmployee.bind(on_press=self.selectOption)
		self.bFootprint.bind(on_press=self.selectOption)

		self.f.add_widget(self.iCard)
		self.f.add_widget(self.bPower)
		self.f.add_widget(self.bCO2)
		self.f.add_widget(self.bCost)
		self.f.add_widget(self.bEmployee)
		self.f.add_widget(self.bFootprint)
		self.f.add_widget(self.labl)

		return self.f

	def selectOption(self, instance):
		if instance == self.bPower:
			self.labl.text = 'Pressed Power!'
		elif instance == self.bCO2:
			self.labl.text = 'Pressed CO2!'
		elif instance == self.bCost:
			self.labl.text = 'Pressed Cost!'
		elif instance == self.bEmployee:
			self.labl.text = 'Pressed Employees!'
		elif instance == self.bFootprint:
			self.labl.text = 'Pressed Footprint!'
		return 0

if __name__ == "__main__":
	ProgramX().run()
