from CRABClient.UserUtilities import config, getUsername
config = config()

config.General.requestName = 'OUTFILENAME'
config.General.workArea = 'resultsAna_JOBTAG/'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/afs/cern.ch/work/l/lgeneros/CMSSW_14_0_9/src/Hcc/HccAna/python/templateMC_QCDZqq_Summer24_JECdB.py'
#config.JobType.outputFiles = ['OUTFILENAME.root']
#config.JobType.scriptExe = 'submitFileCrab.sh'
config.Data.inputDBS = 'global'
config.Data.inputDataset = 'DATASETNAME'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 3
config.Data.allowNonValidInputDataset = True #to run over dataset in "PRODUCTION" status on dBS
config.JobType.numCores = 2
config.JobType.inputFiles  = ['/afs/cern.ch/work/l/lgeneros/CMSSW_14_0_9/src/Hcc/HccAna/python/Summer23Prompt23_V1_MC.db', '/afs/cern.ch/work/l/lgeneros/CMSSW_14_0_9/src/Hcc/HccAna/python/Summer23Prompt23_RunCv1234_JRV1_MC.db', '/afs/cern.ch/work/l/lgeneros/CMSSW_14_0_9/src/Hcc/HccAna/python/Summer23Prompt23_V1_MC_UncertaintySources_AK4PFPuppi.txt']
config.Data.publication = True
# This string is used to construct the output dataset name
config.Data.outputDatasetTag = '140X_mcRun3_2024_realistic_v26_tuple'
config.Site.storageSite = 'T2_IT_Bari'
config.JobType.allowUndistributedCMSSW = True
config.Site.ignoreGlobalBlacklist  = True
