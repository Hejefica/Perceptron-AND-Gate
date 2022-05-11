import numpy as np

Alpha = 0.5
DataSet = np.array([[1, -1, -1, -1], 
                    [1,  1, -1, -1], 
                    [1, -1,  1, -1], 
                    [1,  1,  1,  1]])

GateOutput = np.array([DataSet[0, 3], DataSet[1, 3], DataSet[2, 3], DataSet[3, 3]])
IterationComparison = np.array([1, 1, 0.5])

Iteration = 1
for Cont in range(12):  
    if (Cont % 4) == 0:
        Cont = 0    
    if ((Cont -1) % 4) == 0:
        Cont = 1 
    if ((Cont -2) % 4) == 0:
        Cont = 2
    if ((Cont -3) % 4) == 0:
        Cont = 3  

    PerceptronInput = np.array([DataSet[Cont, 0], DataSet[Cont, 1], DataSet[Cont, 2]])
    PerceptronOutput = np.sign(np.dot(np.transpose(IterationComparison), PerceptronInput))
    IterationComparison = IterationComparison + (Alpha*(GateOutput[Cont] - PerceptronOutput) * PerceptronInput)
    
    print("Iteration #", Iteration)
    print("     Perceptron Input:", PerceptronInput)
    print("     Iteration Comparison:", IterationComparison)
    print("     Perceptron Output:", int(PerceptronOutput))
    Iteration += 1