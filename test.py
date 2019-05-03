import os
from make_seq import MakeSeq
from make_seq import MakeSeqEx


def init():
  os.system('mkdir -p output')
  os.system('rm -f output/*')
  sqllist = []
  try:
     files = os.listdir('sqlfiles')
  except:
     print('no dir named sqlfiles')
     exit(1)
  if files == []:
     print('no execute seq in dir')
     exit(1)

  for i in files:
      f = open('sqlfiles/' + i)
      l = []
      for s in f.readlines():
          l.append(s.strip())
      sqllist.append(l)
  return sqllist
          








           
       
           
           

if __name__ == '__main__':
   l = init()
   mse = MakeSeqEx()
   seqlist = mse.make_seq_extend(l)
   count = 0 
   for seq in seqlist:
       count += 1
       f = open('output/' + str(count), 'w') 
       for s in seq:
           f.write(s)
           f.write('\r\n')
   print('make seq files ok, pls find these in output dir')
   exit(0)
       
