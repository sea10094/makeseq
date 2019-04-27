import os


def init():
  os.system('mkdir -p output')
  os.system('rm -f output/*')
  sqllist = []
  files = os.listdir('sqlfiles')
  for i in files:
      f = open('sqlfiles/' + i)
      l = []
      for s in f.readlines():
          l.append(s.strip())
      sqllist.append(l)
  return sqllist
          





class Seq():
   
      seqlist = []

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
    

def make_seq_extend(sqllist):
    if len(sqllist) == 1:
       pass
    if len(sqllist) == 2:
       seq = Seq()
       seq.make_seq([], sqllist[0], sqllist[1])
       return seq.seqlist
    if len(sqllist) > 2:
       pass
           
           

if __name__ == '__main__':
   l = init()
   seqlist = make_seq_extend(l)
   count = 0 
   for seq in seqlist:
       count += 1
       f = open('output/' + str(count), 'w') 
       for s in seq:
           f.write(s)
           f.write('\r\n')
       
