% clear all;
% close all;
% load '../degree/eowiki_cent_deg.dat'
% load '../degree/lawiki_centrality.dat'
% kl(eowiki_cent_deg, lawiki_centrality, 'eola_kldiv_deg.txt', 2,2);
% clear all;
% load '../degree/afwiki_centrality.dat'
% load '../degree/scowiki_centrality.dat'
% load '../degree/vlswiki_centrality.dat'
% load '../degree/hifwiki_centrality.dat'
% kl(afwiki_centrality, scowiki_centrality, 'afsco_kldiv_deg.txt', 2,2);
% kl(afwiki_centrality, hifwiki_centrality, 'afhif_kldiv_deg.txt', 2,2);
% kl(afwiki_centrality, vlswiki_centrality, 'afvls_kldiv_deg.txt', 2,2);
% clear all;
% load '../degree/dewiki_cent_deg.dat'
% load '../degree/eswiki_cent_deg.dat'
% kl(dewiki_cent_deg, eswiki_cent_deg, 'dees_kldiv_deg.txt', 2,2);
% clear eswiki_cent_deg;
% load '../degree/frwiki_cent_deg.dat'
% kl(dewiki_cent_deg, frwiki_cent_deg, 'defr_kldiv_deg.txt', 2,2);
% clear frwiki_cent_deg;
% load '../degree/itwiki_cent_deg.dat'
% kl(dewiki_cent_deg, itwiki_cent_deg, 'deit_kldiv_deg.txt', 2,2);
% clear itwiki_cent_deg;
% load '../degree/ptwiki_cent_deg.dat'
% kl(dewiki_cent_deg, ptwiki_cent_deg, 'dept_kldiv_deg.txt', 2,2);
% clear ptwiki_cent_deg;
% load '../degree/ruwiki_cent_deg.dat'
% kl(dewiki_cent_deg, ruwiki_cent_deg, 'deru_kldiv_deg.txt', 2,2);
% clear ruwiki_cent_deg;
% load '../degree/afwiki_centrality.dat'
% load '../degree/scowiki_centrality.dat'
% load '../degree/vlswiki_centrality.dat'
% load '../degree/hifwiki_centrality.dat'
% kl(dewiki_cent_deg, afwiki_centrality, 'deaf_kldiv_deg.txt', 2,2);
% kl(dewiki_cent_deg, scowiki_centrality, 'desco_kldiv_deg.txt', 2,2);
% kl(dewiki_cent_deg, hifwiki_centrality, 'dehif_kldiv_deg.txt', 2,2);
% kl(dewiki_cent_deg, vlswiki_centrality, 'devls_kldiv_deg.txt', 2,2);
% clear afwiki_centrality;
% clear scowiki_centrality;
% clear hifwiki_centrality;
% clear vlswiki_centrality;
% 
% load '../degree/eowiki_cent_deg.dat'
% load '../degree/lawiki_centrality.dat'
% kl(dewiki_cent_deg, lawiki_centrality, 'dela_kldiv_deg.txt', 2,2);
% kl(dewiki_cent_deg, eowiki_cent_deg, 'deeo_kldiv_deg.txt', 2,2);
% clear all;



%=================closeness===================================

