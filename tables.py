from PyQt4 import QtCore, QtGui
import sys
import window
import dialog
import storage, maths
import json
import datetime




class Trade_table(object):
    """
    The class represents main table with all trades.
    """
    
    def setup(self, table, entries_number):
        """
        Installs cell headers names. Rows and columns numbers.
        """
        headers = ['Date', 'Time', 'Contract', 'Entry', 'Exit', 'Stop-loss', 'Positions', 'Result']
        Qt_headers = QtCore.QStringList(headers)
        table.setColumnCount(8)
        table.setRowCount(entries_number+5)
        table.setHorizontalHeaderLabels(Qt_headers)
    def all_trades(self, table, storage):
        """
        Puts all entries from the json list in the main table.
        """
        # table - QTableWidget object, storage - list of dicts
        i = 0
        list = storage
        
        # revesal sorting by date and time
        list.sort(key = lambda t: datetime.datetime.strptime(t['Date'], '%d.%m.%Y'), reverse=True)
        list.sort(key = lambda t: datetime.datetime.strptime(t['Time'], '%H %M'), reverse=True)
        
        # puts content of dicts in table rows
        for dict in list:
            
            table.setItem(i, 0, QtGui.QTableWidgetItem(dict['Date']))
            table.setItem(i, 1, QtGui.QTableWidgetItem(dict['Time']))
            table.setItem(i, 2, QtGui.QTableWidgetItem(dict['Contract']))
            table.setItem(i, 3, QtGui.QTableWidgetItem(dict['Entry point']))
            table.setItem(i, 5, QtGui.QTableWidgetItem(dict['Stop-loss']))
            table.setItem(i, 6, QtGui.QTableWidgetItem(dict['Positions']))
            if 'Exit' in dict:
                result = maths.result(dict['Contract'],dict,int(dict['Positions']))
                table.setItem(i,4,QtGui.QTableWidgetItem(dict['Exit']))
                table.setItem(i,7,QtGui.QTableWidgetItem(result))
            i+=1
    def open_trades(self, table, storage):
        """
        Puts only open trades from the json list in the main table.
        """
        i = 0
        list = storage
        
        list.sort(key = lambda t: datetime.datetime.strptime(t['Time'], '%H %M'))
        list.sort(key = lambda t: datetime.datetime.strptime(t['Date'], '%d.%m.%Y'))
        
        for dict in list:
            # only if trade is not closed
            if dict['Closed'] == False:
                table.setItem(i, 0, QtGui.QTableWidgetItem(dict['Date']))
                table.setItem(i, 1, QtGui.QTableWidgetItem(dict['Time']))
                table.setItem(i, 2, QtGui.QTableWidgetItem(dict['Contract']))
                table.setItem(i, 3, QtGui.QTableWidgetItem(dict['Entry point']))
                table.setItem(i, 5, QtGui.QTableWidgetItem(dict['Stop-loss']))
                table.setItem(i, 6, QtGui.QTableWidgetItem(dict['Positions']))
                i+=1

    def closed_trades(self,table, storage):
        """
        Puts only closed trades from the json list in the main table.
        """
        i = 0
        list = storage
        list.sort(key = lambda t: datetime.datetime.strptime(t['Time'],'%H %M'), reverse = True)
        list.sort(key = lambda t: datetime.datetime.strptime(t['Date'],'%d.%m.%Y'), reverse = True)
       
        for dict in list:
            if dict['Closed'] == True:
                table.setItem(i, 0, QtGui.QTableWidgetItem(dict['Date']))
                table.setItem(i, 1, QtGui.QTableWidgetItem(dict['Time']))
                table.setItem(i, 2, QtGui.QTableWidgetItem(dict['Contract']))
                table.setItem(i, 3, QtGui.QTableWidgetItem(dict['Entry point']))
                table.setItem(i, 4, QtGui.QTableWidgetItem(dict['Exit']))
                table.setItem(i, 5, QtGui.QTableWidgetItem(dict['Stop-loss']))
                table.setItem(i, 6, QtGui.QTableWidgetItem(dict['Positions']))
                result = maths.result(dict['Contract'], dict, int(dict['Positions']))
                table.setItem(i, 7, QtGui.QTableWidgetItem(result))
                i += 1
    
    def refresh_all(self, table, storage, entries):
        """
        Completely clears main table. Then sets up its parameters.
        Then puts in it all entries from json file.
        """
        
        table.clear()
        self.setup(table, entries)
        self.all_trades(table, storage)
    
    def refresh_open(self, table, storage, entries):
        """
        Completely clears main table. Then sets up its parameters.
        Then puts in open trades from json file.
        """

        table.clear()
        self.setup(table, entries)
        self.open_trades(table, storage)

    def refresh_closed(self, table, storage, entries):
        """
        Completely clears main table. Then sets up its parameters.
        Then puts in closed trades from json file.
        """
        table.clear()
        self.setup(table, entries)
        self.closed_trades(table, storage)
        
    
    def save_changes(self, table, json_path):
        """
        Scans all items from the main table and puts them into a json file
        """
        
        list = []
        i = 0
        
        # Scans talbe rows untill next row contract field is empy
        while table.item(i, 3) != None:
            # each row is a dict, each dict appends to list, list is written in json file
            dict = {}
            
            if table.item(i, 2) != None and table.item(i, 2) != "":
                dict['Contract'] = str(table.item(i, 2).text())
            else:
                dict['Contract'] = '1'
            
            dict['Entry point'] = str(table.item(i, 3).text())
            dict['Stop-loss'] = str(table.item(i, 5).text())
            dict['Closed'] = False
            
            if table.item(i, 6) != None and table.item(i, 6) != "":
                dict['Positions'] = str(table.item(i, 6).text())
            else:
                dict['Positions'] = '1'
            
            # if date/time fields is empty fills them with current time and date
            if table.item(i, 0) != None and table.item(i, 1) != None and table.item(i, 0) != "" and table.item(i,1) != "":
              
                dict['Date'] = str(table.item(i, 0).text())
                dict['Time'] = str(table.item(i, 1).text())
            else:
                dict['Date'], dict['Time'] = maths.datetime_format() 
                
            
            if table.item(i, 4) != None and table.item(i, 4) != '':
                
                dict['Exit'] = str(table.item(i, 4).text())
                dict['Closed'] = True
            i+=1
            list.append(dict)
        with open(json_path,'w') as file:
            json.dump(list, file, indent = 5)
        
            
        
