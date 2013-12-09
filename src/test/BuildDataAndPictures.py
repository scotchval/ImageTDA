'''
Created on Dec 6, 2013

@author: Scott
'''

import glob, os, WatershedMapping.ImageTest, functools, sys
import WatershedMapping.ImageTransforms as ImageTransforms
import WatershedMapping.EdgeMetric as EdgeMetric

MIN = 'min_depth'
SUM = 'sum_depths'
PNG = 'png'
GRADIENT = 'gradient'
BLUE_FILTER = 'blue_filter'
GREY_SCALE = 'grey'
CENTRAL_REPOSITORY = "all_watershed_data"

def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions)

def getFileName(filepath):
    x = filepath.split('/')
    a = x[len(x)  -1]
    
    z = a.split('\\')
    a = z[len(z)-1]
    
    y = a.split('.')
    return y[0] 

'''
Performs tests on all .ext files (where ext is the argument) in the directorypath. Constructs folders for all of them.
'''
def performTests(directorypath, ext):
    pictures = [getFileName(f) for f in glob.glob(filepath + "*." + ext)]

    os.mkdir(directorypath +CENTRAL_REPOSITORY)
    for picName in pictures:
        print(picName)
        constructWatershedAndImages(picName, PNG, directorypath +CENTRAL_REPOSITORY, directorypath)

def constructWatershedAndImages(picName, ext, centralDirectory, dirpath):
        dataDir = dirpath + picName
        os.mkdir(dataDir)
        
        metrics = getMetrics()
        transforms = getTransforms()
        
        for transform in transforms:
            transDir = dataDir +'/'+ transform[1] + '/'
            os.mkdir(transDir)
            for metric in metrics:    
                metricDir = transDir + metric[1] + '/'
                os.mkdir(metricDir)
                
                ''' original file, directory to write to, transform function, metric function, step, maxMerge''' 
            
                try:
                    WatershedMapping.ImageTest.runAnalysis(dataDir + '.' + ext, metricDir, transform[0], metric[0], max(metric[2],transform[2]), max(metric[3],transform[3]), centralDirectory + '/', transform[1], metric[1])
                except:
                    print("Failed file: " + dataDir)


'''
Defines metrics to be used to calculate distance between watersheds.
'''
def getMetrics():
    metrics = list()
    metrics.append( (EdgeMetric.minimum,'min_depth',20,300))
    metrics.append( (EdgeMetric.summation,'sum_depths',40,550))
    return metrics


'''
Defines the transforms to perform on the images.
'''
def getTransforms():
    transforms = list()
    transforms.append((ImageTransforms.greyscale, 'grey_scale',20,300))
    transforms.append((compose(ImageTransforms.get_gradient,ImageTransforms.greyscale), 'gradient',100, 5000))
    transforms.append((ImageTransforms.green_blue_filter, "green_blue_enhancement",20,300))
    transforms.append((compose(ImageTransforms.get_gradient,ImageTransforms.green_blue_filter), "green-blue-gradient",100, 5000))
                
    return transforms
    



if __name__ == '__main__':   
    args = sys.argv
    if len(args)  < 1:
        sys.stderr.write("Need to pass file as argument")
        return
    filepath = args[1]
    performTests(filepath, PNG)
    
    