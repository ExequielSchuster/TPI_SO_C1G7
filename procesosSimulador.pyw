import sys
from PyQt5 import uic, QtWidgets

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

from PyQt5 import QtCore

import matplotlib.pyplot as plt

class Ui(QtWidgets.QMainWindow):

	# __init__ es el metodo constructor de la clase
	def __init__(self):
		super(Ui, self).__init__()
		uic.loadUi('simulador.ui', self)

		# Titulo de la ventana
		self.setWindowTitle("Simulador")

		# Colores 
		# self.EntradaIzqGroupBox.setStyleSheet("background-color: gold;")
		# self.EntradaArribaLine.setVisible(False)
		# self.EntradaAbajoLine.setVisible(False)

		# Para agregar algun widget
		# left, top, width and height
		# self.borrar = QLabel(self.ProcesamPorTiempoGroupBox)
		# self.borrar.setGeometry(QtCore.QRect(170, 250, 100, 13))
		# self.borrar.setObjectName("borrar")
		# self.borrar.setText('Label de prueba')

		# Para cargar otra accion al menu file
		# otraAccion = QAction('Examinar', self)
		# otraAccion.triggered.connect(self.mostrarSegunda())
		# self.menuFile.addAction(otraAccion)

		# ESTOY PROBANDO GRAFICAR
		self.DiagramaGanttPushButton.clicked.connect(self.mostrarDiagramaGantt)

		# al abrir que, la pestaña de Entrada se muestre primero
		self.tabWidget.setCurrentIndex(0)

		# CARGA DE COLAS
		self.actionCargar_Cola.triggered.connect(self.cargar_tabla_procesos)

		# TAMAÑO DE MEMORIA
		self.TamMemSpinBox.setMaximum(999999) 	# si no lo pongo aca llega hasta 99, tamaño maximo? 999999 qcyo
		self.TamMemSpinBox.setMinimum(10)		# tamaño minimo ? 10 qcyo		
		self.TamMemSpinBox.setValue(1024)
		# self.TamMemSpinBox.setValue(128)

		# PARTICIONES FIJAS O VARIABLES
		self.VariablesRadioButton.setChecked(True)
		self.PartFijaGroupBox.setVisible(False)
		self.FijasRadioButton.clicked.connect(self.clickEvent)
		self.VariablesRadioButton.clicked.connect(self.clickEvent)

		# PARTICIONES FIJAS
		self.AgregarPartPushButton.clicked.connect(self.agregar_particion)
		self.NroEspacioDispLabel.setText('0')
		self.TamPartSpinBox.setMaximum(self.TamMemSpinBox.value())
		self.ParticionesTableWidget.verticalHeader().setVisible(False)
		# para que no aparezca la barra de desplazamiento en la tabla (queda mal)
		header = self.ParticionesTableWidget.horizontalHeader()
		header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		self.EliminarPartPushButton.clicked.connect(self.eliminar_particion)

		# METODO DE ASIGNACION
		self.FirstRadioButton.setChecked(True)
		self.QuantumLabel.setVisible(False)
		self.QuantumSpinBox.setVisible(False)
		self.AlgortimoComboBox.currentTextChanged.connect(self.clickEvent)

		# LISTA DE PROCESOS CARGADOS
		# self.ListProcCargTableWidget.verticalHeader().setVisible(False)
		self.ListProcCargTableWidget.setColumnCount(4)
		aux = ['Proceso','Tamaño', 'Arribo', 'Rafagas']
		self.ListProcCargTableWidget.setHorizontalHeaderLabels(aux)
		self.ListProcCargTableWidget.verticalHeader().setVisible(False)
		# para que el ancho de la columnas de rafagas sea mayor 
		header = self.ListProcCargTableWidget.horizontalHeader()
		header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
		header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
		header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
		header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
		self.BorrarTablaPushButton.clicked.connect(self.borrar_lista_procesos)
		self.BorrarSeleccionPushButton.clicked.connect(self.borrar_un_proceso)

		# SOLO PARA EL SPRINT ---> BORRABLE 
		self.INICIARPushButton.clicked.connect(self.salida_borrable)

		# NUEVO PROCESO
		# nuevas posiciones de las etiquetas
		# left, top, width and height
		self.TALabel.setGeometry(QtCore.QRect(322, 30, 60, 20))
		self.TALabel.setText('Arribo')
		self.TamProcLabel.setGeometry(QtCore.QRect(160, 30, 81, 20))
		# nuevas posiciones de los spinbox
		self.TamProcSpinBox.setGeometry(QtCore.QRect(229, 30, 50, 22))
		self.TASpinBox.setGeometry(QtCore.QRect(360, 30, 60, 22))
		# demas configuraciones
		self.ProcActualTableWidget.horizontalHeader().setVisible(False)
		self.ProcActualTableWidget.verticalHeader().setVisible(False)
		self.IdProcSpinBox.setMaximum(100)
		self.IdProcSpinBox.setMinimum(0)
		self.IdProcSpinBox.setValue(0)
		self.TASpinBox.setMaximum(100)
		self.TASpinBox.setMinimum(0)
		self.TASpinBox.setValue(0)
		# El tamaño maximo de un proceso se controlara en el metodo de carga del proceso
		self.TamProcSpinBox.setMaximum(self.TamMemSpinBox.value())
		self.TamProcSpinBox.setMinimum(1)
		self.TamProcSpinBox.setValue(1)
		filas = self.ProcActualTableWidget.verticalHeader()
		filas.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
		filas.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		self.AgregarProcPushButton.clicked.connect(self.agregar_proceso)
		# agregar rafaga .... 
		self.AgregarPushButton.clicked.connect(self.agregar_rafaga)

		# SALIDA
		# left, top, width and height
		# cambio de texto y ajust de algunas etiquetas
		self.ColaCPULabel.setText('Cola de Listos')
		self.ColaCPULabel.setGeometry(QtCore.QRect(45, 195, 70, 13))
		self.ColaSuspLabel.setText('Cola de Suspendios')
		self.ColaSuspLabel.setGeometry(QtCore.QRect(20, 280, 111, 31))
		self.CargEnMemLabel.setText('Proceso En CPU')
		self.CargEnMemLabel.setGeometry(QtCore.QRect(38, 370, 111, 31))

		self.PartOcupTextEdit.setReadOnly(True)
		self.HistPlanifTextEdit.setReadOnly(True)



	# ante la seleccion de las partciones y algoritmos, muestra sus respectivas opciones adicionales
	# ya sea la configuracion de las particiones fijas o la del quantum
	def clickEvent(self):
		# selecciono la opcion de RRQ
		if self.AlgortimoComboBox.currentIndex() == 3:
			self.QuantumLabel.setVisible(True)
			self.QuantumSpinBox.setVisible(True)
		else:
			self.QuantumLabel.setVisible(False)
			self.QuantumSpinBox.setVisible(False)

		# seleccion parciones fijas
		if self.FijasRadioButton.isChecked():
			self.PartFijaGroupBox.setVisible(True)
		else:
			self.PartFijaGroupBox.setVisible(False)

	# def cargar_tabla_procesos(self):
	# 	# FALTA HACER EL CONTROL DE QUE NO HAYA OTRO PROCESO
	# 	f = open('ColaDeProcesosEj1b.txt', 'r')
	# 	line = f.readline() # fila con nombres de campos (no interesa)
	# 	line = f.readline() # por eso leenmos de nuevo
	# 	while line != '':
	# 		line = line.split(',')
	# 		# nuevas filas y columnas en la tabla
	# 		self.ListProcCargTableWidget.setRowCount(self.ListProcCargTableWidget.rowCount()+1) 
	# 		# self.ListProcCargTableWidget.setColumnCount(self.ListProcCargTableWidget.columnCount()+1)
	# 		# se crea un "item" nuevo y se alinea su contenido
	# 		proc=QtWidgets.QTableWidgetItem(str(line[0]))
	# 		proc.setTextAlignment(Qt.AlignCenter)
	# 		tam=QtWidgets.QTableWidgetItem(str(line[1]))
	# 		tam.setTextAlignment(Qt.AlignCenter)
	# 		ta=QtWidgets.QTableWidgetItem(str(line[2]))
	# 		ta.setTextAlignment(Qt.AlignCenter)
	# 		raf=QtWidgets.QTableWidgetItem(line[3].rstrip('\n')+'')
	# 		# raf.setTextAlignment(Qt.AlignCenter)
	# 		self.ListProcCargTableWidget.setItem(self.ListProcCargTableWidget.rowCount()-1,0,proc)
	# 		self.ListProcCargTableWidget.setItem(self.ListProcCargTableWidget.rowCount()-1,1,tam)
	# 		self.ListProcCargTableWidget.setItem(self.ListProcCargTableWidget.rowCount()-1,2,ta)
	# 		self.ListProcCargTableWidget.setItem(self.ListProcCargTableWidget.rowCount()-1,3,raf)
	# 		# por si quiere cargar otro proceso, que el id ya sea otro
	# 		self.IdProcSpinBox.setValue(self.ListProcCargTableWidget.rowCount()+1)
	# 		line = f.readline()
	# 	f.close()

	def cargar_tabla_procesos(self):
		# FALTA HACER EL CONTROL DE QUE NO HAYA OTRO PROCESO
		if self.ListProcCargTableWidget.rowCount() == 0:
			f = open('ColaDeProcesosEj1b.txt', 'r')
			line = f.readline() # fila con nombres de campos (no interesa)
			line = f.readline() # por eso leenmos de nuevo
			while line != '':
				line = line.split(',')
				# nuevas filas y columnas en la tabla
				self.ListProcCargTableWidget.setRowCount(self.ListProcCargTableWidget.rowCount()+1) 
				# self.ListProcCargTableWidget.setColumnCount(self.ListProcCargTableWidget.columnCount()+1)
				# se crea un "item" nuevo y se alinea su contenido
				proc=QtWidgets.QTableWidgetItem(str(line[0]))
				proc.setTextAlignment(Qt.AlignCenter) 		
				tam=QtWidgets.QTableWidgetItem(str(line[1]))
				tam.setTextAlignment(Qt.AlignCenter)
				ta=QtWidgets.QTableWidgetItem(str(line[2]))
				ta.setTextAlignment(Qt.AlignCenter)
				raf=QtWidgets.QTableWidgetItem(line[3].rstrip('\n')+'')
				# raf.setTextAlignment(Qt.AlignCenter)
				self.ListProcCargTableWidget.setItem(self.ListProcCargTableWidget.rowCount()-1,0,proc)
				self.ListProcCargTableWidget.setItem(self.ListProcCargTableWidget.rowCount()-1,1,tam)
				self.ListProcCargTableWidget.setItem(self.ListProcCargTableWidget.rowCount()-1,2,ta)
				self.ListProcCargTableWidget.setItem(self.ListProcCargTableWidget.rowCount()-1,3,raf)
				# por si quiere cargar otro proceso, que el id ya sea otro
				self.IdProcSpinBox.setValue(self.ListProcCargTableWidget.rowCount()+1)
				line = f.readline()
			f.close()
		else:
			pass
			# no se que poner xd 

	def borrar_lista_procesos(self):
		i=0
		while self.ListProcCargTableWidget.rowCount()>0:
			self.ListProcCargTableWidget.removeRow(i)
		self.IdProcSpinBox.setValue(self.ListProcCargTableWidget.rowCount()+1)

	def borrar_un_proceso(self):
		borrar = []
		nf = self.ListProcCargTableWidget.rowCount()
		for i in range(nf):
			if self.ListProcCargTableWidget.item(i,0).isSelected():
				borrar.append(i)
		for i in borrar:
			self.ListProcCargTableWidget.removeRow(i)
		if self.ListProcCargTableWidget.rowCount() == 0:
			self.IdProcSpinBox.setValue(1)
		else:
			self.actualizar_procesos()

	def actualizar_procesos(self):
		nf = int(self.ListProcCargTableWidget.rowCount())
		for i in range(nf):
			self.ListProcCargTableWidget.item(i,0).setText(str(i))

	def agregar_particion(self):
		# FALTA EL CONTROL DE NO PASARSE CON EL TAMAÑO DE LA PARTICION
		self.NroEspacioDispLabel.setText(str(self.TamMemSpinBox.value()))
		if (self.TamPartSpinBox.value() != 0):
			tam_part = self.TamPartSpinBox.value()
			if tam_part <= int(self.NroEspacioDispLabel.text()):
				self.ParticionesTableWidget.setRowCount(self.ParticionesTableWidget.rowCount()+1)
				# numero de particion
				# los numeros de particion comienzan en 1, porque 0 es la particiones del SO
				self.ParticionesTableWidget.setItem(self.ParticionesTableWidget.rowCount()-1,0,QTableWidgetItem(str(self.ParticionesTableWidget.rowCount()+1)))
				# tamaño de la particion 
				self.ParticionesTableWidget.setItem(self.ParticionesTableWidget.rowCount()-1,1,QTableWidgetItem(str(tam_part)))
				# alinear contenido
				self.ParticionesTableWidget.item(self.ParticionesTableWidget.rowCount()-1,0).setTextAlignment(Qt.AlignCenter)
				self.ParticionesTableWidget.item(self.ParticionesTableWidget.rowCount()-1,1).setTextAlignment(Qt.AlignCenter)

				# con lo siguiente no se puede editar, pero tampoco seleccionar como por ejemplo para eliminar...
				# self.ParticionesTableWidget.item(self.ParticionesTableWidget.rowCount()-1,0).setFlags(QtCore.Qt.ItemIsEnabled)
				# self.ParticionesTableWidget.item(self.ParticionesTableWidget.rowCount()-1,1).setFlags(QtCore.Qt.ItemIsEnabled)
				self.actualizar_particion()
				self.TamPartSpinBox.setStyleSheet("background-color: rgb(255,255,255);")#blanco
			else:
				self.TamPartSpinBox.setStyleSheet("background-color: rgb(255,0,0);")#rojo
		else:
			self.TamPartSpinBox.setStyleSheet("background-color: rgb(255,0,0);")#rojo

	def eliminar_particion(self):
		borrar = []
		nf = self.ParticionesTableWidget.rowCount()
		for i in range(nf):
			if self.ParticionesTableWidget.item(i,0).isSelected() or self.ParticionesTableWidget.item(i,1).isSelected():
				borrar.append(i)
		for i in borrar:
			self.ParticionesTableWidget.removeRow(i)
		self.actualizar_particion()

	def actualizar_particion(self):
		# restante = 0
		ocupado = 0 
		nf = int(self.ParticionesTableWidget.rowCount())
		for i in range(nf):
			self.ParticionesTableWidget.item(i,0).setText(str(i+1))
			if self.ParticionesTableWidget.item(i,1).text() != '':
				ocupado = ocupado + int(self.ParticionesTableWidget.item(i,1).text())
		restante = self.TamMemSpinBox.value() - ocupado
		self.NroEspacioDispLabel.setText(str(restante))

	def agregar_rafaga(self):
		# agrega columna
		self.ProcActualTableWidget.setColumnCount(self.ProcActualTableWidget.columnCount()+1)
		# pregunta por entrada o salida 
		if (self.EntradaRadioButton.isChecked()):
			self.ProcActualTableWidget.setItem(0, self.ProcActualTableWidget.columnCount()-1, QTableWidgetItem('E'))
		if (self.SalidaRadioButton.isChecked()):
			self.ProcActualTableWidget.setItem(0, self.ProcActualTableWidget.columnCount()-1, QTableWidgetItem('S'))
		# pone 0 al valor de tiempo
		self.ProcActualTableWidget.setItem(1, self.ProcActualTableWidget.columnCount()-1, QTableWidgetItem('0'))
		# alinea el contenido
		self.ProcActualTableWidget.item(0,self.ProcActualTableWidget.columnCount()-1).setTextAlignment(Qt.AlignCenter)
		self.ProcActualTableWidget.item(1,self.ProcActualTableWidget.columnCount()-1).setTextAlignment(Qt.AlignCenter)
		# agrega si o si otra rafaga de CPU, tiempo 0, alinea 
		self.ProcActualTableWidget.setColumnCount(self.ProcActualTableWidget.columnCount()+1)
		self.ProcActualTableWidget.setItem(0, self.ProcActualTableWidget.columnCount()-1, QTableWidgetItem('CPU'))
		self.ProcActualTableWidget.setItem(1, self.ProcActualTableWidget.columnCount()-1, QTableWidgetItem('0'))
		self.ProcActualTableWidget.item(0,self.ProcActualTableWidget.columnCount()-1).setTextAlignment(Qt.AlignCenter)
		self.ProcActualTableWidget.item(1,self.ProcActualTableWidget.columnCount()-1).setTextAlignment(Qt.AlignCenter)
	
	def agregar_proceso(self):
		# FALTA LIMPIAR LOS CAMPOS DE COMPLETAR PROCESOS, 
		# SINO QUEDAN LOS QUE CARGASTE RECIEN. 
		# FALTA CONTROLAR QUE NO CARGUES UN PROCESO CON UN ID YA CARGADO
		if (self.IdProcSpinBox.value()) != 0 and (self.TamProcSpinBox.value()) != 0:
			if (self.verificar_rafagas()):
				self.ListProcCargTableWidget.setRowCount(self.ListProcCargTableWidget.rowCount()+1)

				id_proc = QTableWidgetItem(str(self.IdProcSpinBox.value()))
				id_proc.setTextAlignment(Qt.AlignCenter)

				arribo = QTableWidgetItem(str(self.TASpinBox.value()))
				arribo.setTextAlignment(Qt.AlignCenter)

				tam = QTableWidgetItem(str(self.TamProcSpinBox.value()))
				tam.setTextAlignment(Qt.AlignCenter)

				rafaga = ''
				nc = self.ProcActualTableWidget.columnCount()
				for i in range(nc):
					rafaga = rafaga + self.ProcActualTableWidget.item(0,i).text() + ': ' + self.ProcActualTableWidget.item(1,i).text() + '; '
				raf_item = QTableWidgetItem(rafaga)

				self.ListProcCargTableWidget.setItem(self.ListProcCargTableWidget.rowCount()-1, 0, id_proc)
				self.ListProcCargTableWidget.setItem(self.ListProcCargTableWidget.rowCount()-1, 1, tam)
				self.ListProcCargTableWidget.setItem(self.ListProcCargTableWidget.rowCount()-1, 2, arribo)
				self.ListProcCargTableWidget.setItem(self.ListProcCargTableWidget.rowCount()-1, 3, raf_item)

				self.IdProcSpinBox.setValue(self.ListProcCargTableWidget.rowCount()+1)

				i = 1 # siempre dejamos una columna para la cpu 
				while (self.ProcActualTableWidget.columnCount()) > 1:
					self.ProcActualTableWidget.removeColumn(i)
				self.ProcActualTableWidget.item(1,0).setText('0')

		else:
			if self.IdProcSpinBox.value() == 0:
				self.IdProcSpinBox.setStyleSheet("background-color: rgb(255,0,0);")

	def verificar_rafagas(self):
		# ProcActualTableWidget es donde se cargan las rafagas (mal nombre)
		nc = self.ProcActualTableWidget.columnCount()
		for i in range(nc):
			if (self.ProcActualTableWidget.item(1,i) == None or int(self.ProcActualTableWidget.item(1,i).text()) == 0):
			# if int(self.ProcActualTableWidget.item(1,i).text()) == 0:
				self.ProcActualTableWidget.item(1,i).setBackground(QColor("#FF0000")) # rojo
				return False
		self.limpiar_tabla_ragafas()
		return True

	# por si previamente cargaste mal, entonces no te aparece en rojo
	def limpiar_tabla_ragafas(self):
		nc = self.ProcActualTableWidget.columnCount()
		for i in range(nc):
			self.ProcActualTableWidget.item(1,i).setBackground(QColor("#FFFFFF")) # blanco

	def salida_borrable(self):
		# label_21 : cola cpu
		# label_26 : cola suspendidos
		# label_27 : cola cargados en memoria

		# usamos como ejemplo el ejericio 1.a de la guia: Administración de Memoria Contigua
		self.TamMemSpinBox.setValue(128)
		self.AlgortimoComboBox.setCurrentIndex(0)
		self.FirstRadioButton.setChecked(True)
		self.FijasRadioButton.setChecked(True)
		self.clickEvent()

		self.cargar_tabla_procesos()

		# Particiones
		self.ParticionesTableWidget.setRowCount(self.ParticionesTableWidget.rowCount()+1)
		self.ParticionesTableWidget.setItem(self.ParticionesTableWidget.rowCount()-1,0,QTableWidgetItem(str(self.ParticionesTableWidget.rowCount()+1)))
		self.ParticionesTableWidget.setItem(self.ParticionesTableWidget.rowCount()-1,1,QTableWidgetItem(str(6)))
		self.ParticionesTableWidget.item(self.ParticionesTableWidget.rowCount()-1,0).setTextAlignment(Qt.AlignCenter)
		self.ParticionesTableWidget.item(self.ParticionesTableWidget.rowCount()-1,1).setTextAlignment(Qt.AlignCenter)
		self.actualizar_particion()
		self.ParticionesTableWidget.setRowCount(self.ParticionesTableWidget.rowCount()+1)
		self.ParticionesTableWidget.setItem(self.ParticionesTableWidget.rowCount()-1,0,QTableWidgetItem(str(self.ParticionesTableWidget.rowCount()+1)))
		self.ParticionesTableWidget.setItem(self.ParticionesTableWidget.rowCount()-1,1,QTableWidgetItem(str(20)))
		self.ParticionesTableWidget.item(self.ParticionesTableWidget.rowCount()-1,0).setTextAlignment(Qt.AlignCenter)
		self.ParticionesTableWidget.item(self.ParticionesTableWidget.rowCount()-1,1).setTextAlignment(Qt.AlignCenter)
		self.actualizar_particion()
		self.ParticionesTableWidget.setRowCount(self.ParticionesTableWidget.rowCount()+1)
		self.ParticionesTableWidget.setItem(self.ParticionesTableWidget.rowCount()-1,0,QTableWidgetItem(str(self.ParticionesTableWidget.rowCount()+1)))
		self.ParticionesTableWidget.setItem(self.ParticionesTableWidget.rowCount()-1,1,QTableWidgetItem(str(70)))
		self.ParticionesTableWidget.item(self.ParticionesTableWidget.rowCount()-1,0).setTextAlignment(Qt.AlignCenter)
		self.ParticionesTableWidget.item(self.ParticionesTableWidget.rowCount()-1,1).setTextAlignment(Qt.AlignCenter)
		self.actualizar_particion()

		self.TamPartSpinBox.setValue(70)
		self.EspacioOcupProgressBar.setProperty("value", 75)
		self.NroEspacioDispLabel.setText('0')

		self.SegundoSpinBox.setValue(1)
		
		barra = '#################################'
		self.HistPlanifTextEdit.append(barra)

		# Tiempo 0 
		salida = 'Tiempo: 0\n' + 'CL: 1,2\n' + 'CS: 0\n' + 'CPU: 1'
		self.HistPlanifTextEdit.append(salida)
		barra = '#################################'
		self.HistPlanifTextEdit.append(barra)
		# self.label_21.setText('1,2')
		# self.label_27.setText('1')
		# self.PartOcupTextEdit.setPlainText('2,3')

		# Tiempo 1
		salida = 'Tiempo: 1\n' + 'CL: 1,2,4\n' + 'CS: 0\n' + 'CPU: 1'
		self.HistPlanifTextEdit.append(salida)
		barra = '#################################'
		self.HistPlanifTextEdit.append(barra)
		self.label_21.setText('1,2,4')
		self.label_27.setText('1')
		self.PartOcupTextEdit.setPlainText('1,2,3')

		# Tiempo 2
		salida = 'Tiempo: 2\n' + 'CL: 1,2,4\n' + 'CS: 0\n' + 'CPU: 1'
		self.HistPlanifTextEdit.append(salida)
		barra = '#################################'
		self.HistPlanifTextEdit.append(barra)



	def mostrarDiagramaGantt(self):
		plt.title('Diagrama de Gantt',size=15)
		plt.xlabel('Tiempo',size=12)
		plt.ylabel('Procesos',size=12)

		# [0,0] [0,0] NI IDEA, 
		# marker = marcador , 
		# ls = linestyle, 
		# mec = color del borde de marker
		# ms = tam de marker,
		#  alpha = NI IDEA, 
		# label = pone en "legend" algo 
		plt.plot([0,0],[0,0], marker="^", ls="dashed", color="lime", mec="black", ms=10, alpha=1.0 ,label="Arribo del proceso")
		plt.plot([0,0],[0,0], marker="v", ls="dashed", color="red", mec="black", ms=10, alpha=1.0 ,label="Fin del proceso")
		# para que no molesten el medio del grafico
		plt.plot([0,0],[0,0],marker="^",ls="dashed",color="white",ms=10,alpha=1.0)
		plt.plot([0,0],[0,0],marker="v",ls="dashed",color="white",ms=10,alpha=1.0)
		plt.legend()
		plt.show()



		# TRIBUTO A FACUNDO	
		#self.TamMemSpinBox.setSingleStep()

# Instancia que da inicio al programa
app = QtWidgets.QApplication(sys.argv)
# crea un objeto ventana de la clase ui
window = Ui()
# mostrar ventana
window.show()
# ejecutar 
app.exec_()

