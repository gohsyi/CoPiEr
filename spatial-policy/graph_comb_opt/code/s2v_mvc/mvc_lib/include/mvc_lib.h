#ifndef MVC_LIB_H
#define MVC_LIB_H

extern "C" int Init(const int argc, const char** argv);

extern "C" int InsertGraph(bool isTest, const int g_id, const int num_nodes, const int num_edges, const int* edges_from, const int* edges_to, const int num_opt=0, const int* opt_nodes=NULL, const double prob=0.5);

extern "C" int LoadModel(const char* filename);

extern "C" int SaveModel(const char* filename);

extern "C" int UpdateSnapshot();

extern "C" int ClearTrainGraphs();

extern "C" int PlayGame(const int n_traj, const double eps, bool expert=false);

extern "C" double Fit();
extern "C" double Test(const int gid);

extern "C" double GetSol(const int gid, int* sol);

#endif
