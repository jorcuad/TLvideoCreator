from gi.repository import Gtk, Gdk
from gi.repository.GdkPixbuf import Pixbuf, InterpType
from os.path import abspath, dirname, join
import copy
import Project

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
		self.selected = []; # Array binario si es 1 la imagen esta activa, si es 0 la imagen no se usara en el video.

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
		self.project = Project.Project(self.hashtag.get_text(), self.number.get_text())
		self.project.download()
		# TODO crear carpeta del proyecto, con subcarpetas, abstraer en funcion para luego al pasar a windows facilitar
		# TODO esperar a que finalice la descarga.
		self.create_gallery()
		for i in range(0,len(self.flowbox.get_children())):
			self.selected.append(0)

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
		self.flowbox = Gtk.FlowBox()
		self.flowbox.connect("child-activated", self.on_child_activated)
		self.flowbox.set_valign(Gtk.Align.START)
		self.flowbox.set_max_children_per_line(5)
		self.flowbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
		self.get_images(self.flowbox)
		self.image_gallery.add(self.flowbox)
		self.window.show_all()

	def on_child_activated(self, father, child): #FIXME
		i = copy.copy(child.get_index())
		if(self.selected[i] == 0):
			f = self.get_frame_thumbnail('./pics/originals/'+str(i)+'.jpg')
			self.selected[i] = 1
		else:
			f = self.get_thumbnail('./pics/originals/'+str(i)+'.jpg')
			self.selected[i] = 0
		child.destroy()
		self.flowbox.insert(f, i)
		self.window.show_all()
		#TODO detectar su estado, cambiar estado a descartado o con filtro

	def get_images(self, flowbox):
		# TODO obtener imagenes, crear thumbnail y anadir imagenes
		# FIXME dummy test
		flowbox.add(self.get_thumbnail('./pics/originals/0.jpg'))
		flowbox.add(self.get_thumbnail('./pics/originals/1.jpg'))
		flowbox.add(self.get_thumbnail('./pics/originals/2.jpg'))
		flowbox.add(self.get_thumbnail('./pics/originals/3.jpg'))
		flowbox.add(self.get_thumbnail('./pics/originals/4.jpg'))
		flowbox.add(self.get_thumbnail('./pics/originals/5.jpg'))
		flowbox.add(self.get_thumbnail('./pics/originals/6.jpg'))
		flowbox.add(self.get_thumbnail('./pics/originals/7.jpg'))
		flowbox.add(self.get_thumbnail('./pics/originals/8.jpg'))
		flowbox.add(self.get_thumbnail('./pics/originals/9.jpg'))
		flowbox.add(self.get_thumbnail('./pics/originals/10.jpg'))
		flowbox.add(self.get_thumbnail('./pics/originals/11.jpg'))

	def get_thumbnail(self, path):
		pixbuf = Pixbuf.new_from_file(path)
		pixbuf = pixbuf.scale_simple(80, 80, InterpType.BILINEAR)
		img = Gtk.Image()
		img.set_from_pixbuf(pixbuf)
		return img

	def get_frame_thumbnail(self, path): #TODO cambiar por imagen en escala de grises o imagen con un aspa
		f = Gtk.Frame()
		f.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0,1,0,1))
		pixbuf = Pixbuf.new_from_file(path)
		pixbuf = pixbuf.scale_simple(80, 60, InterpType.BILINEAR)
		img = Gtk.Image()
		img.set_from_pixbuf(pixbuf)
		f.add(img)
		return f

#		button.set_border_width(50)
#eb = gtk.EventBox()
#eb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("pink"))
#eb.add(button)

if __name__ == '__main__':
	gui = MyApp()
	Gtk.main()