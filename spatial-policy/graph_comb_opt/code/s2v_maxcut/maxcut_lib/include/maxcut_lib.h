#ifndef MAXCUT_LIB_H
#define MAXCUT_LIB_H

extern "C" int Init(const int argc, const char** argv);

extern "C" int InsertGraph(bool isTest, const int g_id, const int num_nodes, 
                const int num_edges, const int* edges_from, const int* edges_to, 
                const double* weights, const int num_opt, const int* opt_nodes_v1, 
                const int* opt_nodes_v2, const int num_opt_nodes, const double prob);

extern "C" int LoadModel(const char* filename);

extern "C" int SaveModel(const char* filename);

extern "C" int UpdateSnapshot();

extern "C" int ClearTrainGraphs();

extern "C" int PlayGame(const int n_traj, const double eps, bool expert=false);

extern "C" double Fit();
extern "C" double Test(const int gid);

extern "C" double TestNoStop(const int gid);
extern "C" double GetSol(const int gid, int* sol);

#endif
