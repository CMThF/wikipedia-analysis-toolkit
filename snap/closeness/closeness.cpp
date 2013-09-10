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
  
  TStr FNCentralityDeg = prefix + "_cent_deg.dat";
  TStr FNCentralityPR = prefix + "_cent_pr.dat";
  TStr FNCentralityClose = prefix + "_cent_close.dat";
  TStr FNCentralityBet = prefix + "_cent_bet.dat";
  TStr FNCentralityCC = prefix + "_cent_cc.dat";
  
  Env = TEnv(argc, argv, TNotify::StdNotify);
  Env.PrepArgs(TStr::Fmt("GraphInfo. build: %s, %s. Time: %s", __TIME__, __DATE__, TExeTm::GetCurTm()));
  TExeTm ExeTm;
  Try
  PNGraph Graph = TSnap::LoadEdgeList<PNGraph>(InFNm);
  // if (! IsDir) { TSnap::MakeUnDir(Graph); }
  printf("nodes:%d  edges:%d\nCreating plots...\n", Graph->GetNodes(), Graph->GetEdges());
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
  PUNGraph UGraph = TSnap::ConvertGraph<PUNGraph>(Graph);
  printf(" Undirected Graph build! ");
  TIntFltH BtwH, PRankH, CcfH, CloseH;
  
  
  // printf(" PageRank... ");             TSnap::GetPageRank(Graph, PRankH, 0.85);
  // FILE *FPR = fopen(FNCentralityPR.CStr(), "wt");
  // fprintf(FPR,"#Network: %s\n", prefix.CStr());
  // fprintf(FPR,"#Nodes: %d\tEdges: %d\n", Graph->GetNodes(), Graph->GetEdges());
  // fprintf(FPR,"#NodeId\tPageRank\n");
  // for (TUNGraph::TNodeI NI = UGraph->BegNI(); NI < UGraph->EndNI(); NI++) {
    // const int NId = NI.GetId();
    // const double PgrCentr = PRankH.GetDat(NId);
    // fprintf(FPR, "%d\t%f\n", NId, PgrCentr);
  // }
  // fclose(FPR);
  
  // printf(" Betweenness (SLOW!)...");   TSnap::GetBetweennessCentr(UGraph, BtwH, 0.001);
  // FILE *FBet = fopen(FNCentralityBet.CStr(), "wt");
  // fprintf(FBet,"#Network: %s\n", prefix.CStr());
  // fprintf(FBet,"#Nodes: %d\tEdges: %d\n", Graph->GetNodes(), Graph->GetEdges());
  // fprintf(FBet,"#NodeId\tBetweennes\n");
  // for (TUNGraph::TNodeI NI = UGraph->BegNI(); NI < UGraph->EndNI(); NI++) {
    // const int NId = NI.GetId();
    // const double BtwCentr = BtwH.GetDat(NId);

    // fprintf(FBet, "%d\t%f\n", NId, BtwCentr);
  // }
  // fclose(FBet);
  
  // printf(" Clustering...");            TSnap::GetNodeClustCf(UGraph, CcfH);
  // FILE *FCC = fopen(FNCentralityCC.CStr(), "wt");
  // fprintf(FCC,"#Network: %s\n", prefix.CStr());
  // fprintf(FCC,"#Nodes: %d\tEdges: %d\n", Graph->GetNodes(), Graph->GetEdges());
  // fprintf(FCC,"#NodeId\tClusteringCoefficient\n");
  // for (TUNGraph::TNodeI NI = UGraph->BegNI(); NI < UGraph->EndNI(); NI++) {
    // const int NId = NI.GetId();
    // const double ClustCf = CcfH.GetDat(NId);
    // fprintf(FCC, "%d\t%f\n", NId, ClustCf);
  // }
  // fclose(FCC);
  

  printf(" Closeness (SLOW!)...");
  double NodeFrac = 0.001;
  
  TIntV NIdV;  UGraph->GetNIdV(NIdV);
  if (NodeFrac < 1.0) { // calculate closeness centrality for a subset of nodes
    NIdV.Shuffle(TInt::Rnd);
    for (int i = int((1.0-NodeFrac)*NIdV.Len()); i > 0; i--) { 
      NIdV.DelLast(); }
  }
  for (int k=0; k < NIdV.Len(); k++) {
    const TUNGraph::TNodeI NI = UGraph->GetNI(NIdV[k]);
	const int NId = NI.GetId();
    CloseH.AddDat(NId, TSnap::GetClosenessCentr(UGraph, NId));
  }
  
  // for (TUNGraph::TNodeI NI = UGraph->BegNI(); NI < UGraph->EndNI(); NI++) {
    // const int NId = NI.GetId();
    // CloseH.AddDat(NId, TSnap::GetClosenessCentr(UGraph, NId));
	// printf(" Node closeness calculated. ");
  // }
  
  
  FILE *FClose = fopen(FNCentralityClose.CStr(), "wt");
  fprintf(FClose,"#Network: %s\n", prefix.CStr());
  fprintf(FClose,"#Nodes: %d\tEdges: %d\n", Graph->GetNodes(), Graph->GetEdges());
  fprintf(FClose,"#NodeId\tCloseness\n");
  for (int k=0; k < NIdV.Len(); k++) {
    const TUNGraph::TNodeI NI = UGraph->GetNI(NIdV[k]);
    const int NId = NI.GetId();
    const double CloCentr = CloseH.GetDat(NId);
    fprintf(FClose, "%d\t%f\n", NId, CloCentr);
  }
  fclose(FClose);

  
  // FILE *FDeg = fopen(FNCentralityDeg.CStr(), "wt");
  // fprintf(FDeg,"#Network: %s\n", prefix.CStr());
  // fprintf(FDeg,"#Nodes: %d\tEdges: %d\n", Graph->GetNodes(), Graph->GetEdges());
  // fprintf(FDeg,"#NodeId\tDegree\n");
  // for (TUNGraph::TNodeI NI = UGraph->BegNI(); NI < UGraph->EndNI(); NI++) {
    // const int NId = NI.GetId();
    // const double DegCentr = UGraph->GetNI(NId).GetDeg();
    // fprintf(FDeg, "%d\t%f\n", NId, DegCentr);
  // }
  // fclose(FDeg);
  
  printf("\nDONE! saving...");
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

