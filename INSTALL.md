Step 1: Follow the instructions in the graphnn github
 - cd spatial-policy/graph_comb_opt/
 - export GNN_HOME= \<path to COTRAIN_HOME\spatial-policy/graph_comb_opt/graphnn\>
 - Follow the instructions to install Graphnn and mvc_lib : https://github.com/Hanjun-Dai/graphnn

Step 2: Install scip-4.0.1-affected (in dep/ subfolder):
 - [Optional] (If using open source solver:) https://projects.coin-or.org/Clp
 - [Optional] Use SoPlex; so much faster than Clp
 - Update the LDFLAGS to the relevant LP solvers include and library paths in make/make.project
 - Use gurobi-7.4 version
 - Make command: make OPT=opt ZIMPL=false LPS=grb (or) make OPT=opt ZIMPL=false LPS=clp [for clp solver]

Step 3: Install Lapack
 - Install https://github.com/Reference-LAPACK/lapack
 - Remember: It has several dependencies. Make sure you use the same compiler (gcc/g++-4.9) for the all the dependency packages.

Step 4: Install scip-dagger
 - Install co-training/scip-dagger
 - make OPT=opt ZIMPL=false LPS=grb (or) clp [Use the same command as in step 2]. 

Step 5: Define macros in your ~/.bashrc (and remember to restart your terminal) :
  - export COTRAIN_HOME=\<path to local copier folder\>
  - export COTRAIN_DATA=\<path to data\>
  - export COTRAIN_SCATCH=\<path to scratch folder\>
  - export GNN_HOME=\< path to COTRAIN_HOME\spatial-policy/graph_comb_opt/graphnn \>
  - (optional) export PYTHONDONTWRITEBYTECODE=1 

For training:
  - cd $COTRAIN_HOME
  - Arguments for run-mvc: <data_folder> <exp_id> <#nodes on branch and bound> <#iterations for spatial policy>
  - examples: sh joint-pyscripts/run-mvc.sh mvc_test mvc_exp 100 1000