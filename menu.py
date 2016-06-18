from PyQt4 import QtCore, QtGui

class Menu(QtGui.QMenuBar):
    """
    Defines menu in the main window.
    """
        
        
    def setup(self, Form):
        
        #QMenuBar
        self.menubar = QtGui.QMenuBar(Form)
                        
        #'File' category
        fileMenu = self.menubar.addMenu('&File')
        
        #'New' in 'FIle'
        self.newFile = QtGui.QAction('New', Form)
        self.newFile.setShortcut('Ctrl+N')
        self.newFile.setStatusTip('Create new File')
        fileMenu.addAction(self.newFile)
        
        #'Open' in 'File'
        self.openFile = QtGui.QAction('Open', Form)
        self.openFile.setShortcut('Ctrl+O')
        self.openFile.setStatusTip('Open new File')
        fileMenu.addAction(self.openFile)

        # 'Save' in 'File'
        self.saveFile = QtGui.QAction('Save', Form)
        self.saveFile.setShortcut('Ctrl+S')
        self.saveFile.setStatusTip('Save file')
        fileMenu.addAction(self.saveFile)
        
        #'Exit' in 'File'
        self.exitFile = QtGui.QAction('Exit', Form)
        self.exitFile.setShortcut('Ctrl+E')
        self.exitFile.setStatusTip('Exit the program')
        fileMenu.addAction(self.exitFile)
       
        
        #self.menubar.setPalette(QtGui.QPalette(QtGui.QColor( 160 , 176, 201 )));
        #self.menubar.setStyleSheet("background-color: red;")
        self.menubar.setStyleSheet(
        """
        QMenuBar {
         background: blue;
        }

        QMenuBar::item {
         background: rgb(240,240,240);
        }""")
        self.menubar.adjustSize()
    def open_file_dialog(self, Form, storeob):
        """
        This func opens file dialog and assigns the path of the chosen file to
        storeob.path
        """
        storeob.path = QtGui.QFileDialog.getOpenFileName(Form, 'Open file')

    def new_file_dialog(self, Form, storeob):
        """
        Changes Storage object's path attribute.
        Creates .json file according to this path.
        """
        
        storeob.path = QtGui.QFileDialog.getSaveFileName(Form, 'New file','', '.json' )
        file = open(storeob.path, 'w')


    def save_file_dialog(self, Form, storeob):
        """
        Changes Storage object's path attribute.
        Creates .json file according to this path.
        """

        storeob.path = QtGui.QFileDialog.getSaveFileName(Form, 'Save file','', '.json' )
        file = open(storeob.path, 'w')

    
    def journal_name(self, string):
        """
        Extracts chosen file name from the string with
        the path to that file.
        """
        
        list = str(string).split('/')
        if len(list) == 1:
            list = str(string).split('\\')
       
        item = len(list) - 1
        last_chunk = list[item]
        
        
        #removing file type name
        display_name = last_chunk.split('.')[0]
        
        return display_name