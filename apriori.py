class Apriori:
    def __init__(self,parm):
        self.dbase = parm
        self.reset()
        
    def reset(self):
        self.candidates_sz = 1
        self.support_history = dict() 
        self.candidates = {}
        for x in self.dbase:
            self.candidates[x] = [(a,) for a in self.dbase[x]]

        self.current = {}
        for x,v in self.candidates.items():
            for itemset in v:
                if itemset in self.current:
                    self.current[itemset].add(x)
                else:
                    self.current[itemset] = set([x])

    def support(self,val:float):
        a={x:len(v)/len(self.dbase) 
           for x,v in self.current.items()}
        return{x: v for x,v in a.items() if v>= val}
    
    def scan_dbase(self,val:float):
        d = self.support(val)
        self.support_history.update(d)
        self.current = {x: v for x,v in self.current.items() if x in self.support_history}
                
    def Lk(self):
        return sorted(self.current.keys())

    
        
                    
        

#==================================================================

