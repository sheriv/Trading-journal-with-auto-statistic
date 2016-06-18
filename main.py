"""
This is a module that puts all other modules into action.
It creates all objects, connects and wrapper functions
"""

from PyQt4 import QtGui
import sys
import window
import dialog
import tables
import menu
import storage


def wrapper_refresh_all():
    """
    Refreshed the date using all trades.
    Calls refresh_all(Trades_table class) function in tables module
    """
    
    Tbl.refresh_all(Form_ui.tableWidget, Stor.init_list(), Stor.entries_count())


def wrapper_refresh_open():
    """
    Refreshed the date using only open trades.
    Calls refresh_open(Trades_table class) function in tables module
    """
    
    Tbl.refresh_open(Form_ui.tableWidget, Stor.init_list(), Stor.entries_count())


def wrapper_refresh_closed():
    """
    Refreshed the date using only closed trades.
    Calls refresh_closed(Trades_table class) function in tables module
    """
    
    Tbl.refresh_closed(Form_ui.tableWidget, Stor.init_list(), Stor.entries_count())
    

def wrapper_accept_add_table():
    """
    Saves new record in file. Refreshed the date using all trades.
    
    Receives signal from Ok button of Dlg_ui.ButtonBox
    then calls accept(Add_table class), refresh_all(Trades_table class),
    statistic(Statistic_table class) functions in tables
    module. After that closes dialog window
    """
    
    Add_Tbl.accept(Dlg_ui.tableWidget, Stor.init_list(), Stor.path)
    Tbl.refresh_all(Form_ui.tableWidget, Stor.init_list(), Stor.entries_count())
    St_Tbl.statistic(Form_ui.tableWidget2, Stor.init_list())
    Dlg.close()


def wrapper_save_changes():
    """
    Receives signal from Save/refresh button of Form_ui.saveBtn
    then calls save_changes(Trades_table class), refresh_all(Trades_table class),
    refresh(Statistic_table class) functions in tables module.
    After that closes dialog window
    """
    
    Tbl.save_changes(Form_ui.tableWidget, Stor.path)
    Tbl.refresh_all(Form_ui.tableWidget, Stor.init_list(), Stor.entries_count())
    St_Tbl.refresh(Form_ui.tableWidget2, Stor.init_list())


def wrapper_reject_add_table():
    """
    Closes Add dialog if cancel is pressed.
    """
    
    Dlg.close()
    

def wrapper_open_file_dialog():
    """
    Opens file dialog, saves new path to latest_path.txt,
    sets the file name as label text,
    initiates refresh of both tables, after changing 
    storage file path.
    """
    Menu.open_file_dialog(Form, Stor)
    Stor.new_path(Stor.path)
    Form_ui.label.setText(Menu.journal_name(Stor.path))
    Tbl.refresh_all(Form_ui.tableWidget, Stor.init_list(), Stor.entries_count())
    St_Tbl.refresh(Form_ui.tableWidget2, Stor.init_list())


def wrapper_save_file_dialog():
    """
    Opens file dialog, saves new path to latest_path.txt,
    changes storage object file path attribute,
    sets the file name as label text, calls save_changes
    initiates refresh of both tables.
    """
    Menu.save_file_dialog(Form, Stor)
    Stor.new_path(Stor.path)
    Form_ui.label.setText(Menu.journal_name(Stor.path))
    Tbl.save_changes(Form_ui.tableWidget, Stor.path)
    Tbl.refresh_all(Form_ui.tableWidget, Stor.init_list(), Stor.entries_count())
    St_Tbl.refresh(Form_ui.tableWidget2, Stor.init_list())


def wrapper_new_file_dialog():
    
    Menu.new_file_dialog(Form, Stor)
    Stor.new_path(Stor.path)
    Form_ui.label.setText(Menu.journal_name(Stor.path))
    Tbl.refresh_all(Form_ui.tableWidget, Stor.init_list(), Stor.entries_count())
    St_Tbl.refresh(Form_ui.tableWidget2, Stor.init_list())


def exit_from_menu():
    Form.close()


if __name__ == '__main__':
    # objects
    app = QtGui.QApplication(sys.argv)
    
    # main form objects: the form itself and its UI
    Form = QtGui.QMainWindow()
    Form_ui = window.Ui_Form()
    Form_ui.setupUi(Form)
    
    # Add position dialog object and its UI
    Dlg = QtGui.QDialog()
    Dlg_ui = dialog.Ui_Dialog()
    Dlg_ui.setupUi(Dlg)
    
    # Storage object which define current .json file path
    Stor = storage.Storage()
    Stor.setup()

    # Main table object and UI. Displaying all trades since
    # the program start
    Tbl = tables.Trade_table()
    Tbl.setup(Form_ui.tableWidget, Stor.entries_count())
    Tbl.all_trades(Form_ui.tableWidget, Stor.init_list())
    
    # Table from the Add dialog
    Add_Tbl = tables.Add_table()
    Add_Tbl.setup(Dlg_ui.tableWidget)

    # Main window menu object
    Menu = menu.Menu()
    Menu.setup(Form)
    
    # setting up label
    Form_ui.label.setText(Menu.journal_name(Stor.path))
    
    # Statistic table object. Displays statistic when program starts
    St_Tbl = tables.Statistic_table()
    St_Tbl.setup(Form_ui.tableWidget2)
    St_Tbl.statistic(Form_ui.tableWidget2, Stor.init_list())
    
    # connects
    
    # Add button from the main window. Starts Add dialog loop.
    Form_ui.addBtn.clicked.connect(Dlg.exec_)
    # All, Open, Closed radio buttons from the main window
    Form_ui.radioButton.toggled.connect(wrapper_refresh_all)
    Form_ui.radioButton_2.toggled.connect(wrapper_refresh_open)
    Form_ui.radioButton_3.toggled.connect(wrapper_refresh_closed)
    # Save/refresh button from main window
    Form_ui.saveBtn.clicked.connect(wrapper_save_changes)
    
    # Connects 'Open' from File menu in main window
    Menu.openFile.triggered.connect(wrapper_open_file_dialog)
    Menu.newFile.triggered.connect(wrapper_new_file_dialog)
    Menu.saveFile.triggered.connect(wrapper_save_file_dialog)
    Menu.exitFile.triggered.connect(exit_from_menu)
    
    # Connects Ok and Cancel button from the add dialog.
    Dlg_ui.buttonBox.accepted.connect(wrapper_accept_add_table)
    Dlg_ui.buttonBox.rejected.connect(wrapper_reject_add_table)

    Form.show()
    sys.exit(app.exec_())
