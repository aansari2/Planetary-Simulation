# Creator: Adil Ansari ------ # Hit P to begin.
# This is a simulation that simulates the solar system. The ratio is explained in line 5. Mousemovement + WASD + Z controls movement and mouselook
# Camera is a rijid body in orbit and although has a very negligible mass. WASD controls applyForce in respective directions
########################################################################################################################
factor = 1      #increase the factor to slow the simulation and decrease the factor to speed up the simulation #########
Data = False    #stats wont show if data = false andyou will have to HIT SPACE to show data ############################
########################################################################################################################
import bge
from bge import render
from mathutils import Vector
from math import *
own = bge.logic.getCurrentController().owner
scn = bge.logic.getCurrentScene()
j = scn.objects
g = 10**-3/factor**2
s = []
j['Sun'].mass = 333060.401628
j['Camera'].mass = 0.000001
for x in range(len(j)-1):
    if j[x]['prop'] == True:
        s.append(x)
if own['time'] < 1/59:
    for n in s:
        v = (333060.401628*g/j[n].position.magnitude)**(1/2)
        j[n].setLinearVelocity([0,v,0],0)
    j['Sun'].setLinearVelocity([0,0,0],0)
for n in s:
    s.remove(n)
    for x in s:
        f = -g*(j[n].position-j[x].position)/(j[n].position-j[x].position).magnitude**3*j[n].mass*j[x].mass
        j[n].applyForce(f,0)
        
    s.insert(n,n)
s.remove(8)
info = bge.logic.getSceneList()[1].objects['Text']
info2 = bge.logic.getSceneList()[1].objects['Text1']
vel=""
rad=""
for n in s:
    vel += str(j[n]) + "'s Speed = " + str("%.2f" % ((j[n].linearVelocity.magnitude*5.43/4.63)*(10**-2/g)**.5)) + " km/s\n"
for n in s:
    rad += "|"+str(j[n]) + "'s Radius = " + str("%.0f" % ((j[n].position-j['Sun'].position).magnitude*150/5.16753)) + " million kms\n"
if bge.logic.getCurrentController().sensors['Keyboard'].positive or Data == True:
    info2.text = "|Orbit Radius \n" + rad;info.text = "Years: " + str("%.5f" % (own['time']/(73.80815992012491/(g*333060.401628)**.5))) +"\n"+ vel;info2.size, info.size = .7,.7
else:
    info2.text,info.text = "","Years: " + str("%.5f" % (own['time']/(73.80815992012491/(g*333060.401628)**.5)))
t = 0
s.remove(0)
for n in s:
    while t < 2*pi:
        t+= pi/32
        p = j[n].position
        q = j['Sun'].position
        render.drawLine([q.x+(p-q).magnitude*cos(t),q.y+(p-q).magnitude*sin(t),0], [q.x+(p-q).magnitude*cos(t+pi/32),q.y+(p-q).magnitude*sin(t+pi/32),0],[1,1,1])
    t = 0
    render.drawLine(p,q,[.5,.5,.5])
rot = [0,0.72,-0.72,0.44,0.41,1.03,1,-243,0,58.65]
for n in s:
    spin = 365/rot[n]/factor
    j[n].setAngularVelocity([0,0,spin],0)
