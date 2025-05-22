import FWCore.ParameterSet.Config as cms

process = cms.Process("HccAnalysis")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/Run3Summer23MiniAODv4/VBFHto2C_M-125_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_v14-v3/2550000/05cafea2-5726-42b5-aaea-432421ebcb8b.root')
)
process.CondDB = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('')
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
        0.000157, -3e-06
    )
)

process.METSignificance_params = cms.PSet(
    EB_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    EB_PhiResPar = cms.vdouble(0.00502),
    EE_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    EE_PhiResPar = cms.vdouble(0.02511),
    HB_EtResPar = cms.vdouble(0.0, 1.22, 0.05),
    HB_PhiResPar = cms.vdouble(0.02511),
    HE_EtResPar = cms.vdouble(0.0, 1.3, 0.05),
    HE_PhiResPar = cms.vdouble(0.02511),
    HF_EtResPar = cms.vdouble(0.0, 1.82, 0.09),
    HF_PhiResPar = cms.vdouble(0.05022),
    HO_EtResPar = cms.vdouble(0.0, 1.3, 0.005),
    HO_PhiResPar = cms.vdouble(0.02511),
    PF_EtResType1 = cms.vdouble(0.05, 0, 0),
    PF_EtResType2 = cms.vdouble(0.05, 0, 0),
    PF_EtResType3 = cms.vdouble(0.05, 0, 0),
    PF_EtResType4 = cms.vdouble(0.042, 0.1, 0.0),
    PF_EtResType5 = cms.vdouble(0.41, 0.52, 0.25),
    PF_EtResType6 = cms.vdouble(0.0, 1.22, 0.05),
    PF_EtResType7 = cms.vdouble(0.0, 1.22, 0.05),
    PF_PhiResType1 = cms.vdouble(0.002),
    PF_PhiResType2 = cms.vdouble(0.002),
    PF_PhiResType3 = cms.vdouble(0.002),
    PF_PhiResType4 = cms.vdouble(0.0028, 0.0, 0.0022),
    PF_PhiResType5 = cms.vdouble(0.1, 0.1, 0.13),
    PF_PhiResType6 = cms.vdouble(0.02511),
    PF_PhiResType7 = cms.vdouble(0.02511),
    jdphi0 = cms.vdouble(
        0.034, 0.034, 0.034, 0.034, 0.032,
        0.031, 0.028, 0.027, 0.027, 0.027
    ),
    jdphi1 = cms.vdouble(
        0.034, 0.035, 0.035, 0.035, 0.035,
        0.034, 0.031, 0.03, 0.029, 0.027
    ),
    jdphi2 = cms.vdouble(
        0.04, 0.04, 0.04, 0.04, 0.04,
        0.038, 0.036, 0.035, 0.034, 0.033
    ),
    jdphi3 = cms.vdouble(
        0.042, 0.043, 0.044, 0.043, 0.041,
        0.039, 0.039, 0.036, 0.034, 0.031
    ),
    jdphi4 = cms.vdouble(
        0.042, 0.042, 0.043, 0.042, 0.038,
        0.036, 0.036, 0.033, 0.031, 0.031
    ),
    jdphi5 = cms.vdouble(
        0.069, 0.069, 0.064, 0.058, 0.053,
        0.049, 0.049, 0.043, 0.039, 0.04
    ),
    jdphi6 = cms.vdouble(
        0.084, 0.08, 0.072, 0.065, 0.066,
        0.06, 0.051, 0.049, 0.045, 0.045
    ),
    jdphi7 = cms.vdouble(
        0.077, 0.072, 0.059, 0.05, 0.045,
        0.042, 0.039, 0.039, 0.037, 0.031
    ),
    jdphi8 = cms.vdouble(
        0.059, 0.057, 0.051, 0.044, 0.038,
        0.035, 0.037, 0.032, 0.028, 0.028
    ),
    jdphi9 = cms.vdouble(
        0.062, 0.059, 0.053, 0.047, 0.042,
        0.045, 0.036, 0.032, 0.034, 0.044
    ),
    jdpt0 = cms.vdouble(
        0.749, 0.829, 1.099, 1.355, 1.584,
        1.807, 2.035, 2.217, 2.378, 2.591
    ),
    jdpt1 = cms.vdouble(
        0.718, 0.813, 1.133, 1.384, 1.588,
        1.841, 2.115, 2.379, 2.508, 2.772
    ),
    jdpt2 = cms.vdouble(
        0.841, 0.937, 1.316, 1.605, 1.919,
        2.295, 2.562, 2.722, 2.943, 3.293
    ),
    jdpt3 = cms.vdouble(
        0.929, 1.04, 1.46, 1.74, 2.042,
        2.289, 2.639, 2.837, 2.946, 2.971
    ),
    jdpt4 = cms.vdouble(
        0.85, 0.961, 1.337, 1.593, 1.854,
        2.005, 2.209, 2.533, 2.812, 3.047
    ),
    jdpt5 = cms.vdouble(
        1.049, 1.149, 1.607, 1.869, 2.012,
        2.219, 2.289, 2.412, 2.695, 2.865
    ),
    jdpt6 = cms.vdouble(
        1.213, 1.298, 1.716, 2.015, 2.191,
        2.612, 2.863, 2.879, 2.925, 2.902
    ),
    jdpt7 = cms.vdouble(
        1.094, 1.139, 1.436, 1.672, 1.831,
        2.05, 2.267, 2.549, 2.785, 2.86
    ),
    jdpt8 = cms.vdouble(
        0.889, 0.939, 1.166, 1.365, 1.553,
        1.805, 2.06, 2.22, 2.268, 2.247
    ),
    jdpt9 = cms.vdouble(
        0.843, 0.885, 1.245, 1.665, 1.944,
        1.981, 1.972, 2.875, 3.923, 7.51
    ),
    ptresolthreshold = cms.double(10.0),
    resolutionsAlgo = cms.string('AK5PF'),
    resolutionsEra = cms.string('Spring10')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.nanoDQMIO_perLSoutput = cms.PSet(
    MEsToSave = cms.untracked.vstring(
        'Hcal/DigiTask/Occupancy/depth/depth1',
        'Hcal/DigiTask/Occupancy/depth/depth2',
        'Hcal/DigiTask/Occupancy/depth/depth3',
        'Hcal/DigiTask/Occupancy/depth/depth4',
        'Hcal/DigiTask/Occupancy/depth/depth5',
        'Hcal/DigiTask/Occupancy/depth/depth6',
        'Hcal/DigiTask/Occupancy/depth/depth7',
        'Hcal/DigiTask/Occupancy/depth/depthHO',
        'Hcal/DigiTask/OccupancyCut/depth/depth1',
        'Hcal/DigiTask/OccupancyCut/depth/depth2',
        'Hcal/DigiTask/OccupancyCut/depth/depth3',
        'Hcal/DigiTask/OccupancyCut/depth/depth4',
        'Hcal/DigiTask/OccupancyCut/depth/depth5',
        'Hcal/DigiTask/OccupancyCut/depth/depth6',
        'Hcal/DigiTask/OccupancyCut/depth/depth7',
        'Hcal/DigiTask/OccupancyCut/depth/depthHO',
        'EcalBarrel/EBOccupancyTask/EBOT digi occupancy',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +',
        'EcalBarrel/EBOccupancyTask/EBOT DCC entries',
        'EcalEndcap/EEOccupancyTask/EEOT DCC entries',
        'Ecal/EventInfo/processedEvents',
        'PixelPhase1/Tracks/charge_PXBarrel',
        'PixelPhase1/Tracks/charge_PXForward',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-3',
        'HLT/Vertexing/hltPixelVertices/hltPixelVertices/goodvtxNbr',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_pt',
        'HLT/Tracking/pixelTracks/GeneralProperties/Chi2Prob_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/Chi2oNDFVsEta_ImpactPoint_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DeltaZToPVZoom_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DistanceOfClosestApproachToPVVsPhi_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DistanceOfClosestApproachToPVZoom_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/NumberOfTracks_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/Chi2Prob_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/Chi2oNDFVsEta_ImpactPoint_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DeltaZToPVZoom_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DistanceOfClosestApproachToPVVsPhi_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DistanceOfClosestApproachToPVZoom_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/NumberOfTracks_GenTk',
        'HLT/Tracking/tracks/LUMIanalysis/NumberEventsVsLUMI',
        'HLT/Tracking/tracks/PUmonitoring/NumberEventsVsGoodPVtx',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXBarrel',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXForward',
        'PixelPhase1/Tracks/clusterposition_zphi_ontrack',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__9',
        'SiStrip/MechanicalView/TIB/layer_1/NormalizedHitResiduals_TIB__Layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/NormalizedHitResiduals_TIB__Layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/NormalizedHitResiduals_TIB__Layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/NormalizedHitResiduals_TIB__Layer__4',
        'SiStrip/MechanicalView/TIB/layer_1/Summary_ClusterStoNCorr__OnTrack__TIB__layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/Summary_ClusterStoNCorr__OnTrack__TIB__layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/Summary_ClusterStoNCorr__OnTrack__TIB__layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/Summary_ClusterStoNCorr__OnTrack__TIB__layer__4',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__3',
        'SiStrip/MechanicalView/TOB/layer_1/NormalizedHitResiduals_TOB__Layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/NormalizedHitResiduals_TOB__Layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/NormalizedHitResiduals_TOB__Layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/NormalizedHitResiduals_TOB__Layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/NormalizedHitResiduals_TOB__Layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/NormalizedHitResiduals_TOB__Layer__6',
        'SiStrip/MechanicalView/TOB/layer_1/Summary_ClusterStoNCorr__OnTrack__TOB__layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/Summary_ClusterStoNCorr__OnTrack__TOB__layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/Summary_ClusterStoNCorr__OnTrack__TOB__layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/Summary_ClusterStoNCorr__OnTrack__TOB__layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/Summary_ClusterStoNCorr__OnTrack__TOB__layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/Summary_ClusterStoNCorr__OnTrack__TOB__layer__6',
        'SiStrip/MechanicalView/MainDiagonal Position',
        'SiStrip/MechanicalView/NumberOfClustersInPixel',
        'SiStrip/MechanicalView/NumberOfClustersInStrip',
        'Tracking/TrackParameters/generalTracks/LSanalysis/Chi2oNDF_lumiFlag_GenTk',
        'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfRecHitsPerTrack_lumiFlag_GenTk',
        'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfTracks_lumiFlag_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDxyToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDzToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIP3DToPV_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberOfMissingOuterRecHitsPerTrack_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberMORecHitsPerTrackVsPt_GenTk',
        'OfflinePV/offlinePrimaryVertices/tagVtxProb',
        'OfflinePV/offlinePrimaryVertices/tagType',
        'OfflinePV/Resolution/PV/pull_x',
        'OfflinePV/Resolution/PV/pull_y',
        'OfflinePV/Resolution/PV/pull_z',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Constituents',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta_uncor',
        'JetMET/Jet/Cleanedak4PFJetsCHS/JetEnergyCorr',
        'JetMET/Jet/Cleanedak4PFJetsCHS/NJets',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Pt',
        'JetMET/MET/pfMETT1/Cleaned/METSig',
        'JetMET/vertices'
    )
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(2),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

process.patMultPhiCorrParams_Puppi_ULDATA2016postVFPF = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016postVFPF'),
    px = cms.vdouble(0.0234421, -0.371298),
    py = cms.vdouble(-0.00997438, 0.0809178),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2016postVFPG = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016postVFPG'),
    px = cms.vdouble(0.0182134, -0.335786),
    py = cms.vdouble(-0.0063338, 0.093349),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2016postVFPH = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016postVFPH'),
    px = cms.vdouble(0.015702, -0.340832),
    py = cms.vdouble(-0.00544957, 0.199093),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2016preVFPB = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016preVFPB'),
    px = cms.vdouble(-0.00109025, -0.338093),
    py = cms.vdouble(-0.00356058, 0.128407),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2016preVFPC = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016preVFPC'),
    px = cms.vdouble(-0.00271913, -0.342268),
    py = cms.vdouble(0.00187386, 0.104),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2016preVFPD = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016preVFPD'),
    px = cms.vdouble(-0.00254194, -0.305264),
    py = cms.vdouble(-0.00177408, 0.164639),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2016preVFPE = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016preVFPE'),
    px = cms.vdouble(-0.00358835, -0.225435),
    py = cms.vdouble(-0.000444268, 0.180479),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2016preVFPF = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016preVFPF'),
    px = cms.vdouble(0.0056759, -0.454101),
    py = cms.vdouble(-0.00962707, 0.35731),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2017B = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2017B'),
    px = cms.vdouble(-0.00382117, -0.666228),
    py = cms.vdouble(0.0109034, 0.172188),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2017C = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2017C'),
    px = cms.vdouble(-0.00110699, -0.747643),
    py = cms.vdouble(-0.0012184, 0.303817),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2017D = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2017D'),
    px = cms.vdouble(-0.00141442, -0.721382),
    py = cms.vdouble(-0.0011873, 0.21646),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2017E = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2017E'),
    px = cms.vdouble(0.00593859, -0.851999),
    py = cms.vdouble(-0.00754254, 0.245956),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2017F = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2017F'),
    px = cms.vdouble(0.00765682, -0.945001),
    py = cms.vdouble(-0.0154974, 0.804176),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2018A = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2018A'),
    px = cms.vdouble(-0.0073377, 0.0250294),
    py = cms.vdouble(-0.000406059, 0.0417346),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2018B = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2018B'),
    px = cms.vdouble(0.00434261, 0.00892927),
    py = cms.vdouble(0.00234695, 0.20381),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2018C = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2018C'),
    px = cms.vdouble(0.00198311, 0.37026),
    py = cms.vdouble(-0.016127, 0.402029),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULDATA2018D = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2018D'),
    px = cms.vdouble(0.00220647, 0.378141),
    py = cms.vdouble(-0.0160244, 0.471053),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULMC2016postVFP = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULMC2016postVFP'),
    px = cms.vdouble(-0.0060447, -0.4183),
    py = cms.vdouble(0.008331, -0.0990046),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULMC2016preVFP = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULMC2016preVFP'),
    px = cms.vdouble(-0.0058341, -0.395049),
    py = cms.vdouble(0.00971595, -0.101288),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULMC2017 = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULMC2017'),
    px = cms.vdouble(-0.0102265, -0.446416),
    py = cms.vdouble(0.0198663, 0.243182),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_Puppi_ULMC2018 = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULMC2018'),
    px = cms.vdouble(-0.0214557, 0.969428),
    py = cms.vdouble(0.0167134, 0.199296),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_T0pcT1SmearTxy_25ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
        py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T0pcT1SmearTxy_50ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
        py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T0pcT1T2SmearTxy_25ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
        py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T0pcT1T2SmearTxy_50ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
        py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T0pcT1T2Txy_25ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
        py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T0pcT1T2Txy_50ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
        py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T0pcT1Txy_25ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
        py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T0pcT1Txy_50ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
        py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T0pcTxy_25ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
        py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T0pcTxy_50ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
        py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T1SmearTxy_25ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
        py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T1SmearTxy_50ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
        py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T1T2SmearTxy_25ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
        py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T1T2SmearTxy_50ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
        py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T1T2Txy_25ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
        py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T1T2Txy_50ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
        py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T1Txy_25ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
        py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_T1Txy_50ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
        py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_Txy_25ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
        py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_Txy_50ns = cms.VPSet(
    cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
        py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ),
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    )
)

