import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/042DD685-4FA6-E911-A8F5-C45444922D6C.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/06615DB2-56A6-E911-B902-001E674DAFE0.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/2C9509ED-8E8C-E911-9171-44A84225C851.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/2EF6BC38-4A8D-E911-ABE5-0CC47A4D76CC.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/34B3AE6B-67A6-E911-8AA7-001E67DDBFF7.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/362D6954-52A6-E911-B2D5-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/36A8E27E-4C8D-E911-97FA-002590DE6E86.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/3EF01047-898C-E911-8A04-0CC47AFCC3FE.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/46CD55A7-D28B-E911-B536-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/4CBA4B86-648C-E911-8236-A4BF01013F29.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/5C1FBAB8-9F8B-E911-9C42-EC0D9A82261E.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/6272FB38-3EA5-E911-816E-0CC47AFF24CA.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/667764E0-50A6-E911-9A8B-B026283D4B10.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/6CE11E53-45A6-E911-AAC4-3417EBE644BF.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/746F0F16-96A7-E911-AAA8-001E67E6F49A.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/82A872B9-49A6-E911-895B-BC305B390A8D.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/889AE89F-4FA6-E911-AD1F-AC1F6B1B2364.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/8A864CD5-4FA6-E911-9390-0CC47A6C1038.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/8AB2CA00-48A6-E911-AAD1-98039B3AFB12.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/9ABE6DD3-56A6-E911-9866-0CC47AB65046.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/9AD282EA-48A6-E911-A325-002590907812.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/9C8A1F48-5D8D-E911-A73F-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/9E9C62C5-988C-E911-BFF6-90E2BAD492E8.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/A0610711-648C-E911-9421-0017A4770478.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/A20A4609-648C-E911-9244-002590DE6E28.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/A44DCBAF-6A8D-E911-B889-008CFAF70E92.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/A638C934-4BA6-E911-8DB0-B8CA3A708F98.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/B4AD2592-4AA6-E911-A249-0CC47AC17502.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/B4DA1280-5BA6-E911-9478-0CC47A5FC281.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/C66A2F02-DFA5-E911-9F8A-38EAA78D8AF4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/C8E31F11-46A6-E911-991B-3CFDFE6A9494.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/D2F9A73A-938C-E911-999F-0CC47A7E6A4C.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/DE8784E1-56A6-E911-88E1-1CB72C0A3A5D.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/E8AA8B00-59A6-E911-80D1-20CF3027A62B.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/EA339A89-4FA6-E911-8D26-1866DA87967B.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/EC8216B6-928C-E911-BB14-0CC47AA53D98.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/EE640231-7F8C-E911-A74E-B499BAAB31F6.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/F623A378-B88A-E911-9F1A-AC1F6B23C88A.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/FA91F1E5-50A6-E911-97C3-AC1F6B0DE3FA.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/FC39B207-108D-E911-A666-AC1F6B0DE0C4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/FCA620D7-4BA6-E911-A1F0-FA163EB5BC17.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/3CD9C472-B3B4-E911-93D6-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/58FCFBA4-C9B4-E911-9411-001E677923F4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/769F8312-92B3-E911-AAE0-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/8428EA75-B2B4-E911-944F-0CC47AFF0188.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/260000/F84E808C-B6B4-E911-BE92-001C23C0B671.root',
] )
