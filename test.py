
import numpy as np
from BasicQuantumTheory import Particle

class TestBasicQuantumTheory(unittest.TestCase):
    def setUp(self):
        ket = np.array([1, 0, 0])
        ket_evolve = np.array([0, 1, 0])
        self.particle = Particle(3, ket, ket_evolve)
    
    def test_probability(self):
        self.assertAlmostEqual(self.particle.probability(0), 1.0)
        self.assertAlmostEqual(self.particle.probability(1), 0.0)
        self.assertAlmostEqual(self.particle.probability(2), 0.0)
    
    def test_transition_probability(self):
        other = Particle(3, np.array([0, 1, 0]), np.array([0, 0, 1]))
        self.assertAlmostEqual(self.particle.transition_probability(other), 0.0)
    
    def test_transition_amplitude(self):
        other = Particle(3, np.array([0, 1, 0]), np.array([0, 0, 1]))
        self.assertAlmostEqual(self.particle.transition_amplitude(other), 0.0)
    
    def test_mean_and_variance(self):
        observable = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
        mean, variance = self.particle.mean_and_variance(observable)
        self.assertAlmostEqual(mean, 1.0)
        self.assertAlmostEqual(variance, 0.0)
    
    def test_eigenvalues_and_probabilities(self):
        observable = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
        eigenvalues, eigenvectors, probabilities = self.particle.eigenvalues_and_probabilities(observable)
        self.assertListEqual(list(eigenvalues), [1, 2, 3])
        self.assertListEqual(list(probabilities), [1.0, 0.0, 0.0])
    
    def test_evolve(self):
        U_list = [np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])]
        final_ket = self.particle.evolve(U_list)
        print(final_ket)
        expected_ket = np.array([1, 0, 0])
        self.assertTrue(np.allclose(final_ket, expected_ket))
        
if __name__ == '__main__':
    unittest.main()
