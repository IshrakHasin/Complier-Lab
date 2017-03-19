
import re
import keyword as ks

f = open('input1.txt', 'r+')


for line in f:
      integer_list = line.split()
      c=0
      for s in integer_list:

          #a= re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*", s)
          a = re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*", s)
          #Numval.extend(a)
          c=c+1
          #print a
          if len(a)==c:
              print 'Accept'

          else:
              print'reject'
