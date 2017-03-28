from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

class ProgramX(App):

	def build(self):

		self.f = FloatLayout()

		self.b1 = Button(text='', font_size=20, background_color=[0, 0, 0, 0], \
				pos_hint={'center_x': 0.5, 'center_y': 0.485}, size_hint=(0.75,0.08))
		self.b2 = Button(text='', font_size=20,  background_color=[0, 0, 0, 0], \
				pos_hint={'center_x': 0.5, 'center_y': 0.405}, size_hint=(0.75,0.08))
		self.b3 = Button(text='', font_size=20,  background_color=[0, 0, 0, 0], \
				pos_hint={'center_x': 0.5, 'center_y': 0.325}, size_hint=(0.75,0.08))
		self.b4 = Button(text='', font_size=20,  background_color=[0, 0, 0, 0], \
				pos_hint={'center_x': 0.5, 'center_y': 0.245}, size_hint=(0.75,0.08))
		self.b5 = Button(text='', font_size=20,  background_color=[0, 0, 0, 0], \
				pos_hint={'center_x': 0.5, 'center_y': 0.165}, size_hint=(0.75,0.08))

		self.iCard = Image(source='imgs/Hydro1_small.jpg', allow_stretch=True, keep_ratio=False, \
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

	def selectOption(self, instance):
		if instance == self.b1:
			self.labl.text = 'Pressed Power!'
		elif instance == self.b2:
			self.labl.text = 'Pressed CO2!'
		elif instance == self.b3:
			self.labl.text = 'Pressed Cost!'
		elif instance == self.b4:
			self.labl.text = 'Pressed Employees!'
		elif instance == self.b5:
			self.labl.text = 'Pressed Footprint!'
		return 0

if __name__ == "__main__":
	ProgramX().run()
