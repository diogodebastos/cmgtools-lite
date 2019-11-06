from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *

##------------------------------------------
## GENJET
##------------------------------------------

genJetType = NTupleObjectType("genJets",  baseObjectTypes = [ fourVectorType ], mcOnly=True, variables = [
    NTupleVariable("nConstituents", lambda x : x.nConstituents(), help="Number of Constituents"),
])

##------------------------------------------
## GENPARTICLE
##------------------------------------------

genParticleWithMotherIndex = NTupleObjectType("genParticleWithMotherIndex", baseObjectTypes = [ genParticleWithMotherId ], mcOnly=True, variables = [
    NTupleVariable("nDaughters",     lambda x : x.numberOfDaughters(),                                                               int, help="index of the daughters in the genParticles"),
    NTupleVariable("nMothers",       lambda x : x.numberOfMothers(),                                                                 int, help="index of the mother in the genParticles"),
    NTupleVariable("motherIndex1",   lambda x : x.motherRef(0).index() if x.numberOfMothers() > 0 else -1,                           int, help="index of the first mother in the genParticles"),
    NTupleVariable("daughterIndex1", lambda x : x.daughterRef(0).index() if x.numberOfDaughters() >0 else -1,                        int, help="index of the first mother in the genParticles"),
    NTupleVariable("motherIndex2",   lambda x : x.motherRef(x.numberOfMothers()-1).index() if x.numberOfMothers() > 1 else -1,       int, help="index of the last mother in the genParticles"),
    NTupleVariable("daughterIndex2", lambda x : x.daughterRef(x.numberOfDaughters()-1).index() if x.numberOfDaughters() > 1 else -1, int, help="index of the last mother in the genParticles"),
])

##------------------------------------------
## LEPTON
##------------------------------------------