process.patMultPhiCorrParams_ULDATA2016postVFPF = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016postVFPF'),
    px = cms.vdouble(0.134616, -0.89965),
    py = cms.vdouble(0.0397736, 1.0385),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2016postVFPG = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016postVFPG'),
    px = cms.vdouble(0.121809, -0.584893),
    py = cms.vdouble(0.0558974, 0.891234),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2016postVFPH = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016postVFPH'),
    px = cms.vdouble(0.0868828, -0.703489),
    py = cms.vdouble(0.0888774, 0.902632),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2016preVFPB = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016preVFPB'),
    px = cms.vdouble(-0.0214894, -0.188255),
    py = cms.vdouble(0.0876624, 0.812885),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2016preVFPC = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016preVFPC'),
    px = cms.vdouble(-0.032209, 0.067288),
    py = cms.vdouble(0.113917, 0.743906),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2016preVFPD = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016preVFPD'),
    px = cms.vdouble(-0.0293663, 0.21106),
    py = cms.vdouble(0.11331, 0.815787),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2016preVFPE = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016preVFPE'),
    px = cms.vdouble(-0.0132046, 0.20073),
    py = cms.vdouble(0.134809, 0.679068),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2016preVFPF = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2016preVFPF'),
    px = cms.vdouble(-0.0543566, 0.816597),
    py = cms.vdouble(0.114225, 1.17266),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2017B = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2017B'),
    px = cms.vdouble(-0.211161, 0.419333),
    py = cms.vdouble(0.251789, -1.28089),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2017C = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2017C'),
    px = cms.vdouble(-0.185184, -0.164009),
    py = cms.vdouble(0.200941, -0.56853),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2017D = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2017D'),
    px = cms.vdouble(-0.201606, 0.426502),
    py = cms.vdouble(0.188208, -0.58313),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2017E = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2017E'),
    px = cms.vdouble(-0.162472, 0.176329),
    py = cms.vdouble(0.138076, -0.250239),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2017F = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2017F'),
    px = cms.vdouble(-0.210639, 0.72934),
    py = cms.vdouble(0.198626, 1.028),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2018A = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2018A'),
    px = cms.vdouble(0.263733, -1.91115),
    py = cms.vdouble(0.0431304, -0.112043),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2018B = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2018B'),
    px = cms.vdouble(0.400466, -3.05914),
    py = cms.vdouble(0.146125, -0.533233),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2018C = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2018C'),
    px = cms.vdouble(0.430911, -1.42865),
    py = cms.vdouble(0.0620083, -1.46021),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULDATA2018D = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULDATA2018D'),
    px = cms.vdouble(0.457327, -1.56856),
    py = cms.vdouble(0.0684071, -0.928372),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULMC2016postVFP = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULMC2016postVFP'),
    px = cms.vdouble(-0.153497, -0.231751),
    py = cms.vdouble(0.00731978, 0.243323),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULMC2016preVFP = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULMC2016preVFP'),
    px = cms.vdouble(-0.188743, 0.136539),
    py = cms.vdouble(0.0127927, 0.117747),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULMC2017 = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULMC2017'),
    px = cms.vdouble(-0.300155, 1.90608),
    py = cms.vdouble(0.300213, -2.02232),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.patMultPhiCorrParams_ULMC2018 = cms.VPSet(cms.PSet(
    etaMax = cms.double(9.9),
    etaMin = cms.double(-9.9),
    fx = cms.string('((x*[0])+[1])'),
    fy = cms.string('((x*[0])+[1])'),
    name = cms.string('ULMC2018'),
    px = cms.vdouble(0.183518, 0.546754),
    py = cms.vdouble(0.192263, -0.42121),
    type = cms.int32(0),
    varType = cms.int32(3)
))

process.QGTagger = cms.EDProducer("QGTagger",
    computeLikelihood = cms.bool(True),
    jec = cms.InputTag(""),
    jetsLabel = cms.string('QGL_AK4PFchs'),
    mightGet = cms.optional.untracked.vstring,
    srcConstituentWeights = cms.InputTag(""),
    srcJets = cms.InputTag("updatedPatJetsUpdatedJEC"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll"),
    srcVertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices"),
    systematicsLabel = cms.string(''),
    useQualityCuts = cms.bool(False)
)


process.ak4CaloL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloL6SLBCorrector")
)


process.ak4CaloL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4CaloL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4CaloL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloL6SLBCorrector")
)


process.ak4CaloL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak4CaloL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4CaloJetsSoftMuonTagInfos")
)


process.ak4CaloResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak4JPTL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4L1JPTFastjetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4L1JPTFastjetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2Relative')
)


process.ak4JPTL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L3Absolute')
)


process.ak4JPTResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2L3Residual')
)


process.ak4L1JPTFastjetCorrector = cms.EDProducer("L1JPTOffsetCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.InputTag("ak4CaloL1FastjetCorrector")
)


process.ak4L1JPTOffsetCorrector = cms.EDProducer("L1JPTOffsetCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.InputTag("ak4CaloL1OffsetCorrector")
)


process.ak4PFCHSL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFCHSL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1OffsetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1OffsetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)


process.ak4PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)


process.ak4PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak4PFL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFL6SLBCorrector")
)


process.ak4PFL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1OffsetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1OffsetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFL6SLBCorrector")
)


process.ak4PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2Relative')
)


process.ak4PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)


process.ak4PFL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4PFJetsSoftMuonTagInfos")
)


process.ak4PFPuppiL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1FastjetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1FastjetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFPuppiL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1OffsetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1OffsetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFPuppiL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak4PFPuppiL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak4PFPuppiResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2L3Residual')
)


process.ak4PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak4TrackL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4TrackL2RelativeCorrector", "ak4TrackL3AbsoluteCorrector")
)


process.ak4TrackL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4TRK'),
    level = cms.string('L2Relative')
)


process.ak4TrackL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4TRK'),
    level = cms.string('L3Absolute')
)


