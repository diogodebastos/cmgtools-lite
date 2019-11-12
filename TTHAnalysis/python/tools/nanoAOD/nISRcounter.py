from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.tools import deltaR
import math

class nISRcounter( Module ):
    def __init__(self,
            jetSel = lambda jet : True):

        self.jetSel = jetSel

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.wrappedOutputTree = wrappedOutputTree
        self.wrappedOutputTree.branch("nIsr","F")

    def analyze(self, event):
        jets = filter(self.jetSel, Collection(event, 'Jet'))
        genParticles = Collection(event, 'GenPart')

        #Can only be performed on MC
        #if not isMC: return True
        event.nIsr = 0
        for jet in jets:
            matched = False
            for part in genParticles:
                if matched: break
                if (part.status != 23 or abs(part.pdgId)>5): continue
                momid = abs(part.genPartIdxMother.pdgId)
                if not (momid==6 or momid==23 or momid==24 or momid==25 or momid>1e6): continue
                for idau in range(part.numberOfDaughters):
                    dR = deltaR(jet.eta,jet.phi, part.daughter(idau).p4().eta,part.daughter(idau).p4().phi)
                    if dR < 0.3:
                        matched = True
                        break
            if not matched:
                event.nIsr+=1

        self.wrappedOutputTree.fillBranch('nIsr', self.nIsr)

        pass
        return True
