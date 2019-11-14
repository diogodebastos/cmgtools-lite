##########################################################
##        CONFIGURATION FOR SUSY Stop 4 Body TREES      ##
##########################################################

import re, os, sys
from CMGTools.RootTools.samples.configTools import printSummary, mergeExtensions, doTestN, configureSplittingFromTime, cropToLumi
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
from CMGTools.RootTools.samples.autoAAAconfig import autoAAA

from CMGTools.TTHAnalysis.analyzers.treeProducerStop4Body import *
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()
def byCompName(components, regexps):
    return [ c for c in components if any(re.match(r, c.name) for r in regexps) ]

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
        from CMGTools.RootTools.samples.samples_13TeV_DATA2018_NanoAOD import dataSamples_1June2019 as allData
    elif year == 2017:
        from CMGTools.RootTools.samples.samples_13TeV_RunIIFall17NanoAODv4 import samples as mcSamples_
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

mcSamples = byCompName(mcSamples_, ["%s(|_PS)$"%dset for dset in [
    # TTJets - ttbar
    "TTJets", "TT(Lep|Had|Semi)_pow",
    # WJets
    "WJetsToLNu_HT.*"
    # ZJets
    "ZJetsToNuNu_HT.*"
    # OtherMC1
    ## Multiboson
    "WW", "WZ", "ZZ",
    ## DYJets
    "DYJetsToLL_M50_HT.*",
    # OtherMC2
    ## QCD - Multijet
    "QCD_HT.*",
    ## Single Top
    "T_sch_lep","T_tch","TBar_tch","T_tWch_noFullyHad","TBar_tWch_noFullyHad",
    ## ttbarX
    "TTGJets","TTW_LO","TTWToLNu_fxfx","TTZToLLNuNu_amc",

    #"QCD_Mu15", "QCD_Pt(20|30|50|80|120|170)to.*_Mu5",
]])

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

selectedComponents = mcSamples + dataSamples

if getHeppyOption('selectComponents'):
    if getHeppyOption('selectComponents')=='MC':
        selectedComponents = mcSamples
    elif getHeppyOption('selectComponents')=='DATA':
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
#from CMGTools.TTHAnalysis.tools.nanoAOD.ttH_modules import *
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *

jmeCorrections = createJMECorrector(isMC=runData, dataYear = year, jesUncert="All",isFastSim=runFastSim)
#jmeCorrections = createJMECorrector(isMC=runData, dataYear = year, jesUncert="Total",isFastSim=runFastSim)

#ttH_sequence_step1 = [lepSkim, lepMerge, autoPuWeight, yearTag, xsecTag, lepJetBTagCSV, lepJetBTagDeepCSV, lepJetBTagDeepFlav, lepMasses]

modules = s4b_sequence_step1 + [jmeCorrections]
cut = None
compression = "ZLIB:3" #"LZ4:4" #"LZMA:9"
branchsel_in = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/python/tools/nanoAOD/branchsel_in.txt"
branchsel_out = None

POSTPROCESSOR = PostProcessor(None, [], modules = modules,
        cut = cut, prefetch = True, longTermCache = False,
        branchsel = branchsel_in, outputbranchsel = branchsel_out, compression = compression)

sys.exit(0)

# =======================================================

# ==== NEED THIS =====

#add LHE Analyzer
from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer
LHEAna = LHEAnalyzer.defaultConfig
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),LHEAna)

# =======================================================


# --- LEPTON SKIMMING ---
ttHLepSkim.minLeptons = 0
ttHLepSkim.maxLeptons = 999

#-----------------------------------------------------------------------
# Lepton Preselection
#electron
#lepAna.loose_electron_id = "MVA_ID_NonTrig_Spring16_VLooseIdEmu"
lepAna.loose_electron_id      = "POG_Cuts_ID_SPRING15_25ns_v1_ConvVeto_Veto"
lepAna.loose_electron_eta     = 2.5
lepAna.inclusive_electron_pt  = 3
lepAna.loose_electron_pt      = 3
lepAna.inclusive_electron_id  = ""
#muon
lepAna.inclusive_muon_id  = ""
lepAna.inclusive_muon_pt  = 3
lepAna.loose_muon_pt      = 3
lepAna.loose_muon_eta     = 2.4

