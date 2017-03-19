import re
import sys
f = open('input', 'r+')
N=int(f.readline())
#print N
escapes = ''.join([chr(char) for char in range(1, 32)])


line1=[]

for i in range(N):
    line=f.next().strip()
    line1.append(line)


print line1

#firstNlines=f.readlines()[0:N].s
#print firstNlines

M=int(raw_input("Give the number of texts "))
for i in range(M):
    text=raw_input()

   # print text
    checkmatch=False
    for j in range(N):
        temp1=line1[j].strip('')
        temp1=temp1.replace("'", "")
        temp1 = temp1.translate(None, escapes)
        # print temp1
        #temp0=a(bc)*de
        #temp1='r'+"'"+temp1+"'"
        temp1 = temp1.translate(None, escapes)
        #print temp1
        #if re.match(temp1,text):
            # print 'Yes %d'%j
             #checkmatch=True
        match = re.search(temp1, text)
        if match:
            c=j+1
            checkmatch = True
            print 'Yes %d for %s' % (c,text)

    if checkmatch == False:
        print "Reject for all RE %s." % text