process.basicJetsForMet = cms.EDProducer("PATJetCleanerForType1MET",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    offsetCorrLabel = cms.InputTag("L1FastJet"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("patJetsReapplyJEC"),
    type1JetPtThreshold = cms.double(15.0)
)


process.cleanedPatJets = cms.EDProducer("PATJetCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("slimmedElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("slimmedMuons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string(''),
    src = cms.InputTag("jetSelectorForMet")
)


process.corrPfMetType1 = cms.EDProducer("PFJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    jetCorrLabelRes = cms.InputTag("ak4PFCHSL1FastL2L3ResidualCorrector"),
    offsetCorrLabel = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("ak4PFJetsCHS"),
    type1JetPtThreshold = cms.double(15.0)
)


process.corrPfMetType2 = cms.EDProducer("Type2CorrectionProducer",
    srcUnclEnergySums = cms.VInputTag(cms.InputTag("corrPfMetType1","type2"), cms.InputTag("corrPfMetType1","offset"), cms.InputTag("pfCandMETcorr")),
    type2CorrFormula = cms.string('A'),
    type2CorrParameter = cms.PSet(
        A = cms.double(1.4)
    )
)


process.genMetExtractor = cms.EDProducer("GenMETExtractor",
    metSource = cms.InputTag("slimmedMETs","","@skipCurrentProcess")
)


process.metrawCalo = cms.EDProducer("RecoMETExtractor",
    correctionLevel = cms.string('rawCalo'),
    metSource = cms.InputTag("slimmedMETs","","@skipCurrentProcess")
)


process.particleFlowDisplacedVertex = cms.EDProducer("PFDisplacedVertexProducer",
    avfParameters = cms.PSet(
        Tini = cms.double(256.0),
        ratio = cms.double(0.25),
        sigmacut = cms.double(6.0)
    ),
    debug = cms.untracked.bool(False),
    longSize = cms.double(5),
    mainVertexLabel = cms.InputTag("offlinePrimaryVertices"),
    minAdaptWeight = cms.double(0.5),
    offlineBeamSpotLabel = cms.InputTag("offlineBeamSpot"),
    primaryVertexCut = cms.double(1.8),
    switchOff2TrackVertex = cms.untracked.bool(True),
    tecCut = cms.double(220),
    tobCut = cms.double(100),
    tracksSelectorParameters = cms.PSet(
        bSelectTracks = cms.bool(True),
        dxy_min = cms.double(0.2),
        nChi2_max = cms.double(5.0),
        nChi2_min = cms.double(0.5),
        nHits_min = cms.int32(6),
        nOuterHits_max = cms.int32(9),
        pt_min = cms.double(0.2),
        quality = cms.string('HighPurity')
    ),
    transvSize = cms.double(1.0),
    verbose = cms.untracked.bool(False),
    vertexCandidatesLabel = cms.InputTag("particleFlowDisplacedVertexCandidate"),
    vertexIdentifierParameters = cms.PSet(
        angles = cms.vdouble(15, 15),
        bIdentifyVertices = cms.bool(True),
        logPrimSec_min = cms.double(0.0),
        looper_eta_max = cms.double(0.1),
        masses = cms.vdouble(
            0.05, 0.485, 0.515, 0.48, 0.52,
            1.107, 1.125, 0.2
        ),
        pt_kink_min = cms.double(3.0),
        pt_min = cms.double(0.5)
    )
)


process.particleFlowPtrs = cms.EDProducer("PFCandidateFwdPtrProducer",
    src = cms.InputTag("particleFlow")
)


process.patCHSMet = cms.EDProducer("PATMETProducer",
    addEfficiencies = cms.bool(False),
    addGenMET = cms.bool(False),
    addMuonCorrections = cms.bool(False),
    addResolutions = cms.bool(False),
    computeMETSignificance = cms.bool(False),
    computeMETSignificant = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genMETSource = cms.InputTag("genMetTrue"),
    metSource = cms.InputTag("pfMetCHS"),
    muonSource = cms.InputTag("muons"),
    parameters = cms.PSet(
        dRMatch = cms.double(0.4),
        jetThreshold = cms.double(15),
        jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
        jpar = cms.vdouble(1.39, 1.26, 1.21, 1.23, 1.28),
        pjpar = cms.vdouble(-0.2586, 0.6173)
    ),
    resolutions = cms.PSet(

    ),
    srcJetResPhi = cms.string('AK4PFchs_phi'),
    srcJetResPt = cms.string('AK4PFchs_pt'),
    srcJetSF = cms.string('AK4PFchs'),
    srcJets = cms.InputTag("cleanedPatJets"),
    srcLeptons = cms.VInputTag("selectedPatElectrons", "selectedPatMuons", "selectedPatPhotons"),
    srcPFCands = cms.InputTag("particleFlow"),
    srcRho = cms.InputTag("fixedGridRhoAll"),
    srcWeights = cms.InputTag(""),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patCaloMet = cms.EDProducer("PATMETProducer",
    addEfficiencies = cms.bool(False),
    addGenMET = cms.bool(False),
    addMuonCorrections = cms.bool(False),
    addResolutions = cms.bool(False),
    computeMETSignificance = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genMETSource = cms.InputTag("genMetTrue"),
    metSource = cms.InputTag("metrawCalo"),
    muonSource = cms.InputTag("muons"),
    parameters = cms.PSet(
        dRMatch = cms.double(0.4),
        jetThreshold = cms.double(15),
        jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
        jpar = cms.vdouble(1.39, 1.26, 1.21, 1.23, 1.28),
        pjpar = cms.vdouble(-0.2586, 0.6173)
    ),
    resolutions = cms.PSet(

    ),
    srcJetResPhi = cms.string('AK4PFchs_phi'),
    srcJetResPt = cms.string('AK4PFchs_pt'),
    srcJetSF = cms.string('AK4PFchs'),
    srcJets = cms.InputTag("cleanedPatJets"),
    srcLeptons = cms.VInputTag("selectedPatElectrons", "selectedPatMuons", "selectedPatPhotons"),
    srcPFCands = cms.InputTag("particleFlow"),
    srcRho = cms.InputTag("fixedGridRhoAll"),
    srcWeights = cms.InputTag(""),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetCorrFactorsReapplyJEC = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet',
        'L2Relative',
        'L3Absolute'
    ),
    mightGet = cms.optional.untracked.vstring,
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsUpdatedJEC = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet',
        'L2Relative',
        'L3Absolute',
        'L2L3Residual'
    ),
    mightGet = cms.optional.untracked.vstring,
    payload = cms.string('AK4PFPuppi'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedJetsPuppi"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetsReapplyJEC = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJEC")),
    jetSource = cms.InputTag("slimmedJets"),
    mightGet = cms.optional.untracked.vstring,
    printWarning = cms.bool(True),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patMETs = cms.EDProducer("PATMETProducer",
    addEfficiencies = cms.bool(False),
    addGenMET = cms.bool(True),
    addMuonCorrections = cms.bool(False),
    addResolutions = cms.bool(False),
    computeMETSignificance = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genMETSource = cms.InputTag("genMetTrue"),
    metSource = cms.InputTag("pfMetT1"),
    muonSource = cms.InputTag("muons"),
    parameters = cms.PSet(
        dRMatch = cms.double(0.4),
        jetThreshold = cms.double(15),
        jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
        jpar = cms.vdouble(1.39, 1.26, 1.21, 1.23, 1.28),
        pjpar = cms.vdouble(-0.2586, 0.6173)
    ),
    resolutions = cms.PSet(

    ),
    srcJetResPhi = cms.string('AK4PFchs_phi'),
    srcJetResPt = cms.string('AK4PFchs_pt'),
    srcJetSF = cms.string('AK4PFchs'),
    srcJets = cms.InputTag("cleanedPatJets"),
    srcLeptons = cms.VInputTag("selectedPatElectrons", "selectedPatMuons", "selectedPatPhotons"),
    srcPFCands = cms.InputTag("particleFlow"),
    srcRho = cms.InputTag("fixedGridRhoAll"),
    srcWeights = cms.InputTag(""),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patPFMet = cms.EDProducer("PATMETProducer",
    addEfficiencies = cms.bool(False),
    addGenMET = cms.bool(True),
    addMuonCorrections = cms.bool(False),
    addResolutions = cms.bool(False),
    computeMETSignificance = cms.bool(True),
    efficiencies = cms.PSet(

    ),
    genMETSource = cms.InputTag("genMetExtractor"),
    metSource = cms.InputTag("pfMet"),
    muonSource = cms.InputTag("muons"),
    parameters = cms.PSet(
        dRMatch = cms.double(0.4),
        jetThreshold = cms.double(15),
        jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
        jpar = cms.vdouble(1.39, 1.26, 1.21, 1.23, 1.28),
        pjpar = cms.vdouble(-0.2586, 0.6173)
    ),
    resolutions = cms.PSet(

    ),
    srcJetResPhi = cms.string('AK4PFchs_phi'),
    srcJetResPt = cms.string('AK4PFchs_pt'),
    srcJetSF = cms.string('AK4PFchs'),
    srcJets = cms.InputTag("cleanedPatJets"),
    srcLeptons = cms.VInputTag(cms.InputTag("slimmedElectrons"), cms.InputTag("slimmedMuons"), cms.InputTag("slimmedPhotons")),
    srcPFCands = cms.InputTag("packedPFCandidates"),
    srcRho = cms.InputTag("fixedGridRhoAll"),
    srcWeights = cms.InputTag(""),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patPFMetT0Corr = cms.EDProducer("Type0PFMETcorrInputProducer",
    correction = cms.PSet(
        formula = cms.string('(x<35)?(-( [0]+x*[1]+pow(x, 2)*[2]+pow(x, 3)*[3] )):(-( [0]+35*[1]+pow(35, 2)*[2]+pow(35, 3)*[3] ))'),
        par0 = cms.double(-0.181414),
        par1 = cms.double(-0.476934),
        par2 = cms.double(0.00863564),
        par3 = cms.double(-4.94181e-05)
    ),
    minDz = cms.double(0.2),
    srcHardScatterVertex = cms.InputTag("selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0"),
    srcPFCandidateToVertexAssociations = cms.InputTag("pfCandidateToVertexAssociation")
)


process.patPFMetT0pcT1 = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"), cms.InputTag("patPFMetT0Corr"))
)


process.patPFMetT0pcT1Smear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag("patPFMetT1T2SmearCorr:type1", cms.InputTag("patPFMetT0Corr"))
)


process.patPFMetT0pcT1T2 = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"), cms.InputTag("patPFMetT2Corr","type2"), cms.InputTag("patPFMetT0Corr"))
)


process.patPFMetT0pcT1T2Smear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag("patPFMetT1T2SmearCorr:type1", cms.InputTag("patPFMetT2SmearCorr","type2"), cms.InputTag("patPFMetT0Corr"))
)


process.patPFMetT0pcT1T2Txy = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"), cms.InputTag("patPFMetT2Corr","type2"), cms.InputTag("patPFMetT0Corr"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT0pcT1T2TxySmear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag("patPFMetT1T2SmearCorr:type1", cms.InputTag("patPFMetT2SmearCorr","type2"), cms.InputTag("patPFMetT0Corr"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT0pcT1Txy = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"), cms.InputTag("patPFMetT0Corr"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT0pcT1TxySmear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag("patPFMetT1T2SmearCorr:type1", cms.InputTag("patPFMetT0Corr"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT1 = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"))
)


process.patPFMetT1ElectronEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrElectronEnDown"))
)


process.patPFMetT1ElectronEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrElectronEnUp"))
)


process.patPFMetT1JetEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetEnDown"))
)


process.patPFMetT1JetEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetEnUp"))
)


process.patPFMetT1JetResDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetResDown"))
)


process.patPFMetT1JetResUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetResUp"))
)


process.patPFMetT1MuonEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrMuonEnDown"))
)


process.patPFMetT1MuonEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrMuonEnUp"))
)


process.patPFMetT1PhotonEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrPhotonEnDown"))
)


process.patPFMetT1PhotonEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrPhotonEnUp"))
)


process.patPFMetT1Smear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2SmearCorr","type1"))
)


process.patPFMetT1SmearElectronEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrElectronEnDown"))
)


process.patPFMetT1SmearElectronEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrElectronEnUp"))
)


process.patPFMetT1SmearJetEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetEnDown"))
)


process.patPFMetT1SmearJetEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetEnUp"))
)


process.patPFMetT1SmearJetResDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrSmearedJetResDown"))
)


process.patPFMetT1SmearJetResUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrSmearedJetResUp"))
)


process.patPFMetT1SmearMuonEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrMuonEnDown"))
)


process.patPFMetT1SmearMuonEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrMuonEnUp"))
)


process.patPFMetT1SmearPhotonEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrPhotonEnDown"))
)


process.patPFMetT1SmearPhotonEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrPhotonEnUp"))
)


process.patPFMetT1SmearTauEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrTauEnDown"))
)


process.patPFMetT1SmearTauEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrTauEnUp"))
)


process.patPFMetT1SmearUnclusteredEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrUnclusteredEnDown"))
)


process.patPFMetT1SmearUnclusteredEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrUnclusteredEnUp"))
)


process.patPFMetT1T2 = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"), cms.InputTag("patPFMetT2Corr","type2"))
)


process.patPFMetT1T2Corr = cms.EDProducer("PATPFJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    mightGet = cms.optional.untracked.vstring,
    offsetCorrLabel = cms.InputTag("L1FastJet"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("cleanedPatJets"),
    type1JetPtThreshold = cms.double(15)
)


process.patPFMetT1T2Smear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag("patPFMetT1T2SmearCorr:type1", cms.InputTag("patPFMetT2SmearCorr","type2"))
)


process.patPFMetT1T2SmearCorr = cms.EDProducer("PATPFJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    mightGet = cms.optional.untracked.vstring,
    offsetCorrLabel = cms.InputTag("L1FastJet"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("selectedPatJetsForMetT1T2SmearCorr"),
    type1JetPtThreshold = cms.double(15)
)


process.patPFMetT1T2Txy = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"), cms.InputTag("patPFMetT2Corr","type2"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT1T2TxySmear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag("patPFMetT1T2SmearCorr:type1", cms.InputTag("patPFMetT2SmearCorr","type2"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT1TauEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrTauEnDown"))
)


process.patPFMetT1TauEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrTauEnUp"))
)


process.patPFMetT1Txy = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT1TxySmear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag("patPFMetT1T2SmearCorr:type1", cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT1UnclusteredEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrUnclusteredEnDown"))
)


process.patPFMetT1UnclusteredEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrUnclusteredEnUp"))
)


