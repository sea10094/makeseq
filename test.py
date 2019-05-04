from make_seq import MakeSeq
from make_seq import MakeSeqEx
from clients import Client 


          


if __name__ == '__main__':
   client = Client('sqlfiles', 'output')
   mse = MakeSeqEx()
   seqlist = mse.make_seq_extend(client.sqllist)
   count = 0 
   for seq in seqlist:
       count += 1
       f = open('output/' + str(count), 'w') 
       for s in seq:
           f.write(s)
           f.write('\r\n')
   print('make seq files ok, pls find these in output dir')
   exit(0)
       
