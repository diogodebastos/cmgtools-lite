# COMPONENT CREATOR
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

# ====== W + Jets ======
#--- BEGIN MULTIPLE MATCHES
WJetsToLNu_LO = kreator.makeMCComponent("WJetsToLNu_LO","/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 3* 20508.9)
WJetsToLNu_LO = kreator.makeMCComponent("WJetsToLNu_LO","/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM", "CMS", ".*root", 3* 20508.9)
#--- END MULTIPLE MATCHES

## LO XSec from genXSecAna times NNLO/LO XSec for inclusive W+jets
W1JetsToLNu_LO = kreator.makeMCComponent("W1JetsToLNu_LO","/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 8123*1.17)
W2JetsToLNu_LO = kreator.makeMCComponent("W2JetsToLNu_LO","/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 2785*1.17)
W3JetsToLNu_LO = kreator.makeMCComponent("W3JetsToLNu_LO","/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 993.4*1.17)
W4JetsToLNu_LO = kreator.makeMCComponent("W4JetsToLNu_LO","/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 542.4*1.17)

### W+jets HT-binned
WJetsToLNu_HT70to100 = kreator.makeMCComponent("WJetsToLNu_HT70to100", "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",1289*1.27) # miniAOD v2
WJetsToLNu_HT100to200 = kreator.makeMCComponent("WJetsToLNu_HT100to200", "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",1395*1.17) # miniAOD v2
WJetsToLNu_HT200to400 = kreator.makeMCComponent("WJetsToLNu_HT200to400", "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",408.7*1.17) # miniAOD v2
WJetsToLNu_HT400to600 = kreator.makeMCComponent("WJetsToLNu_HT400to600", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",57.52*1.17) # miniAOD v2
WJetsToLNu_HT600to800 = kreator.makeMCComponent("WJetsToLNu_HT600to800", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",12.78*1.17) # miniAOD v2
WJetsToLNu_HT800to1200 = kreator.makeMCComponent("WJetsToLNu_HT800to1200", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",5.246*1.17) # miniAOD v2
WJetsToLNu_HT1200to2500 = kreator.makeMCComponent("WJetsToLNu_HT1200to2500",   "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",1.071*1.17) # miniAOD v2
WJetsToLNu_HT2500toInf = kreator.makeMCComponent("WJetsToLNu_HT2500toInf", "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",0.00819*1.17) # miniAOD v2

WJetsToLNuHT = [WJetsToLNu_HT70to100, WJetsToLNu_HT100to200, WJetsToLNu_HT200to400, WJetsToLNu_HT400to600, WJetsToLNu_HT600to800, WJetsToLNu_HT800to1200, WJetsToLNu_HT1200to2500, WJetsToLNu_HT2500toInf,]

WJets = [WJetsToLNu_LO, W1JetsToLNu_LO, W2JetsToLNu_LO, W3JetsToLNu_LO, W4JetsToLNu_LO,] + WJetsToLNuHT

# ====== TT INCLUSIVE ======
# TTbar cross section: NNLO, https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO (172.5)
TTJets = kreator.makeMCComponent("TTJets", "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 831.76, fracNegWeights=0.319)

TTLep_pow  = kreator.makeMCComponent("TTLep_pow", "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2) )
TTHad_pow  = kreator.makeMCComponent("TTHad_pow", "/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 831.76*((1-3*0.108)**2) )
TTSemi_pow = kreator.makeMCComponent("TTSemi_pow", "/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 831.76*2*(3*0.108)*(1-3*0.108) )

TTs = [ TTJets, TTLep_pow, TTHad_pow, TTHad_pow_ext2, TTSemi_pow,]

# ====== ZInv ======
# ZJetToNunu, cross sections are determined from GenXSecAnalyzer

ZJetsToNuNu_HT100to200 = kreator.makeMCComponent("ZJetsToNuNu_HT100to200", "/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",304.1*1.14)
ZJetsToNuNu_HT200to400 = kreator.makeMCComponent("ZJetsToNuNu_HT200to400", "/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",91.51*1.05)
ZJetsToNuNu_HT400to600 = kreator.makeMCComponent("ZJetsToNuNu_HT400to600", "/ZJetsToNuNu_HT-400To600_13TeV-madgraph/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",13.04*1.04)
ZJetsToNuNu_HT600to800 = kreator.makeMCComponent("ZJetsToNuNu_HT600to800", "/ZJetsToNuNu_HT-600To800_13TeV-madgraph/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",3.251*1.22)
ZJetsToNuNu_HT800to1200 = kreator.makeMCComponent("ZJetsToNuNu_HT800to1200", "/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",1.49*1.22)
ZJetsToNuNu_HT1200to2500 = kreator.makeMCComponent("ZJetsToNuNu_HT1200to2500", "/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",0.3414*1.30)
ZJetsToNuNu_HT2500toInf = kreator.makeMCComponent("ZJetsToNuNu_HT2500toInf", "/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",0.005112*1.98)

ZJetsToNuNuHT = [ ZJetsToNuNu_HT100to200, ZJetsToNuNu_HT200to400, ZJetsToNuNu_HT400to600, ZJetsToNuNu_HT600to800, ZJetsToNuNu_HT800to1200, ZJetsToNuNu_HT1200to2500, ZJetsToNuNu_HT2500toInf,]

# ====== Multiboson ======
WW = kreator.makeMCComponent("WW", "/WW_TuneCP5_13TeV-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 63.21 * 1.82)
WZ = kreator.makeMCComponent("WZ", "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 47.13)
ZZ = kreator.makeMCComponent("ZZ", "/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 16.523)

DiBosons = [WW, WZ, ZZ,]

## Cross sections from getXSecAnalyzer
DYJetsToLL_M4to50_HT100to200 = kreator.makeMCComponent("DYJetsToLL_M4to50_HT100to200","/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM","CMS", ".*root", 202.8)
DYJetsToLL_M4to50_HT100to200_ext1 = kreator.makeMCComponent("DYJetsToLL_M4to50_HT100to200_ext1", "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM", "CMS", ".*root", 202.8)
DYJetsToLL_M4to50_HT200to400 = kreator.makeMCComponent("DYJetsToLL_M4to50_HT200to400","/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM","CMS", ".*root", 53.7)
DYJetsToLL_M4to50_HT200to400_ext1 = kreator.makeMCComponent("DYJetsToLL_M4to50_HT200to400_ext1", "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM", "CMS", ".*root", 53.7)
DYJetsToLL_M4to50_HT400to600 = kreator.makeMCComponent("DYJetsToLL_M4to50_HT400to600","/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM","CMS", ".*root", 5.66)
DYJetsToLL_M4to50_HT400to600_ext1 = kreator.makeMCComponent("DYJetsToLL_M4to50_HT400to600_ext1", "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM", "CMS", ".*root", 5.66)
DYJetsToLL_M4to50_HT600toInf= kreator.makeMCComponent("DYJetsToLL_M4to50_HT600toInf","/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM","CMS", ".*root", 1.852)
DYJetsToLL_M4to50_HT600toInf_ext1 = kreator.makeMCComponent("DYJetsToLL_M4to50_HT600toInf_ext1", "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM", "CMS", ".*root", 1.852)

DYJetsToLLM4to50HT = [ DYJetsToLL_M4to50_HT100to200, DYJetsToLL_M4to50_HT100to200_ext1, DYJetsToLL_M4to50_HT200to400, DYJetsToLL_M4to50_HT200to400_ext1, DYJetsToLL_M4to50_HT400to600, DYJetsToLL_M4to50_HT400to600_ext1, DYJetsToLL_M4to50_HT600toInf, DYJetsToLL_M4to50_HT600toInf_ext1,]

## Cross sections from getXSecAnalyzer times k-factor 1.08 from ratio of FEWZ to inclusive DYJetsToLL_M50_LO
DYJetsToLL_M50_HT100to200 = kreator.makeMCComponent("DYJetsToLL_M50_HT100to200","/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM",   "CMS", ".*root", 161.1*1.08)
DYJetsToLL_M50_HT100to200_ext1 = kreator.makeMCComponent("DYJetsToLL_M50_HT100to200_ext1", "/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM", "CMS", ".*root", 161.1*1.08)
DYJetsToLL_M50_HT200to400 = kreator.makeMCComponent("DYJetsToLL_M50_HT200to400","/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM ", "CMS", ".*root", 49.32*1.08)
DYJetsToLL_M50_HT200to400_ext1 = kreator.makeMCComponent("DYJetsToLL_M50_HT200to400_ext1", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM",  "CMS", ".*root", 49.32*1.08)
DYJetsToLL_M50_HT400to600 = kreator.makeMCComponent("DYJetsToLL_M50_HT400to600","/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 7.021*1.08)
DYJetsToLL_M50_HT400to600_ext1 = kreator.makeMCComponent("DYJetsToLL_M50_HT400to600_ext1", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM",  "CMS", ".*root", 7.021*1.08)
DYJetsToLL_M50_HT600to800 = kreator.makeMCComponent("DYJetsToLL_M50_HT600to800","/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 1.743*1.08 )
DYJetsToLL_M50_HT800to1200 = kreator.makeMCComponent("DYJetsToLL_M50_HT800to1200", "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM","CMS", ".*root", 0.8082*1.08 )
DYJetsToLL_M50_HT1200to2500 = kreator.makeMCComponent("DYJetsToLL_M50_HT1200to2500", "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 0.1925*1.08 )
DYJetsToLL_M50_HT2500toInf = kreator.makeMCComponent("DYJetsToLL_M50_HT2500toInf", "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM","CMS", ".*root", 0.003486*1.08 )

DYJetsToLLM50HT = [ DYJetsToLL_M50_HT100to200, DYJetsToLL_M50_HT100to200_ext1, DYJetsToLL_M50_HT200to400, DYJetsToLL_M50_HT200to400_ext1, DYJetsToLL_M50_HT400to600, DYJetsToLL_M50_HT400to600_ext1, DYJetsToLL_M50_HT600to800, DYJetsToLL_M50_HT800to1200, DYJetsToLL_M50_HT1200to2500, DYJetsToLL_M50_HT2500toInf, ]

DYs = DYJetsToLLM4to50HT + DYJetsToLLM50HT

# QCD HT bins (cross sections from McM)
QCD_HT100to200 = kreator.makeMCComponent("QCD_HT100to200", "/QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 2.463e+07*1.13073)
QCD_HT200to300 = kreator.makeMCComponent("QCD_HT200to300", "/QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 1.553e+06*1.1056)
QCD_HT300to500 = kreator.makeMCComponent("QCD_HT300to500", "/QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 347500*1.01094)
QCD_HT500to700 = kreator.makeMCComponent("QCD_HT500to700", "/QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 29930*1.0568)
QCD_HT700to1000 = kreator.makeMCComponent("QCD_HT700to1000", "/QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 6370*1.06782)
QCD_HT1000to1500 = kreator.makeMCComponent("QCD_HT1000to1500", "/QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 1100*1.09636)
QCD_HT1500to2000 = kreator.makeMCComponent("QCD_HT1500to2000", "/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM", "CMS", ".*root", 98.71)
QCD_HT2000toInf = kreator.makeMCComponent("QCD_HT2000toInf", "/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 20.2)

QCDHT = [ QCD_HT100to200, QCD_HT200to300, QCD_HT300to500, QCD_HT500to700, QCD_HT700to1000, QCD_HT1000to1500, QCD_HT1500to2000, QCD_HT2000toInf,]

# ====== SINGLE TOP ======
# Single top cross sections: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
T_sch_lep = kreator.makeMCComponent("T_sch_lep", "/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", (7.20+4.16)*0.108*3, fracNegWeights=0.188)

T_tch = kreator.makeMCComponent("T_tch", "/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 136.02) # inclusive sample
TBar_tch = kreator.makeMCComponent("TBar_tch", "/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 80.95) # inclusive sample

T_tWch_noFullyHad = kreator.makeMCComponent("T_tWch_noFullyHad", "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",19.55)
TBar_tWch_noFullyHad = kreator.makeMCComponent("TBar_tWch_noFullyHad", "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",19.55)

Ts = [ T_sch_lep ,T_tch , TBar_tch,T_tWch_noFullyHad, TBar_tWch_noFullyHad,]

# ====== T(T) + BOSON =====

TTGJets = kreator.makeMCComponent("TTGJets", "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 4.09, fracNegWeights=0.306)
TTGJets_ext = kreator.makeMCComponent("TTGJets_ext", "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM", "CMS", ".*root", 4.09, fracNegWeights=0.306)

TTWToLNu_fxfx = kreator.makeMCComponent("TTWToLNu_fxfx", "/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 0.2043, fracNegWeights=0.227)
TTW_LO = kreator.makeMCComponent("TTW_LO", "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",  0.6105 )
TTW_LO_ext1 = kreator.makeMCComponent("TTW_LO_ext1", "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM", "CMS", ".*root",  0.6105 )

# TODO: No v7! Using nanoAOD v6 now
TTZToLLNuNu_amc = kreator.makeMCComponent("TTZToLLNuNu_amc", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/NANOAODSIM", "CMS", ".*root", 0.2529, fracNegWeights=0.264)
TTZToLLNuNu_amc_psw = kreator.makeMCComponent("TTZToLLNuNu_amc_psw", "/TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root", 0.2529, fracNegWeights=0.264)
TTZ_LO = kreator.makeMCComponent("TTZ_LO", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", "CMS", ".*root",  0.5297/0.692)
TTZ_LO_ext1 = kreator.makeMCComponent("TTZ_LO_ext1", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM", "CMS", ".*root",  0.5297/0.692)

TTXs = [ TTGJets, TTGJets_ext, TTWToLNu_fxfx, TTW_LO, TTW_LO_ext1, TTZToLLNuNu_amc,TTZToLLNuNu_amc_psw, TTZ_LO, TTZ_LO_ext1,]

# ----------------------------- summary ----------------------------------------

mcSamples = WJets + TTs + ZJetsToNuNuHT + DiBosons + DYs + QCDHT + Ts + TTXs

#mcSamples = ZJetsToNuNuHT + QCDPt + QCDHT + QCD_Mus + QCD_EMs + QCD_bcToE + Ws + DYs + VJetsQQHT + TTs + Ts + TTXs + TTXXs + DiBosons + TriBosons + Higgs


samples = mcSamples

# ---------------------------------------------------------------------

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples, localobjs=locals())