class Add_table(object):
    """
    Class defines Add position table from the Add dialog.
    """
    
    def setup(self, table):
        """
        Setup cell headers, row, columns.
        """
        
        headers = ['Date', 'Time', 'Contract', 'Entry', 'Exit', 'Stop-loss', 'Positions']
        Qt_headers = QtCore.QStringList(headers)
        table.setColumnCount(7)
        table.setRowCount(1)
        table.setHorizontalHeaderLabels(Qt_headers)
        
    def accept(self, table, json_list, path):
        """
        Executes when Ok button in the Add dialog is pressed.
        """
        #reads entires list from json file
        list = json_list
        dict = {}
        
        # scans table into a dict
        dict['Contract'] = str(table.item(0, 2).text())
        dict['Entry point'] = str(table.item(0, 3).text())
        dict['Stop-loss'] = str(table.item(0, 5).text())
        dict['Closed'] = False
        dict['Positions'] = str(table.item(0, 6).text())
        if table.item(0,4) != None and str(table.item(0, 4).text()) != "":
            
            dict['Exit'] = str(table.item(0, 4).text())
            dict['Closed'] = True
        if table.item(0,0) != None and table.item(0, 1) != None and table.item(0, 0) != "" and table.item(0, 1) != "":
              
            dict['Date'] = str(table.item(0, 0).text())
            dict['Time'] = str(table.item(0, 1).text())
        else:
            dict['Date'], dict['Time'] = maths.datetime_format() 
            
        # appends this dict into the entries list
        list.append(dict)
        
        # writes updated list into a file
        with open(path, 'w') as file:
            json.dump(list,file, indent = 5)
        
    
        
class Statistic_table(object):
    """
    The class defines the table with strategy statistics data.
    """
    
    def setup(self, table):
        """
        Table setup.
        """
        
        headers = ['Expectancy', 'Exp per 1', 'Win-Loss ratio', 'Profit ratio',
        'Avg win', 'Avg Loss', 'Win %', 'Loss %', 'Balance', 'Max drdwn', 'Curr. drdwn', 'C/M']
        Qt_headers = QtCore.QStringList(headers)
        headers_v = ['']
        Qt_headers_v = QtCore.QStringList(headers_v)
        table.setColumnCount(12)
        table.setRowCount(1)
        table.setHorizontalHeaderLabels(Qt_headers)
        table.setVerticalHeaderLabels(Qt_headers_v)
        # sets a cell width
        table.horizontalHeader().setDefaultSectionSize(72);
        
    def statistic(self, table, stor_list):
        """
        Takes strategy statistic data from maths.statistic()
        and puts it into a table.
        """
        #takes list
        list =  maths.statistic(stor_list)
        
        # displays its elements in the table
        if list != None:
            i = 0
            
            while i < 12:
                
                table.setItem(0,i,QtGui.QTableWidgetItem(list[i]))
                
                i+=1
    def refresh(self, table, stor_list):
        """
        Updates statistic table items.
        """
        
        # clears whole table
        table.clear()
        # setups it again
        self.setup(table)
        # put the data f
        self.statistic(table, stor_list)
        
    
    
            
            
        