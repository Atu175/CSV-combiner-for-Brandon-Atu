import pandas
import sys
p = sys.argv[0]
x = sys.argv[1]
y = sys.argv[2]
pathx = x.split("/")
pathy = y.split("/")
df1 = pandas.read_csv(x)
df1.insert(2, 'filename', pathx[1])
df2 = pandas.read_csv(y)
df2.insert(2, 'filename', pathy[1])
merged = pandas.concat([df1, df2])
merged.to_csv("answer.csv")
