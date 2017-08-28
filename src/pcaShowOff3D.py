import numpy as n, pylab as p
data = n.random.multivariate_normal([0,0,0],[[1,.9,.8],[.9,1,.95],[.8,.95,1]],1000)

# M = data
M = n.copy(data)
for i in range(M.shape[1]):
    if M[:, i].std():
        M[:, i]=(M[:, i]-M[:, i].mean())/M[:, i].std()
    else:
        M[:, i]=0.

#### make PCA
final_dimensions = 3

# convariance matrix:
C=n.cov(M.T,bias=1)

eig_values, eig_vectors = n.linalg.eig(C)

# Ordering eigenvalues and eigenvectors
args=n.argsort(eig_values)[::-1]
eig_values=eig_values[args]
eig_vectors=eig_vectors[:,args]
# retaining only some eigenvectors
feature_vec=eig_vectors[:,:final_dimensions]
final_data=n.dot(M,feature_vec)
x=final_data[:,0]
y=final_data[:,1]
# if final_dimensions=3 => z=final_data[:,3]

# to understand how the measurements combine into the principal components
eig_values_=100*eig_values/n.sum(n.abs(eig_values))
eig_vectors_=n.array([100*eig_vectors[:,i]/n.abs(eig_vectors[:,i]).sum() for i in range(eig_vectors.shape[1])]).T
feature_vec_=n.array([100*feature_vec[:,i]/n.abs(feature_vec[:,i]).sum() for i in range(feature_vec.shape[1])]).T


ver1 = n.array([(0,0,0),(1,0,0)])
# ver1 = n.array((1,0))
ver1_ = n.dot(ver1, feature_vec)

# ver2 = n.array((0,1))
ver2 = n.array([(0,0,0),(0,1,0)])
ver2_ = n.dot(ver2, feature_vec)

ver3 = n.array([(0,0,0),(0,0,1)])
ver3_ = n.dot(ver3, feature_vec)

# p.plot(xx,yy, "ro")
# p.plot(ver1_[:,0],ver1_[:,1],"g")
# p.plot(ver2_[:,1],ver2_[:,0],"b")
# p.plot(M[:,0],M[:,1], "ro")
# # p.show()
# p.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
fig = plt.figure()
# ax = fig.gca(projection='3D')
ax = fig.add_subplot(111, projection='3d')
ax.plot(M[:,0], M[:,1], M[:,2], "ro", ms=2)
# ax.plot(ver1_[:,0],ver1_[:,1],ver1_[:,2],"g")
# ax.plot(ver2_[:,0],ver2_[:,1],ver2_[:,2],"b")
# ax.plot(ver3_[:,0],ver3_[:,1],ver3_[:,2],"k")

v1 = n.vstack(([0,0,0], feature_vec[:,0]))
v2 = n.vstack(([0,0,0], feature_vec[:,1]))
v3 = n.vstack(([0,0,0], feature_vec[:,2]))
ax.plot(v1[:,0],v1[:,1],v1[:,2],"g")
ax.plot(v2[:,0],v2[:,1],v2[:,2],"b")
ax.plot(v3[:,0],v3[:,1],v3[:,2],"k")

p.show()