lepAna.loose_electron_dxy     = 0.1
lepAna.loose_electron_dz      = 0.5
lepAna.loose_muon_dxy         = 0.1
lepAna.loose_muon_dz          = 0.5

lepAna.loose_electron_relIso     = 0.0
lepAna.loose_muon_relIso         = 0.0
lepAna.inclusive_electron_relIso = 0.0
lepAna.inclusive_muon_relIso     = 0.0

lepAna.loose_electron_lostHits     = 3.0
lepAna.inclusive_electron_lostHits = 3.0

lepAna.match_inclusiveLeptons = True

lepAna.packedCandidates = 'packedPFCandidates'

isolation = "hybIso"
lepAna.doIsolationScan = False

if isolation == "miniIso":
    lepAna.doMiniIsolation = True
    lepAna.miniIsolationPUCorr = 'rhoArea'
    lepAna.miniIsolationVetoLeptons = None
    lepAna.loose_muon_isoCut     = lambda muon : muon.miniRelIso < 0.4
    lepAna.loose_electron_isoCut = lambda elec : elec.miniRelIso < 0.4
elif isolation == "relIso03":
    lepAna.ele_isoCorr = "rhoArea"
    lepAna.mu_isoCorr = "rhoArea"
    lepAna.loose_electron_relIso = 0.5
    lepAna.loose_muon_relIso = 0.5
elif isolation == "hybIso":
    lepAna.doMiniIsolation = False
    lepAna.ele_isoCorr = "rhoArea"
    lepAna.mu_isoCorr = "rhoArea"
    absIsoCut   = 20
    ptSwitch    = 25
    relIsoCut   = 1.*absIsoCut/ptSwitch
    lepAna.loose_muon_isoCut     = lambda mu: (mu.absIso03 < absIsoCut) or (mu.relIso03 < relIsoCut)
    lepAna.loose_electron_isoCut = lambda el: (el.absIso03 < absIsoCut) or (el.relIso03 < relIsoCut)

#-----------------------------------------------------------------------
# Jet & MET Preselection
if not removeJecUncertainty:
    jetAna.addJECShifts = True
    jetAna.addJERShifts= True

jetAna.jetPt = 20.
if not removeJecUncertainty:
    jetAnaScaleUp.jetPt   = 20
    jetAnaScaleDown.jetPt = 20

jetAna.jetEta = 4.7
if not removeJecUncertainty:
    jetAnaScaleUp.jetEta   = 4.7
    jetAnaScaleDown.jetEta = 4.7

# Jet-lepton cleaning
jetAna.minLepPt = -1
if not removeJecUncertainty:
    jetAnaScaleUp.minLepPt   = -1
    jetAnaScaleDown.minLepPt = -1

jetAna.copyJetsByValue = True # do not remove this
metAna.copyMETsByValue = True # do not remove this
if not removeJecUncertainty:
    jetAnaScaleDown.copyJetsByValue = True # do not remove this
    metAnaScaleDown.copyMETsByValue = True # do not remove this
    jetAnaScaleUp.copyJetsByValue   = True # do not remove this
    metAnaScaleUp.copyMETsByValue   = True # do not remove this

jetAna.cleanSelectedLeptons = True
jetAna.jetEtaCentral        = 2.4
if not removeJecUncertainty:
    jetAnaScaleDown.cleanSelectedLeptons = True
    jetAnaScaleDown.jetEtaCentral        = 2.4
    jetAnaScaleUp.cleanSelectedLeptons   = True
    jetAnaScaleUp.jetEtaCentral          = 2.4

jetAna.applyL2L3Residual = "Data"
if not removeJecUncertainty:
    jetAnaScaleDown.applyL2L3Residual = "Data"
    jetAnaScaleUp.applyL2L3Residual   = "Data"


# Switch on slow QGL
jetAna.doQG = True
if not removeJecUncertainty:
    jetAnaScaleUp.doQG   = True
    jetAnaScaleDown.doQG = True

jetAna.smearJets = True
if not removeJecUncertainty:
    jetAnaScaleUp.smearJets   = True
    jetAnaScaleDown.smearJets = True

