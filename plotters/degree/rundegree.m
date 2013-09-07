clear all;
close all;

load 'afwiki_centrality.dat'
degree(afwiki_centrality, 'afwiki_cent_deg.png', 'af');
clear all;

load 'dewiki_cent_deg.dat'
degree(dewiki_cent_deg, 'dewiki_cent_deg.png', 'de');
clear all;

load 'eowiki_cent_deg.dat'
degree(eowiki_cent_deg, 'eowiki_cent_deg.png', 'eo');
clear all;

load 'eswiki_cent_deg.dat'
degree(eswiki_cent_deg, 'eswiki_cent_deg.png', 'es');
clear all;

load 'frwiki_cent_deg.dat'
degree(frwiki_cent_deg, 'frwiki_cent_deg.png', 'fr');
clear all;

load 'hifwiki_centrality.dat'
degree(hifwiki_centrality, 'hifwiki_cent_deg.png', 'hif');
clear all;

load 'itwiki_cent_deg.dat'
degree(itwiki_cent_deg, 'itwiki_cent_deg.png', 'it');
clear all;

load 'lawiki_centrality.dat'
degree(lawiki_centrality, 'lawiki_cent_deg.png', 'la');
clear all;

load 'ptwiki_cent_deg.dat'
degree(ptwiki_cent_deg, 'ptwiki_cent_deg.png', 'pt');
clear all;

load 'ruwiki_cent_deg.dat'
degree(ruwiki_cent_deg, 'ruwiki_cent_deg.png', 'ru');
clear all;

load 'scowiki_centrality.dat'
degree(scowiki_centrality, 'scowiki_cent_deg.png', 'sco');
clear all;

load 'vlswiki_centrality.dat'
degree(vlswiki_centrality, 'vlswiki_cent_deg.png', 'vls');
clear all;
close all;