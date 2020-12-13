
data = []
for n in range(0,748):
    data.append(input().strip())

import numpy as np

def rotate(orientation, degrees):
    theta = np.radians(degrees)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((c, -s), (s,c)))
    new_orient = np.matmul(R, orientation)
    return new_orient

#part 1
sOri = np.array([[1], [0]])
sPos = np.array([[0], [0]])
pos = sPos.copy()
orient = sOri.copy()
for l in data:
    if l[0] == "N":
        pos[1] = pos[1] + int(l[1:])
    elif l[0] == "S":
        pos[1] = pos[1] - int(l[1:])
    elif l[0] == "E":
        pos[0] = pos[0] + int(l[1:])
    elif l[0] == "W":
        pos[0] = pos[0] - int(l[1:])
    elif l[0] == "L":
        orient = rotate(orient, +int(l[1:]))
    elif l[0] == "R":
        orient = rotate(orient, -int(l[1:]))
    elif l[0] == "F":
        pos = pos + int(l[1:]) * orient

man_dist = abs(pos[0]) + abs(pos[1])
print(man_dist[0])

#part 2
sOri = np.array([[1], [0]])
sPos = np.array([[0], [0]])
pos = sPos.copy()
wPos = np.array([[10], [1]]).copy()

for l in data:
    if l[0] == "N":
        wPos[1] = wPos[1] + int(l[1:])
    elif l[0] == "S":
        wPos[1] = wPos[1] - int(l[1:])
    elif l[0] == "E":
        wPos[0] = wPos[0] + int(l[1:])
    elif l[0] == "W":
        wPos[0] = wPos[0] - int(l[1:])
    elif l[0] == "L":
        wPos = rotate(wPos, +int(l[1:]))
    elif l[0] == "R":
        wPos = rotate(wPos, -int(l[1:]))
    elif l[0] == "F":
        pos = pos + int(l[1:]) * wPos

man_dist = abs(pos[0]) + abs(pos[1])
print(man_dist[0])