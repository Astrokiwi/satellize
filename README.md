# satellize

A quick and silly library to add satellite trails to your matplotlib plots, for memes.

For quick tests:

```
import satellize

satellize.example(output="test.png") # quick example, dumps to file
```
![Sample test image](test.png)


For great justice:
```
satellize.satellize(ax) # ax is some matplotlib axis object
satellize.satellize(plt) # plt is the matplotlib.pyplot object
```
