import numpy as n

# use some real data: substitute the data variable below by something worth analyzing
data = n.random.random((100,20))

# take the zscore of each column
M = n.copy(data)
for i in range(M.shape[1]):
    if M[:, i].std():
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

# plot PCA
import pylab as p
p.clf()
p.plot(x, y, "ro", ms=3)
p.xlabel( 'first component')
p.ylabel('second component')
p.savefig("../figs/pcaSounds.png")

# Consider C, eig_values_ and eig_vectors_ for obtaining insights
