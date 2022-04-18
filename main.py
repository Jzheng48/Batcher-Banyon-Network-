# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 16:19:04 2022

@author: User
"""



import random

port_number={0:'A1',1:'A2',2:'A3',3:'A4',4:'A5',5:'A6',6:'A7',7:'A8',
             8:'A1',9:'A2',10:'A3',11:'A4',12:'A5',13:'A6',14:'A7',15:'A8'}
port_number8={0:'B1',1:'B2',2:'B3',3:'B4',
              4:'B1',5:'B2',6:'B3',7:'B4'}
class START:

  def __init__(self, port,innum):
    self.portnumber = port
    
    self.pathway=[]
    if innum==16:
        self.binary="{0:04b}".format(port) 
        self.pathway.append(port_number[port])

    if innum==8:
        self.binary="{0:03b}".format(port) 
        self.pathway.append(port_number8[port])
        
            

  def path_AtoB(self, num):
      ab = {
        'A1': ['B1', 'B5'],
        'A2': ['B2', 'B6'],
        'A3': ['B3', 'B7'],
        'A4': ['B4', 'B8'],
        'A5': ['B1', 'B5'],
        'A6': ['B2', 'B6'],
        'A7': ['B3', 'B7'],
        'A8': ['B4', 'B8']
         }
      
      if self.binary[num]=="0":
           self.pathway.append((ab[self.pathway[num]])[0])
      else:
          self.pathway.append((ab[self.pathway[num]])[1])
  

  def path_BtoC(self,num):
       bc={
        'B1': ['C1', 'C3'],
        'B2': ['C2', 'C4'],
        'B3': ['C1', 'C3'],
        'B4': ['C2', 'C4'],
        'B5': ['C5', 'C7'],
        'B6': ['C6', 'C8'],
        'B7': ['C5', 'C7'],
        'B8': ['C6', 'C8']
        }

       if self.binary[num]=="0":
           self.pathway.append((bc[self.pathway[num]])[0])
       else:
          self.pathway.append((bc[self.pathway[num]])[1])

  def path_CtoD(self,num):
      cd={
        'C1': ['D1', 'D2'],
        'C2': ['D1', 'D2'],
        'C3': ['D3', 'D4'],
        'C4': ['D3', 'D4'],
        'C5': ['D5', 'D6'],
        'C6': ['D5', 'D6'],
        'C7': ['D7', 'D8'],
        'C8': ['D7', 'D8']
        }

      if self.binary[num]=="0":
           self.pathway.append((cd[self.pathway[num]])[0])
      else:
          self.pathway.append((cd[self.pathway[num]])[1])

  def path_DtoO(self,num):
      do={
        'D1': ['0','1'],
        'D2': ['2','3'],
        'D3': ['4','5'],
        'D4': ['6','7'],
        'D5': ['8','9'],
        'D6': ['10','11'],
        'D7': ['12','13'],
        'D8': ['14','15']
        }

      if self.binary[num]=="0":
           self.pathway.append((do[self.pathway[num]])[0])
      else:
          self.pathway.append((do[self.pathway[num]])[1])

#=========================================================================
#Banyon network 

def input16(listb):
    for i in listb:
        i.path_AtoB(0)
        i.path_BtoC(1)
        i.path_CtoD(2)
        i.path_DtoO(3)
        
      
def input8(listb):
    for i in listb:
       
        i.path_BtoC(0)
        i.path_CtoD(1)
        i.path_DtoO(2)
        
        
#=====================================================================     
    
        

#innum = input("Enter number of inputs(8 or 16): ")
innum=int(16)

list=[]

while len(list)<innum:
    r=random.randint(0,innum-1)
    if r not in list: list.append(r)
#=============================================

print("Random Generator:",list)
#==============================
#Batcher Sorter 

list=sorted(list)
listb=[]
for i in list:
    
    port=START(i,innum)
    listb.append(port)
if innum==8:
    input8(listb)
elif innum==16:
    input16(listb)

for i in listb:
    print("Path for"+str(i.portnumber),"->"+"->".join(i.pathway))

    
