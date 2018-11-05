import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/00307C35-8A8B-E811-A7F9-0CC47AB0B828.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/00362515-658B-E811-B6D5-0CC47A0AD456.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/02730CA6-F48A-E811-B2B2-002590586F7C.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/042237F0-648B-E811-ACA3-0CC47AA53D98.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/04E43606-A78A-E811-BDCB-0025907D250C.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/0678EF3D-898B-E811-854B-0CC47A0AD3BC.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/0874C4F8-648B-E811-9EA5-00259029E91C.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/08772800-658B-E811-9EDE-0CC47A0AD6F8.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/088370A5-C68A-E811-A161-002590D9D8D4.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/0A30AC02-658B-E811-BACB-003048CB87DE.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/0E06C3A5-EA8A-E811-AED0-0CC47AA53D98.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/0EE5B899-858B-E811-A547-0CC47A57CBF8.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/10FAF9FD-648B-E811-9C42-00259075D72C.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/128223BC-C68A-E811-83F4-002590D9D96E.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/1469DD10-A78A-E811-975F-002590D9D8C0.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/16EF283C-898B-E811-9771-0CC47AD24D28.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/18E9418F-858B-E811-9F66-0CC47A57CEB4.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/1C44C651-368A-E811-A025-0CC47A57D086.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/1ECF07DE-F38A-E811-AD74-0025907D250C.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/1EF09FF9-648B-E811-9B84-002590FD5A48.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/209FF1BC-EA8A-E811-9FEC-00259029E71C.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/2ABAF9A4-C68A-E811-B792-00259029E920.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/2E02FB57-898B-E811-841B-002590D9D990.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/308223A7-858B-E811-862A-0025907D24F0.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/30B0DC1B-668B-E811-AB3D-0CC47AB0B826.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/32D13212-A78A-E811-AE43-002590D9D8C0.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/32E7A23F-898B-E811-89BC-0CC47A57CDD2.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/36135D90-858B-E811-ADDC-0CC47AB0B828.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/3673A726-5F8A-E811-8371-00259048AD6A.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/385B082D-868A-E811-9C70-0CC47AA53D66.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/3A093923-5F8A-E811-B30F-003048CB7A8A.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/3C5D76E8-648B-E811-B85D-0007432CAA50.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/3E41A931-868A-E811-8117-0CC47A57CC42.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/40A6BC49-898B-E811-BE59-0CC47AB0B828.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/485B7CC0-418A-E811-9E9D-00259029E670.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/48F7639E-1F8C-E811-B4D6-002590D9D894.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/4A2550B4-C68A-E811-A3E7-0CC47A0AD69E.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/4A56EE53-898B-E811-A2D3-0CC47AB0BB0A.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/4CF6A149-898B-E811-A68C-0CC47A0AD6E4.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/521A0058-898B-E811-9100-002590D9D880.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/54736A32-868A-E811-B4A9-0CC47A57CBBC.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/54E0AD21-5F8A-E811-972E-0CC47AA53D6A.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/56789C35-868A-E811-80FE-002590D9D8BA.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/58263F03-658B-E811-A678-0025901AC12A.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/5A503A9D-EA8A-E811-A6FD-0CC47AA53D5A.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/5A594925-5F8A-E811-9807-003048CB8584.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/5AB12D0A-A78A-E811-9C74-0025907D24F0.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/5E8A7EE6-648B-E811-BC57-0CC47AA53D92.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/5E962162-368A-E811-9178-00259029E670.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/62960BC0-C68A-E811-9399-0025901AC3EE.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/62E3FCEB-F78A-E811-B947-0CC47AA53D60.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/660D2748-898B-E811-BFA5-0CC47A57CCE8.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/66290F3A-F88A-E811-A85E-0CC47A57D086.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/6824E43E-868A-E811-9D5E-002590FD5A78.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/68A949EF-278A-E811-9290-00259075D62E.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/68C85146-868A-E811-B3A9-00259048AD6A.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/6ACAAA2C-658B-E811-98D2-002590D9D980.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/6CB7C621-658B-E811-96C1-00259029E84C.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/70D8EEED-648B-E811-BFE8-0025901ABB72.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/76D92053-368A-E811-A532-0CC47A57D086.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/76E0DEEA-648B-E811-B5D8-0CC47AA53D6A.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/78BBFF05-658B-E811-A5A6-003048CB87DE.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/82C2C92D-868A-E811-8453-0CC47A57D1F8.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/84C88007-A78A-E811-9529-0CC47A0AD3BC.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/86295F4C-898B-E811-A879-002590D9D984.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/86EFE1DF-F38A-E811-93D9-002590D9D966.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/8A2C67B4-EA8A-E811-B59D-0CC47A57D036.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/9685008E-858B-E811-BA09-0CC47A57CC26.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/980F3A0C-A78A-E811-B181-0025901AC3EE.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/98B3188D-C68A-E811-BFB7-0025901AC0FA.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/9A56BD48-898B-E811-A996-0025901AC0F8.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/9AE2E8F3-278A-E811-8638-0CC47A0AD742.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/A2B2AA18-5F8A-E811-A06A-0CC47AB0B704.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/A438043C-5F8A-E811-826E-002590FD5122.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/A46191E5-8A8B-E811-A9F6-0CC47A57CEB4.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/A4CC7309-658B-E811-9C35-00259048AE50.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/AA4CED45-658B-E811-9DC9-0025907859C4.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/AEE67FE8-648B-E811-912F-0CC47AA53D6A.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/B4680EB2-C68A-E811-83FC-0CC47AA47824.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/B4EE25F8-648B-E811-8BC6-0CC47A0AD630.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/B6E26547-868A-E811-8222-002590D9D9F6.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/B8391FB6-418A-E811-8374-0025901AC404.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/B8391FB6-418A-E811-8F80-0025901AC404.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/B8ABCC1C-658B-E811-B7F0-0CC47AB0BB0A.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/BADF01AA-EA8A-E811-9E50-002590D9D968.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/BCB640EA-648B-E811-8378-0CC47AA53D5A.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/C04A6BF9-F78A-E811-9B2E-0025907D2000.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/C0812EE1-F78A-E811-832C-0CC47AA53D60.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/C2C21A89-C68A-E811-8719-0CC47AA47824.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/C48241C1-418A-E811-A76D-00259029E670.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/C679889C-C68A-E811-AF7E-0CC47A57D13E.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/C811A157-368A-E811-801A-003048CB8584.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/C83C1A15-658B-E811-8514-003048CB8572.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/CCB57FEE-278A-E811-BFAC-0CC47A57CC42.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/CEEE8708-A78A-E811-AEEA-0CC47AA53D82.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/D238FE42-898B-E811-A02A-0025907859B8.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/D60A1011-A78A-E811-8EBD-002590D9D8C0.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/DC2903AB-EA8A-E811-8219-002590FD5A48.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/DED6BC3E-898B-E811-A83E-0CC47A0AD456.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/E23D703D-868A-E811-B0DC-002590D9D880.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/E44F4F36-868A-E811-92C2-00259029E720.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/E44FCA34-898B-E811-8E7E-0CC47AD24D2A.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/E4BC4908-A78A-E811-91A5-0CC47AA53D82.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/E68D4EF1-278A-E811-A6F7-0CC47A57CCF4.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/E6C51FD5-C68A-E811-92FC-00259075D72C.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/E6CBB102-A78A-E811-B911-0CC47AA53D66.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/E8B6E09D-EA8A-E811-A140-F45214101150.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/EA7916F6-648B-E811-BF26-00259075D62E.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/ECAE1768-658B-E811-BD5E-0025904CBF10.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/F0B04F97-C68A-E811-A4A5-003048CB87DE.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/F67CDE9E-EA8A-E811-AA32-0CC47AA4861C.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/F883DE3B-868A-E811-9962-002590D9D968.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/F885ECF1-648B-E811-B9D5-0CC47A0AD742.root',
       '/store/data/Run2016C/MET/MINIAOD/17Jul2018-v1/00000/F8AFB74B-898B-E811-90C1-0CC47AB0B828.root',
] )