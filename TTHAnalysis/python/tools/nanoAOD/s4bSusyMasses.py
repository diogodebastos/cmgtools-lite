from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection

class stopNeutralinoMasses( Module ):
    def __init__(self):

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.wrappedOutputTree.branch("GenSusyMStop","F")
        self.wrappedOutputTree.branch("GenSusyMNeutralino","F")
    def analyze(self, event):
        genParticles = [ x for x in Collection(event, "GenPart")]

        for gen in genParticles:
            #sTop
            if abs(gen.pdgId)==1000006:
                self.wrappedOutputTree.fillBranch("GenSusyMStop", gen.mass)
            #Neutralino
            if gen.pdgId ==1000022:
                self.wrappedOutputTree.fillBranch("GenSusyMNeutralino", gen.mass)
        return True

stopMasses = lambda : stopNeutralinoMasses()
