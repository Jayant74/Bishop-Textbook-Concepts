import numpy as np
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
# Class for all things Polynomial

class PolyCurveFit:
    
    def __init__(self,coeffecient_array, x, dataset):
        
        # local variables
        self.M = np.size(coeffecient_array)
        self.N = np.size(dataset)
        self.data = np.array(dataset)
        self.x = np.array(x)

    # Function evaluates a polynomial of order M, given a coefficients array, at value x
    def PolyVal(self, x, coeff_vector):
        val = 0
        for i in range(self.M):
            val += coeff_vector[i]*(x**i)   
        return val
    
    def PolyArray(self, coeff_vector):
        poly_array = np.empty(self.N)
        for i in range(self.N):
            poly_array[i] = self.PolyVal(self.x[i], coeff_vector)
        return poly_array
    
    # Compute gradient of E, args: target value array y; returns partial derivative for each coefficient w_i
    # returns array of partial derivative at each coefficient
    # dE/dw_i = SIGMA(y(x_n,w)-t_n)*x_n^(index of w_i)
    def GradientComp(self, coeff_vector):
        x = self.PolyArray(coeff_vector)
        PD_w_i = np.empty(self.N,dtype=float)
        gradE = np.empty(self.M,dtype=float) # Array to store partial derivative
        for j in range(self.M):
            for k in range(self.N): 
                PD_w_i[k] = (x[k] - self.data[k])*((self.x[k])**j)  
            dE_dw_i = np.sum(PD_w_i)   # sum all partial derivatives evaluated at index i
            gradE[j] = dE_dw_i  # store final partial derivative for each coefficient
        
        return gradE
    
    # Compute Sum of Square Error
    def SSE(self,coeff_vector):
        SSE_array = np.empty(self.N)
        for i in range(self.N):
            SSE_array[i] = (self.PolyVal(self.x[i],coeff_vector) - self.data[i])**2   
        E_w = 0.5*np.sum(SSE_array)
        
        return E_w
    
    # Update Coefficient Vector
    def updateCoefficient(self,new_coeff_vector,gradE_array,nu):
        for m in range(self.M):
            new_coeff_vector[m] = new_coeff_vector[m] - (nu*gradE_array[m])

        return new_coeff_vector

