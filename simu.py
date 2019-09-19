# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulador.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventana(object):

    def setupUi(self, Ventana):

        Ventana.setObjectName("Ventana")
        Ventana.resize(858, 838)

        # centralwidget al parecer es como el widget donde se colocan los demas
        # no entiendo cual es la diferencia entre centralwidget y Ventana 

        # QtWidgets es la clase base de todos los widgets 
        # cuyas instancias sin un padre asignado se convertirán también en ventanas

        self.centralwidget = QtWidgets.QWidget(Ventana)
        self.centralwidget.setObjectName("centralwidget")

        # tabWidget es la especia de groupBox que esta tanto en Entrada como Salida pero no es una groupBox xd

        # QtCore contiene funcionalidad no GUI 
        # La clase QRect define un rectangulo en el plano, usando presicion entera
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 9, 821, 781))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded) # forma de las pestanias, puede ser Rounded o Triangular
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone) # como se elude el nombre de los elementos si no hay suficiente espacio para mostrarlos
        self.tabWidget.setObjectName("tabWidget")

        ## ----------------------------------PESTAÑA DE ENTRADA----------------------------------
        self.EntradaTab = QtWidgets.QWidget()         
        self.EntradaTab.setObjectName("EntradaTab")    

        self.EntradaDerGroupBox = QtWidgets.QGroupBox(self.EntradaTab)     
        self.EntradaDerGroupBox.setGeometry(QtCore.QRect(330, 20, 481, 721))
        self.EntradaDerGroupBox.setObjectName("EntradaDerGroupBox")

        self.NuevoProcGroupBox = QtWidgets.QGroupBox(self.EntradaDerGroupBox)
        self.NuevoProcGroupBox.setGeometry(QtCore.QRect(20, 30, 440, 280))
        self.NuevoProcGroupBox.setObjectName("NuevoProcGroupBox")

        self.IdProcLabel = QtWidgets.QLabel(self.NuevoProcGroupBox)
        self.IdProcLabel.setGeometry(QtCore.QRect(20, 30, 60, 20))
        self.IdProcLabel.setObjectName("IdProcLabel")

        self.TALabel = QtWidgets.QLabel(self.NuevoProcGroupBox)
        self.TALabel.setGeometry(QtCore.QRect(143, 30, 81, 20))
        self.TALabel.setObjectName("TALabel")

        self.TamProcLabel = QtWidgets.QLabel(self.NuevoProcGroupBox)
        self.TamProcLabel.setGeometry(QtCore.QRect(299, 30, 60, 20))
        self.TamProcLabel.setObjectName("TamProcLabel")

        self.IdProcSpinBox = QtWidgets.QSpinBox(self.NuevoProcGroupBox)
        self.IdProcSpinBox.setGeometry(QtCore.QRect(80, 30, 42, 22))
        self.IdProcSpinBox.setObjectName("IdProcSpinBox")

        # ESTE HAY QUE CAMBIAR DE LUGAR
        self.TASpinBox = QtWidgets.QSpinBox(self.NuevoProcGroupBox)
        self.TASpinBox.setGeometry(QtCore.QRect(229, 30, 50, 22))
        self.TASpinBox.setObjectName("TASpinBox")

        # ESTE HAY QUE CAMBIAR DE LUGAR
        self.TamProcSpinBox = QtWidgets.QSpinBox(self.NuevoProcGroupBox)
        self.TamProcSpinBox.setGeometry(QtCore.QRect(360, 30, 60, 22))
        self.TamProcSpinBox.setObjectName("TamProcSpinBox")

        self.CicloDeVidaLabel = QtWidgets.QLabel(self.NuevoProcGroupBox)
        self.CicloDeVidaLabel.setGeometry(QtCore.QRect(20, 100, 71, 16))
        # creacion de un objeto fuente
        # lo que no entiendo es por que no hace esto con todas ? 
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.CicloDeVidaLabel.setFont(font)
        self.CicloDeVidaLabel.setObjectName("CicloDeVidaLabel")

        self.ProcActualTableWidget = QtWidgets.QTableWidget(self.NuevoProcGroupBox)
        self.ProcActualTableWidget.setGeometry(QtCore.QRect(20, 140, 401, 90))
        self.ProcActualTableWidget.setObjectName("ProcActualTableWidget")
        self.ProcActualTableWidget.setColumnCount(1)    # cuantas columnas: 1
        self.ProcActualTableWidget.setRowCount(2)       # cuantas filas: 2 


        # NI IDEA ESTO 
        # parece que es la definicion de los items R, T
        item = QtWidgets.QTableWidgetItem()
        self.ProcActualTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ProcActualTableWidget.setVerticalHeaderItem(1, item)

        # self.ProcActualTableWidget.setVerticalHeaderItem(0, item)
        # item = self.ProcActualTableWidget.verticalHeaderItem(0)
        # item.setText(_translate("Ventana", "R"))

        # parece que es la defincion de a 
        item = QtWidgets.QTableWidgetItem()
        self.ProcActualTableWidget.setHorizontalHeaderItem(0, item) 
        # parece que es la definicion de los items CPU, 0

        item = QtWidgets.QTableWidgetItem()
        self.ProcActualTableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ProcActualTableWidget.setItem(1, 0, item)

        # item = QtWidgets.QTableWidgetItem()
        # self.ProcActualTableWidget.setItem(0, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.ProcActualTableWidget.setItem(1, 1, item)


        self.AgregarProcPushButton = QtWidgets.QPushButton(self.NuevoProcGroupBox)
        self.AgregarProcPushButton.setGeometry(QtCore.QRect(320, 240, 100, 30))
        self.AgregarProcPushButton.setObjectName("AgregarProcPushButton")

        # NO SE CUAL ES LA DIFERENCIA ENTRE ESTE Y (1)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.NuevoProcGroupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(160, 80, 261, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        # (1)
        self.AgregarEoSHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.AgregarEoSHorizontalLayout.setContentsMargins(0, 0, 0, 0)          # LA VERDAD QUE NI IDEA
        self.AgregarEoSHorizontalLayout.setObjectName("AgregarEoSHorizontalLayout")

        # 3 veces dfine, da nombre, y agrega con add
        self.EntradaRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.EntradaRadioButton.setObjectName("EntradaRadioButton")
        self.AgregarEoSHorizontalLayout.addWidget(self.EntradaRadioButton)

        self.SalidaRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.SalidaRadioButton.setObjectName("SalidaRadioButton")
        self.AgregarEoSHorizontalLayout.addWidget(self.SalidaRadioButton)

        self.AgregarPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.AgregarPushButton.setObjectName("AgregarPushButton")
        self.AgregarEoSHorizontalLayout.addWidget(self.AgregarPushButton)

        self.ListProcCargTableWidget = QtWidgets.QTableWidget(self.EntradaDerGroupBox)
        self.ListProcCargTableWidget.setGeometry(QtCore.QRect(20, 370, 440, 251))
        self.ListProcCargTableWidget.setObjectName("ListProcCargTableWidget")
        self.ListProcCargTableWidget.setColumnCount(4)
        self.ListProcCargTableWidget.setRowCount(0)

        self.INICIARPushButton = QtWidgets.QPushButton(self.EntradaDerGroupBox)
        self.INICIARPushButton.setGeometry(QtCore.QRect(350, 660, 101, 41))
        self.INICIARPushButton.setObjectName("INICIARPushButton")

        self.BorrarSeleccionPushButton = QtWidgets.QPushButton(self.EntradaDerGroupBox)
        self.BorrarSeleccionPushButton.setGeometry(QtCore.QRect(30, 670, 101, 31))
        self.BorrarSeleccionPushButton.setObjectName("BorrarSeleccionPushButton")

        self.BorrarTablaPushButton = QtWidgets.QPushButton(self.EntradaDerGroupBox)
        self.BorrarTablaPushButton.setGeometry(QtCore.QRect(160, 670, 101, 31))
        self.BorrarTablaPushButton.setObjectName("BorrarTablaPushButton")

        self.ListaProcCargLabel = QtWidgets.QLabel(self.EntradaDerGroupBox)
        self.ListaProcCargLabel.setGeometry(QtCore.QRect(30, 340, 131, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.ListaProcCargLabel.setFont(font)
        self.ListaProcCargLabel.setObjectName("ListaProcCargLabel")

        self.EntradaIzqGroupBox = QtWidgets.QGroupBox(self.EntradaTab)
        self.EntradaIzqGroupBox.setGeometry(QtCore.QRect(30, 20, 280, 721))
        self.EntradaIzqGroupBox.setObjectName("EntradaIzqGroupBox")

        self.PartFijaGroupBox = QtWidgets.QGroupBox(self.EntradaIzqGroupBox)
        self.PartFijaGroupBox.setGeometry(QtCore.QRect(-1, 139, 281, 271))
        self.PartFijaGroupBox.setTitle("")
        self.PartFijaGroupBox.setObjectName("PartFijaGroupBox")

        self.EliminarPartPushButton = QtWidgets.QPushButton(self.PartFijaGroupBox)
        self.EliminarPartPushButton.setGeometry(QtCore.QRect(150, 50, 75, 30))
        self.EliminarPartPushButton.setObjectName("EliminarPartPushButton")

        self.FijasRadioButton = QtWidgets.QRadioButton(self.EntradaIzqGroupBox)
        self.FijasRadioButton.setGeometry(QtCore.QRect(160, 120, 51, 17))
        self.FijasRadioButton.setObjectName("FijasRadioButton")

        self.AgregarPartPushButton = QtWidgets.QPushButton(self.PartFijaGroupBox)
        self.AgregarPartPushButton.setGeometry(QtCore.QRect(60, 50, 75, 30))
        self.AgregarPartPushButton.setObjectName("AgregarPartPushButton")

        self.PartLabel = QtWidgets.QLabel(self.EntradaIzqGroupBox)
        self.PartLabel.setGeometry(QtCore.QRect(30, 90, 71, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.PartLabel.setFont(font)
        self.PartLabel.setObjectName("PartLabel")

        self.VariablesRadioButton = QtWidgets.QRadioButton(self.EntradaIzqGroupBox)
        self.VariablesRadioButton.setGeometry(QtCore.QRect(60, 120, 82, 17))
        self.VariablesRadioButton.setObjectName("VariablesRadioButton")

        self.ParticionesTableWidget = QtWidgets.QTableWidget(self.PartFijaGroupBox)
        self.ParticionesTableWidget.setGeometry(QtCore.QRect(40, 87, 201, 121))
        self.ParticionesTableWidget.setObjectName("ParticionesTableWidget")
        self.ParticionesTableWidget.setColumnCount(2)
        self.ParticionesTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ParticionesTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ParticionesTableWidget.setHorizontalHeaderItem(1, item)

        self.EspacioOcupProgressBar = QtWidgets.QProgressBar(self.PartFijaGroupBox)
        self.EspacioOcupProgressBar.setGeometry(QtCore.QRect(140, 217, 118, 23))
        self.EspacioOcupProgressBar.setProperty("value", 60)
        self.EspacioOcupProgressBar.setObjectName("EspacioOcupProgressBar")

        self.EspacioOcupLabel = QtWidgets.QLabel(self.PartFijaGroupBox)
        self.EspacioOcupLabel.setGeometry(QtCore.QRect(49, 220, 91, 16))
        self.EspacioOcupLabel.setObjectName("EspacioOcupLabel")

        self.EspacioDispLabel = QtWidgets.QLabel(self.PartFijaGroupBox)
        self.EspacioDispLabel.setGeometry(QtCore.QRect(49, 247, 111, 16))
        self.EspacioDispLabel.setObjectName("EspacioDispLabel")

        self.NroEspacioDispLabel = QtWidgets.QLabel(self.PartFijaGroupBox)
        self.NroEspacioDispLabel.setGeometry(QtCore.QRect(170, 250, 47, 13))
        self.NroEspacioDispLabel.setObjectName("NroEspacioDispLabel")

        self.MetAsigGroupBox = QtWidgets.QGroupBox(self.EntradaIzqGroupBox)
        self.MetAsigGroupBox.setGeometry(QtCore.QRect(20, 430, 240, 100))
        self.MetAsigGroupBox.setObjectName("MetAsigGroupBox")

        self.FirstRadioButton = QtWidgets.QRadioButton(self.MetAsigGroupBox)
        self.FirstRadioButton.setGeometry(QtCore.QRect(50, 30, 61, 17))
        self.FirstRadioButton.setObjectName("FirstRadioButton")

        self.BestRadioButton = QtWidgets.QRadioButton(self.MetAsigGroupBox)
        self.BestRadioButton.setGeometry(QtCore.QRect(50, 50, 61, 17))
        self.BestRadioButton.setObjectName("BestRadioButton")

        self.WorstRadioButton = QtWidgets.QRadioButton(self.MetAsigGroupBox)
        self.WorstRadioButton.setGeometry(QtCore.QRect(50, 70, 71, 17))
        self.WorstRadioButton.setObjectName("WorstRadioButton")

        self.AlgoritmoGroupBox = QtWidgets.QGroupBox(self.EntradaIzqGroupBox)
        self.AlgoritmoGroupBox.setGeometry(QtCore.QRect(20, 550, 240, 120))
        self.AlgoritmoGroupBox.setObjectName("AlgoritmoGroupBox")

        self.AlgortimoComboBox = QtWidgets.QComboBox(self.AlgoritmoGroupBox)
        self.AlgortimoComboBox.setGeometry(QtCore.QRect(20, 30, 200, 22))
        self.AlgortimoComboBox.setObjectName("AlgortimoComboBox")
        self.AlgortimoComboBox.addItem("")
        self.AlgortimoComboBox.addItem("")
        self.AlgortimoComboBox.addItem("")
        self.AlgortimoComboBox.addItem("")

        # lo mismo que antes, no se por que define dos veces 
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.AlgoritmoGroupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 70, 170, 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.QuantumHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.QuantumHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.QuantumHorizontalLayout.setObjectName("QuantumHorizontalLayout")

        self.QuantumLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.QuantumLabel.setObjectName("QuantumLabel")
        self.QuantumHorizontalLayout.addWidget(self.QuantumLabel)

        self.QuantumSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.QuantumSpinBox.setObjectName("QuantumSpinBox")
        self.QuantumHorizontalLayout.addWidget(self.QuantumSpinBox)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.PartFijaGroupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(60, 10, 160, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.TamPartHorizLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.TamPartHorizLayout.setContentsMargins(0, 0, 0, 0)
        self.TamPartHorizLayout.setObjectName("TamPartHorizLayout")

        self.TamPartLabel = QtWidgets.QLabel(self.PartFijaGroupBox)
        self.TamPartLabel.setObjectName("TamPartLabel")
        self.TamPartHorizLayout.addWidget(self.TamPartLabel)

        self.TamPartSpinBox = QtWidgets.QSpinBox(self.PartFijaGroupBox)
        self.TamPartSpinBox.setObjectName("TamPartSpinBox")
        self.TamPartHorizLayout.addWidget(self.TamPartSpinBox)

        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.EntradaIzqGroupBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 30, 231, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.TamMemHorizLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.TamMemHorizLayout.setContentsMargins(0, 0, 0, 0)
        self.TamMemHorizLayout.setObjectName("TamMemHorizLayout")

        self.TamMemLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.TamMemLabel.setObjectName("TamMemLabel")
        self.TamMemHorizLayout.addWidget(self.TamMemLabel)

        self.TamMemSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_4)
        # para poner un tamaño bastante grande de memoria
        self.TamMemSpinBox.setMaximum(999999)
        self.TamMemSpinBox.setObjectName("TamMemSpinBox")
        self.TamMemHorizLayout.addWidget(self.TamMemSpinBox)

        self.EntradaArribaLine = QtWidgets.QFrame(self.EntradaIzqGroupBox)
        self.EntradaArribaLine.setGeometry(QtCore.QRect(10, 70, 241, 20))
        self.EntradaArribaLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.EntradaArribaLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.EntradaArribaLine.setObjectName("EntradaArribaLine")

        self.EntradaAbajoLine = QtWidgets.QFrame(self.EntradaTab)
        self.EntradaAbajoLine.setGeometry(QtCore.QRect(49, 430, 241, 20))
        self.EntradaAbajoLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.EntradaAbajoLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.EntradaAbajoLine.setObjectName("EntradaAbajoLine")

        self.tabWidget.addTab(self.EntradaTab, "") # NO SE QUE ES 

        # ----------------------------------PESTAÑA DE SALIDA----------------------------------
        self.SalidaTab = QtWidgets.QWidget()
        self.SalidaTab.setObjectName("SalidaTab")

        self.ProcesamPorTiempoGroupBox = QtWidgets.QGroupBox(self.SalidaTab)
        self.ProcesamPorTiempoGroupBox.setGeometry(QtCore.QRect(70, 50, 291, 621))
        self.ProcesamPorTiempoGroupBox.setObjectName("ProcesamPorTiempoGroupBox")

        self.SalidaArribaLine = QtWidgets.QFrame(self.ProcesamPorTiempoGroupBox)
        self.SalidaArribaLine.setGeometry(QtCore.QRect(10, 20, 270, 16))
        self.SalidaArribaLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.SalidaArribaLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SalidaArribaLine.setObjectName("SalidaArribaLine")

        self.SalidaMedioLine = QtWidgets.QFrame(self.ProcesamPorTiempoGroupBox)
        self.SalidaMedioLine.setGeometry(QtCore.QRect(10, 100, 270, 16))
        self.SalidaMedioLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.SalidaMedioLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SalidaMedioLine.setObjectName("SalidaMedioLine")

        self.SalidaAbajoLine = QtWidgets.QFrame(self.ProcesamPorTiempoGroupBox)
        self.SalidaAbajoLine.setGeometry(QtCore.QRect(10, 480, 270, 16))
        self.SalidaAbajoLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.SalidaAbajoLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SalidaAbajoLine.setObjectName("SalidaAbajoLine")

        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.ProcesamPorTiempoGroupBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(140, 40, 131, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.SegundoHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.SegundoHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.SegundoHorizontalLayout.setObjectName("SegundoHorizontalLayout")

        self.SegundoLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.SegundoLabel.setObjectName("SegundoLabel")
        self.SegundoHorizontalLayout.addWidget(self.SegundoLabel)

        self.SegundoSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_5)
        self.SegundoSpinBox.setObjectName("SegundoSpinBox")
        self.SegundoHorizontalLayout.addWidget(self.SegundoSpinBox)

        self.SalidaVerticalLine = QtWidgets.QFrame(self.ProcesamPorTiempoGroupBox)
        self.SalidaVerticalLine.setGeometry(QtCore.QRect(120, 20, 20, 590))
        self.SalidaVerticalLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.SalidaVerticalLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SalidaVerticalLine.setObjectName("SalidaVerticalLine")

        self.ClockLabel = QtWidgets.QLabel(self.ProcesamPorTiempoGroupBox)
        self.ClockLabel.setGeometry(QtCore.QRect(50, 60, 47, 13))
        self.ClockLabel.setObjectName("ClockLabel")

        self.ColaCPULabel = QtWidgets.QLabel(self.ProcesamPorTiempoGroupBox)
        self.ColaCPULabel.setGeometry(QtCore.QRect(50, 200, 47, 20)) # 13
        self.ColaCPULabel.setObjectName("ColaCPULabel")

        self.ColaSuspLabel = QtWidgets.QLabel(self.ProcesamPorTiempoGroupBox)
        self.ColaSuspLabel.setGeometry(QtCore.QRect(30, 290, 81, 16))
        self.ColaSuspLabel.setObjectName("ColaSuspLabel")

        self.CargEnMemLabel = QtWidgets.QLabel(self.ProcesamPorTiempoGroupBox)
        self.CargEnMemLabel.setGeometry(QtCore.QRect(10, 370, 111, 31))
        self.CargEnMemLabel.setObjectName("CargEnMemLabel")

        self.IdsProcsLabel = QtWidgets.QLabel(self.ProcesamPorTiempoGroupBox)
        self.IdsProcsLabel.setGeometry(QtCore.QRect(160, 120, 101, 20))
        self.IdsProcsLabel.setObjectName("IdsProcsLabel")

        self.PartOcupLabel = QtWidgets.QLabel(self.ProcesamPorTiempoGroupBox)
        self.PartOcupLabel.setGeometry(QtCore.QRect(10, 530, 111, 16))
        self.PartOcupLabel.setObjectName("PartOcupLabel")

        self.IdPartLabel = QtWidgets.QLabel(self.ProcesamPorTiempoGroupBox)
        self.IdPartLabel.setGeometry(QtCore.QRect(150, 500, 47, 13))
        self.IdPartLabel.setObjectName("IdPartLabel")

        self.TamPartSalidaLabel = QtWidgets.QLabel(self.ProcesamPorTiempoGroupBox)
        self.TamPartSalidaLabel.setGeometry(QtCore.QRect(200, 500, 70, 13))
        self.TamPartSalidaLabel.setObjectName("TamPartSalidaLabel")

        self.PartOcupTextEdit = QtWidgets.QTextEdit(self.ProcesamPorTiempoGroupBox)
        self.PartOcupTextEdit.setGeometry(QtCore.QRect(140, 520, 131, 81))
        self.PartOcupTextEdit.setObjectName("PartOcupTextEdit")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.ProcesamPorTiempoGroupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 159, 121, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.IDsProcsVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.IDsProcsVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.IDsProcsVerticalLayout.setObjectName("IDsProcsVerticalLayout")

       # LABEL COLA CPU 
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.IDsProcsVerticalLayout.addWidget(self.label_21)


        # LABEL COLA SUSPENDIDOS
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_26.setObjectName("label_26")
        self.IDsProcsVerticalLayout.addWidget(self.label_26)

        # LABEL CARGADOS EN MEMORIA
        self.label_27 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_27.setObjectName("label_27")
        self.IDsProcsVerticalLayout.addWidget(self.label_27)

        self.HistDePlanifGroupBox = QtWidgets.QGroupBox(self.SalidaTab)
        self.HistDePlanifGroupBox.setGeometry(QtCore.QRect(430, 50, 341, 631))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.HistDePlanifGroupBox.setFont(font)

        self.HistDePlanifGroupBox.setObjectName("HistDePlanifGroupBox")
        self.HistPlanifTextEdit = QtWidgets.QTextEdit(self.HistDePlanifGroupBox)
        self.HistPlanifTextEdit.setGeometry(QtCore.QRect(30, 40, 281, 501))
        self.HistPlanifTextEdit.setObjectName("HistPlanifTextEdit")

        self.DiagramaGanttPushButton = QtWidgets.QPushButton(self.HistDePlanifGroupBox)
        self.DiagramaGanttPushButton.setGeometry(QtCore.QRect(30, 560, 111, 41))
        self.DiagramaGanttPushButton.setObjectName("DiagramaGanttPushButton")

        self.GuardarColaPushButton = QtWidgets.QPushButton(self.HistDePlanifGroupBox)
        self.GuardarColaPushButton.setGeometry(QtCore.QRect(200, 560, 111, 41))
        self.GuardarColaPushButton.setObjectName("GuardarColaPushButton")

        self.tabWidget.addTab(self.SalidaTab, "") # intuicion

        #---------------------------------------------------------------------------------------------------

        Ventana.setCentralWidget(self.centralwidget) # NI IDEA

        # status bar es la barra donde esta file etc etc
        self.statusbar = QtWidgets.QStatusBar(Ventana)
        self.statusbar.setObjectName("statusbar")
        Ventana.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(Ventana)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        Ventana.setMenuBar(self.menubar)

        self.actionCargar_Cola = QtWidgets.QAction(Ventana)
        self.actionCargar_Cola.setObjectName("actionCargar_Cola")

        self.menuFile.addAction(self.actionCargar_Cola)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Ventana)
        self.tabWidget.setCurrentIndex(0) # esto se usa para definir cual ventana mostrar primero
        QtCore.QMetaObject.connectSlotsByName(Ventana)

    def retranslateUi(self, Ventana):
        _translate = QtCore.QCoreApplication.translate
        Ventana.setWindowTitle(_translate("Ventana", "MainWindow"))
        self.EntradaDerGroupBox.setTitle(_translate("Ventana", "Procesos"))
        self.NuevoProcGroupBox.setTitle(_translate("Ventana", "Nuevo Proceso"))
        self.IdProcLabel.setText(_translate("Ventana", "ID Proceso"))
        self.TALabel.setText(_translate("Ventana", "Tiempo de Arribo"))
        self.TamProcLabel.setText(_translate("Ventana", "Tamaño (kB)"))
        self.CicloDeVidaLabel.setText(_translate("Ventana", "Ciclo de Vida"))
        item = self.ProcActualTableWidget.verticalHeaderItem(0)
        item.setText(_translate("Ventana", "R"))
        item = self.ProcActualTableWidget.verticalHeaderItem(1)
        item.setText(_translate("Ventana", "T"))
        item = self.ProcActualTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Ventana", "a"))
        __sortingEnabled = self.ProcActualTableWidget.isSortingEnabled()
        self.ProcActualTableWidget.setSortingEnabled(False)
        item = self.ProcActualTableWidget.item(0, 0)
        item.setText(_translate("Ventana", "CPU"))
        item = self.ProcActualTableWidget.item(1, 0)
        item.setText(_translate("Ventana", "0"))
        self.ProcActualTableWidget.setSortingEnabled(__sortingEnabled)
        self.AgregarProcPushButton.setText(_translate("Ventana", "Agregar Proceso"))
        self.EntradaRadioButton.setText(_translate("Ventana", "Entrada"))
        self.SalidaRadioButton.setText(_translate("Ventana", "Salida"))
        self.AgregarPushButton.setText(_translate("Ventana", "Agregar"))
        self.INICIARPushButton.setText(_translate("Ventana", "INICIAR"))
        self.BorrarSeleccionPushButton.setText(_translate("Ventana", "Borrar Selección"))
        self.BorrarTablaPushButton.setText(_translate("Ventana", "Borrar Tabla"))
        self.ListaProcCargLabel.setText(_translate("Ventana", "Lista de procesos cargados"))
        self.EntradaIzqGroupBox.setTitle(_translate("Ventana", "Memoria"))
        self.EliminarPartPushButton.setText(_translate("Ventana", "Eliminar"))
        self.FijasRadioButton.setText(_translate("Ventana", "Fijas"))
        self.AgregarPartPushButton.setText(_translate("Ventana", "Agregar"))
        self.PartLabel.setText(_translate("Ventana", "Particiones"))
        self.VariablesRadioButton.setText(_translate("Ventana", "Variables"))
        item = self.ParticionesTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Ventana", "Numero"))
        item = self.ParticionesTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Ventana", "Tamaño"))
        self.EspacioOcupLabel.setText(_translate("Ventana", "Espacio Ocupado"))
        self.EspacioDispLabel.setText(_translate("Ventana", "Espacio Disponible (kB):"))
        self.NroEspacioDispLabel.setText(_translate("Ventana", "N"))
        self.MetAsigGroupBox.setTitle(_translate("Ventana", "Metodo de Asignación"))
        self.FirstRadioButton.setText(_translate("Ventana", "First Fit"))
        self.BestRadioButton.setText(_translate("Ventana", "Best Fit"))
        self.WorstRadioButton.setText(_translate("Ventana", "Worst  Fit"))
        self.AlgoritmoGroupBox.setTitle(_translate("Ventana", "Algoritmo"))
        self.AlgortimoComboBox.setItemText(0, _translate("Ventana", "First Coming First Service (FCFS)"))
        self.AlgortimoComboBox.setItemText(1, _translate("Ventana", "Shorted Job First (SJF)"))
        self.AlgortimoComboBox.setItemText(2, _translate("Ventana", "Shorted Remain Time First (SRTF)"))
        self.AlgortimoComboBox.setItemText(3, _translate("Ventana", "Round Robin with Quantum (RRQ)"))
        self.QuantumLabel.setText(_translate("Ventana", "Quantum"))
        self.TamPartLabel.setText(_translate("Ventana", "Tamaño(kB)"))
        self.TamMemLabel.setText(_translate("Ventana", "Tamaño (kB)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EntradaTab), _translate("Ventana", "Entrada"))
        self.ProcesamPorTiempoGroupBox.setTitle(_translate("Ventana", "Procesamiento por tiempo"))
        self.SegundoLabel.setText(_translate("Ventana", "Segundo"))
        self.ClockLabel.setText(_translate("Ventana", "Clock"))
        self.ColaCPULabel.setText(_translate("Ventana", "Cola Listos"))
        self.ColaSuspLabel.setText(_translate("Ventana", "Cola Supendidos"))
        self.CargEnMemLabel.setText(_translate("Ventana", "Cargados en memoria"))
        self.IdsProcsLabel.setText(_translate("Ventana", "IDs de Procesos"))
        self.PartOcupLabel.setText(_translate("Ventana", "Particiones Ocupadas"))
        self.IdPartLabel.setText(_translate("Ventana", "ID Part."))
        self.TamPartSalidaLabel.setText(_translate("Ventana", "Tamaño (kB)"))
        self.label_21.setText(_translate("Ventana", "0"))
        self.label_26.setText(_translate("Ventana", "0"))
        self.label_27.setText(_translate("Ventana", "0"))
        self.HistDePlanifGroupBox.setTitle(_translate("Ventana", "Historial de Planificación"))
        self.DiagramaGanttPushButton.setText(_translate("Ventana", "Diagrama de Gantt"))
        self.GuardarColaPushButton.setText(_translate("Ventana", "Guardar Cola "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SalidaTab), _translate("Ventana", "Salida"))
        self.menuFile.setTitle(_translate("Ventana", "File"))
        self.actionCargar_Cola.setText(_translate("Ventana", "Cargar Cola"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ventana = QtWidgets.QMainWindow()
    ui = Ui_Ventana()
    ui.setupUi(Ventana)
    Ventana.show()
    sys.exit(app.exec_())
