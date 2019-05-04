from make_seq import MakeSeq
from make_seq import MakeSeqEx
from clients import Client 
from writer import Writer


          


if __name__ == '__main__':
   client = Client('sqlfiles')
   mse = MakeSeqEx()
   seqlist = mse.make_seq_extend(client.sqllist)
   wt = Writer('output')
   wt.todo(seqlist)
   exit(0)
       
