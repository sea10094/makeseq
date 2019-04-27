
f1 = open('sql1.txt')
f2 = open('sql2.txt')

l1 = []
l2 = []
for i in f1.readlines() :
    l1.append(i.strip())
for i in f2.readlines():
    l2.append(i.strip())


f = open('output.txt', 'a')

   

def make_seq(prelist, l1, l2):
    if len(l1) == 1 or len(l2) == 1:
       pre1 = prelist[:];pre1.extend(l1);pre1.extend(l2)
       pre2 = prelist[:];pre2.extend(l2);pre2.extend(l1)
       f.write(str(pre1));f.write('\r\n')
       f.write(str(pre2));f.write('\r\n')
    else:
       pre1 = prelist[:]
       pre1.append(l1[0])
       make_seq(pre1, l1[1:], l2)

       pre2 = prelist[:]
       pre2.append(l2[0])
       make_seq(pre2, l1, l2[1:])
    

if __name__ == '__main__':
   make_seq([], l1, l2)
       