process.patPFMetT2Corr = cms.EDProducer("PATPFJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    mightGet = cms.optional.untracked.vstring,
    offsetCorrLabel = cms.InputTag("L1FastJet"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("cleanedPatJets"),
    type1JetPtThreshold = cms.double(15)
)


process.patPFMetT2SmearCorr = cms.EDProducer("PATPFJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    mightGet = cms.optional.untracked.vstring,
    offsetCorrLabel = cms.InputTag("L1FastJet"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("selectedPatJetsForMetT2SmearCorr"),
    type1JetPtThreshold = cms.double(15)
)


process.patPFMetTxy = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetTxyCorr = cms.EDProducer("MultShiftMETcorrInputProducer",
    parameters = cms.VPSet(
        cms.PSet(
            etaMax = cms.double(2.7),
            etaMin = cms.double(0),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('hEtaPlus'),
            px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
            py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
            type = cms.int32(1),
            varType = cms.int32(0)
        ),
        cms.PSet(
            etaMax = cms.double(0),
            etaMin = cms.double(-2.7),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('hEtaMinus'),
            px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
            py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
            type = cms.int32(1),
            varType = cms.int32(0)
        ),
        cms.PSet(
            etaMax = cms.double(1.392),
            etaMin = cms.double(-1.392),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('h0Barrel'),
            px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
            py = cms.vdouble(0.00798098092474, -0.000103998219585),
            type = cms.int32(5),
            varType = cms.int32(0)
        ),
        cms.PSet(
            etaMax = cms.double(3),
            etaMin = cms.double(1.392),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('h0EndcapPlus'),
            px = cms.vdouble(-0.00305719113962, -0.00032676418359),
            py = cms.vdouble(-0.00345131507897, 0.000164816815994),
            type = cms.int32(5),
            varType = cms.int32(0)
        ),
        cms.PSet(
            etaMax = cms.double(-1.392),
            etaMin = cms.double(-3.0),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('h0EndcapMinus'),
            px = cms.vdouble(-0.000159031461755, 0.00012231873804),
            py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
            type = cms.int32(5),
            varType = cms.int32(0)
        ),
        cms.PSet(
            etaMax = cms.double(1.479),
            etaMin = cms.double(-1.479),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('gammaBarrel'),
            px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
            py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
            type = cms.int32(4),
            varType = cms.int32(0)
        ),
        cms.PSet(
            etaMax = cms.double(3.0),
            etaMin = cms.double(1.479),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('gammaEndcapPlus'),
            px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
            py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
            type = cms.int32(4),
            varType = cms.int32(0)
        ),
        cms.PSet(
            etaMax = cms.double(-1.479),
            etaMin = cms.double(-3.0),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('gammaEndcapMinus'),
            px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
            py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
            type = cms.int32(4),
            varType = cms.int32(0)
        ),
        cms.PSet(
            etaMax = cms.double(5.2),
            etaMin = cms.double(2.901376),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('hHFPlus'),
            px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
            py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
            type = cms.int32(6),
            varType = cms.int32(0)
        ),
        cms.PSet(
            etaMax = cms.double(-2.901376),
            etaMin = cms.double(-5.2),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('hHFMinus'),
            px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
            py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
            type = cms.int32(6),
            varType = cms.int32(0)
        ),
        cms.PSet(
            etaMax = cms.double(5.2),
            etaMin = cms.double(2.901376),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('egammaHFPlus'),
            px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
            py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
            type = cms.int32(7),
            varType = cms.int32(0)
        ),
        cms.PSet(
            etaMax = cms.double(-2.901376),
            etaMin = cms.double(-5.2),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('egammaHFMinus'),
            px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
            py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
            type = cms.int32(7),
            varType = cms.int32(0)
        )
    ),
    srcPFlow = cms.InputTag("packedPFCandidates"),
    srcWeights = cms.InputTag(""),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.patSmearedJets = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFchs'),
    algopt = cms.string('AK4PFchs_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJets"),
    useDeterministicSeed = cms.bool(True),
    variation = cms.int32(0)
)


process.patTrkMet = cms.EDProducer("PATMETProducer",
    addEfficiencies = cms.bool(False),
    addGenMET = cms.bool(False),
    addMuonCorrections = cms.bool(False),
    addResolutions = cms.bool(False),
    computeMETSignificance = cms.bool(False),
    computeMETSignificant = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genMETSource = cms.InputTag("genMetTrue"),
    metSource = cms.InputTag("pfMetTrk"),
    muonSource = cms.InputTag("muons"),
    parameters = cms.PSet(
        dRMatch = cms.double(0.4),
        jetThreshold = cms.double(15),
        jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
        jpar = cms.vdouble(1.39, 1.26, 1.21, 1.23, 1.28),
        pjpar = cms.vdouble(-0.2586, 0.6173)
    ),
    resolutions = cms.PSet(

    ),
    srcJetResPhi = cms.string('AK4PFchs_phi'),
    srcJetResPt = cms.string('AK4PFchs_pt'),
    srcJetSF = cms.string('AK4PFchs'),
    srcJets = cms.InputTag("cleanedPatJets"),
    srcLeptons = cms.VInputTag("selectedPatElectrons", "selectedPatMuons", "selectedPatPhotons"),
    srcPFCands = cms.InputTag("particleFlow"),
    srcRho = cms.InputTag("fixedGridRhoAll"),
    srcWeights = cms.InputTag(""),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.pfCandMETcorr = cms.EDProducer("PFCandMETcorrInputProducer",
    src = cms.InputTag("pfCandsNotInJetsForMetCorr"),
    srcWeights = cms.InputTag("")
)


process.pfCandidateToVertexAssociation = cms.EDProducer("PFCand_AssoMap",
    AssociationType = cms.InputTag("Both"),
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    ConversionsCollection = cms.InputTag("allConversions"),
    FinalAssociation = cms.untracked.int32(1),
    GetCleanedCollections = cms.bool(False),
    MaxNumberOfAssociations = cms.int32(1),
    NIVertexCollection = cms.InputTag("particleFlowDisplacedVertex"),
    PFCandidateCollection = cms.InputTag("particleFlow"),
    UseBeamSpotCompatibility = cms.untracked.bool(True),
    V0KshortCollection = cms.InputTag("generalV0Candidates","Kshort"),
    V0LambdaCollection = cms.InputTag("generalV0Candidates","Lambda"),
    VertexCollection = cms.InputTag("offlinePrimaryVertices"),
    doReassociation = cms.bool(True),
    ignoreMissingCollection = cms.bool(True),
    nTrackWeight = cms.double(0.001)
)


process.pfCandsForUnclusteredUnc = cms.EDProducer("CandPtrProjector",
    extendVetoBySingleSourcePtr = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("pfCandsNoJetsNoEleNoMuNoTau"),
    useDeltaRforFootprint = cms.bool(False),
    veto = cms.InputTag("slimmedPhotons")
)


process.pfCandsNoJets = cms.EDProducer("CandPtrProjector",
    extendVetoBySingleSourcePtr = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("packedPFCandidates"),
    useDeltaRforFootprint = cms.bool(False),
    veto = cms.InputTag("cleanedPatJets")
)


process.pfCandsNoJetsNoEle = cms.EDProducer("CandPtrProjector",
    extendVetoBySingleSourcePtr = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("pfCandsNoJets"),
    useDeltaRforFootprint = cms.bool(False),
    veto = cms.InputTag("slimmedElectrons")
)


process.pfCandsNoJetsNoEleNoMu = cms.EDProducer("CandPtrProjector",
    extendVetoBySingleSourcePtr = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("pfCandsNoJetsNoEle"),
    useDeltaRforFootprint = cms.bool(False),
    veto = cms.InputTag("slimmedMuons")
)


process.pfCandsNoJetsNoEleNoMuNoTau = cms.EDProducer("CandPtrProjector",
    extendVetoBySingleSourcePtr = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("pfCandsNoJetsNoEleNoMu"),
    useDeltaRforFootprint = cms.bool(False),
    veto = cms.InputTag("slimmedTaus")
)


process.pfCandsNotInJetsForMetCorr = cms.EDProducer("PFCandidateFromFwdPtrProducer",
    src = cms.InputTag("pfCandsNotInJetsPtrForMetCorr")
)


process.pfCandsNotInJetsPtrForMetCorr = cms.EDProducer("TPPFJetsOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(False),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('noJet'),
    topCollection = cms.InputTag("pfJetsPtrForMetCorr")
)


process.pfJetsPtrForMetCorr = cms.EDProducer("PFJetFwdPtrProducer",
    src = cms.InputTag("ak4PFJets")
)


process.pfMETcorrType0 = cms.EDProducer("Type0PFMETcorrInputProducer",
    correction = cms.PSet(
        formula = cms.string('(x<35)?(-( [0]+x*[1]+pow(x, 2)*[2]+pow(x, 3)*[3] )):(-( [0]+35*[1]+pow(35, 2)*[2]+pow(35, 3)*[3] ))'),
        par0 = cms.double(-0.181414),
        par1 = cms.double(-0.476934),
        par2 = cms.double(0.00863564),
        par3 = cms.double(-4.94181e-05)
    ),
    minDz = cms.double(0.2),
    srcHardScatterVertex = cms.InputTag("selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0"),
    srcPFCandidateToVertexAssociations = cms.InputTag("pfCandidateToVertexAssociation")
)


process.pfMet = cms.EDProducer("RecoMETExtractor",
    correctionLevel = cms.string('raw'),
    metSource = cms.InputTag("slimmedMETs","","@skipCurrentProcess")
)


process.pfMetCHS = cms.EDProducer("PFMETProducer",
    alias = cms.string('@module_label'),
    applyWeight = cms.bool(False),
    calculateSignificance = cms.bool(False),
    globalThreshold = cms.double(0),
    mightGet = cms.optional.untracked.vstring,
    parameters = cms.PSet(

    ),
    src = cms.InputTag("pfCHS"),
    srcJetResPhi = cms.optional.string,
    srcJetResPt = cms.optional.string,
    srcJetSF = cms.optional.string,
    srcJets = cms.optional.InputTag,
    srcLeptons = cms.optional.VInputTag,
    srcRho = cms.optional.InputTag,
    srcWeights = cms.InputTag("")
)


process.pfMetTrk = cms.EDProducer("PFMETProducer",
    alias = cms.string('@module_label'),
    applyWeight = cms.bool(False),
    calculateSignificance = cms.bool(False),
    globalThreshold = cms.double(0),
    mightGet = cms.optional.untracked.vstring,
    parameters = cms.PSet(

    ),
    src = cms.InputTag("pfTrk"),
    srcJetResPhi = cms.optional.string,
    srcJetResPt = cms.optional.string,
    srcJetSF = cms.optional.string,
    srcJets = cms.optional.InputTag,
    srcLeptons = cms.optional.VInputTag,
    srcRho = cms.optional.InputTag,
    srcWeights = cms.InputTag("")
)


process.pileupJetIdUpdated = cms.EDProducer("PileupJetIdProducer",
    algos = cms.VPSet(
        cms.PSet(
            JetIdParams = cms.PSet(
                Pt010_Loose = cms.vdouble(-0.95, -0.72, -0.68, -0.47),
                Pt010_Medium = cms.vdouble(0.26, -0.33, -0.54, -0.37),
                Pt010_Tight = cms.vdouble(0.77, 0.38, -0.31, -0.21),
                Pt1020_Loose = cms.vdouble(-0.95, -0.72, -0.68, -0.47),
                Pt1020_Medium = cms.vdouble(0.26, -0.33, -0.54, -0.37),
                Pt1020_Tight = cms.vdouble(0.77, 0.38, -0.31, -0.21),
                Pt2030_Loose = cms.vdouble(-0.88, -0.55, -0.6, -0.43),
                Pt2030_Medium = cms.vdouble(0.68, -0.04, -0.43, -0.3),
                Pt2030_Tight = cms.vdouble(0.9, 0.6, -0.12, -0.13),
                Pt3040_Loose = cms.vdouble(-0.63, -0.18, -0.43, -0.24),
                Pt3040_Medium = cms.vdouble(0.9, 0.36, -0.16, -0.09),
                Pt3040_Tight = cms.vdouble(0.96, 0.82, 0.2, 0.09),
                Pt4050_Loose = cms.vdouble(-0.19, 0.22, -0.13, -0.03),
                Pt4050_Medium = cms.vdouble(0.96, 0.61, 0.14, 0.12),
                Pt4050_Tight = cms.vdouble(0.98, 0.92, 0.47, 0.29)
            ),
            cutBased = cms.bool(False),
            etaBinnedWeights = cms.bool(True),
            impactParTkThreshold = cms.double(1.0),
            label = cms.string('full'),
            nEtaBins = cms.int32(4),
            tmvaMethod = cms.string('JetIDMVAHighPt'),
            tmvaSpectators = cms.vstring(
                'jetPt',
                'jetEta'
            ),
            trainings = cms.VPSet(
                cms.PSet(
                    jEtaMax = cms.double(2.5),
                    jEtaMin = cms.double(0.0),
                    tmvaVariables = cms.vstring(
                        'nvtx',
                        'beta',
                        'dR2Mean',
                        'frac01',
                        'frac02',
                        'frac03',
                        'frac04',
                        'majW',
                        'minW',
                        'jetR',
                        'jetRchg',
                        'nParticles',
                        'nCharged',
                        'ptD',
                        'pull'
                    ),
                    tmvaWeights = cms.FileInPath('RecoJets/JetProducers/data/pileupJetId_UL18_Eta0p0To2p5_chs_BDT.weights.xml.gz')
                ),
                cms.PSet(
                    jEtaMax = cms.double(2.75),
                    jEtaMin = cms.double(2.5),
                    tmvaVariables = cms.vstring(
                        'nvtx',
                        'beta',
                        'dR2Mean',
                        'frac01',
                        'frac02',
                        'frac03',
                        'frac04',
                        'majW',
                        'minW',
                        'jetR',
                        'jetRchg',
                        'nParticles',
                        'nCharged',
                        'ptD',
                        'pull'
                    ),
                    tmvaWeights = cms.FileInPath('RecoJets/JetProducers/data/pileupJetId_UL18_Eta2p5To2p75_chs_BDT.weights.xml.gz')
                ),
                cms.PSet(
                    jEtaMax = cms.double(3.0),
                    jEtaMin = cms.double(2.75),
                    tmvaVariables = cms.vstring(
                        'nvtx',
                        'beta',
                        'dR2Mean',
                        'frac01',
                        'frac02',
                        'frac03',
                        'frac04',
                        'majW',
                        'minW',
                        'jetR',
                        'jetRchg',
                        'nParticles',
                        'nCharged',
                        'ptD',
                        'pull'
                    ),
                    tmvaWeights = cms.FileInPath('RecoJets/JetProducers/data/pileupJetId_UL18_Eta2p75To3p0_chs_BDT.weights.xml.gz')
                ),
                cms.PSet(
                    jEtaMax = cms.double(5.0),
                    jEtaMin = cms.double(3.0),
                    tmvaVariables = cms.vstring(
                        'nvtx',
                        'dR2Mean',
                        'frac01',
                        'frac02',
                        'frac03',
                        'frac04',
                        'majW',
                        'minW',
                        'jetR',
                        'nParticles',
                        'ptD',
                        'pull'
                    ),
                    tmvaWeights = cms.FileInPath('RecoJets/JetProducers/data/pileupJetId_UL18_Eta3p0To5p0_chs_BDT.weights.xml.gz')
                )
            ),
            version = cms.int32(-1)
        ),
        cms.PSet(
            JetIdParams = cms.PSet(
                Pt010_BetaStarLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt010_BetaStarMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt010_BetaStarTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt010_RMSLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt010_RMSMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt010_RMSTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt1020_BetaStarLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt1020_BetaStarMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt1020_BetaStarTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt1020_RMSLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt1020_RMSMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt1020_RMSTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt2030_BetaStarLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt2030_BetaStarMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt2030_BetaStarTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt2030_RMSLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt2030_RMSMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt2030_RMSTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt3040_BetaStarLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt3040_BetaStarMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt3040_BetaStarTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt3040_RMSLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt3040_RMSMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt3040_RMSTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt4050_BetaStarLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt4050_BetaStarMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt4050_BetaStarTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt4050_RMSLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt4050_RMSMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt4050_RMSTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0)
            ),
            cutBased = cms.bool(True),
            impactParTkThreshold = cms.double(1.0),
            label = cms.string('cutbased')
        )
    ),
    applyJec = cms.bool(False),
    inputIsCorrected = cms.bool(True),
    jec = cms.string('AK4PFchs'),
    jetids = cms.InputTag(""),
    jets = cms.InputTag("slimmedJetsSmeared"),
    produceJetIds = cms.bool(True),
    residualsFromTxt = cms.bool(False),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runMvas = cms.bool(True),
    srcConstituentWeights = cms.InputTag(""),
    vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.shiftedPatElectronEnDown = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("pfElectrons"),
    srcWeights = cms.InputTag(""),
    uncertainty = cms.string('((abs(y)<1.479)?(0.006+0*x):(0.015+0*x))')
)


process.shiftedPatElectronEnUp = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(1.0),
    src = cms.InputTag("pfElectrons"),
    srcWeights = cms.InputTag(""),
    uncertainty = cms.string('((abs(y)<1.479)?(0.006+0*x):(0.015+0*x))')
)


process.shiftedPatJetEnDown = cms.EDProducer("ShiftedPATJetProducer",
    addResidualJES = cms.bool(True),
    jetCorrLabelUpToL3 = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3ResidualCorrector"),
    jetCorrPayloadName = cms.string('AK4PFchs'),
    jetCorrUncertaintyTag = cms.string('Uncertainty'),
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("cleanedPatJets")
)


process.shiftedPatJetEnUp = cms.EDProducer("ShiftedPATJetProducer",
    addResidualJES = cms.bool(True),
    jetCorrLabelUpToL3 = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3ResidualCorrector"),
    jetCorrPayloadName = cms.string('AK4PFchs'),
    jetCorrUncertaintyTag = cms.string('Uncertainty'),
    shiftBy = cms.double(1.0),
    src = cms.InputTag("cleanedPatJets")
)


process.shiftedPatJetResDown = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFchs'),
    algopt = cms.string('AK4PFchs_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJets"),
    useDeterministicSeed = cms.bool(True),
    variation = cms.int32(-101)
)


process.shiftedPatJetResUp = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFchs'),
    algopt = cms.string('AK4PFchs_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJets"),
    useDeterministicSeed = cms.bool(True),
    variation = cms.int32(101)
)


process.shiftedPatMETCorrElectronEnDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("pfElectrons"),
    srcShifted = cms.InputTag("shiftedPatElectronEnDown"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrElectronEnUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("pfElectrons"),
    srcShifted = cms.InputTag("shiftedPatElectronEnUp"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrJetEnDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("cleanedPatJets"),
    srcShifted = cms.InputTag("shiftedPatJetEnDown"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrJetEnUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("cleanedPatJets"),
    srcShifted = cms.InputTag("shiftedPatJetEnUp"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrJetResDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("cleanedPatJets"),
    srcShifted = cms.InputTag("shiftedPatJetResDown"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrJetResUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("cleanedPatJets"),
    srcShifted = cms.InputTag("shiftedPatJetResUp"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrMuonEnDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("pfMuons"),
    srcShifted = cms.InputTag("shiftedPatMuonEnDown"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrMuonEnUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("pfMuons"),
    srcShifted = cms.InputTag("shiftedPatMuonEnUp"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrPhotonEnDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("pfPhotons"),
    srcShifted = cms.InputTag("shiftedPatPhotonEnDown"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrPhotonEnUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("pfPhotons"),
    srcShifted = cms.InputTag("shiftedPatPhotonEnUp"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrSmearedJetResDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("selectedPatJetsForMetT1T2SmearCorr"),
    srcShifted = cms.InputTag("shiftedPatSmearedJetResDown"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrSmearedJetResUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("selectedPatJetsForMetT1T2SmearCorr"),
    srcShifted = cms.InputTag("shiftedPatSmearedJetResUp"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrTauEnDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("pfTaus"),
    srcShifted = cms.InputTag("shiftedPatTauEnDown"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrTauEnUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("pfTaus"),
    srcShifted = cms.InputTag("shiftedPatTauEnUp"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrUnclusteredEnDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("pfCandsForUnclusteredUnc"),
    srcShifted = cms.InputTag("shiftedPatUnclusteredEnDown"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMETCorrUnclusteredEnUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("pfCandsForUnclusteredUnc"),
    srcShifted = cms.InputTag("shiftedPatUnclusteredEnUp"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatMuonEnDown = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("pfMuons"),
    srcWeights = cms.InputTag(""),
    uncertainty = cms.string('((x<100)?(0.002+0*y):(0.05+0*y))')
)


process.shiftedPatMuonEnUp = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(1.0),
    src = cms.InputTag("pfMuons"),
    srcWeights = cms.InputTag(""),
    uncertainty = cms.string('((x<100)?(0.002+0*y):(0.05+0*y))')
)


process.shiftedPatPhotonEnDown = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("pfPhotons"),
    srcWeights = cms.InputTag(""),
    uncertainty = cms.string('((abs(y)<1.479)?(0.01+0*x):(0.025+0*x))')
)


process.shiftedPatPhotonEnUp = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(1.0),
    src = cms.InputTag("pfPhotons"),
    srcWeights = cms.InputTag(""),
    uncertainty = cms.string('((abs(y)<1.479)?(0.01+0*x):(0.025+0*x))')
)


process.shiftedPatSmearedJetResDown = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFchs'),
    algopt = cms.string('AK4PFchs_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJets"),
    useDeterministicSeed = cms.bool(True),
    variation = cms.int32(-1)
)


process.shiftedPatSmearedJetResUp = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFchs'),
    algopt = cms.string('AK4PFchs_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJets"),
    useDeterministicSeed = cms.bool(True),
    variation = cms.int32(1)
)


process.shiftedPatTauEnDown = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("pfTaus"),
    srcWeights = cms.InputTag(""),
    uncertainty = cms.string('0.03+0*x*y')
)


process.shiftedPatTauEnUp = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(1.0),
    src = cms.InputTag("pfTaus"),
    srcWeights = cms.InputTag(""),
    uncertainty = cms.string('0.03+0*x*y')
)


process.shiftedPatUnclusteredEnDown = cms.EDProducer("ShiftedParticleProducer",
    binning = cms.VPSet(
        cms.PSet(
            binSelection = cms.string('charge!=0'),
            binUncertainty = cms.string('sqrt(pow(0.00009*x,2)+pow(0.0085/sqrt(sin(2*atan(exp(-y)))),2))')
        ),
        cms.PSet(
            binSelection = cms.string('pdgId==130'),
            binUncertainty = cms.string('((abs(y)<1.3)?(min(0.25,sqrt(0.64/x+0.0025))):(min(0.30,sqrt(1.0/x+0.0016))))'),
            energyDependency = cms.bool(True)
        ),
        cms.PSet(
            binSelection = cms.string('pdgId==22'),
            binUncertainty = cms.string('sqrt(0.0009/x+0.000001)+0*y'),
            energyDependency = cms.bool(True)
        ),
        cms.PSet(
            binSelection = cms.string('pdgId==1 || pdgId==2'),
            binUncertainty = cms.string('sqrt(1./x+0.0025)+0*y'),
            energyDependency = cms.bool(True)
        )
    ),
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("pfCandsForUnclusteredUnc"),
    srcWeights = cms.InputTag("")
)


process.shiftedPatUnclusteredEnUp = cms.EDProducer("ShiftedParticleProducer",
    binning = cms.VPSet(
        cms.PSet(
            binSelection = cms.string('charge!=0'),
            binUncertainty = cms.string('sqrt(pow(0.00009*x,2)+pow(0.0085/sqrt(sin(2*atan(exp(-y)))),2))')
        ),
        cms.PSet(
            binSelection = cms.string('pdgId==130'),
            binUncertainty = cms.string('((abs(y)<1.3)?(min(0.25,sqrt(0.64/x+0.0025))):(min(0.30,sqrt(1.0/x+0.0016))))'),
            energyDependency = cms.bool(True)
        ),
        cms.PSet(
            binSelection = cms.string('pdgId==22'),
            binUncertainty = cms.string('sqrt(0.0009/x+0.000001)+0*y'),
            energyDependency = cms.bool(True)
        ),
        cms.PSet(
            binSelection = cms.string('pdgId==1 || pdgId==2'),
            binUncertainty = cms.string('sqrt(1./x+0.0025)+0*y'),
            energyDependency = cms.bool(True)
        )
    ),
    shiftBy = cms.double(1.0),
    src = cms.InputTag("pfCandsForUnclusteredUnc"),
    srcWeights = cms.InputTag("")
)


process.slimmedJetsSmeared = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFPuppi'),
    algopt = cms.string('AK4PFPuppi_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("updatedPatJetsUpdatedJEC"),
    uncertaintySource = cms.string(''),
    variation = cms.int32(0)
)


process.slimmedJetsSmearedDown = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFPuppi'),
    algopt = cms.string('AK4PFPuppi_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("updatedPatJetsUpdatedJEC"),
    uncertaintySource = cms.string(''),
    variation = cms.int32(-1)
)


process.slimmedJetsSmearedUp = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFPuppi'),
    algopt = cms.string('AK4PFPuppi_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("updatedPatJetsUpdatedJEC"),
    uncertaintySource = cms.string(''),
    variation = cms.int32(1)
)


process.slimmedMETs = cms.EDProducer("PATMETSlimmer",
    addDeepMETs = cms.bool(False),
    caloMET = cms.InputTag("patCaloMet"),
    chsMET = cms.InputTag("patCHSMet"),
    deepMETResolutionTune = cms.InputTag("deepMETsResolutionTune"),
    deepMETResponseTune = cms.InputTag("deepMETsResponseTune"),
    rawVariation = cms.InputTag("patPFMet"),
    runningOnMiniAOD = cms.bool(True),
    src = cms.InputTag("patPFMetT1"),
    t01Variation = cms.InputTag("slimmedMETs","","@skipCurrentProcess"),
    t1SmearedVarsAndUncs = cms.InputTag("patPFMetT1Smear%s"),
    t1Uncertainties = cms.InputTag("patPFMetT1%s"),
    tXYUncForT1 = cms.InputTag("patPFMetT1Txy"),
    trkMET = cms.InputTag("patTrkMet")
)


process.unpackedPatTrigger = cms.EDProducer("PATTriggerObjectStandAloneUnpacker",
    patTriggerObjectsStandAlone = cms.InputTag("slimmedPatTrigger"),
    triggerResults = cms.InputTag("TriggerResults","","HLT"),
    unpackFilterLabels = cms.bool(True)
)


process.updatedPatJetsPileupJetID = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag("updatedPatJetCorrFactors"),
    jetSource = cms.InputTag("slimmedJetsSmeared"),
    mightGet = cms.optional.untracked.vstring,
    printWarning = cms.bool(True),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("pileupJetIdUpdated:fullDiscriminant")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("pileupJetIdUpdated:fullId")
        )
    )
)


process.updatedPatJetsQGT = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag("updatedPatJetCorrFactors"),
    jetSource = cms.InputTag("updatedPatJetsUpdatedJEC"),
    mightGet = cms.optional.untracked.vstring,
    printWarning = cms.bool(True),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("QGTagger:qgLikelihood")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.updatedPatJetsUpdatedJEC = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsUpdatedJEC")),
    jetSource = cms.InputTag("slimmedJetsPuppi"),
    mightGet = cms.optional.untracked.vstring,
    printWarning = cms.bool(True),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.jetSelectorForMet = cms.EDFilter("PATJetSelector",
    cut = cms.string('pt>15 && abs(eta)<9.9'),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("basicJetsForMet")
)


process.pfCHS = cms.EDFilter("CandPtrSelector",
    cut = cms.string('fromPV(0)>0 || (vertexRef().key<=2 && abs(dz(0))<0.2)'),
    src = cms.InputTag("packedPFCandidates")
)


process.pfElectrons = cms.EDFilter("CandPtrSelector",
    cut = cms.string("pt > 5 && isPF && gsfTrack.isAvailable() && gsfTrack.hitPattern().numberOfLostHits(\'MISSING_INNER_HITS\') < 2"),
    src = cms.InputTag("slimmedElectrons")
)


process.pfMuons = cms.EDFilter("CandPtrSelector",
    cut = cms.string('pt > 5.0 && isPFMuon && abs(eta) < 2.4'),
    src = cms.InputTag("slimmedMuons")
)


process.pfNoPileUp = cms.EDFilter("CandPtrSelector",
    cut = cms.string('fromPV > 1'),
    src = cms.InputTag("packedPFCandidates")
)


process.pfPhotons = cms.EDFilter("CandPtrSelector",
    cut = cms.string('abs(pdgId) = 22'),
    src = cms.InputTag("pfCHS")
)


process.pfTaus = cms.EDFilter("PATTauRefSelector",
    cut = cms.string('pt > 18.0 & abs(eta) < 2.6 & tauID("decayModeFinding") > 0.5 & isPFTau'),
    src = cms.InputTag("slimmedTaus")
)


process.pfTrk = cms.EDFilter("CandPtrSelector",
    cut = cms.string('charge()!=0 && pvAssociationQuality()>=4 && vertexRef().key()==0'),
    src = cms.InputTag("packedPFCandidates")
)


process.selectedPatJetsForMetT1T2Corr = cms.EDFilter("PATJetSelector",
    cut = cms.string('abs(eta) < 9.9'),
    filter = cms.bool(False),
    src = cms.InputTag("patJets")
)


process.selectedPatJetsForMetT1T2SmearCorr = cms.EDFilter("PATJetSelector",
    cut = cms.string('abs(eta) < 9.9'),
    filter = cms.bool(False),
    src = cms.InputTag("patSmearedJets")
)


process.selectedPatJetsForMetT2Corr = cms.EDFilter("PATJetSelector",
    cut = cms.string('abs(eta) > 9.9'),
    filter = cms.bool(False),
    src = cms.InputTag("patJets")
)


process.selectedPatJetsForMetT2SmearCorr = cms.EDFilter("PATJetSelector",
    cut = cms.string('abs(eta) > 9.9'),
    filter = cms.bool(False),
    src = cms.InputTag("patSmearedJets")
)


process.selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0 = cms.EDFilter("PATSingleVertexSelector",
    filter = cms.bool(False),
    mode = cms.string('firstVertex'),
    vertices = cms.InputTag("selectedVerticesForPFMEtCorrType0")
)


process.selectedUpdatedPatJetsPileupJetID = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("updatedPatJetsPileupJetID")
)


process.selectedUpdatedPatJetsQGT = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("updatedPatJetsQGT")
)


process.selectedUpdatedPatJetsUpdatedJEC = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("updatedPatJetsUpdatedJEC")
)


process.selectedVerticesForPFMEtCorrType0 = cms.EDFilter("VertexSelector",
    cut = cms.string('isValid & ndof >= 4 & chi2 > 0 & tracksSize > 0 & abs(z) < 24 & abs(position.Rho) < 2.'),
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices")
)


process.Ana = cms.EDAnalyzer("HccAna",
    AK4PuppiJetSmearDownSrc = cms.InputTag("slimmedJetsSmearedDown"),
    AK4PuppiJetSmearSrc = cms.InputTag("slimmedJetsSmeared"),
    AK4PuppiJetSmearUpSrc = cms.InputTag("slimmedJetsSmearedUp"),
    AK4PuppiJetSrc = cms.InputTag("updatedPatJetsQGT"),
    AK4PuppiJetUncorrSrc = cms.InputTag("slimmedJetsPuppi"),
    AK8PuppiJetSrc = cms.untracked.InputTag("slimmedJetsAK8"),
    CrossSection = cms.untracked.double(1),
    FilterEff = cms.untracked.double(1),
    JECUncFileAK4Src = cms.string('Summer23Prompt23_V1_MC_UncertaintySources_AK4PFPuppi.txt'),
    beamSpotSrc = cms.untracked.InputTag("offlineBeamSpot"),
    conversionSrc = cms.untracked.InputTag("reducedEgamma","reducedConversions"),
    doJEC = cms.untracked.bool(True),
    doJER = cms.untracked.bool(True),
    doTriggerMatching = cms.untracked.bool(False),
    elRhoSrc = cms.untracked.InputTag("fixedGridRhoFastjetAll"),
    electronSrc = cms.untracked.InputTag("slimmedElectrons"),
    electronUnSSrc = cms.untracked.InputTag("selectedElectrons"),
    fsrPhotonsSrc = cms.untracked.InputTag("boostedFsrPhotons"),
    genJetsSrc = cms.untracked.InputTag("slimmedGenJets"),
    generatorSrc = cms.untracked.InputTag("generator"),
    isCode4l = cms.untracked.bool(True),
    isHcc = cms.untracked.bool(True),
    isMC = cms.untracked.bool(True),
    isQCD = cms.untracked.bool(False),
    isSignal = cms.untracked.bool(True),
    isZbb = cms.untracked.bool(False),
    isZcc = cms.untracked.bool(True),
    isZqq = cms.untracked.bool(False),
    lheInfoSrc = cms.untracked.InputTag("externalLHEProducer"),
    mH = cms.untracked.double(125.0),
    metSrc = cms.untracked.InputTag("slimmedMETsPuppi"),
    muRhoSrc = cms.untracked.InputTag("fixedGridRhoFastjetAll"),
    muonSrc = cms.untracked.InputTag("slimmedMuons"),
    packedgenParticlesSrc = cms.untracked.InputTag("packedGenParticles"),
    payload = cms.string('AK4PFPuppi'),
    pfCandsSrc = cms.untracked.InputTag("packedPFCandidates"),
    photonSrc = cms.untracked.InputTag("slimmedPhotons"),
    pileupSrc = cms.untracked.InputTag("slimmedAddPileupInfo"),
    prunedgenParticlesSrc = cms.untracked.InputTag("prunedGenParticles"),
    reweightForPU = cms.untracked.bool(True),
    rhoSrcSUS = cms.untracked.InputTag("fixedGridRhoFastjetCentralNeutral"),
    skimLooseLeptons = cms.untracked.int32(0),
    skimTightLeptons = cms.untracked.int32(0),
    triggerList = cms.untracked.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v',
        'HLT_QuadPFJet100_88_70_30_v',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v',
        'HLT_QuadPFJet105_88_75_30_v',
        'HLT PFJet80_v',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v',
        'PFHT1050_v',
        'PFJet500_v',
        'AK8PFJet500_v',
        'AK8PFJet400_TrimMass30_v',
        'AK8PFJet420_TrimMass30_v',
        'AK8PFHT800_TrimMass50_v'
    ),
    triggerObjects = cms.InputTag("unpackedPatTrigger"),
    triggerSrc = cms.InputTag("TriggerResults","","HLT"),
    verbose = cms.untracked.bool(False),
    vertexSrc = cms.untracked.InputTag("offlineSlimmedPrimaryVertices"),
    weightEvents = cms.untracked.bool(True),
    year = cms.untracked.int32(2023)
)


process.printTree = cms.EDAnalyzer("ParticleListDrawer",
    maxEventsToPrint = cms.untracked.int32(1),
    printOnlyHardInteraction = cms.untracked.bool(False),
    printVertex = cms.untracked.bool(False),
    src = cms.InputTag("genParticles")
)


process.DQMStore = cms.Service("DQMStore",
    MEsToSave = cms.untracked.vstring(
        'Hcal/DigiTask/Occupancy/depth/depth1',
        'Hcal/DigiTask/Occupancy/depth/depth2',
        'Hcal/DigiTask/Occupancy/depth/depth3',
        'Hcal/DigiTask/Occupancy/depth/depth4',
        'Hcal/DigiTask/Occupancy/depth/depth5',
        'Hcal/DigiTask/Occupancy/depth/depth6',
        'Hcal/DigiTask/Occupancy/depth/depth7',
        'Hcal/DigiTask/Occupancy/depth/depthHO',
        'Hcal/DigiTask/OccupancyCut/depth/depth1',
        'Hcal/DigiTask/OccupancyCut/depth/depth2',
        'Hcal/DigiTask/OccupancyCut/depth/depth3',
        'Hcal/DigiTask/OccupancyCut/depth/depth4',
        'Hcal/DigiTask/OccupancyCut/depth/depth5',
        'Hcal/DigiTask/OccupancyCut/depth/depth6',
        'Hcal/DigiTask/OccupancyCut/depth/depth7',
        'Hcal/DigiTask/OccupancyCut/depth/depthHO',
        'EcalBarrel/EBOccupancyTask/EBOT digi occupancy',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +',
        'EcalBarrel/EBOccupancyTask/EBOT DCC entries',
        'EcalEndcap/EEOccupancyTask/EEOT DCC entries',
        'Ecal/EventInfo/processedEvents',
        'PixelPhase1/Tracks/charge_PXBarrel',
        'PixelPhase1/Tracks/charge_PXForward',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-3',
        'HLT/Vertexing/hltPixelVertices/hltPixelVertices/goodvtxNbr',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_pt',
        'HLT/Tracking/pixelTracks/GeneralProperties/Chi2Prob_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/Chi2oNDFVsEta_ImpactPoint_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DeltaZToPVZoom_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DistanceOfClosestApproachToPVVsPhi_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DistanceOfClosestApproachToPVZoom_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/NumberOfTracks_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/Chi2Prob_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/Chi2oNDFVsEta_ImpactPoint_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DeltaZToPVZoom_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DistanceOfClosestApproachToPVVsPhi_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DistanceOfClosestApproachToPVZoom_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/NumberOfTracks_GenTk',
        'HLT/Tracking/tracks/LUMIanalysis/NumberEventsVsLUMI',
        'HLT/Tracking/tracks/PUmonitoring/NumberEventsVsGoodPVtx',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXBarrel',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXForward',
        'PixelPhase1/Tracks/clusterposition_zphi_ontrack',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__9',
        'SiStrip/MechanicalView/TIB/layer_1/NormalizedHitResiduals_TIB__Layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/NormalizedHitResiduals_TIB__Layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/NormalizedHitResiduals_TIB__Layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/NormalizedHitResiduals_TIB__Layer__4',
        'SiStrip/MechanicalView/TIB/layer_1/Summary_ClusterStoNCorr__OnTrack__TIB__layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/Summary_ClusterStoNCorr__OnTrack__TIB__layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/Summary_ClusterStoNCorr__OnTrack__TIB__layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/Summary_ClusterStoNCorr__OnTrack__TIB__layer__4',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__3',
        'SiStrip/MechanicalView/TOB/layer_1/NormalizedHitResiduals_TOB__Layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/NormalizedHitResiduals_TOB__Layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/NormalizedHitResiduals_TOB__Layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/NormalizedHitResiduals_TOB__Layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/NormalizedHitResiduals_TOB__Layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/NormalizedHitResiduals_TOB__Layer__6',
        'SiStrip/MechanicalView/TOB/layer_1/Summary_ClusterStoNCorr__OnTrack__TOB__layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/Summary_ClusterStoNCorr__OnTrack__TOB__layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/Summary_ClusterStoNCorr__OnTrack__TOB__layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/Summary_ClusterStoNCorr__OnTrack__TOB__layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/Summary_ClusterStoNCorr__OnTrack__TOB__layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/Summary_ClusterStoNCorr__OnTrack__TOB__layer__6',
        'SiStrip/MechanicalView/MainDiagonal Position',
        'SiStrip/MechanicalView/NumberOfClustersInPixel',
        'SiStrip/MechanicalView/NumberOfClustersInStrip',
        'Tracking/TrackParameters/generalTracks/LSanalysis/Chi2oNDF_lumiFlag_GenTk',
        'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfRecHitsPerTrack_lumiFlag_GenTk',
        'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfTracks_lumiFlag_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDxyToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDzToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIP3DToPV_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberOfMissingOuterRecHitsPerTrack_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberMORecHitsPerTrackVsPt_GenTk',
        'OfflinePV/offlinePrimaryVertices/tagVtxProb',
        'OfflinePV/offlinePrimaryVertices/tagType',
        'OfflinePV/Resolution/PV/pull_x',
        'OfflinePV/Resolution/PV/pull_y',
        'OfflinePV/Resolution/PV/pull_z',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Constituents',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta_uncor',
        'JetMET/Jet/Cleanedak4PFJetsCHS/JetEnergyCorr',
        'JetMET/Jet/Cleanedak4PFJetsCHS/NJets',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Pt',
        'JetMET/MET/pfMETT1/Cleaned/METSig',
        'JetMET/vertices'
    ),
    assertLegacySafe = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(True),
    onlineMode = cms.untracked.bool(False),
    saveByLumi = cms.untracked.bool(False),
    trackME = cms.untracked.string(''),
    verbose = cms.untracked.int32(0)
)


process.MessageLogger = cms.Service("MessageLogger",
    cerr = cms.untracked.PSet(
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        enable = cms.untracked.bool(True),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.untracked.bool(False),
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.untracked.string('WARNING'),
        threshold = cms.untracked.string('INFO'),
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    cout = cms.untracked.PSet(
        enable = cms.untracked.bool(False),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.optional.untracked.bool,
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.optional.untracked.string,
        threshold = cms.optional.untracked.string,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    debugModules = cms.untracked.vstring(),
    default = cms.untracked.PSet(
        limit = cms.optional.untracked.int32,
        lineLength = cms.untracked.int32(80),
        noLineBreaks = cms.untracked.bool(False),
        noTimeStamps = cms.untracked.bool(False),
        reportEvery = cms.untracked.int32(1),
        statisticsThreshold = cms.untracked.string('INFO'),
        threshold = cms.untracked.string('INFO'),
        timespan = cms.optional.untracked.int32,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    files = cms.untracked.PSet(
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            enableStatistics = cms.untracked.bool(False),
            extension = cms.optional.untracked.string,
            filename = cms.optional.untracked.string,
            lineLength = cms.optional.untracked.int32,
            noLineBreaks = cms.optional.untracked.bool,
            noTimeStamps = cms.optional.untracked.bool,
            output = cms.optional.untracked.string,
            resetStatistics = cms.untracked.bool(False),
            statisticsThreshold = cms.optional.untracked.string,
            threshold = cms.optional.untracked.string,
            allowAnyLabel_=cms.optional.untracked.PSetTemplate(
                limit = cms.optional.untracked.int32,
                reportEvery = cms.untracked.int32(1),
                timespan = cms.optional.untracked.int32
            )
        )
    ),
    suppressDebug = cms.untracked.vstring(),
    suppressFwkInfo = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    allowAnyLabel_=cms.optional.untracked.PSetTemplate(
        limit = cms.optional.untracked.int32,
        reportEvery = cms.untracked.int32(1),
        timespan = cms.optional.untracked.int32
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    CTPPSFastRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1357987)
    ),
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    RPSiDetDigitizer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(137137)
    ),
    RPixDetDigitizer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(137137)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    fastSimProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    fastTrackerRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('out_MC_Summer23_JECs.root')
)


process.Timing = cms.Service("Timing",
    summaryOnly = cms.untracked.bool(True)
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL',
        'ZDC',
        'CASTOR',
        'EcalBarrel',
        'EcalEndcap',
        'EcalPreshower',
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService",
    maxExtrapolationTimeInSec = cms.uint32(0)
)


process.EcalLaserCorrectionServiceMC = cms.ESProducer("EcalLaserCorrectionServiceMC",
    appendToDataLabel = cms.string('')
)


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    fromDD4hep = cms.untracked.bool(False),
    fromDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    usePhase2Stacks = cms.bool(False)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.ctppsBeamParametersFromLHCInfoESSource = cms.ESProducer("CTPPSBeamParametersFromLHCInfoESSource",
    appendToDataLabel = cms.string(''),
    beamDivX45 = cms.double(0.1),
    beamDivX56 = cms.double(0.1),
    beamDivY45 = cms.double(0.1),
    beamDivY56 = cms.double(0.1),
    lhcInfoLabel = cms.string(''),
    vtxOffsetX45 = cms.double(0.01),
    vtxOffsetX56 = cms.double(0.01),
    vtxOffsetY45 = cms.double(0.01),
    vtxOffsetY56 = cms.double(0.01),
    vtxOffsetZ45 = cms.double(0.01),
    vtxOffsetZ56 = cms.double(0.01),
    vtxStddevX = cms.double(0.02),
    vtxStddevY = cms.double(0.02),
    vtxStddevZ = cms.double(0.02)
)


process.ctppsInterpolatedOpticalFunctionsESSource = cms.ESProducer("CTPPSInterpolatedOpticalFunctionsESSource",
    appendToDataLabel = cms.string(''),
    lhcInfoLabel = cms.string(''),
    opticsLabel = cms.string('')
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.multipleScatteringParametrisationMakerESProducer = cms.ESProducer("MultipleScatteringParametrisationMakerESProducer",
    appendToDataLabel = cms.string('')
)


process.muonGeometryConstants = cms.ESProducer("MuonGeometryConstantsESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    appendToDataLabel = cms.string(''),
    siPixelQualityLabel = cms.string(''),
    siPixelQualityLabel_RawToDigi = cms.string('')
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ),
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('130X_mcRun3_2023_realistic_v14'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ),
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ),
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(208),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(208),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.jec = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('sqlite_file:Summer23Prompt23_V1_MC.db'),
    toGet = cms.VPSet(cms.PSet(
        label = cms.untracked.string('AK4PFPuppi'),
        record = cms.string('JetCorrectionsRecord'),
        tag = cms.string('JetCorrectorParametersCollection_Summer23Prompt23_V1_MC_AK4PFPuppi')
    ))
)


process.jer = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('sqlite_file:Summer23Prompt23_RunCv1234_JRV1_MC.db'),
    toGet = cms.VPSet(
        cms.PSet(
            label = cms.untracked.string('AK4PFPuppi_pt'),
            record = cms.string('JetResolutionRcd'),
            tag = cms.string('JR_Summer23Prompt23_RunCv1234_JRV1_MC_PtResolution_AK4PFPuppi')
        ),
        cms.PSet(
            label = cms.untracked.string('AK4PFPuppi'),
            record = cms.string('JetResolutionScaleFactorRcd'),
            tag = cms.string('JR_Summer23Prompt23_RunCv1234_JRV1_MC_SF_AK4PFPuppi')
        )
    )
)


process.prefer("es_hardcode")

process.prefer("jec")

process.prefer("jer")

process.extractMET_task = cms.Task(process.genMetExtractor, process.metrawCalo, process.pfMet)


process.updateJECs_task = cms.Task(process.patJetCorrFactorsReapplyJEC, process.patJetsReapplyJEC)


process.jetCleaning_task = cms.Task(process.cleanedPatJets)


process.getJetCollectionForCorsAndUncs_task = cms.Task(process.basicJetsForMet, process.jetSelectorForMet)


process.miniAODConfigurationPre_task = cms.Task(process.extractMET_task, process.patCHSMet, process.patCaloMet, process.patTrkMet, process.pfCHS, process.pfMetCHS, process.pfMetTrk, process.pfTrk)


process.ak4CaloL1FastL2L3CorrectorTask = cms.Task(process.ak4CaloL1FastL2L3Corrector, process.ak4CaloL1FastjetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector)


process.ak4CaloL1FastL2L3L6CorrectorTask = cms.Task(process.ak4CaloL1FastL2L3L6Corrector, process.ak4CaloL1FastjetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloL6SLBCorrector)


process.ak4CaloL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4CaloL1FastL2L3ResidualCorrector, process.ak4CaloL1FastjetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloResidualCorrector)


process.ak4CaloL1L2L3CorrectorTask = cms.Task(process.ak4CaloL1L2L3Corrector, process.ak4CaloL1OffsetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector)


process.ak4CaloL1L2L3ResidualCorrectorTask = cms.Task(process.ak4CaloL1L2L3ResidualCorrector, process.ak4CaloL1OffsetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloResidualCorrector)


process.ak4CaloL2L3CorrectorTask = cms.Task(process.ak4CaloL2L3Corrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector)


process.ak4CaloL2L3L6CorrectorTask = cms.Task(process.ak4CaloL2L3L6Corrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloL6SLBCorrector)


process.ak4CaloL2L3ResidualCorrectorTask = cms.Task(process.ak4CaloL2L3ResidualCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloResidualCorrector)


process.ak4L1JPTFastjetCorrectorTask = cms.Task(process.ak4CaloL1FastjetCorrector, process.ak4L1JPTFastjetCorrector)


process.ak4L1JPTOffsetCorrectorTask = cms.Task(process.ak4CaloL1OffsetCorrector, process.ak4L1JPTOffsetCorrector)


process.ak4PFCHSL1FastL2L3CorrectorTask = cms.Task(process.ak4PFCHSL1FastL2L3Corrector, process.ak4PFCHSL1FastjetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector)


process.ak4PFCHSL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4PFCHSL1FastL2L3ResidualCorrector, process.ak4PFCHSL1FastjetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector, process.ak4PFCHSResidualCorrector)


process.ak4PFCHSL1L2L3CorrectorTask = cms.Task(process.ak4PFCHSL1L2L3Corrector, process.ak4PFCHSL1OffsetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector)


process.ak4PFCHSL1L2L3ResidualCorrectorTask = cms.Task(process.ak4PFCHSL1L2L3ResidualCorrector, process.ak4PFCHSL1OffsetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector, process.ak4PFCHSResidualCorrector)


process.ak4PFCHSL2L3CorrectorTask = cms.Task(process.ak4PFCHSL2L3Corrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector)


process.ak4PFCHSL2L3ResidualCorrectorTask = cms.Task(process.ak4PFCHSL2L3ResidualCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector, process.ak4PFCHSResidualCorrector)


process.ak4PFL1FastL2L3CorrectorTask = cms.Task(process.ak4PFL1FastL2L3Corrector, process.ak4PFL1FastjetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector)


process.ak4PFL1FastL2L3L6CorrectorTask = cms.Task(process.ak4PFL1FastL2L3L6Corrector, process.ak4PFL1FastjetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFL6SLBCorrector)


process.ak4PFL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4PFL1FastL2L3ResidualCorrector, process.ak4PFL1FastjetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFResidualCorrector)


