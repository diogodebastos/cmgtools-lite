from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.tools import deltaR
import math

# From: https://github.com/sscruz/nanoAOD-tools/blob/legacy_edge/python/postprocessing/modules/EdgeZ/susyReweight.py
def isInDecayOf(daught, mother, gens):
    isIn = False
    idx = gens.index(daught)
    while (idx > -1):
        if idx != gens.index(mother):
            idx = gens[idx].genPartIdxMother # mother is not the mother of daught, trying with the mother of daught
        else:
            isIn = True
            break
    return isIn

def getRightParentage( gen, gens):
    parentage = []
    idx = gens.index(gen)

    while (idx > -1):
        if abs(gens[idx].pdgId) == 6: return True
        if abs(gens[idx].pdgId) == 23: return True
        if abs(gens[idx].pdgId) == 24: return True
        if abs(gens[idx].pdgId) == 25: return True
        if abs(gens[idx].pdgId) > 99999: return True
        idx = gens[idx].genPartIdxMother
    return False

class nISRcounter( Module ):
    def __init__(self,
            jetSel = lambda jet : True):

        self.jetSel = jetSel

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.wrappedOutputTree = wrappedOutputTree
        self.wrappedOutputTree.branch("nIsr","F")
        self.isMC = bool(inputTree.GetBranch("GenJet_pt"))

    def analyze(self, event):
        #Can only be performed on MC
        #if not isMC: return True
        if not self.isMC: return True

        leps = [ x for x in Collection(event, "Electron")] + [ x for x in Collection(event, "Muon")]
        jets = [ x for x in Collection(event, "Jet")]
        gens = [ x for x in Collection(event, "GenPart")]
        #jets = filter(self.jetSel, Collection(event, 'Jet'))
        #gens = Collection(event, 'GenPart')

        jets = filter( lambda x : x.pt > 35 and abs(x.eta) < 2.4, jets)

        nIsr = 0
        for jet in jets:
            matched = False
            skip = False
            for lep in leps:
                if deltaR(jet,lep) < 0.4:
                    skip = True
                    break
            if skip: continue
            for gen in gens:
                if abs(gen.pdgId)>5 or gen.status != 23: continue
                if gen.genPartIdxMother < 0: continue
#                mom = gens[gen.genPartIdxMother]
#                momid = abs(mom.pdgId)
#                if momid not in [6,23,24,25] and momid < 1e6: continue
#                for gen2 in gens:
#                    if isInDecayOf(gen2, gen, gens):
#                        if deltaR(gen2,jet) < 0.3:
#                            matched = True
#                            break
#                if matched: break
#            if not matched:
#              nIsr+=1
                if deltaR( jet, gen) > 0.3: continue
                if not getRightParentage( gen, gens): continue
                matched = True
                break
            if not matched:
                nIsr+=1

        self.wrappedOutputTree.fillBranch("nIsr", nIsr)
	return True
