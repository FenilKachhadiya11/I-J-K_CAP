class a:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j
        
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
    
class b(a):
    def __init__(self, i, j, k):
        # self.icap = i
        # self.jcap = j
        
        super().__init__(i, j)
        
        self.kcap = k
        
    def __str__(self):
        
        return f"{self.icap}i + {self.jcap}j +{self.kcap}k"
    
q = a(1,2)
w = b(1,2,3)


print(q)
print(w)
        