% clear all;
% close all;
% load '../closeness/eowiki_cent_close.dat'
% load '../closeness/lawiki_centrality.dat'
% kl(eowiki_cent_close, lawiki_centrality, 'eola_kldiv_close.txt', 2,3);
% clear all;
% load '../closeness/afwiki_centrality.dat'
% load '../closeness/scowiki_centrality.dat'
% load '../closeness/vlswiki_centrality.dat'
% load '../closeness/hifwiki_centrality.dat'
% kl(afwiki_centrality, scowiki_centrality, 'afsco_kldiv_close.txt', 3,3);
% kl(afwiki_centrality, hifwiki_centrality, 'afhif_kldiv_close.txt', 3,3);
% kl(afwiki_centrality, vlswiki_centrality, 'afvls_kldiv_close.txt', 3,3);
% clear all;
% load '../closeness/dewiki_cent_close.dat'
% load '../closeness/eswiki_cent_close.dat'
% kl(dewiki_cent_close, eswiki_cent_close, 'dees_kldiv_close.txt', 2,2);
% clear eswiki_cent_close;
% load '../closeness/frwiki_cent_close.dat'
% kl(dewiki_cent_close, frwiki_cent_close, 'defr_kldiv_close.txt', 2,2);
% clear frwiki_cent_close;
% load '../closeness/itwiki_cent_close.dat'
% kl(dewiki_cent_close, itwiki_cent_close, 'deit_kldiv_close.txt', 2,2);
% clear itwiki_cent_close;
% load '../closeness/ptwiki_cent_close.dat'
% kl(dewiki_cent_close, ptwiki_cent_close, 'dept_kldiv_close.txt', 2,2);
% clear ptwiki_cent_close;
% load '../closeness/ruwiki_cent_close.dat'
% kl(dewiki_cent_close, ruwiki_cent_close, 'deru_kldiv_close.txt', 2,2);
% clear ruwiki_cent_close;
% load '../closeness/afwiki_centrality.dat'
% load '../closeness/scowiki_centrality.dat'
% load '../closeness/vlswiki_centrality.dat'
% load '../closeness/hifwiki_centrality.dat'
% kl(dewiki_cent_close, afwiki_centrality, 'deaf_kldiv_close.txt', 2,3);
% kl(dewiki_cent_close, scowiki_centrality, 'desco_kldiv_close.txt', 2,3);
% kl(dewiki_cent_close, hifwiki_centrality, 'dehif_kldiv_close.txt', 2,3);
% kl(dewiki_cent_close, vlswiki_centrality, 'devls_kldiv_close.txt', 2,3);
% clear afwiki_centrality;
% clear scowiki_centrality;
% clear hifwiki_centrality;
% clear vlswiki_centrality;
% 
% load '../closeness/eowiki_cent_close.dat'
% load '../closeness/lawiki_centrality.dat'
% kl(dewiki_cent_close, lawiki_centrality, 'dela_kldiv_close.txt', 2,3);
% kl(dewiki_cent_close, eowiki_cent_close, 'deeo_kldiv_close.txt', 2,2);
% clear all;

%=================between===================================
% clear all;
% 
% load '../betweeness/eowiki_cent_bet.dat'
% load '../betweeness/lawiki_cent_bet.dat'
% kl(eowiki_cent_bet, lawiki_cent_bet, 'eola_kldiv_bet.txt', 2,2);
% clear all;
% load '../betweeness/afwiki_cent_bet.dat'
% load '../betweeness/scowiki_cent_bet.dat'
% load '../betweeness/vlswiki_cent_bet.dat'
% load '../betweeness/hifwiki_cent_bet.dat'
% kl(afwiki_cent_bet, scowiki_cent_bet, 'afsco_kldiv_bet.txt', 2,2);
% kl(afwiki_cent_bet, hifwiki_cent_bet, 'afhif_kldiv_bet.txt', 2,2);
% kl(afwiki_cent_bet, vlswiki_cent_bet, 'afvls_kldiv_bet.txt', 2,2);
% clear all;
% load '../betweeness/dewiki_cent_bet.dat'
% load '../betweeness/eswiki_cent_bet.dat'
% kl(dewiki_cent_bet, eswiki_cent_bet, 'dees_kldiv_bet.txt', 2,2);
% clear eswiki_cent_bet;
% load '../betweeness/frwiki_cent_bet.dat'
% kl(dewiki_cent_bet, frwiki_cent_bet, 'defr_kldiv_bet.txt', 2,2);
% clear frwiki_cent_bet;
% load '../betweeness/itwiki_cent_bet.dat'
% kl(dewiki_cent_bet, itwiki_cent_bet, 'deit_kldiv_bet.txt', 2,2);
% clear itwiki_cent_bet;
% load '../betweeness/ptwiki_cent_bet.dat'
% kl(dewiki_cent_bet, ptwiki_cent_bet, 'dept_kldiv_bet.txt', 2,2);
% clear ptwiki_cent_bet;
% load '../betweeness/ruwiki_cent_bet.dat'
% kl(dewiki_cent_bet, ruwiki_cent_bet, 'deru_kldiv_bet.txt', 2,2);
% clear ruwiki_cent_bet;
% load '../betweeness/afwiki_cent_bet.dat'
% load '../betweeness/scowiki_cent_bet.dat'
% load '../betweeness/vlswiki_cent_bet.dat'
% load '../betweeness/hifwiki_cent_bet.dat'
% kl(dewiki_cent_bet, afwiki_cent_bet, 'deaf_kldiv_bet.txt', 2,2);
% kl(dewiki_cent_bet, scowiki_cent_bet, 'desco_kldiv_bet.txt', 2,2);
% kl(dewiki_cent_bet, hifwiki_cent_bet, 'dehif_kldiv_bet.txt', 2,2);
% kl(dewiki_cent_bet, vlswiki_cent_bet, 'devls_kldiv_bet.txt', 2,2);
% clear afwiki_cent_bet;
% clear scowiki_cent_bet;
% clear hifwiki_cent_bet;
% clear vlswiki_cent_bet;
% 
% load '../betweeness/eowiki_cent_bet.dat'
% load '../betweeness/lawiki_cent_bet.dat'
% kl(dewiki_cent_bet, lawiki_cent_bet, 'dela_kldiv_bet.txt', 2,2);
% kl(dewiki_cent_bet, eowiki_cent_bet, 'deeo_kldiv_bet.txt', 2,2);
% clear all;

