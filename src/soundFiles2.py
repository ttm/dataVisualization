import pickle, numpy as n

durations, powers, spectral, sounds, srates = pickle.load(open('../data/sFiles.pickle', 'rb'))

data = n.vstack((durations, powers, spectral)).T

# take zscore of each column
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

# if we wanted to study how the measurements combine into the principal components
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



