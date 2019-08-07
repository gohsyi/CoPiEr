import numpy as np
import networkx as nx
#import cPickle as cp
import _pickle as cp
import pickle
import random
import ctypes
import os
import sys
import time, glob
from tqdm import tqdm

sys.path.append( '%s/mvc_lib' % os.path.dirname(os.path.realpath(__file__)) )
from mvc_lib import MvcLib
    
if __name__ == '__main__':
    api = MvcLib(sys.argv)
    
    opt = {}
    for i in range(1, len(sys.argv), 2):
        opt[sys.argv[i][1:]] = sys.argv[i + 1]

    model_file = opt['modelF']
    assert model_file is not None
    print('loading', model_file)
    sys.stdout.flush()
    api.LoadModel(model_file)

    dataF = opt['data_test']
    resultFolder = opt['save_dir']
    os.system('mkdir -p %s'%resultFolder)

    for k, cF in enumerate(glob.glob(dataF + '/*gpickle')):
        print('Reading: '+cF)
        with open(cF, 'rb') as F:
            g = pickle.load(F)

        api.InsertGraph(g, is_test=True)
        val, sol = api.GetSol(k, nx.number_of_nodes(g))

        selectNodes = {}
        for i in range(nx.number_of_nodes(g)):
            # zero indexed from the generator
            selectNodes[i] = 0

        for i in range(sol[0]):
            selectNodes[sol[i + 1]] = 1

        # Write output
        outF = resultFolder + '/' + os.path.basename(cF).replace('.gpickle', '.sol')
        print('writing %s'%outF)
        with open(outF, 'w') as f_out:
            obj = 0
            for i in range(nx.number_of_nodes(g)):    
                obj += selectNodes[i]
            f_out.write('#Solution Generated by RL policy\n')
            f_out.write('#Objective value: %d\n'%obj)
            for i in range(nx.number_of_nodes(g)):    
                f_out.write('v%d %d\n'%(i, selectNodes[i]))

