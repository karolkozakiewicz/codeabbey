answer = []
d, h, m, s = 86400, 3600, 60, 1
n = int(input())
for i in range(n):
    x = input().split()
    d1, h1, m1, s1 = (d*int(x[0])), (h*int(x[1])), (m*int(x[2])), (s*int(x[3]))
    d2, h2, m2, s2 = (d*int(x[4])), (h*int(x[5])), (m*int(x[6])), (s*int(x[7]))
    d3, h3, m3, s3 = 0, 0, 0, 0
    sum1 = d1 + h1 + m1 + s1
    sum2 = d2 + h2 + m2 + s2
    difference = abs(sum1-sum2)
    s3 = difference%60 #sekundy
    difference = (difference - s3)/60 #z sekund na minuty
    m3 = difference%60 #minuty
    difference = (difference - m3)/60 #z minut na godziny
    h3 = difference%24 #godziny
    difference = (difference - h3)/24 #z godzin na dni
    d3 = difference%30 #dni
    answer.append(str("(")+str(int(d3)))
    answer.append(int(h3))
    answer.append(int(m3))
    answer.append(str(int(s3))+str(")"))
print(*answer) 
