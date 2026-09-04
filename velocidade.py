g=-9.8 #em m/s²
v0=25 
for i in range (51):
    t=i*0.1
    v=v0 + g*t
    print (t, v)
    if v <=0:
        break
    print ("A velocidade chegou a zero ou ficou negativa em t = ", t, " s")



'''
if v <= 0:
    print ("A velocidade chegou a zero ou ficou negativa. ")
for i in range(21):
    t = i * 0.1
    v = v0 + a * t
    print (t, v)
    if v <= 0:
        print ("Atingiu a altura máxima.")
        break
'''
    