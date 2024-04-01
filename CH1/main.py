import numpy as np
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
from src import PolyCurveFitting

if __name__=='__main__':
    N = 15
    coeff_vector = np.array([0.2,2.89,-24.43,19.37])
    x = np.linspace(0,1,N,endpoint=False)
    
    data = np.empty(N, dtype=object)
    for i in range(N):
        data[i] = np.sin(2*np.pi*(i/N))
    
    noise = np.random.normal(0,0.3,N)
    y = data + noise

    total_error = 10
    error_min = 1e-5
    nu = 0.03
    
    polyObject = PolyCurveFitting.PolyCurveFit(coeff_vector,x,y)

    while total_error > error_min:
        error_old = polyObject.SSE(coeff_vector)
        gradE = polyObject.GradientComp(coeff_vector)
        coeff_vector = polyObject.updateCoefficient(coeff_vector,gradE,nu)
        error_new = polyObject.SSE(coeff_vector)
        total_error = np.abs(error_old - error_new)
        print(total_error)
    

    # Plot
    #print(coeff_vector)
    plt.plot(x, y, 'bo')
    plt.plot(x,polyObject.PolyArray(coeff_vector),'r')
    plt.show()