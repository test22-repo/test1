import sys

def test1():
  for x in sys.argv[1:]
  print(x)
  f = open('testing_read.txt','w')
  f.write('sup fam')
  f.close()
  f = open('testing_read.txt','r')
  print(f.read())
test1()