leptonTypeStop4Body = NTupleObjectType("leptonStop4Body", baseObjectTypes = [ leptonTypeSusy ], variables = [
    NTupleVariable("eleCutIdPog2017",     lambda x : (1*x.electronID("POG_Cuts_ID_FALL17_94X_v1_Veto") + 1*x.electronID("POG_Cuts_ID_FALL17_94X_v1_Loose") + 1*x.electronID("POG_Cuts_ID_FALL17_94X_v1_Medium") + 1*x.electronID("POG_Cuts_ID_FALL17_94X_v1_Tight")) if abs(x.pdgId()) == 11 else -1, int, help="Electron cut-based id (POG 2017): 0=none, 1=veto, 2=loose, 3=medium, 4=tight"),

    # ELECTRON SUSY ID
    NTupleVariable("eleMVAId2017",     lambda x : (1*x.electronID("MVA_ID_nonIso_Fall17_wp90") + 1*x.electronID("MVA_ID_nonIso_Fall17_wp80")) if abs(x.pdgId()) == 11 else -1, int, help="Electron MVA-based id (POG 2017): 0=none, 1=wp90, 2=wp80"),
    NTupleVariable("SOSTightID2017_wp90",        lambda x : (x.electronID("MVA_ID_nonIso_Fall17_wp90") if x.pt()<10 else x.electronID("MVA_ID_nonIso_Fall17_SUSYTight")) if abs(x.pdgId())==11 else 0, int, help="SOS tight electron MVA noIso ID 2017 (WP: POG wp90 below 10 GeV, SUSYTight above)"),
    NTupleVariable("SOSTightID2017_wp80",        lambda x : (x.electronID("MVA_ID_nonIso_Fall17_wp80") if x.pt()<10 else x.electronID("MVA_ID_nonIso_Fall17_SUSYTight")) if abs(x.pdgId())==11 else 0, int, help="SOS tight electron MVA noIso ID 2017 (WP: POG wp80 below 10 GeV, SUSYTight above)"),
    NTupleVariable("SUSYVLooseFOFall17",         lambda x : x.electronID("MVA_ID_nonIso_Fall17_SUSYVLooseFO")       if abs(x.pdgId())==11 and x.pt()> 5 else 0, int, help="SUSYVLooseFOFall17"),
    NTupleVariable("SUSYVLooseFall17",           lambda x : x.electronID("MVA_ID_nonIso_Fall17_SUSYVLoose")         if abs(x.pdgId())==11 and x.pt()> 5 else 0, int, help="SUSYVLooseFall17"),
    NTupleVariable("SUSYTightFall17",            lambda x : x.electronID("MVA_ID_nonIso_Fall17_SUSYTight")          if abs(x.pdgId())==11 and x.pt()>10 else 0, int, help="SUSYTightFall17"),
    NTupleVariable("trkIso03", lambda x : (x.dr03TkSumPt() if abs(x.pdgId())==11 else x.isolationR03().sumPt)/x.pt(), help="TrkIso R=0.3"),
    NTupleVariable("trkIso045", lambda x : (x.dr04TkSumPt() if abs(x.pdgId())==11 else x.isolationR05().sumPt)/x.pt(), help="TrkIso R=0.4 (e), 0.5 (mu)"),

    #MUON ID
    NTupleVariable("muCutIdPog2017",     lambda x : (1*x.muonID("POG_ID_Soft") + 1*x.muonID("POG_ID_Loose") + 1*x.muonID("POG_ID_Medium") + 1*x.muonID("POG_ID_Tight")) if abs(x.pdgId()) == 13 else -1, int, help="Muon cut-based id (POG 2017): 0=none, 1=soft, 2=loose, 3=medium, 4=tight"),

    NTupleVariable("hOverE",  lambda x : x.hadronicOverEm() if abs(x.pdgId())==11 else 0,                                                                           help="Electron hadronicOverEm"),
    NTupleVariable("ooEmooP", lambda x : ((1.0/x.ecalEnergy() - x.eSuperClusterOverP()/x.ecalEnergy()) if x.ecalEnergy()>0. else 9e9) if abs(x.pdgId())==11 else 0, help="Electron 1/E - 1/p  (without absolute value!)"),

    NTupleVariable("sigmaIEtaIEta",  lambda x : x.full5x5_sigmaIetaIeta() if abs(x.pdgId())==11 else 0,                                                                    help="Electron sigma(ieta ieta), with full5x5 cluster shapes"),
    NTupleVariable("dEtaScTrkIn",    lambda x : x.deltaEtaSuperClusterTrackAtVtx() if abs(x.pdgId())==11 else 0,                                                           help="Electron deltaEtaSuperClusterTrackAtVtx (without absolute value!)"),
    NTupleVariable("dPhiScTrkIn",    lambda x : x.deltaPhiSuperClusterTrackAtVtx() if abs(x.pdgId())==11 else 0,                                                           help="Electron deltaPhiSuperClusterTrackAtVtx (without absolute value!)"),
    NTupleVariable("hadronicOverEm", lambda x : x.hadronicOverEm() if abs(x.pdgId())==11 else 0,                                                                           help="Electron hadronicOverEm"),
    NTupleVariable("eInvMinusPInv",  lambda x : ((1.0/x.ecalEnergy() - x.eSuperClusterOverP()/x.ecalEnergy()) if x.ecalEnergy()>0. else 9e9) if abs(x.pdgId())==11 else 0, help="Electron 1/E - 1/p  (without absolute value!)"),

    #new version used by EGM in Spring15, 7_4_14:
    NTupleVariable("eInvMinusPInv_tkMom", lambda x: ((1.0/x.ecalEnergy()) - (1.0 / x.trackMomentumAtVtx().R() ) if (x.ecalEnergy()>0. and x.trackMomentumAtVtx().R()>0.) else 9e9) if abs(x.pdgId())==11 else 0, help="Electron 1/E - 1/p_tk_vtx  (without absolute value!)"),
    NTupleVariable("etaSc",               lambda x : x.superCluster().eta() if abs(x.pdgId())==11 else -100,                                                                                                     help="Electron supercluster pseudorapidity"),

    NTupleVariable("absIso03",     lambda x : x.absIso03, help="PF Abs Iso, R=0.3, pile-up corrected"),
    NTupleVariable("absIso",       lambda x : x.absIso04, help="PF Rel Iso, R=0.4, pile-up corrected"),

#    NTupleVariable("mt", lambda x : x.mt, help="Transverse Mass calculated for lepton"),
#    NTupleVariable("Q80",          lambda x : x.Q80  ,    help="Q80 variable for the deconstrcuted transverse mass"),
])

##------------------------------------------
## JET
##------------------------------------------

jetTypeStop4Body = NTupleObjectType("jetStop4Body", baseObjectTypes = [ jetTypeSusy ], variables = [
    #NTupleVariable("fixEE2017",      lambda x : ... if x.isData else -1, help="..."),
])
