

class Particle:
    def __init__(self, n, ket, ket_evolve):
        self.n = n
        self.ket = ket
        if np.linalg.norm(self.ket) != 1:
            self.ket = ket / np.linalg.norm(ket) # normalizar el vector ket
        self.ket_evolve = ket_evolve

        
    def probability(self, position):
        return abs(self.ket[position])**2
    
    def transition_probability(self, other):
        return abs(np.dot(self.ket.conj(), other.ket))**2
    
    def transition_amplitude(self, other):
        return np.dot(self.ket.conj(), other.ket)
    
    def mean_and_variance(self, observable):
        if not np.allclose(observable, observable.conj().T):
            print("La matriz observable no es hermitiana")
            return None
        else:
            bra=np.dot(observable,self.ket).conj().T
            mean = np.dot(bra,self.ket)
            delta = observable-mean*np.identity(len(observable))
            variance = np.dot(np.dot(np.dot(delta,delta),self.ket).conj().T,self.ket)
            
        return mean, variance
        
    def eigenvalues_and_probabilities(self, observable):
        if not np.allclose(observable, observable.conj().T):
            print("La matriz observable no es hermitiana")
            return None
        else:
            eigenvalues, eigenvectors = np.linalg.eigh(observable)
            probabilities = abs(np.dot(self.ket.conj(), eigenvectors)**2)
            return eigenvalues, eigenvectors, probabilities
        
    def evolve(self, U_list):
        U_matrix = np.zeros((self.n, self.n),                      dtype=np.complex128)
        for U in U_list:
            U_matrix += U
        final_ket = U_matrix @ self.ket_evolve
        return final_ket
    
