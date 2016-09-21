from gi.repository import Gtk
from os.path import abspath, dirname, join

WHERE_AM_I = abspath(dirname(__file__))

class MyApp(object):

	def __init__(self):
		"""
		Build GUI
		"""

		# Declare states / variables
		self.counter = 0

		# Build GUI from Glade file
		self.builder = Gtk.Builder()
		self.glade_file = join(WHERE_AM_I, 'app.ui')
		self.builder.add_from_file(self.glade_file)

		# Get objects
		go = self.builder.get_object

		# Buttons
		self.window = go('window1')
		self.download = go('download')
		self.filter = go('filter')
		self.music = go('music')
		self.video = go('video')

		# Fields
		self.number = go('numero')
		self.hashtag = go('hashtag_text')
		self.filters = go('filters')
		self.music_file = go('music_file')

		# Data
		self.projects = go('projects')

		#Obtener lista de proyectos
		#TODO esto es un codigo de ejemplo
		self.projects.append(["Proyecto 1"])
		self.projects.append(["Proyecto 2"])

		# Connect signals
		self.builder.connect_signals(self)

		# Configure interface
		self.window.connect('delete-event', lambda x,y: Gtk.main_quit())

		# Everything is ready
		self.window.show()

	def _download(self, widget, data=None):
		print "Downloading"
		print self.number.get_text()
		print self.hashtag.get_text()

	def _filter(self, widget, data=None):
		print "Filtering"
		print self.filters.get_filename()

	def _music(self, widget, data=None):
		print "Adding music"
		print self.music_file.get_filename()

	def _video(self, widget, data=None):
		print "Generationg Video"

if __name__ == '__main__':
	gui = MyApp()
	Gtk.main()