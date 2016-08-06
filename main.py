
import sys
from PySide import QtCore, QtGui
import pyqtgraph as pg
import numpy as np
import time
import math

class MainWindow( QtGui.QMainWindow ):


	def __init__( self ):
		super( MainWindow, self ).__init__( None )

		self.m_baseWidget = QtGui.QWidget()
		self.m_baseLayout = QtGui.QHBoxLayout()

		self.m_graph = pg.PlotWidget()
		self.m_btnStart = QtGui.QPushButton( 'Start' )

		self.setCentralWidget( self.m_baseWidget )
		self.m_baseWidget.setLayout( self.m_baseLayout )
		self.m_baseLayout.addWidget( self.m_graph )
		self.m_baseLayout.addWidget( self.m_btnStart )

		self.m_timer = QtCore.QTimer( self )

		self.m_gTime = 0

		self.initUI()

	def initUI( self ):
		##QtCore.QObject.connect( self.m_btnStart, QtCore.SIGNAL( 'clicked()' ), self.onPlot )
		self.m_btnStart.clicked.connect( self.onPlot )

		self.connect( self.m_timer, QtCore.SIGNAL( 'timeout()' ), self.update )
		self.m_timer.start( 100 )

		self.show()

	def onPlot( self ):
		xx = []
		yy = []
		for q in range( 100 ):
			x = self.m_gTime + q * 2 * math.pi / 100
			xx.append( x )
			yy.append( math.sin( x ) )

		self.m_graph.plot( x=xx, y=yy, symbol='o' )
		print 'foooooo'

	def update( self ):
		self.m_gTime += 0.1

def main():
	print 'init application'
	app = QtGui.QApplication( sys.argv )
	gWindow = MainWindow()
	sys.exit( app.exec_() )

if __name__ == '__main__':
	print 'main'
	main()