if not skipT1METCorr:
    jetAna.calculateType1METCorrection = True
    #metAna.recalibrate                 = 'type1'
    metAna.recalibrate                 = True
    if not removeJecUncertainty:
        jetAnaScaleUp.calculateType1METCorrection   = True
        metAnaScaleUp.recalibrate                   = True
        jetAnaScaleDown.calculateType1METCorrection = True
        metAnaScaleDown.recalibrate                 = True

if removeJetReCalibration:
    jetAna.recalibrateJets = False
    if not removeJecUncertainty:
        jetAnaScaleUp.recalibrateJets   = False
        jetAnaScaleDown.recalibrateJets = False

if runFastSim:
    myMCGlobalTag = "Spring16_FastSimV1_MC"
    jetAna.applyL2L3Residual = False
    jetAna.relaxJetId = True # relax jetId for FastSIM
    if not removeJecUncertainty:
        jetAnaScaleUp.applyL2L3Residual   = False
        jetAnaScaleDown.applyL2L3Residual = False
        jetAnaScaleUp.relaxJetId   = True
        jetAnaScaleDown.relaxJetId = True

jetAna.calculateSeparateCorrections = True

jetAna.lepSelCut = lambda lep: ( abs(lep.pdgId()) == 11 and lep.pt() > 5 ) or ( abs(lep.pdgId()) == 13 and lep.pt() > 3 )

def jetLepRatio( jet, lepton):
    lep_jet_ratio = lepton.pt()/jet.pt()
    if lep_jet_ratio < 0.5 :
        return (jet, lepton)   ## Don't Clean Jet
    else:
        return lepton             ## Clean Jet
jetAna.jetLepArbitration = jetLepRatio
if not removeJecUncertainty:
    jetAnaScaleUp.jetLepArbitration   = jetLepRatio
    jetAnaScaleDown.jetLepArbitration = jetLepRatio

# SET UP GLOBAL TAGS
jetAna.mcGT        = myMCGlobalTag
jetAna.dataGT      = myDataGlobalTag
#jetAna.runsDataJEC = myDataRuns
if not removeJecUncertainty:
    jetAnaScaleDown.mcGT        = myMCGlobalTag
    jetAnaScaleDown.dataGT      = myDataGlobalTag
    jetAnaScaleUp.mcGT          = myMCGlobalTag
    jetAnaScaleUp.dataGT        = myDataGlobalTag
    #jetAnaScaleDown.runsDataJEC = myDataRuns
    #jetAnaScaleUp.runsDataJEC   = myDataRuns

#-----------------------------------------------------------------------

genAna.allGenTaus = True

if allGenParts:
    susySingleLepton_collections.update(
        {
            #"jets"               : NTupleCollection("JetDirty",    genJetType,                   25, help="Cental jets after full selection but before cleaning, sorted by pt"),
            "genJets"            : NTupleCollection("GenJetDirty", genJetType,                   30, help="Gen Jets before cleaning, sorted by pt"),
            "genParticles"       : NTupleCollection("genPartAll",  genParticleWithMotherIndex,  300, help="all pruned genparticles"),
            "packedGenParticles" : NTupleCollection("PkdGenPart",  genParticleWithMotherIndex, 5000, help="all packed genparticles"),
            "packedPFCandidates" : NTupleCollection("PkdPFCands",  genParticleWithMotherIndex, 5000, help="all packed PF Candidates"),
            "gentopquarks"       : NTupleCollection("GenTop",      genParticleType,               2, help="Generated top quarks from hard scattering (needed separately for top pt reweighting)"),
        }
    )

## Event Analyzer for susy single-lepton (at the moment, it's the TTH one)
from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
ttHEventAna = cfg.Analyzer(
    ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
    minJets25 = 0,
    )

addSoftTracks = False
if addSoftTracks:
    from PhysicsTools.Heppy.analyzers.objects.TrackAnalyzer import TrackAnalyzer
    trackAna = cfg.Analyzer(
        TrackAnalyzer, name='trackAnalyzer',
        setOff=False,
        trackOpt="reco",
        do_mc_match=True,
        )
    genTrackAna = cfg.Analyzer(
        TrackAnalyzer, name='GenTrackAnalyzer',
        setOff=False,
        trackOpt="gen",
        )
    # Insert TrackAna in the sequence:
    susyCoreSequence.insert(susyCoreSequence.index(metAna)+1,
                            genTrackAna)
    susyCoreSequence.insert(susyCoreSequence.index(genTrackAna)+1,
                            trackAna)


