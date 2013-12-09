'''
Created on Dec 6, 2013

@author: Scott
'''

import utils.Utils as utils
import WatershedMapping.watershed_mapping as ws_map
import WatershedMapping.WatershedMerge as WatershedMerge
import WatershedMapping.FileWriter as FileWriter
import WatershedMapping.ImageTransforms as ImageTransforms
import WatershedMapping.EdgeMetric as EdgeMetric
import sys, os, functools


def getFilename(originalFile):
    x = originalFile.split('/')
    
    a = x[len(x) - 1]
    return a.split('.')[0]

def runAnalysis(originalFile, saveDir,transform, metric, step, mergeLimit, centralDirectory, transformName, metricName):
    

    array = utils.get_array(originalFile)

    transformed = transform(array)

    
    print("size: " + str(len(transformed)) + " X " + str(len(transformed[0])) + " (pixels: " + str(len(transformed) * len(transformed[0])) + ")")
   
    ws = ws_map.build_index_map(utils.get_gradient(transformed))

    edge_merges = dict()
    
    edge_map = ws.get_edge_weight_map(metric)
    
    try:
        FileWriter.writeSparseMatrix(saveDir + getFilename(originalFile) + '-' +transformName + '-' +metricName +'.data',edge_map);
        if len(centralDirectory) != 0:
            FileWriter.writeSparseMatrix(centralDirectory +getFilename(originalFile) + '-' +transformName + '-' +metricName +'.data',edge_map);
    except:
        sys.stderr.write("Unable to write file")
      
    
    s = 0
    while s < mergeLimit:
        edge_merges = WatershedMerge.merge_watersheds_at_limit(edge_merges, ws, s, edge_map)
        utils.write_image(ws.get_watershed_picture(edge_merges,len(transformed), len(transformed[0])), saveDir + str(s) + '.png')
        s += step
        
        
def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions)        


'''
Running this main makes a directory, fills said directory with images merged by the specificiations.
Also generates the .data file of the sparse matrix
'''

if __name__ == '__main__': 
    
    originalFile = "../../data/man.png"
    step = 10
    merge_limit = 1000
    
    saveDir = originalFile.split('.png')[0]
    os.mkdir(saveDir)
    saveDir += '/'
    transform = compose(ImageTransforms.get_gradient, ImageTransforms.greyscale)
    transformName  = "gradient"
    
    metric = EdgeMetric.minimum
    metricName = "min"
    
    runAnalysis(originalFile, saveDir,transform, metric, step, merge_limit, "", transformName, metricName)
    