from gi.repository import Gtk
from os.path import abspath, dirname, join

WHERE_AM_I = abspath(dirname(__file__))

class MyApp(object):

	def __init__(self):
		"""
		Build GUI
		"""

		# Build GUI from Glade file
		self.builder = Gtk.Builder()
		self.glade_file = join(WHERE_AM_I, './ui/app.ui')
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
		self.choosed_size = go('sizes')

		# Containers
		self.gallery = go('galery')
		self.image_gallery = go('viewport1')
		self.filter_gallery = go('viewport2')
		self.gallery_image_add = go('gallery_image_add')

		# Data
		self.projects = go('projects')
		self.get_projects(self.projects)

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
		# TODO esperar a que finalice la descarga.
		self.create_gallery()

	def _filter(self, widget, data=None):
		print "Filtering"
		print self.filters.get_filename()
		#TODO guardar filtros en carpeta de filtros del proyecto.
		#TODO mostrar filtros en el selector de filtros.

	def _music(self, widget, data=None):
		print "Adding music"
		print self.music_file.get_filename()

	def _video(self, widget, data=None):
		print "Generationg Video"

	def _resize(self, widget, data=None):
		size_text = self.get_size(self.choosed_size)
		print "Resizing to... "+size_text

	def get_projects(self, projects):
		#TODO obtener proyectos buscando las carpetas de proyectos existentes en la carpeta del programa.
		#FIXME dummy test
		self.projects.append(["Proyecto 1"])
		self.projects.append(["Proyecto 2"])

	def get_size(self, combo):
		index = combo.get_active()
		model = combo.get_model()
		item = model[index]
		return item[0]

	def create_gallery(self):
		# Creamos la galeria con las fotos descargadas
		self.gallery_image_add.destroy()
		flowbox = Gtk.FlowBox()
		flowbox.set_valign(Gtk.Align.START)
		flowbox.set_max_children_per_line(10)
		flowbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
		self.get_images(self, flowbox)
		self.image_gallery.add(flowbox)
		self.window.show_all()

	def get_images(flowbox):
		# TODO obtener imagenes, crear thumbnail y anadir imagenes
		# FIXME dummy test
		flowbox.add(Gtk.Button())
		flowbox.add(Gtk.Button())
		flowbox.add(Gtk.Button())

if __name__ == '__main__':
	gui = MyApp()
	Gtk.main()