%=================ccf===================================
clear all;

load '../ccf/ccf.eowiki.tab'
load '../ccf/ccf.lawiki.tab'
klccf(ccf_eowiki, ccf_lawiki, 'eola_kldiv_ccf.txt', 2,2);
clear all;
load '../ccf/ccf.afwiki.tab'
load '../ccf/ccf.scowiki.tab'
load '../ccf/ccf.vlswiki.tab'
load '../ccf/ccf.hifwiki.tab'
klccf(ccf_afwiki, ccf_scowiki, 'afsco_kldiv_ccf.txt', 2,2);
klccf(ccf_afwiki, ccf_hifwiki, 'afhif_kldiv_ccf.txt', 2,2);
klccf(ccf_afwiki, ccf_vlswiki, 'afvls_kldiv_ccf.txt', 2,2);
clear all;
load '../ccf/ccf.dewiki.tab'
load '../ccf/ccf.eswiki.tab'
klccf(ccf_dewiki, ccf_eswiki, 'dees_kldiv_ccf.txt', 2,2);
clear eswiki;
load '../ccf/ccf.frwiki.tab'
klccf(ccf_dewiki, ccf_frwiki, 'defr_kldiv_ccf.txt', 2,2);
clear frwiki;
load '../ccf/ccf.itwiki.tab'
klccf(ccf_dewiki, ccf_itwiki, 'deit_kldiv_ccf.txt', 2,2);
clear itwiki;
load '../ccf/ccf.ptwiki.tab'
klccf(ccf_dewiki, ccf_ptwiki, 'dept_kldiv_ccf.txt', 2,2);
clear ptwiki;
load '../ccf/ccf.ruwiki.tab'
klccf(ccf_dewiki, ccf_ruwiki, 'deru_kldiv_ccf.txt', 2,2);
clear ruwiki;
load '../ccf/ccf.afwiki.tab'
load '../ccf/ccf.scowiki.tab'
load '../ccf/ccf.vlswiki.tab'
load '../ccf/ccf.hifwiki.tab'
klccf(ccf_dewiki, ccf_afwiki, 'deaf_kldiv_ccf.txt', 2,2);
klccf(ccf_dewiki, ccf_scowiki, 'desco_kldiv_ccf.txt', 2,2);
klccf(ccf_dewiki, ccf_hifwiki, 'dehif_kldiv_ccf.txt', 2,2);
klccf(ccf_dewiki, ccf_vlswiki, 'devls_kldiv_ccf.txt', 2,2);
clear afwiki;
clear scowiki;
clear hifwiki;
clear vlswiki;

load '../ccf/ccf.eowiki.tab'
load '../ccf/ccf.lawiki.tab'
klccf(ccf_dewiki, ccf_lawiki, 'dela_kldiv_ccf.txt', 2,2);
klccf(ccf_dewiki, ccf_eowiki, 'deeo_kldiv_ccf.txt', 2,2);
clear all;

