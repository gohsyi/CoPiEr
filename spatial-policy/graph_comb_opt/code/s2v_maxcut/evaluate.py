import numpy as np
import networkx as nx
import cPickle as cp
import pickle
import random
import ctypes
import os
import sys
import time, glob
from tqdm import tqdm

sys.path.append( '%s/maxcut_lib' % os.path.dirname(os.path.realpath(__file__)) )
from maxcut_lib import MaxcutLib
    
if __name__ == '__main__':
    api = MaxcutLib(sys.argv)
    
    opt = {}
    for i in range(1, len(sys.argv), 2):
        opt[sys.argv[i][1:]] = sys.argv[i + 1]

    model_file = opt['modelF']
    assert model_file is not None
    print 'loading', model_file
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
            parseHash = {}
            sol = []
            for v1, v2, cdata in g.edges.data():    
              cv1 = min(v1, v2)
              cv2 = max(v1, v2)

              # Hash
              if (cv1, cv2) in parseHash:
                continue
              parseHash[(cv1, cv2)] = 1

              if selectNodes[cv1] != selectNodes[cv2]:
                  obj -= cdata['weight'] # Converted to a minimization problem
                  sol.append('u%d_%d 1\n'%(cv1, cv2))
              else:
                  sol.append('u%d_%d 0\n'%(cv1, cv2))

            f_out.write('#Solution Generated by RL policy\n')
            f_out.write('#Objective value: %d\n'%obj)
            for csol in sol:    
                f_out.write(csol)