process.ak4PFL1L2L3CorrectorTask = cms.Task(process.ak4PFL1L2L3Corrector, process.ak4PFL1OffsetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector)


process.ak4PFL1L2L3ResidualCorrectorTask = cms.Task(process.ak4PFL1L2L3ResidualCorrector, process.ak4PFL1OffsetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFResidualCorrector)


process.ak4PFL2L3CorrectorTask = cms.Task(process.ak4PFL2L3Corrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector)


process.ak4PFL2L3L6CorrectorTask = cms.Task(process.ak4PFL2L3L6Corrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFL6SLBCorrector)


process.ak4PFL2L3ResidualCorrectorTask = cms.Task(process.ak4PFL2L3ResidualCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFResidualCorrector)


process.ak4PFPuppiL1FastL2L3CorrectorTask = cms.Task(process.ak4PFPuppiL1FastL2L3Corrector, process.ak4PFPuppiL1FastjetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector)


process.ak4PFPuppiL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4PFPuppiL1FastL2L3ResidualCorrector, process.ak4PFPuppiL1FastjetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector, process.ak4PFPuppiResidualCorrector)


process.ak4PFPuppiL1L2L3CorrectorTask = cms.Task(process.ak4PFPuppiL1L2L3Corrector, process.ak4PFPuppiL1OffsetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector)


