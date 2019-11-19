import random

def satellize(ax,n=5,color='black',ls='--',**kwargs):
    """satellize
    A simple and important function that adds artificial satellite trails to a maplotlib axis, as caused by some hypothetical unnamed
    cluster of satellites

    Signature:  
    satellize(ax,n=5,**kwargs)
        ax: a matplotlib axis object (or pyplot object)
        n: the number of satellites to plot
        **kwargs: kwargs that get passed to the line plot (use this for color etc)
    
    Details:
    Draws dotted lines across the x axis, all with th e
    
    """
    
    try:
        ymin, ymax = ax.get_ylim()
        xmin, xmax = ax.get_xlim()
    except AttributeError:
        ymin, ymax = ax.ylim()
        xmin, xmax = ax.xlim()
    

    if ymin>ymax: ymin,ymax = ymax,ymin
    if xmin>xmax: xmin,xmax = xmax,xmin

    linear_slope = (ymax-ymin)/(xmax-xmin)
    
    sat_slopes = random.uniform(-2.,2.) * linear_slope
    dy = ymax-ymin

    for line in range(n):
        y_cent = random.uniform(ymin,ymax)
        x_cent = random.uniform(xmin,xmax)
        
        y0 = y_cent-sat_slopes*(x_cent-xmin)
        y1 = y_cent+sat_slopes*(xmax-x_cent)
        
        x0 = xmin
        x1 = xmax

        if y0<ymin or y0>ymax:
            if sat_slopes<0:
                y0 = ymax
            else:
                y0 = ymin
            x0 = x1-(y1-y0)/sat_slopes
        
        if y1<ymin or y1>ymax:
            if sat_slopes>0:
                y1 = ymax
            else:
                y1 = ymin
            x1 = (y1-y0)/sat_slopes+x0
            
        ax.plot([x0,x1],[y0,y1],color=color,ls=ls,**kwargs)


def example(output="test.png"):
    import numpy as np
    import matplotlib.pyplot as plt
    fig,ax = plt.subplots()
    map = np.random.random((128,128))
    ax.imshow(map)
    satellize(plt,color='white',n=10)
    fig.savefig(output)

if __name__=='__main__':
    example()
