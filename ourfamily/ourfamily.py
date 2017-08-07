a=['1','2','3','who']
print a.index('who')



x=[4,6,2,1,7,9]
x.sort(reverse= False )
print x

x=['dlkjo','djhjsao','ddf','jkldfffd']
x.sort(key=len)
print x







print tuple ('456')
print tuple((1,2,3))
print list((1,2,3))

print 3*(40+9,)

x=[4,16,2,1,79,9]
x.sort(reverse= True)
print x



number=[59,23,9,7]
number.sort(cmp)
print number

l=sorted('python')
l.reverse()
print l


w=[2,8,4,6,10]
z=w[:]
z.sort()
print w,z


y=[2,1,3,5,6,7]
y.insert(3,4)
print y
print list(reversed(y))
y.sort()
print y
print y[0]



x=[1,2,3,6,7]
print x.pop(3)
x.insert(3,6)
print x
x.append(9)
print x
x.reverse()
print x
print list(reversed(x))



number=[1,2,3]
b=[4,7,3,9]
number.extend(b)
print number
print number.count(3)



