import os

class Client():
   

   def __init__(self, clients_dir, output):
       osstr1 = 'mkdir -p ' + output
       osstr2 = 'rm -f ' + output + '/*' 

       os.system(osstr1)
       os.system(osstr2)
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
