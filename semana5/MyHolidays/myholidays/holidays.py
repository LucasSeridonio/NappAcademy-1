from datetime import date, datetime

class MyCalendar:
    def __init__(self, *args):
        self.datas = []
        for item in args:            
            if isinstance(item, date): 
                if item in self.datas:
                    continue
                else:
                    self.datas.append(item)
            else:
                try:
                    if isinstance(item, str):
                        if item in self.datas:
                            continue
                        else:
                            dt =  datetime.strptime(item, '%d/%m/%Y')
                            self.datas.append(dt)
                except:
                    pass


    def add_holiday(self, *args):              
        for item in args:       
            if isinstance(item, date):
                if item in self.datas:
                    continue
                else:   
                    self.datas.append(item)                                
            else:
                try:
                    if isinstance(item, str):
                        dt =  datetime.strptime(item, '%d/%m/%Y')
                        if dt in self.datas:
                            continue
                        else:   
                            self.datas.append(dt)
                except:
                    pass


    def check_holiday(self, *args): 
        for item in args:                        
            if isinstance(item, date): 
                if item in self.datas:
                    return True 
                else:
                    return False                  
            else: 
                try:
                    if isinstance(item, str):
                        dt =  datetime.strptime(item, '%d/%m/%Y')
                        if dt in self.datas:
                            return True
                        else:
                            return False
                except:
                    return False
                    pass
