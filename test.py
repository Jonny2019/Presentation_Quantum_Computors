from dwave.system import EmbeddingComposite, DWaveSampler

# Define the problem as two Python dictionaries: 
#   h for linear terms, J for quadratic terms
h = {} 
J = {
    (0,1): 1,
    (1,3): 1,
    (3,2): 1,
    (2,0): 1
} 

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
sampleset = sampler.sample_ising(h, J, num_reads = 10)
print(sampleset)