if lepAna.doIsolationScan:
    leptonTypeSusyExtraLight.addVariables([
        NTupleVariable("scanAbsIsoCharged005", lambda x : getattr(x, 'ScanAbsIsoCharged005', -999), help="PF abs charged isolation dR=0.05, no pile-up correction"),
        NTupleVariable("scanAbsIsoCharged01",  lambda x : getattr(x, 'ScanAbsIsoCharged01', -999),  help="PF abs charged isolation dR=0.1, no pile-up correction"),
        NTupleVariable("scanAbsIsoCharged02",  lambda x : getattr(x, 'ScanAbsIsoCharged02', -999),  help="PF abs charged isolation dR=0.2, no pile-up correction"),
        NTupleVariable("scanAbsIsoCharged03",  lambda x : getattr(x, 'ScanAbsIsoCharged03', -999),  help="PF abs charged isolation dR=0.3, no pile-up correction"),
        NTupleVariable("scanAbsIsoCharged04",  lambda x : getattr(x, 'ScanAbsIsoCharged04', -999),  help="PF abs charged isolation dR=0.4, no pile-up correction"),
        NTupleVariable("scanAbsIsoNeutral005", lambda x : getattr(x, 'ScanAbsIsoNeutral005', -999), help="PF abs neutral+photon isolation dR=0.05, no pile-up correction"),
        NTupleVariable("scanAbsIsoNeutral01",  lambda x : getattr(x, 'ScanAbsIsoNeutral01', -999),  help="PF abs neutral+photon isolation dR=0.1, no pile-up correction"),
        NTupleVariable("scanAbsIsoNeutral02",  lambda x : getattr(x, 'ScanAbsIsoNeutral02', -999),  help="PF abs neutral+photon isolation dR=0.2, no pile-up correction"),
        NTupleVariable("scanAbsIsoNeutral03",  lambda x : getattr(x, 'ScanAbsIsoNeutral03', -999),  help="PF abs neutral+photon isolation dR=0.3, no pile-up correction"),
        NTupleVariable("scanAbsIsoNeutral04",  lambda x : getattr(x, 'ScanAbsIsoNeutral04', -999),  help="PF abs neutral+photon isolation dR=0.4, no pile-up correction"),
        NTupleVariable("miniIsoR",             lambda x : getattr(x, 'miniIsoR', -999),             help="miniIso cone size"),
        NTupleVariable("effArea",              lambda x : getattr(x, 'EffectiveArea03', -999),      help="effective area used for PU subtraction"),
        NTupleVariable("rhoForEA",             lambda x : getattr(x, 'rho', -999),                  help="rho used for EA PU subtraction")
        ])


## Tree Producer
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name = 'treeProducerStop4Body',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     defaultFloatType = 'F', # use Float_t for floating point
     PDFWeights = PDFWeights,
     globalVariables = susyStop4Body_globalVariables,
     globalObjects = susyStop4Body_globalObjects,
     collections = susyStop4Body_collections,
)

if not runFastSim:
    susyScanAna.doLHE = False # until a proper fix is put in the analyzer
    susyScanAna.useLumiInfo = False
    susyCoreSequence.insert(susyCoreSequence.index(skimAnalyzer), susyCounter)
else:
    lheWeightAna.useLumiInfo = True
    susyScanAna.useLumiInfo  = True
    susyScanAna.doLHE        = True
    susyCounter.bypass_trackMass_check = False
    susyCounter.SMS_varying_masses     = [ 'genSusyMNeutralino','genSusyMChargino' , 'genSusyMStop']
    susyCoreSequence.insert(susyCoreSequence.index(susyScanAna)+1, susyCounter)

jsonAna.useLumiBlocks = True


if runTTJets:
        comp.splitFactor = 3000
if runWJets:
        comp.splitFactor = 500
if runZInv:
        comp.splitFactor = 450
if runOtherMC1:
        comp.splitFactor = 2800
if runOtherMC2:
        comp.splitFactor = 1100
if runFastSim:
        comp.splitFactor = 500
if runFullSimSignal:
        comp.splitFactor = 500
if runData:
        comp.splitFactor = 2800
