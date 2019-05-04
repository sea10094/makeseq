import os

class Client():
   

   def __init__(self, clients_dir):
       self.sqllist = []
       try:
         files = os.listdir(clients_dir)
       except:
         print('no dir named %s') %clients_dir 
         exit(1)
       if files == []:
         print('no execute seq in dir')
         exit(1)

       for i in files:
           f = open(clients_dir + '/' + i)
           l = []
           for s in f.readlines():
               l.append(s.strip())
               self.sqllist.append(l)
