import json
import os

class Storage(object):
    def setup(self):
        #this attribute contains the path to json file
        #with trade entries
        #by default it's dump.json
        #self.path = 'dump.json'
        self.latest_path_storage = 'latest_path.txt'
        
        
        if os.path.exists(self.latest_path_storage) == True and  os.stat(self.latest_path_storage).st_size != 0:
            with open(self.latest_path_storage,'r') as file:
                self.path = file.read()
                
                if os.path.exists(self.path) == True:
                    
                    if  os.stat(self.path).st_size != 0:
                        
                        return self.path
                else:
                    
                    with open('latest_path.txt','w') as new_file:
                        self.path = os.path.abspath('new journal.json')
                        new_file.write(self.path)
                        
                        new_json = open('new journal.json', 'w')
                        new_json.close()
                
                        return self.path
        else:
            
            with open('latest_path.txt','w') as new_file:
                self.path = os.path.abspath('new journal.json')
                new_file.write(self.path)
                
                new_json = open('new journal.json', 'w')
                new_json.close()
                
                return self.path
            
            
            
            
        
    def new_path(self, new_path):
        #saves latest open path to menu.txt
        with open(self.latest_path_storage, 'w') as file:
            file.write(new_path)

    
    def init_list(self):
        """
        Checks if json file exists and not empty.
        If empty creates a new list, if not empty loads json file in list.
        List is used to remove the need in parsing json file.
        
        """
        Exists = False
        
        
        #checking if json file exists
        if os.path.exists(self.path) == True:
            Exists = True
        else:
            
            list = []
            return list
        
        #with open(path,'w') as file:
            #json.dump(list,file, indent = 5)
        
        
        #if json file exists and not empty load it into the list
        if Exists == True and os.stat(self.path).st_size != 0: 
            with open(self.path,'r') as file:
                list = json.load(file)
                return list
            
        else:
            
            list = []
            return list
        
    def entries_count(self):
        #returns dict number in list
        n = 0
        for dict in self.init_list():
            n +=1
        return n