#include "stdafx.h"
// #include <sstream>
// #include <string>
// #include <iostream>
// using namespace std;

int main(int argc, char* argv[]) {
  
  
  // const TStr InFNm = Env.GetIfArgPrefixStr("-i:", "graph.txt", "Input graph (one edge per line, tab/space separated)");
  // const TBool IsDir = Env.GetIfArgPrefixBool("-d:", true, "Directed graph");
  // const TStr OutFNm = Env.GetIfArgPrefixStr("-o:", "graph", "Output file prefix");
  // const TStr Desc = Env.GetIfArgPrefixStr("-t:", "", "Title (description)");
  // const TStr Plot = Env.GetIfArgPrefixStr("-p:", "cdhwsCvV", "What statistics to plot string:"
    // "\n\tc: cummulative degree distribution"
    // "\n\td: degree distribution"
    // "\n\th: hop plot (diameter)"
    // "\n\tw: distribution of weakly connected components"
    // "\n\ts: distribution of strongly connected components"
    // "\n\tC: clustering coefficient"
    // "\n\tv: singular values"
    // "\n\tV: left and right singular vector\n\t");
  // bool PlotDD, PlotCDD, PlotHop, PlotWcc, PlotScc, PlotSVal, PlotSVec, PlotClustCf;
  // PlotDD = Plot.SearchCh('d') != -1;
  // PlotCDD = Plot.SearchCh('c') != -1;
  // PlotHop = Plot.SearchCh('h') != -1;
  // PlotWcc = Plot.SearchCh('w') != -1;
  // PlotScc = Plot.SearchCh('s') != -1;
  // PlotClustCf = Plot.SearchCh('C') != -1;
  // PlotSVal = Plot.SearchCh('v') != -1;
  // PlotSVec = Plot.SearchCh('V') != -1;
  // if (Env.IsEndOfRun()) { return 0; }
  //PNGraph G = TGGen<PNGraph>::GenRMat(1000, 3000, 0.40, 0.25, 0.2);
  //G->SaveEdgeList("graph.txt", "RMat graph (a:0.40, b:0.25, c:0.20)");
  printf("Loading...");
  if (argc < 3)
    return 0;
  TStr InFNm = argv[1];
  TStr prefix = argv[2];
  // ostringstream os;
  // os << InFNm << "_OutDegreeDistribution";
  // TStr FNOutDD = os.str();
  // os.str("");
  // os.clear();
  const TStr Desc = prefix;
  TStr FNOutDD = prefix;
  
  // os << InFNm << "_InDegreeDistribution";
  // TStr FNInDD = os.str();
  // os.str("");
  // os.clear();
  TStr FNInDD = prefix;
  
  // os << InFNm << "_HopPlot";
  // TStr FNHops = os.str();
  // os.str("");
  // os.clear();
  TStr FNHops = prefix;
   
  // os << InFNm << "_WeaklyConnectedComponents";
  // TStr FNWeaklyConnectedComps = os.str();
  // os.str("");
  // os.clear();
  TStr FNWeaklyConnectedComps = prefix;
  
  // os << InFNm << "_StronglyConnectedComponents";
  // TStr FNStronglyConnectedComps = os.str();
  // os.str("");
  // os.clear();
  TStr FNStronglyConnectedComps = prefix;
  
  // os << InFNm << "ClusteringCoefficient";
  // TStr FNClusteringCoeff = os.str();
  // os.str("");
  // os.clear(); 
  TStr FNClusteringCoeff = prefix;
  TStr FNCentrality = prefix + "_centrality.dat";
  
  TStr InOutDeg = prefix + "_InOutDeg.dat";
  
  Env = TEnv(argc, argv, TNotify::StdNotify);
  Env.PrepArgs(TStr::Fmt("GraphInfo. build: %s, %s. Time: %s", __TIME__, __DATE__, TExeTm::GetCurTm()));
  TExeTm ExeTm;
  Try
  PNGraph Graph = TSnap::LoadEdgeList<PNGraph>(InFNm);
  // if (! IsDir) { TSnap::MakeUnDir(Graph); }
  printf("nodes:%d  edges:%d\nCreating plots...\n", Graph->GetNodes(), Graph->GetEdges());
  
  FILE *F = fopen(InOutDeg.CStr(), "wt");
  fprintf(F,"#Network: %s\n", prefix.CStr());
  fprintf(F,"#Nodes: %d\tEdges: %d\n", Graph->GetNodes(), Graph->GetEdges());
  fprintf(F,"#In\tOut\n");
  
  for (typename TNGraph::TNodeI NI = Graph->BegNI(); NI < Graph->EndNI(); NI++) {
	const int inDeg = NI.GetInDeg();
	const int outDeg = NI.GetOutDeg();
    fprintf(F, "%d\t%d\n", inDeg, outDeg);
  }
  fclose(F);
  
  
  
  
  // const int Vals = Graph->GetNodes()/2 > 200 ? 200 : Graph->GetNodes()/2;
  // if (PlotDD) {
  // TSnap::PlotOutDegDistr(Graph, FNOutDD, Desc, false, false);
  // TSnap::PlotInDegDistr(Graph, FNInDD, Desc, false, false);
  // printf("In and Out done\n");
  // }
  // if (PlotCDD) {
    // TSnap::PlotOutDegDistr(Graph, FNOutCDD, Desc, true, false);   // <======== waere interessant
    // TSnap::PlotInDegDistr(Graph, FNInCDD, Desc, true, false);
  // }
  // if (PlotHop) {
  // TSnap::PlotHops(Graph, FNHops, Desc, false, 8);
  // printf("hops done\n");
  // }
  // if (PlotWcc) {
  // TSnap::PlotWccDistr(Graph, FNWeaklyConnectedComps, Desc);
  // printf("wcc done\n");
  // }
  // if (PlotScc) {
  // TSnap::PlotSccDistr(Graph, FNStronglyConnectedComps, Desc);
  // printf("scc done\n");
  // }
  // if (PlotClustCf) {
  // TSnap::PlotClustCf(Graph, FNClusteringCoeff, Desc);
  // printf("CC done\n");
  // }
  // if (PlotSVal) {
    // TSnap::PlotSngValRank(Graph, Vals, OutFNm, Desc);
  // }
  // if(PlotSVec) {
    // TSnap::PlotSngVec(Graph, OutFNm, Desc);
  // }
  // PUNGraph UGraph = TSnap::ConvertGraph<PUNGraph>(Graph);
  // TIntFltH BtwH, PRankH, CcfH, CloseH;
  // printf(" PageRank... ");             TSnap::GetPageRank(Graph, PRankH, 0.85);
  // printf(" Betweenness (SLOW!)...");   TSnap::GetBetweennessCentr(UGraph, BtwH, 0.01);
  // printf(" Clustering...");            TSnap::GetNodeClustCf(UGraph, CcfH);
  // printf(" Closeness (SLOW!)...");
  // for (TUNGraph::TNodeI NI = UGraph->BegNI(); NI < UGraph->EndNI(); NI++) {
    // const int NId = NI.GetId();
    // CloseH.AddDat(NId, TSnap::GetClosenessCentr(UGraph, NId));
  // }
  
  // printf("\nDONE! saving...");
  // FILE *F = fopen(FNCentrality.CStr(), "wt");
  // fprintf(F,"#Network: %s\n", prefix.CStr());
  // fprintf(F,"#Nodes: %d\tEdges: %d\n", Graph->GetNodes(), Graph->GetEdges());
  // fprintf(F,"#NodeId\tDegree\tCloseness\tBetweennes\tClusteringCoefficient\tPageRank\n");
  // for (TUNGraph::TNodeI NI = UGraph->BegNI(); NI < UGraph->EndNI(); NI++) {
    // const int NId = NI.GetId();
    // const double DegCentr = UGraph->GetNI(NId).GetDeg();
    // const double CloCentr = CloseH.GetDat(NId);
    // const double BtwCentr = BtwH.GetDat(NId);
    // const double ClustCf = CcfH.GetDat(NId);
    // const double PgrCentr = PRankH.GetDat(NId);
    // fprintf(F, "%d\t%f\t%f\t%f\t%f\t%f\n", NId, 
      // DegCentr, CloCentr, BtwCentr, ClustCf, PgrCentr);
  // }
  // fclose(F);
  
  Catch
  
  
  printf("\nrun time: %s (%s)\n", ExeTm.GetTmStr(), TSecTm::GetCurTm().GetTmStr().CStr());
  return 0;
}

