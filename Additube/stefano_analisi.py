from pybotics.robot import Robot
from pybotics.predefined_models import ur10
from pybotics.tool import Tool
import numpy as np
import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import sys

from pybotics.predefined_models import ur10


def filtpost(vec_in):
    for cnt in range(1,vec_in.size):
        while True:
            if round(np.abs(vec_in[cnt-1]-vec_in[cnt])/np.pi) > 0 :
                vec_in[cnt] = vec_in[cnt] + (np.sign(vec_in[cnt-1]-vec_in[cnt]) * 2 * np.pi)
                continue
            break
    return vec_in

with open(sys.argv[1],"r") as f:
    lines = f.readlines()


START_LINE = 22

joints = np.zeros((6,len(lines[START_LINE:])),np.float32)
tmp_vec = np.zeros((len(lines[START_LINE:]),),np.float32)

for cnt,line in enumerate(lines[START_LINE:]):
    jnt_vec =  line.split()
    tmp_vec[cnt] = jnt_vec[0] 
    joints[:,cnt] = np.asarray(jnt_vec[1:7])


joints[1] = filtpost(joints[1])
joints[2] = filtpost(joints[2])



with open("robot_log_lungo.txt","r") as ftcp:
    linestcp = ftcp.readlines()

tcp_pos     = np.zeros((3,len(linestcp[1:])),np.float32)
tmp_vec_tcp = np.zeros((len(linestcp[1:]),),np.float32)

for cnt,line in enumerate(linestcp[1:]):
    jnt_vec =  line.split()
    tmp_vec_tcp[cnt] = jnt_vec[1] 
    tcp_pos[:,cnt] = np.asarray(jnt_vec[2:5])


if len(sys.argv) == 3 and sys.argv[2] == "plot_tcp":
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(tcp_pos[0], tcp_pos[1], tcp_pos[2], 'gray')
    # ax.scatter(tcp_pos[0], tcp_pos[1], tcp_pos[2], 'gray')
    plt.show()


if len(sys.argv) == 3 and sys.argv[2] == "plot":
    figjoy, axjoy = plt.subplots(6, 1)
    axjoy[0].plot(tmp_vec, joints[0],label="j0")
    axjoy[1].plot(tmp_vec, joints[1],label="j1")
    axjoy[2].plot(tmp_vec, joints[2],label="j2")
    axjoy[3].plot(tmp_vec, joints[3],label="j3")
    axjoy[4].plot(tmp_vec, joints[4],label="j4")
    axjoy[5].plot(tmp_vec, joints[5],label="j5")
    plt.show()

def irb4600() -> np.ndarray:
    return np.array(
        [
            [0        , 495   ,-np.pi/2 ,  175],
            [-np.pi /2, 0     , 0       ,  900],
            [0        , 0     ,-np.pi/2 ,  175],
            [0        , 960   , np.pi/2 ,    0],
            [0        , 0     ,-np.pi/2 ,    0],
            [np.pi    , 135   , 0       ,    0],
        ]
    )


robot = Robot.from_parameters(irb4600())
tool = Tool()
tool.position = [249.792,-2.99778,101.579]
tool.vector   = [1.570,-1.570,0]
robot.tool = tool

x_pos = []
y_pos = []
z_pos = []

# for tmp in np.linspace(0,6.28,200):
#     joints_in = np.deg2rad([0,0,0,tmp,0,0])
#     pose = robot.fk(joints_in)
#     x_pos.append(pose[0,3])
#     y_pos.append(pose[1,3])
#     z_pos.append(pose[2,3])

# fig = plt.figure()
# ax = plt.axes(projection='3d')

# ax.plot3D(x_pos, y_pos, z_pos, 'gray')

# plt.show()

for cnt,tmp in enumerate(tmp_vec):    
    joints_in = np.deg2rad([joints[0][cnt],joints[1][cnt],joints[2][cnt],joints[3][cnt],joints[4][cnt],joints[5][cnt]])
    pose = robot.fk(joints_in)
    x_pos.append(pose[0,3])
    y_pos.append(pose[1,3])
    z_pos.append(pose[2,3])

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x_pos, y_pos, z_pos, 'gray')

plt.show()