import csv
from eegs.models import Trial, Patient, Channel
import os

lab = ['C3','C4','F3','F4','F7','F8','Fp1','Fp2','O1','O2','P3','P4','T3','T4','T5','T6']
tr = [35,25,10,33,1,22,3,32,18,38,47,37,29,39,46,28,59,40,46,37,19,17,2]
estado = [1,0,1,0,0,1,0,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,0]

lista_de_archivos = os.listdir('C:\\Users\\pao-m\\Desktop\\Yachay\\Prog. Web\\project4_estesi\\project4_new\\datos')
tr_id = 0

for counter in range(len(tr)):
   p = Patient()
   p.id = counter
   if estado[counter] == 0:
      p.state = "sano"
   else:
      p.state = "enfermo"
   p.save()
   for tri in range(tr[counter]):
      pid = Patient.objects.get(id=counter)
      t = Trial()
      t.patient = pid
      t.save()

os.chdir('C:\\Users\\pao-m\\Desktop\\Yachay\\Prog. Web\\project4_estesi\\project4_new\\datos')
cnt=1
for archivo in lista_de_archivos:
   f = open(archivo, 'r')
   aux=0
   for line in f:
      c = Channel()
      c.label = lab[aux]
      aux += 1
      c.values = line
      tr = Trial.objects.get(id=cnt)
      c.trial = tr
      c.save()
   f.close()
   cnt += 1


