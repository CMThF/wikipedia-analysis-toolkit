#include "stdafx.h"
// #include <sstream>
// #include <string>
// #include <iostream>
// using namespace std;

int main(int argc, char* argv[]) {
  
  
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
  
  TStr FNCentralityDeg = prefix + "_deg.dat";
  TStr FNCentralityDegIN = prefix + "_degIN.dat";
  TStr FNCentralityDegOUT = prefix + "_degOUT.dat";
  
  Env = TEnv(argc, argv, TNotify::StdNotify);
  Env.PrepArgs(TStr::Fmt("GraphInfo. build: %s, %s. Time: %s", __TIME__, __DATE__, TExeTm::GetCurTm()));
  TExeTm ExeTm;
  Try
  PNGraph Graph = TSnap::LoadEdgeList<PNGraph>(InFNm);
  // if (! IsDir) { TSnap::MakeUnDir(Graph); }
  printf("nodes:%d  edges:%d\nCreating plots...\n", Graph->GetNodes(), Graph->GetEdges());
  
  FILE *FDeg = fopen(FNCentralityDeg.CStr(), "wt");
  fprintf(FDeg,"#Network: %s\n", prefix.CStr());
  fprintf(FDeg,"#Nodes: %d\tEdges: %d\n", Graph->GetNodes(), Graph->GetEdges());
  fprintf(FDeg,"#NodeId\tDegree\n");
  for (TUNGraph::TNodeI NI = UGraph->BegNI(); NI < UGraph->EndNI(); NI++) {
    const int NId = NI.GetId();
    const double DegCentr = UGraph->GetNI(NId).GetDeg();
    fprintf(FDeg, "%d\t%f\n", NId, DegCentr);
  }
  fclose(FDeg);
  
  printf("\nDONE DEG! saving...");
  
  FILE *FDeg = fopen(FNCentralityDegIN.CStr(), "wt");
  fprintf(FDeg,"#Network: %s\n", prefix.CStr());
  fprintf(FDeg,"#Nodes: %d\tEdges: %d\n", Graph->GetNodes(), Graph->GetEdges());
  fprintf(FDeg,"#NodeId\tINDegree\n");
  for (TUNGraph::TNodeI NI = UGraph->BegNI(); NI < UGraph->EndNI(); NI++) {
    const int NId = NI.GetId();
    const double DegCentr = UGraph->GetNI(NId).GetInDeg();
    fprintf(FDeg, "%d\t%f\n", NId, DegCentr);
  }
  fclose(FDeg);
  
  printf("\nDONE IN DEG! saving...");
  
  FILE *FDeg = fopen(FNCentralityDegOUT.CStr(), "wt");
  fprintf(FDeg,"#Network: %s\n", prefix.CStr());
  fprintf(FDeg,"#Nodes: %d\tEdges: %d\n", Graph->GetNodes(), Graph->GetEdges());
  fprintf(FDeg,"#NodeId\tOUTDegree\n");
  for (TUNGraph::TNodeI NI = UGraph->BegNI(); NI < UGraph->EndNI(); NI++) {
    const int NId = NI.GetId();
    const double DegCentr = UGraph->GetNI(NId).GetOutDeg();
    fprintf(FDeg, "%d\t%f\n", NId, DegCentr);
  }
  fclose(FDeg);
  
  printf("\nDONE OUT DEG! saving...");

  Catch
  
  printf("\nrun time: %s (%s)\n", ExeTm.GetTmStr(), TSecTm::GetCurTm().GetTmStr().CStr());
  return 0;
}