process.ak4PFPuppiL1L2L3ResidualCorrectorTask = cms.Task(process.ak4PFPuppiL1L2L3ResidualCorrector, process.ak4PFPuppiL1OffsetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector, process.ak4PFPuppiResidualCorrector)


process.ak4PFPuppiL2L3CorrectorTask = cms.Task(process.ak4PFPuppiL2L3Corrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector)


process.ak4PFPuppiL2L3ResidualCorrectorTask = cms.Task(process.ak4PFPuppiL2L3ResidualCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector, process.ak4PFPuppiResidualCorrector)


process.ak4TrackL2L3CorrectorTask = cms.Task(process.ak4TrackL2L3Corrector, process.ak4TrackL2RelativeCorrector, process.ak4TrackL3AbsoluteCorrector)


process.correctionTermsPfMetType1Type2Task = cms.Task(process.ak4PFCHSL1FastL2L3CorrectorTask, process.ak4PFCHSL1FastL2L3ResidualCorrectorTask, process.corrPfMetType1, process.corrPfMetType2, process.particleFlowPtrs, process.pfCandMETcorr, process.pfCandsNotInJetsForMetCorr, process.pfCandsNotInJetsPtrForMetCorr, process.pfJetsPtrForMetCorr)


process.patPFMetSmearCorrTask = cms.Task(process.patPFMetT1T2SmearCorr, process.patSmearedJets, process.selectedPatJetsForMetT1T2SmearCorr)


