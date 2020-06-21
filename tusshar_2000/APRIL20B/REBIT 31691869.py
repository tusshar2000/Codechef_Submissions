mod=998244353
#inverse modulo
def invmod(p,q):
    return ((p%mod)*(pow(q,mod-2,mod)%mod))%mod

#every time the sun comes up, I'm in trouble..
def and1(a,b):
    mylove=[0,0,0,0]
    
    mylove[0]=((a[0])%mod*(b[0])%mod)%mod
    mylove[0]+=((a[0])%mod*(b[1])%mod)%mod
    mylove[0]+=((a[0])%mod*(b[2])%mod)%mod
    mylove[0]+=((a[0])%mod*(b[3])%mod)%mod
    mylove[0]+=((a[2])%mod*(b[0])%mod)%mod
    mylove[0]+=((a[2])%mod*(b[3])%mod)%mod
    mylove[0]+=((a[1])%mod*(b[0])%mod)%mod
    mylove[0]+=((a[3])%mod*(b[0])%mod)%mod
    mylove[0]+=((a[3])%mod*(b[2])%mod)%mod
    
    mylove[1]=((a[1])%mod*(b[1])%mod)%mod
    
    mylove[2]=((a[2])%mod*(b[1])%mod)%mod
    mylove[2]+=((a[2])%mod*(b[2])%mod)%mod
    mylove[2]+=((a[1])%mod*(b[2])%mod)%mod
    
    mylove[3]=((a[1])%mod*(b[3])%mod)%mod
    mylove[3]+=((a[3])%mod*(b[1])%mod)%mod  
    mylove[3]+=((a[3])%mod*(b[3])%mod)%mod
    
    return mylove
    
def or1(a,b):
    mylove=[0,0,0,0]
    
    mylove[0]=((a[0])%mod*(b[0])%mod)%mod
    
    mylove[1]=((a[0])%mod*(b[1])%mod)%mod
    mylove[1]+=((a[1])%mod*(b[0])%mod)%mod
    mylove[1]+=((a[1])%mod*(b[1])%mod)%mod
    mylove[1]+=((a[1])%mod*(b[2])%mod)%mod
    mylove[1]+=((a[1])%mod*(b[3])%mod)%mod
    mylove[1]+=((a[2])%mod*(b[1])%mod)%mod
    mylove[1]+=((a[2])%mod*(b[3])%mod)%mod
    mylove[1]+=((a[3])%mod*(b[1])%mod)%mod
    mylove[1]+=((a[3])%mod*(b[2])%mod)%mod
    
    mylove[2]=((a[0])%mod*(b[2])%mod)%mod
    mylove[2]+=((a[2])%mod*(b[0])%mod)%mod
    mylove[2]+=((a[2])%mod*(b[2])%mod)%mod
    
    mylove[3]=((a[0])%mod*(b[3])%mod)%mod
    mylove[3]+=((a[3])%mod*(b[0])%mod)%mod
    mylove[3]+=((a[3])%mod*(b[3])%mod)%mod
    
    return mylove
    
def xor(a,b):
    mylove=[0,0,0,0]
    
    mylove[0]=((a[0])%mod*(b[0])%mod)%mod
    mylove[0]+=((a[1])%mod*(b[1])%mod)%mod
    mylove[0]+=((a[2])%mod*(b[2])%mod)%mod
    mylove[0]+=((a[3])%mod*(b[3])%mod)%mod
    
    mylove[1]+=((a[0])%mod*(b[1])%mod)%mod
    mylove[1]+=((a[1])%mod*(b[0])%mod)%mod
    mylove[1]+=((a[2])%mod*(b[3])%mod)%mod
    mylove[1]+=((a[3])%mod*(b[2])%mod)%mod
    
    mylove[2]+=((a[0])%mod*(b[3])%mod)%mod
    mylove[2]+=((a[1])%mod*(b[3])%mod)%mod
    mylove[2]+=((a[2])%mod*(b[0])%mod)%mod
    mylove[2]+=((a[3])%mod*(b[1])%mod)%mod
    
    mylove[3]+=((a[0])%mod*(b[3])%mod)%mod
    mylove[3]+=((a[1])%mod*(b[2])%mod)%mod
    mylove[3]+=((a[2])%mod*(b[1])%mod)%mod
    mylove[3]+=((a[3])%mod*(b[0])%mod)%mod
    
    return mylove

#took help from gfg for conversion and made changes the way I needed.    
class i_will_separate_your_head_from_your_soul: 
    def __init__(self, cap): 
        self.top=-1 
        self.cap=cap 
        self.arr=[] 
        self.op=[] 
        self.predator={'^':1, '&':1, '|':1} 
      
    def checkisEmpty(self): 
        if self.top == -1:
            return True
        else:
            return False
      
    def peek(self): 
        return self.arr[-1] 
      
    def pop(self): 
        if not self.checkisEmpty(): 
            self.top-=1
            return self.arr.pop() 
    
    #gonna listen to "push"-(by Enrique) after I get AC 
    def push(self, op): 
        self.top+=1
        self.arr.append(op)  
  
    def checkisOperand(self, ch): 
        return ch.isalpha() 
  
    def notGreater(self, i): 
        try: 
            a=self.predator[i] 
            b=self.predator[self.peek()] 
            if a<=b:
                return True
            else:
                False
                
        except KeyError:  
            return False
              
    def is_this_real(self, exp): 
        for i in exp: 
            if i=="#":
                self.op.append(i)
            
            elif self.checkisOperand(i): 
                self.op.append(i) 
              
            elif i=='(': 
                self.push(i) 
  
            elif i==')': 
                while((not self.checkisEmpty()) and self.peek() != '('): 
                    a = self.pop() 
                    self.op.append(a) 
                if (not self.checkisEmpty() and self.peek() != '('): 
                    return -1
                else: 
                    self.pop() 
  
            else: 
                while(not self.checkisEmpty() and self.notGreater(i)): 
                    self.op.append(self.pop()) 
                self.push(i) 
  
        while not self.checkisEmpty(): 
            self.op.append(self.pop()) 
  
        return "".join(self.op) 


t=int(input())
while t>0:
    blow_my_whistle=input()
    u_are_mine=i_will_separate_your_head_from_your_soul(len(blow_my_whistle)) 
    string=u_are_mine.is_this_real(blow_my_whistle)
    # print(string)
    stack=[]
    for i in string:
        if i=="#":
            stack.append([1,1,1,1])
        elif i=="&":
            stack.append(and1(stack.pop(),stack.pop()))
        elif i=="|":
            stack.append(or1(stack.pop(),stack.pop()))
        else:
            stack.append(xor(stack.pop(),stack.pop()))        
    finalans=[0]*4
    q=sum(stack[0])
    for i in range(4):
        finalans[i]=invmod(stack[0][i],q)
    print(*finalans)
    t-=1



