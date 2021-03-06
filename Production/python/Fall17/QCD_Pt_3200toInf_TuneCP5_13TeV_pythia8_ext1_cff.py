import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/0A1E33A4-92F6-E811-B463-246E96D14E34.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/1076BD4E-91F6-E811-BCC5-0242AC1C0505.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/2418E147-91F6-E811-90EB-AC1F6B0DE2E6.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/30A0CF51-91F6-E811-8E72-0CC47AFCC6BA.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/3A919CC0-91F6-E811-9744-A0369FC5E9A4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/46C0A6B7-91F6-E811-BD6E-F4E9D4AF6CE0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/5200550E-91F6-E811-B314-1866DA87AFB4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/645E71EE-92F6-E811-BAB6-002590A80DF4.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/6C61B546-91F6-E811-9DCC-001E675A622F.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/82210F7A-97F6-E811-B6DC-5C260AFC8138.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/825D3041-91F6-E811-A559-003048CB8824.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/8E4AEAED-90F6-E811-BD63-002590102E72.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/B45F9DC7-91F6-E811-B58A-3CFDFE636600.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/B61D5467-BBF2-E811-96D4-0025905D1D50.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/BE8A80B9-91F6-E811-BB34-44A842CF0598.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/CE7CCBB0-A2F6-E811-AD20-008CFAF28DB2.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/CEC93E57-91F6-E811-930F-0025905A60AA.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/DEC201B8-91F6-E811-BE80-ECB1D7B67E10.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/E01EDE46-91F6-E811-B0F2-E0071B7A18F0.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/90000/0EA8F1C7-47F9-E811-9BA7-008CFAF74A32.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/90000/4CDB4579-CEFB-E811-8634-509A4C74D078.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/90000/BA64A9EE-46F9-E811-9AF0-0CC47A4D99B6.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/90000/DA35C701-EEF8-E811-A679-1C6A7A266B8F.root',
] )