process.patPFMetT1T2CorrTask = cms.Task(process.patPFMetT1T2Corr, process.selectedPatJetsForMetT1T2Corr)


process.patPFMetT2CorrTask = cms.Task(process.patPFMetT2Corr)


process.patPFMetT2SmearCorrTask = cms.Task(process.patPFMetT1T2SmearCorr, process.patPFMetT2SmearCorr, process.patSmearedJets, process.selectedPatJetsForMetT1T2SmearCorr, process.selectedPatJetsForMetT2SmearCorr)


process.patPFMetTxyCorrTask = cms.Task(process.patPFMetTxyCorr)


process.type0PFMEtCorrectionPFCandToVertexAssociationTask = cms.Task(process.particleFlowDisplacedVertex, process.pfCandidateToVertexAssociation, process.selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0, process.selectedVerticesForPFMEtCorrType0)


process.type0PFMEtCorrectionTask = cms.Task(process.pfMETcorrType0, process.type0PFMEtCorrectionPFCandToVertexAssociationTask)


process.miniAODConfiguration_task = cms.Task(process.slimmedMETs)


process.getCorrectedMET_task = cms.Task(process.patPFMetSmearCorrTask, process.patPFMetT1, process.patPFMetT1Smear, process.patPFMetT1T2CorrTask, process.patPFMetT1Txy, process.patPFMetTxy, process.patPFMetTxyCorrTask)


process.createShiftedModules_task = cms.Task(process.shiftedPatElectronEnDown, process.shiftedPatElectronEnUp, process.shiftedPatJetEnDown, process.shiftedPatJetEnUp, process.shiftedPatJetResDown, process.shiftedPatJetResUp, process.shiftedPatMETCorrElectronEnDown, process.shiftedPatMETCorrElectronEnUp, process.shiftedPatMETCorrJetEnDown, process.shiftedPatMETCorrJetEnUp, process.shiftedPatMETCorrJetResDown, process.shiftedPatMETCorrJetResUp, process.shiftedPatMETCorrMuonEnDown, process.shiftedPatMETCorrMuonEnUp, process.shiftedPatMETCorrPhotonEnDown, process.shiftedPatMETCorrPhotonEnUp, process.shiftedPatMETCorrSmearedJetResDown, process.shiftedPatMETCorrSmearedJetResUp, process.shiftedPatMETCorrTauEnDown, process.shiftedPatMETCorrTauEnUp, process.shiftedPatMETCorrUnclusteredEnDown, process.shiftedPatMETCorrUnclusteredEnUp, process.shiftedPatMuonEnDown, process.shiftedPatMuonEnUp, process.shiftedPatPhotonEnDown, process.shiftedPatPhotonEnUp, process.shiftedPatSmearedJetResDown, process.shiftedPatSmearedJetResUp, process.shiftedPatTauEnDown, process.shiftedPatTauEnUp, process.shiftedPatUnclusteredEnDown, process.shiftedPatUnclusteredEnUp)


