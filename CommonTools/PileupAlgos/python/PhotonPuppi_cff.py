import FWCore.ParameterSet.Config as cms
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

puppiPhoton = cms.EDProducer("PuppiPhoton",
                             candName       = cms.InputTag('packedPFCandidates'),
                             puppiCandName  = cms.InputTag('puppi'),
                             photonName     = cms.InputTag('slimmedPhotons'),
                             photonId       = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-25ns-V1-standalone-loose"), 
                             pt             = cms.double(10),
                             eta            = cms.double(2.5),
                             useRefs        = cms.bool(True),
                             dRMatch        = cms.vdouble(10,10,10,10),
                             pdgids         = cms.vint32 (22,11,211,130),
                             weight         = cms.double(1.),
                             useValueMap    = cms.bool(False),
                             weightsName    = cms.InputTag('puppi'),
                             )


def setupPuppiPhoton(process):
    my_id_modules = ['RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Spring15_25ns_V1_cff']
    switchOnVIDPhotonIdProducer(process, DataFormat.MiniAOD)
    for idmod in my_id_modules:
        setupAllVIDIdsInModule(process,idmod,setupVIDPhotonSelection)


#puppiPhotonSeq = cms.Sequence(egmPhotonIDSequence*puppiPhoton)
