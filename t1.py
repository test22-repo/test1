def test1():
  f = open('testing_read.txt','w')
  f.write('sup fam')
  f.close()
  f = open('testing_read.txt','r')
  print(f.read())
test1()
