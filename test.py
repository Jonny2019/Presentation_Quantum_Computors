from dwave.system import EmbeddingComposite, DWaveSampler

# Define the problem as two Python dictionaries: 
#   h for linear terms, J for quadratic terms


# Kreuzung einfach
h = {0,0,0,0}
J = {
    (0, 1): 1,
    (0, 3): 1,
    (1, 2): 1,
    (2, 3): 1
}

# Schachbrett 3 x 3
h = {0,0,0,0}
J = {
    (0, 1): 1,
    (0, 3): 1,
    (1, 2): 1,
    (1, 4): 1,
    (2, 5): 1,
    (3, 4): 1,
    (3, 6): 1,
    (4, 5): 1,
    (4, 7): 1,
    (5, 8): 1
}

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
sampleset = sampler.sample_ising(h, J, num_reads = 10)
print(sampleset)