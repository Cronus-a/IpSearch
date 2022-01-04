from tkinter import *
from tkinter import messagebox
import requests

global qry, stts, ctc, cty, rn

qry = 'REQUERID CONSULT'
stts = 'REQUERID CONSULT'
ctc = 'REQUERID CONSULT'
cty = 'REQUERID CONSULT'
rn = 'REQUERID CONSULT'

def Search():
 get = ip.get()
 rsp = requests.get('http://ip-api.com/json/'+get).json()
 stts = rsp['status']
 cty = rsp['city']
 qry = rsp['query']
 ctc = rsp['countryCode']
 rn = rsp['regionName']
 msg = f"""
 Ipv4: {qry}
 Status: {stts}
 Cidade: {cty}
 Ct. Code: {ctc}
 N. Região: {rn}
 
 """
 
 messagebox.showinfo(title="CONSULTA REALIZADA!", message=msg)

class Window(Tk):
 def __init__(self):
  self.app = Tk()
  self.name = 'IPSEARCH'
  self.app.title(self.name)
 def Run(self):
  Label(self.app, text='IPSEARCH', font='Courier 15', foreground="#cc33cc").grid(row=1, column=1)
  Label(self.app, text='Ipv4 or Url: ').grid(row=4, column=0)
  global ip
  ip = Entry(self.app)
  ip.grid(row=4, column=1)
  btn = Button(self.app, text='Search', foreground='#cc33cc', command=Search).grid(row=5, column=1)
  self.app.mainloop()
  
Window().Run()
