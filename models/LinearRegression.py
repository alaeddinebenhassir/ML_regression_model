import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt

def normalize(data):
    normalized_data=(data-data.mean())/data.std()
    return normalized_data

def denormalize(thetas ,x ,y):
    seg_x = x.std()
    seg_y = y.std()
    mean_x = x.mean()
    mean_y = y.mean()
    theta1 = (seg_y/seg_x)*thetas[1]
    theta0 = seg_y*(thetas[0] - thetas[1]*(mean_x / seg_x) )+ mean_y
    
    return np.array([theta0 , theta1])


def gradient(x ,y):
    
    #ndf = normalize(df)
    x_n = np.array(normalize(x))
    y_n = np.array(normalize(y))
    itr = 10000
    lr = 0.01
    n= len(x_n)
    x_bar = np.c_[np.ones(x_n.shape),x_n]
   
    thetas = np.array([x_n[0], y_n[0]])
    
    for i in range(itr):
        
        h_o = np.dot( x_bar,thetas)
       
        error = h_o -y_n 
        
        cost = (1/(n))*sum((error)**2)

        thetas = thetas - (2/n)*lr*np.dot(x_bar.T,error)
    Y = thetas[0] + thetas[1]*x_n 
    print("[  normalized space  ] >> theta_0 :{}  theta_1 :{} ".format( thetas[0] ,thetas[1] ))
    print("cost  :" ,cost)
    """"
    plt.figure(figsize=(20,3
                   ))
    plt.scatter(x_n, y_n,s=20
        )
    plt.plot(x_n,Y,color="red")
    """
    theta = denormalize(thetas ,x ,y)
    print("[ Original space  ] >> theta_0 :{}  theta_1 :{} ".format( theta[0] ,theta[1] ))
    
    
    return theta


