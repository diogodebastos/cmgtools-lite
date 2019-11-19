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
        genParticles = [ x for x in Collection(event, "GenPart")]
        #jets = filter(self.jetSel, Collection(event, 'Jet'))
        #genParticles = Collection(event, 'GenPart')

        nIsr = 0
        for jet in jets:
            matched = False
            skip = False
            for lep in leps:
                if deltaR(jet,lep) < 0.4:
                    skip = True
                    break
            if skip: continue
            for part in genParticles:
                if part.status != 23 or abs(part.pdgId)>5: continue
                if part.genPartIdxMother < 0: continue
                mom = genParticles[part.genPartIdxMother]
                momid = abs(mom.pdgId)
                if momid not in [6,23,24,25] and momid < 1e6: continue
                for part2 in genParticles:
                    if isInDecayOf(part2, part, genParticles):
                        if deltaR(part2,jet) < 0.3:
                            matched = True
                            break
                if matched: break
            if not matched:
              nIsr+=1

        self.wrappedOutputTree.fillBranch("nIsr", nIsr)
	return True
