import sys
from PyQt5 import uic, QtWidgets

class Ui(QtWidgets.QMainWindow):

	def __init__(self):
		super(Ui, self).__init__()
		uic.loadUi('simulador.ui', self)
		self.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui
app.exec_()

