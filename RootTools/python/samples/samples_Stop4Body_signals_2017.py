import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### -----2017
## FullSIM ###
#XS(genAnalyzer) = 0.1523 +/- 0.0008689 pb :  kFactor = 6.56599 ERROR  f(negw): 0.004 +- 0.000 -> 0.1523*6.56599
SMS_T2_4bd_genMET_80_mStop_500_mLSP_420 = kreator.makeMCComponent("SMS_T2_4bd_genMET_80_mStop_500_mLSP_420","/SMS-T2-4bd_genMET-80_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",0.1523*6.56599)
#XS(genAnalyzer) = 0.1444 +/- 0.001218 pb :  kFactor = 6.92521 ERROR  f(negw): 0.003 +- 0.000 -> 0.1444*6.92521
SMS_T2_4bd_genMET_80_mStop_500_mLSP_490 = kreator.makeMCComponent("SMS_T2_4bd_genMET_80_mStop_500_mLSP_490","/SMS-T2-4bd_genMET-80_mStop-500_mLSP-490_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 0.1444*6.92521)

## FastSIM ##
SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1 = kreator.makeMCComponent("SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1","/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM","CMS", ".*root", useAAA = True)

SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1_ext1 = kreator.makeMCComponent("SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1","/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15_ext1-v1/MINIAODSIM","CMS", ".*root", useAAA = True)

signalFullSim = [
SMS_T2_4bd_genMET_80_mStop_500_mLSP_420,
SMS_T2_4bd_genMET_80_mStop_500_mLSP_490
]

signalFastSim = [
SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1
SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1_ext1
]

samples = signalFullSim + signalFastSim


from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

#Define splitting
for comp in signalFullSim:
    comp.isMC = True
    comp.isData = False
    comp.isFastSim = False
    comp.splitFactor = 250 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100

for comp in signalFastSim:
    comp.isMC = True
    comp.isData = False
    comp.isFastSim = True
    comp.splitFactor = 250 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples, localobjs=locals())
    import sys
    if "test" in sys.argv:
        from CMGTools.RootTools.samples.ComponentCreator import testSamples
        testSamples(samples)
