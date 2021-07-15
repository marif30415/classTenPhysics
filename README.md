Assalamu alaikum(Peace be upon you),

In the name of Allah


This is a helpful python package to solve many questions of class ten physics book (bd).
In this package, there are four modules:


1.work.py which calculates functions related energy, efficiency and power 

2.motion.py which calculates functions related velocity, acceleration, time and distance


3.light_reflection.py which calculates functions about plane mirror, convex and concave mirror. 
It also gives description of image depending on focus distance and distance of object from mirror.


4.electricity.py which calculates functions related to electricity, potential difference and resistances.

These modules ease solving many physics questions, helps to get right answer of the questions, saves time and energy in getting solution.

#TUTORIAL

All the functions of work.py,motion.py and electricity.py are written in the same way. So it is 
easy to use. For example, 

Question 1:
There is a 2 kg brick is on a 10-meter above wall. How much potential energy it has?
To solve this problem by this package, type as told here

1.from classTenPhysics import work

2.potential_energy = work.potential_energy(m=2,h=10)

3.print(potential_energy)

In terminal, the answer will be found, which is 196

light_reflection.py is slightly complex module, but it is not hard to use.

Question 2:
An object is 3 meter away from a convex mirror. The focus of this mirror is 6 meter. 
Where the image of the object will be seen? 
to solve this problem, type as told

1.from classTenPhysics import light_reflection

2.object = light_reflection.ConvexMirror(u=3,f=-6)

3.print(object.distance_of_image)

In terminal, the answer will be found, which is 6

Question 3:
Describe the image of the object. 
Solution: Delete line 3, then 

3.print(object.description_of_image)

*To get specific information(for example the state of the image):

3.print(object.description_of_image['state'])

In terminal, the answer will be found, which is 'straight'

Question 3:If the mirror is concave, where the image will be seen?
Solution: Delete line 2 and 3, then

2.object = light_reflection.ConcaveMirror(u=3,f=6)

3.print(object.distance_of_image)

Question 4:
Describe the image of the object.
Solution: In line 4

4.description = object.image(focus=-6,distance_of_object=3)

5.print(description)

Question 5:
Describe the size of the image.
Solution: Delete 5 line. Then

5.print(description['size'])

In terminal, the answer will be seen 'smaller than object'

#MORE HELP
For more help, e-mail me at marif30415@gmail.com
or, message me in facebook "Omayer Hasan Marif". Spread the advantages you have got using this package.
May Allah help all of us.




