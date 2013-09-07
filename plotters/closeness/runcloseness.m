clear all;
close all;

load 'afwiki_centrality.dat'
closeness1(afwiki_centrality, 'afwiki_cent_close.png', 'af');
clear all;

load 'dewiki_cent_close.dat'
closeness2(dewiki_cent_close, 'dewiki_cent_close.png', 'de');
clear all;

load 'eowiki_cent_close.dat'
closeness2(eowiki_cent_close, 'eowiki_cent_close.png', 'eo');
clear all;

load 'eswiki_cent_close.dat'
closeness2(eswiki_cent_close, 'eswiki_cent_close.png', 'es');
clear all;

load 'frwiki_cent_close.dat'
closeness2(frwiki_cent_close, 'frwiki_cent_close.png', 'fr');
clear all;

load 'hifwiki_centrality.dat'
closeness1(hifwiki_centrality, 'hifwiki_cent_close.png', 'hif');
clear all;

load 'itwiki_cent_close.dat'
closeness2(itwiki_cent_close, 'itwiki_cent_close.png', 'it');
clear all;

load 'lawiki_centrality.dat'
closeness1(lawiki_centrality, 'lawiki_cent_close.png', 'la');
clear all;

load 'ptwiki_cent_close.dat'
closeness2(ptwiki_cent_close, 'ptwiki_cent_close.png', 'pt');
clear all;

load 'ruwiki_cent_close.dat'
closeness2(ruwiki_cent_close, 'ruwiki_cent_close.png', 'ru');
clear all;

load 'scowiki_centrality.dat'
closeness1(scowiki_centrality, 'scowiki_cent_close.png', 'sco');
clear all;

load 'vlswiki_centrality.dat'
closeness1(vlswiki_centrality, 'vlswiki_cent_close.png', 'vls');
clear all;
close all;