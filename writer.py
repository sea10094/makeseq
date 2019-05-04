import os

class Writer():

   def __init__(self, output):
       osstr1 = 'mkdir -p ' + output
       osstr2 = 'rm -f ' + output + '/*' 

       os.system(osstr1)
       os.system(osstr2)
       self.output = output
       

   def todo(self, seqlist):
       count = 0 
       for seq in seqlist:
           count += 1
           f = open(self.output + '/' + str(count), 'w') 
           for s in seq:
               f.write(s)
               f.write('\r\n')
       print('make seq files ok, pls find these in output dir')