process.getMETUncertainties_task = cms.Task(process.patPFMetT1ElectronEnDown, process.patPFMetT1ElectronEnUp, process.patPFMetT1JetEnDown, process.patPFMetT1JetEnUp, process.patPFMetT1JetResDown, process.patPFMetT1JetResUp, process.patPFMetT1MuonEnDown, process.patPFMetT1MuonEnUp, process.patPFMetT1PhotonEnDown, process.patPFMetT1PhotonEnUp, process.patPFMetT1SmearElectronEnDown, process.patPFMetT1SmearElectronEnUp, process.patPFMetT1SmearJetEnDown, process.patPFMetT1SmearJetEnUp, process.patPFMetT1SmearJetResDown, process.patPFMetT1SmearJetResUp, process.patPFMetT1SmearMuonEnDown, process.patPFMetT1SmearMuonEnUp, process.patPFMetT1SmearPhotonEnDown, process.patPFMetT1SmearPhotonEnUp, process.patPFMetT1SmearTauEnDown, process.patPFMetT1SmearTauEnUp, process.patPFMetT1SmearUnclusteredEnDown, process.patPFMetT1SmearUnclusteredEnUp, process.patPFMetT1TauEnDown, process.patPFMetT1TauEnUp, process.patPFMetT1UnclusteredEnDown, process.patPFMetT1UnclusteredEnUp, process.pfCandsForUnclusteredUnc, process.pfCandsNoJets, process.pfCandsNoJetsNoEle, process.pfCandsNoJetsNoEleNoMu, process.pfCandsNoJetsNoEleNoMuNoTau, process.pfElectrons, process.pfMuons, process.pfNoPileUp, process.pfPhotons, process.pfTaus)


process.patMetCorrectionTask = cms.Task(process.getCorrectedMET_task)


process.patMetUncertaintyTask = cms.Task(process.ak4PFCHSL1FastL2L3CorrectorTask, process.ak4PFCHSL1FastL2L3ResidualCorrectorTask, process.createShiftedModules_task, process.getMETUncertainties_task)


process.patShiftedModuleTask = cms.Task()


process.ak4JPTL1FastL2L3CorrectorTask = cms.Task(process.ak4JPTL1FastL2L3Corrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4L1JPTFastjetCorrectorTask)


process.ak4JPTL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4JPTL1FastL2L3ResidualCorrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4JPTResidualCorrector, process.ak4L1JPTFastjetCorrectorTask)


process.ak4JPTL1L2L3CorrectorTask = cms.Task(process.ak4JPTL1L2L3Corrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.ak4JPTL1L2L3ResidualCorrectorTask = cms.Task(process.ak4JPTL1L2L3ResidualCorrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4JPTResidualCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.ak4JPTL2L3CorrectorTask = cms.Task(process.ak4JPTL2L3Corrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.ak4JPTL2L3ResidualCorrectorTask = cms.Task(process.ak4JPTL2L3ResidualCorrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4JPTResidualCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.jetCorrectorsTask = cms.Task(process.ak4CaloL1FastL2L3CorrectorTask, process.ak4CaloL1FastL2L3L6CorrectorTask, process.ak4CaloL1FastL2L3ResidualCorrectorTask, process.ak4CaloL1L2L3CorrectorTask, process.ak4CaloL1L2L3ResidualCorrectorTask, process.ak4CaloL2L3CorrectorTask, process.ak4CaloL2L3L6CorrectorTask, process.ak4CaloL2L3ResidualCorrectorTask, process.ak4JPTL1FastL2L3CorrectorTask, process.ak4JPTL1FastL2L3ResidualCorrectorTask, process.ak4JPTL1L2L3CorrectorTask, process.ak4JPTL1L2L3ResidualCorrectorTask, process.ak4JPTL2L3CorrectorTask, process.ak4JPTL2L3ResidualCorrectorTask, process.ak4L1JPTFastjetCorrectorTask, process.ak4L1JPTOffsetCorrectorTask, process.ak4PFCHSL1FastL2L3CorrectorTask, process.ak4PFCHSL1FastL2L3ResidualCorrectorTask, process.ak4PFCHSL1L2L3CorrectorTask, process.ak4PFCHSL1L2L3ResidualCorrectorTask, process.ak4PFCHSL2L3CorrectorTask, process.ak4PFCHSL2L3ResidualCorrectorTask, process.ak4PFL1FastL2L3CorrectorTask, process.ak4PFL1FastL2L3L6CorrectorTask, process.ak4PFL1FastL2L3ResidualCorrectorTask, process.ak4PFL1L2L3CorrectorTask, process.ak4PFL1L2L3ResidualCorrectorTask, process.ak4PFL2L3CorrectorTask, process.ak4PFL2L3L6CorrectorTask, process.ak4PFL2L3ResidualCorrectorTask, process.ak4PFPuppiL1FastL2L3CorrectorTask, process.ak4PFPuppiL1FastL2L3ResidualCorrectorTask, process.ak4PFPuppiL1L2L3CorrectorTask, process.ak4PFPuppiL1L2L3ResidualCorrectorTask, process.ak4PFPuppiL2L3CorrectorTask, process.ak4PFPuppiL2L3ResidualCorrectorTask, process.ak4TrackL2L3CorrectorTask)


process.patPFMetT0CorrTask = cms.Task(process.patPFMetT0Corr, process.type0PFMEtCorrectionPFCandToVertexAssociationTask)


process.producePatPFMETCorrectionsTask = cms.Task(process.patPFMet, process.patPFMetT0Corr, process.patPFMetT0pcT1, process.patPFMetT0pcT1T2, process.patPFMetT1, process.patPFMetT1T2, process.patPFMetT1T2Corr, process.patPFMetT2Corr, process.pfCandMETcorr, process.pfCandsNotInJetsForMetCorr, process.selectedPatJetsForMetT1T2Corr, process.selectedPatJetsForMetT2Corr, process.type0PFMEtCorrectionPFCandToVertexAssociationTask)


process.producePatPFMETCorrectionsUncTask = cms.Task(process.patPFMet, process.patPFMetT0Corr, process.patPFMetT1T2Corr, process.patPFMetT2Corr, process.pfCandMETcorr, process.pfCandsNotInJetsForMetCorr, process.selectedPatJetsForMetT1T2Corr, process.selectedPatJetsForMetT2Corr, process.type0PFMEtCorrectionPFCandToVertexAssociationTask)


process.produceMET_task = cms.Task(process.jetCorrectorsTask, process.patPFMet, process.patPFMetT2SmearCorrTask, process.patPFMetTxyCorrTask, process.producePatPFMETCorrectionsTask)


process.patMetModuleTask = cms.Task(process.extractMET_task, process.getJetCollectionForCorsAndUncs_task, process.jetCleaning_task, process.miniAODConfigurationPre_task, process.miniAODConfiguration_task, process.produceMET_task, process.updateJECs_task)


process.fullPatMetTask = cms.Task(process.patCaloMet, process.patMetCorrectionTask, process.patMetModuleTask, process.patMetUncertaintyTask, process.patShiftedModuleTask, process.slimmedMETs)


process.patAlgosToolsTask = cms.Task(process.ak4PFCHSL1FastL2L3CorrectorTask, process.ak4PFCHSL1FastL2L3ResidualCorrectorTask, process.basicJetsForMet, process.cleanedPatJets, process.createShiftedModules_task, process.fullPatMetTask, process.genMetExtractor, process.jetSelectorForMet, process.metrawCalo, process.miniAODConfiguration_task, process.patCHSMet, process.patCaloMet, process.patJetCorrFactorsReapplyJEC, process.patJetCorrFactorsUpdatedJEC, process.patJetsReapplyJEC, process.patMetCorrectionTask, process.patPFMetT1ElectronEnDown, process.patPFMetT1ElectronEnUp, process.patPFMetT1JetEnDown, process.patPFMetT1JetEnUp, process.patPFMetT1JetResDown, process.patPFMetT1JetResUp, process.patPFMetT1MuonEnDown, process.patPFMetT1MuonEnUp, process.patPFMetT1PhotonEnDown, process.patPFMetT1PhotonEnUp, process.patPFMetT1TauEnDown, process.patPFMetT1TauEnUp, process.patPFMetT1UnclusteredEnDown, process.patPFMetT1UnclusteredEnUp, process.patShiftedModuleTask, process.patTrkMet, process.pfCHS, process.pfCandsForUnclusteredUnc, process.pfCandsNoJets, process.pfCandsNoJetsNoEle, process.pfCandsNoJetsNoEleNoMu, process.pfCandsNoJetsNoEleNoMuNoTau, process.pfElectrons, process.pfMet, process.pfMetCHS, process.pfMetTrk, process.pfMuons, process.pfNoPileUp, process.pfPhotons, process.pfTaus, process.pfTrk, process.produceMET_task, process.selectedUpdatedPatJetsPileupJetID, process.selectedUpdatedPatJetsQGT, process.selectedUpdatedPatJetsUpdatedJEC, process.slimmedMETs, process.updatedPatJetsPileupJetID, process.updatedPatJetsQGT, process.updatedPatJetsUpdatedJEC)


process.jecSequence = cms.Sequence(process.patJetCorrFactorsUpdatedJEC+process.updatedPatJetsUpdatedJEC)


process.jerSequence = cms.Sequence(process.slimmedJetsSmeared)


process.ak4CaloL1FastL2L3CorrectorChain = cms.Sequence(process.ak4CaloL1FastL2L3CorrectorTask)


process.ak4CaloL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak4CaloL1FastL2L3L6CorrectorTask)


process.ak4CaloL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL1FastL2L3ResidualCorrectorTask)


process.ak4CaloL1L2L3CorrectorChain = cms.Sequence(process.ak4CaloL1L2L3CorrectorTask)


process.ak4CaloL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL1L2L3ResidualCorrectorTask)


process.ak4CaloL2L3CorrectorChain = cms.Sequence(process.ak4CaloL2L3CorrectorTask)


process.ak4CaloL2L3L6CorrectorChain = cms.Sequence(process.ak4CaloL2L3L6CorrectorTask)


process.ak4CaloL2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL2L3ResidualCorrectorTask)


process.ak4JPTL1FastL2L3CorrectorChain = cms.Sequence(process.ak4JPTL1FastL2L3CorrectorTask)


process.ak4JPTL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL1FastL2L3ResidualCorrectorTask)


process.ak4JPTL1L2L3CorrectorChain = cms.Sequence(process.ak4JPTL1L2L3CorrectorTask)


process.ak4JPTL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL1L2L3ResidualCorrectorTask)


process.ak4JPTL2L3CorrectorChain = cms.Sequence(process.ak4JPTL2L3CorrectorTask)


process.ak4JPTL2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL2L3ResidualCorrectorTask)


process.ak4L1JPTFastjetCorrectorChain = cms.Sequence(process.ak4L1JPTFastjetCorrectorTask)


process.ak4L1JPTOffsetCorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorTask)


process.ak4PFCHSL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL1FastL2L3CorrectorTask)


process.ak4PFCHSL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL1FastL2L3ResidualCorrectorTask)


process.ak4PFCHSL1L2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL1L2L3CorrectorTask)


process.ak4PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL1L2L3ResidualCorrectorTask)


process.ak4PFCHSL2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL2L3CorrectorTask)


process.ak4PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL2L3ResidualCorrectorTask)


process.ak4PFL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFL1FastL2L3CorrectorTask)


process.ak4PFL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak4PFL1FastL2L3L6CorrectorTask)


process.ak4PFL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL1FastL2L3ResidualCorrectorTask)


process.ak4PFL1L2L3CorrectorChain = cms.Sequence(process.ak4PFL1L2L3CorrectorTask)


process.ak4PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL1L2L3ResidualCorrectorTask)


process.ak4PFL2L3CorrectorChain = cms.Sequence(process.ak4PFL2L3CorrectorTask)


process.ak4PFL2L3L6CorrectorChain = cms.Sequence(process.ak4PFL2L3L6CorrectorTask)


process.ak4PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL2L3ResidualCorrectorTask)


process.ak4PFPuppiL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL1FastL2L3CorrectorTask)


process.ak4PFPuppiL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL1FastL2L3ResidualCorrectorTask)


process.ak4PFPuppiL1L2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL1L2L3CorrectorTask)


process.ak4PFPuppiL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL1L2L3ResidualCorrectorTask)


process.ak4PFPuppiL2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL2L3CorrectorTask)


process.ak4PFPuppiL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL2L3ResidualCorrectorTask)


process.ak4TrackL2L3CorrectorChain = cms.Sequence(process.ak4TrackL2L3CorrectorTask)


process.correctionTermsPfMetType1Type2 = cms.Sequence(process.correctionTermsPfMetType1Type2Task)


process.type0PFMEtCorrection = cms.Sequence(process.type0PFMEtCorrectionTask)


process.type0PFMEtCorrectionPFCandToVertexAssociation = cms.Sequence(process.type0PFMEtCorrectionPFCandToVertexAssociationTask)


process.type0PFMEtCorrectionPFCandToVertexAssociationForValidation = cms.Sequence(process.type0PFMEtCorrectionPFCandToVertexAssociationTask)


process.type0PFMEtCorrectionPFCandToVertexAssociationForValidationMiniAOD = cms.Sequence(process.type0PFMEtCorrectionPFCandToVertexAssociationTask)


process.p = cms.Path(process.jecSequence+process.jerSequence+process.slimmedJetsSmearedDown+process.slimmedJetsSmearedUp+process.QGTagger+process.updatedPatJetsQGT+process.unpackedPatTrigger+process.Ana)


