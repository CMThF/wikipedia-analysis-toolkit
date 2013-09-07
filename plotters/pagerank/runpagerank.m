clear all;
close all;

load 'afwiki_centrality.dat'
pagerank1(afwiki_centrality, 'afwiki_cent_pr.png');
clear all;

load 'dewiki_cent_pr.dat'
pagerank2(dewiki_cent_pr, 'dewiki_cent_pr.png');
clear all;

load 'eowiki_cent_pr.dat'
pagerank2(eowiki_cent_pr, 'eowiki_cent_pr.png');
clear all;

load 'eswiki_cent_pr.dat'
pagerank2(eswiki_cent_pr, 'eswiki_cent_pr.png');
clear all;

load 'frwiki_cent_pr.dat'
pagerank2(frwiki_cent_pr, 'frwiki_cent_pr.png');
clear all;

load 'hifwiki_centrality.dat'
pagerank1(hifwiki_centrality, 'hifwiki_cent_pr.png');
clear all;

load 'itwiki_cent_pr.dat'
pagerank2(itwiki_cent_pr, 'itwiki_cent_pr.png');
clear all;

load 'lawiki_centrality.dat'
pagerank1(lawiki_centrality, 'lawiki_cent_pr.png');
clear all;

load 'ptwiki_cent_pr.dat'
pagerank2(ptwiki_cent_pr, 'ptwiki_cent_pr.png');
clear all;

load 'ruwiki_cent_pr.dat'
pagerank2(ruwiki_cent_pr, 'ruwiki_cent_pr.png');
clear all;

load 'scowiki_centrality.dat'
pagerank1(scowiki_centrality, 'scowiki_cent_pr.png');
clear all;

load 'vlswiki_centrality.dat'
pagerank1(vlswiki_centrality, 'vlswiki_cent_pr.png');
clear all;
close all;