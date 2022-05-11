import numpy as np

Alpha = 0.5
DataSet = np.array([[1, -1, -1, -1], 
                    [1,  1, -1, -1], 
                    [1, -1,  1, -1], 
                    [1,  1,  1,  1]])

GateOutput = np.array([DataSet[0, 3], DataSet[1, 3], DataSet[2, 3], DataSet[3, 3]])
W = np.array([1, 1, 0.5])

Iteration = 1
for cont in range(12):  
    if (cont % 4) == 0:
        cont = 0    
    if ((cont -1) % 4) == 0:
        cont = 1 
    if ((cont -2) % 4) == 0:
        cont = 2
    if ((cont -3) % 4) == 0:
        cont = 3  

    PerceptronInput = np.array([DataSet[cont, 0], DataSet[cont, 1], DataSet[cont, 2]])
    PerceptronOutput = np.sign(np.dot(np.transpose(W), PerceptronInput))
    W = W + (Alpha*(GateOutput[cont] - PerceptronOutput) * PerceptronInput)
    print("Iteration #", Iteration)
    Iteration += 1
    print("     Perceptron Input:", PerceptronInput)
    print("     Iterative Comparison:", W)
    print("     Perceptron Output:", int(PerceptronOutput))