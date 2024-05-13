from room import Room
from building import Building

r = Room(name="9213", floor=2, num_seats=30)
r1  = Room(name="333", floor = 4, num_seats=12)
r2 = Room(name="612", floor= 6, num_seats=4)
print(r)

b = Building(name="SMI", address="Via Sierra Nevada",floors=5)
print(b)
print(len(b.get_room()))
b.add_room(r)
print(b)
print(len(b.get_room()))
add = b.add_room(r2)

print(add)