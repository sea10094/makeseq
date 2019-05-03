

class MakeSeq():
   
      def __init__(self):
          self.seqlist = []

      def make_seq(self, prelist, l1, l2):
          if len(l1) == 1 or len(l2) == 1:
             pre1 = prelist[:];pre1.extend(l1);pre1.extend(l2)
             pre2 = prelist[:];pre2.extend(l2);pre2.extend(l1)
             self.seqlist.append(pre1)
             self.seqlist.append(pre2)
          else:
             pre1 = prelist[:]
             pre1.append(l1[0])
             self.make_seq(pre1, l1[1:], l2)

             pre2 = prelist[:]
             pre2.append(l2[0])
             self.make_seq(pre2, l1, l2[1:])
    

class MakeSeqEx():
      total = []


      def make_seqlist_extend(self, seqlist, sqllist):
          for seq in seqlist:
              if len(sqllist) == 1:
                 ms = MakeSeq()
                 ms.make_seq([], seq, sqllist[0])
                 self.total.extend(ms.seqlist)
              else:
                 ms = MakeSeq()
                 ms.make_seq([], seq, sqllist[0])
                 self.make_seqlist_extend(ms.seqlist, sqllist[1:])
          return self.total 


      def make_seq_extend(self, sqllist):
          if len(sqllist) == 1:
             return sqllist
          if len(sqllist) == 2:
             ms = MakeSeq()
             ms.make_seq([], sqllist[0], sqllist[1])
             return seq.seqlist
          if len(sqllist) > 2:
             ms = MakeSeq()
             ms.make_seq([], sqllist[0], sqllist[1])
             return self.make_seqlist_extend(ms.seqlist, sqllist[2:])
