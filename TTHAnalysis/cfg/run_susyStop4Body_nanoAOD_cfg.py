##########################################################
##        CONFIGURATION FOR SUSY Stop 4 Body TREES      ##
##########################################################

import re, os, sys
from CMGTools.RootTools.samples.configTools import printSummary, mergeExtensions, doTestN, configureSplittingFromTime, cropToLumi
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
from CMGTools.RootTools.samples.autoAAAconfig import autoAAA

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

def byCompName(components, regexps):
    return [ c for c in components if any(re.match(r, c.name) for r in regexps) ]

def extractEra(sampleName):
    return sampleName[sampleName.find("Run"):sampleName.find("Run")+len('Run2000A')]

# OPTIONS

year = int(getHeppyOption("year", "2018"))
preprocessor = getHeppyOption("nanoPreProcessor")
applyTriggersInMC = getHeppyOption('applyTriggersInMC')
justSummary = getHeppyOption("justSummary")

runTTJets = getHeppyOption("runTTJets", False)
runWJets = getHeppyOption("runWJets", False)
runZInv = getHeppyOption("runZInv", False)
runOtherMC1 = getHeppyOption("runOtherMC1", False)
runOtherMC2 = getHeppyOption("runOtherMC2", False)
runFastSim = getHeppyOption("runFastSim",False)
runFullSimSignal = getHeppyOption("runFullSimSignal",False)
runData = getHeppyOption("runData",False)

removeJetReCalibration = getHeppyOption("removeJetReCalibration",False)
removeJecUncertainty = getHeppyOption("removeJecUncertainty",False)
skipT1METCorr = getHeppyOption("skipT1METCorr",False)
isTest = getHeppyOption("test",None) != None and not re.match("^\d+$",getHeppyOption("test"))
allGenParts = getHeppyOption("allGenParts", False)

# SAMPLES

if preprocessor:
    if year == 2018:
        from CMGTools.RootTools.samples.samples_13TeV_RunIIAutumn18MiniAOD import *
        from CMGTools.RootTools.samples.samples_Stop4Body_signals_2018 import *
        from CMGTools.RootTools.samples.samples_13TeV_DATA2018_MiniAOD import *
    elif year == 2017:
        from CMGTools.RootTools.samples.samples_13TeV_RunIIFall17MiniAOD import *
        from CMGTools.RootTools.samples.samples_Stop4Body_signals_2017 import *
        from CMGTools.RootTools.samples.samples_13TeV_DATA2017 import *
    elif year == 2016:
        from CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv2 import *
        from CMGTools.RootTools.samples.samples_Stop4Body_signals_2016 import *
        from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *
else:
    if year == 2018:
        from CMGTools.RootTools.samples.samples_13TeV_RunIIAutumn18NanoAODv4 import samples as mcSamples_
        from CMGTools.RootTools.samples.samples_Stop4Body_signalsNanoAOD_2018 import samples as signalSamples_
        from CMGTools.RootTools.samples.samples_13TeV_DATA2018_NanoAOD import dataSamples_1June2019 as allData
    elif year == 2017:
        from CMGTools.RootTools.samples.samples_13TeV_RunIIFall17NanoAODv4 import samples as mcSamples_
        from CMGTools.RootTools.samples.samples_Stop4Body_signalsNanoAOD_2017 import samples as signalSamples_
        from CMGTools.RootTools.samples.samples_13TeV_DATA2017_NanoAOD import dataSamples_1June2019 as allData
    elif year == 2016:
        from CMGTools.RootTools.samples.samples_13TeV_RunIISummer16NanoAODv4 import samples as mcSamples_
        from CMGTools.RootTools.samples.samples_13TeV_DATA2016_NanoAOD import dataSamples_1June2019 as allData

autoAAA(mcSamples_+allData, quiet=not(getHeppyOption("verboseAAA",False)), redirectorAAA="xrootd-cms.infn.it") # must be done before mergeExtensions
mcSamples_, _ = mergeExtensions(mcSamples_)

# TRIGGERS

if year == 2018:
    from CMGTools.RootTools.samples.triggers_13TeV_DATA2018 import all_triggers as triggers
elif year == 2017:
    from CMGTools.RootTools.samples.triggers_13TeV_DATA2017 import all_triggers as triggers
elif year == 2016:
    from CMGTools.RootTools.samples.triggers_13TeV_Spring16_degStop import all_triggers as triggers
    #from CMGTools.RootTools.samples.triggers_13TeV_DATA2016 import *

DatasetsAndTriggers = []

