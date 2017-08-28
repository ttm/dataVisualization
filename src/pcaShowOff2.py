import numpy as n, pylab as p

xx = n.linspace(5,50,1000)
yy = 3.4*xx-100

data = n.vstack((xx,yy)).T
data = n.random.multivariate_normal([0,0],[[1,.0],[.0,1]],1000)

data[:,0] = data[:,0]*.7+2 
data[:,1] = data[:,1]*100+50 

M = n.copy(data)
# M = data

M = n.copy(data)
for i in range(M.shape[1]):
    if M[:, i].std():
        # M[:, i]=(M[:, i]-M[:, i].mean())
        M[:, i]=(M[:, i]-M[:, i].mean())/M[:, i].std()
    else:
        M[:, i]=0.


#### make PCA
final_dimensions = 2

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

p.plot(M[:,0],M[:,1], "ro", ms=2)
# p.show()

ver1 = n.array([(0,0),(1,0)])
# ver1 = n.array((1,0))
ver1_ = n.dot(ver1, feature_vec)

# ver2 = n.array((0,1))
ver2 = n.array([(0,0),(0,1)])
ver2_ = n.dot(ver2, feature_vec)

v1 = n.vstack(([0,0], feature_vec[:,0]))
v2 = n.vstack(([0,0], feature_vec[:,1]))

# p.plot(xx,yy, "ro")
p.plot(v1[:,0],v1[:,1], "g")
p.plot(v2[:,0],v2[:,1], "b")
p.show()