MCs = []
if runTTJets:   MCs += ["TTJets", "TT(Lep|Had|Semi)_pow"] # TTJets - ttbar
if runWJets:    MCs += ["WJetsToLNu_HT.*"] # WJets
if runZInv:     MCs += ["ZJetsToNuNu_HT.*"] # ZJets
if runOtherMC1: MCs += ["WW", "WZ", "ZZ", # Multiboson
                        "DYJetsToLL_M50_HT.*"] # DYJets
if runOtherMC2: MCs += ["QCD_HT.*", # QCD - Multijet
                        "T_sch_lep","T_tch","TBar_tch","T_tWch_noFullyHad","TBar_tWch_noFullyHad", # Single Top
                        "TTGJets","TTW_LO","TTWToLNu_fxfx","TTZToLLNuNu_amc"] # ttbarX
#"QCD_Mu15", "QCD_Pt(20|30|50|80|120|170)to.*_Mu5",

if runFastSim:  MCs += ["SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1"]

mcSamples = byCompName(mcSamples_, ["%s(|_PS)$"%dset for dset in MCs])
signalSamples = byCompName(signalSamples_,["%s"%dset for dset in MCs])

DatasetsAndTriggers.append(("MET",triggers["met"]))
DatasetsAndTriggers.append(("JetHT",triggers["pfht"]))
#DatasetsAndTriggers.append( ("SingleMuon", triggers["1mu_iso"]) )
#DatasetsAndTriggers.append( ("SingleElectron", triggers["1e_iso"]) if year != 2018 else (None,None) )
#DatasetsAndTriggers.append( ("DoubleMuon", triggers["mumu_iso"] + triggers["3mu"]) )
#DatasetsAndTriggers.append( ("EGamma", triggers["ee"] + triggers["3e"] + triggers["1e_iso"]) if year == 2018 else ("DoubleEG", triggers["ee"] + triggers["3e"]) )
#DatasetsAndTriggers.append( ("MuonEG",triggers["mue"] + triggers["2mu1e"] + triggers["2e1mu"]) )

# make MC
mcTriggers = sum((trigs for (pd,trigs) in DatasetsAndTriggers if trigs), [])
if applyTriggersInMC:
    for comp in mcSamples:
        comp.triggers = mcTriggers

# make data
dataSamples = []; vetoTriggers = []
for pd, trigs in DatasetsAndTriggers:
    if not trigs: continue
    for comp in byCompName(allData, [pd]):
        comp.triggers = trigs[:]
        comp.vetoTriggers = vetoTriggers[:]
        dataSamples.append(comp)
    vetoTriggers += trigs[:]

selectedComponents = mcSamples + dataSamples + signalSamples

if runTTJets or runWJets or runZInv or runOtherMC1 or runOtherMC2:
  selectedComponents = mcSamples
elif runFastSim:
  selectedComponents = signalSamples
elif runData:
  selectedComponents = dataSamples
else:
  selectedComponents = byCompName(selectedComponents, getHeppyOption('selectComponents').split(","))

autoAAA(selectedComponents, quiet=not(getHeppyOption("verboseAAA",False)), redirectorAAA="xrootd-cms.infn.it")

configureSplittingFromTime(mcSamples,  150 if preprocessor else 10,12)
configureSplittingFromTime(dataSamples,100 if preprocessor else 5 ,12)

selectedComponents, _ = mergeExtensions(selectedComponents)

# print summary of components to process
if justSummary:
    printSummary(selectedComponents)
    sys.exit(0)

from CMGTools.TTHAnalysis.tools.nanoAOD.s4b_modules import *
modules = s4b_sequence_step1
cut = None
compression = "ZLIB:3" #"LZ4:4" #"LZMA:9"
branchsel_in = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/python/tools/nanoAOD/branchsel_in.txt"
#branchsel_in = None
branchsel_out = None
#from CMGTools.TTHAnalysis.tools.nanoAOD.ttH_modules import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

if runFastSim:
    modules += [stopMasses]

if runData:
  for comp in selectedComponents:
      era = extractEra(comp.name)[-1]
      jmeCorrections = createJMECorrector(isMC=not runData, dataYear = year, runPeriod=era, jesUncert="Total")
      modules += [jmeCorrections]
      POSTPROCESSOR = PostProcessor(None, [], modules = modules, cut = cut, prefetch = True, longTermCache = False, branchsel = branchsel_in, outputbranchsel = branchsel_out, compression = compression)
      del modules[-1]
      print "comp.name: ", comp.name
      print "era: ", era
else:
  jmeCorrections = createJMECorrector(isMC=not runData, dataYear = year, jesUncert="Total",isFastSim=runFastSim)
  modules += [jmeCorrections, nISR]
  POSTPROCESSOR = PostProcessor(None, [], modules = modules, cut = cut, prefetch = True, longTermCache = False, branchsel = branchsel_in, outputbranchsel = branchsel_out, compression = compression)
