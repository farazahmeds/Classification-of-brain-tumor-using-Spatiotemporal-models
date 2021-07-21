import torchio


def brats():
    p1 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_2_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p2 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_3_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p3 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_4_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p4 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_5_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p5 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_7_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p6 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_10_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p7 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_11_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p8 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_12_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p9 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_13_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p10 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_14_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p11 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_17_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p12 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_18_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p13 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_19_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p14 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_20_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p15 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_21_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p16 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_22_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p17 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_23_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p18 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_25_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p19 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_26_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p20 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_2013_27_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p21 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AAB_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p22 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AAG_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p23 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AAL_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p24 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AAP_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p25 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ABB_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p26 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ABE_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p27 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ABM_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p28 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ABN_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p29 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ABO_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p30 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ABY_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p31 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ALN_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p32 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ALU_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p33 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ALX_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p34 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AME_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p35 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AMH_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p36 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ANG_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p37 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ANI_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p38 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ANP_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',

    )
    p39 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ANV_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p40 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ANZ_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p41 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AOC_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p42 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AOD_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p43 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AOH_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p44 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AOO_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p45 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AOP_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p46 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AOS_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p47 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AOZ_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p49 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_APK_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p50 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_APR_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p51 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_APY_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p52 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_APY_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p53 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_APZ_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p54 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AQA_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p55 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AQD_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p56 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AQG_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p57 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AQJ_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p58 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AQN_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p59 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AQO_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p60 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AQP_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p61 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AQQ_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p62 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AQR_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p63 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AQT_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p64 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AQU_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p65 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AQV_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p66 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AQY_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p67 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_AQZ_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p68 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ARF_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p69 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ARW_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p70 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ARZ_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p71 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ASA_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p72 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ASE_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p73 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ASF_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p74 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ASG_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p75 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ASH_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )
    p76 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/HGG/BraTS19_CBICA_ASK_1_t1ce.nii.gz', mylabel=1),

        diagnosis='I',
    )

    p77 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_2013_0_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p78 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_2013_1_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p79 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_2013_6_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p80 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_2013_8_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p81 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_2013_9_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p82 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI315-IOP-0888-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',
    )

    p83 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_2013_16_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p84 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_2013_24_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p85 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_2013_28_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p86 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_2013_29_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p87 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA09_141_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p88 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA09_177_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p89 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA09_254_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )

    p90 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA09_255_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )

    p91 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA09_312_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )

    p92 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA09_451_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p93 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA09_462_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )

    p94 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA09_493_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p95 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA09_620_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p96 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_103_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p97 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_109_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p98 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_130_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p99 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_152_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p100 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_175_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p101 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_202_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p102 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_241_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p103 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_261_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p104 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_266_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p105 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_276_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p106 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_282_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p107 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_299_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p108 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_307_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p109 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_310_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p110 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_325_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p111 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_330_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p112 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_346_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p113 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_351_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )

    p114 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_310_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p115 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_387_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p116 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_393_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p117 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_408_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p118 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_410_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p119 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_413_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )

    p120 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_420_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p121 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_442_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p122 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_449_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p123 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_490_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p124 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_625_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p125 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_628_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p126 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_629_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p127 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_632_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p128 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_637_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p129 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_639_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p130 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_640_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p131 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA10_644_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    ##################################3

    p132 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA12_101_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )

    p133 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA12_249_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p134 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA12_298_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p135 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA12_466_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p136 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA12_470_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p137 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA12_480_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p138 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA13_615_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p139 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA13_618_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p140 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA13_621_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p141 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA13_623_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p142 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA13_624_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p143 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA13_630_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p144 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA13_633_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p145 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA13_634_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p146 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA13_642_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p147 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA13_645_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p148 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA13_650_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p149 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA13_653_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p150 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TCIA13_654_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',
    )
    p151 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/LGG/BraTS19_TMC_09043_1_t1ce.nii.gz', mylabel=0),

        diagnosis='I',

    )

    p152 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_ASR_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p153 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_ASU_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p154 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_ASV_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p155 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_ASW_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p156 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_ASY_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p157 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_ATB_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p158 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_ATD_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p159 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_ATF_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p160 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_ATN_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p161 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_ATP_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p162 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_ATV_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p163 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_ATX_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p164 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AUA_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p165 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AUN_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p166 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AUQ_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p167 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AUR_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p168 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AUW_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p169 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AUX_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p170 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AVB_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p171 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AVF_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p172 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AVG_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p173 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AVJ_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p174 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AVT_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p175 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AVV_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p176 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AWG_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p177 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AWH_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p178 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AWI_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p179 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AWV_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p180 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AWX_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p181 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AXJ_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p182 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AXL_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p183 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AXM_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p184 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AXN_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p185 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AXO_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p186 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AXQ_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p187 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AXW_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p188 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AYA_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p189 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AYC_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p190 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AYG_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p191 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AYI_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p192 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AYU_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p193 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AYW_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p194 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AZD_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p195 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_AZH_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p196 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BAN_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p197 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BAP_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p198 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BAX_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p199 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BBG_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p200 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BCF_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p201 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BCL_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p202 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BDK_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p203 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BEM_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p204 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BFB_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p205 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BFP_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p206 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BGE_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p207 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BGG_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p208 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BGN_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p209 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BGO_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p210 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BGR_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p211 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BGT_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p212 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BGW_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p213 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BGX_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p214 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BHB_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p215 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BHK_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p216 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BHM_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p217 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BHQ_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p218 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BHV_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p219 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BHZ_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p220 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BIC_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p221 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BJY_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p222 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BKV_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p223 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BLJ_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p224 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_CBICA_BNR_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p225 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_131_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p226 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_147_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p227 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_150_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p228 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_180_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p229 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_186_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p230 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_190_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p231 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_201_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p232 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_203_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p233 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_221_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p234 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_231_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p235 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_235_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p236 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_335_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p237 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_378_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p238 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_390_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p239 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_401_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p240 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_411_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p241 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_412_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p242 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_425_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p243 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_429_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p244 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_448_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p245 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_460_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p246 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA01_499_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p247 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_117_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p248 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_118_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p249 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_135_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p250 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_151_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p251 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_168_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p252 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_171_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p253 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_179_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    p254 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_198_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p255 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_208_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p256 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_222_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p257 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_226_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p258 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_274_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p259 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_283_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p260 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_290_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p261 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_300_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p262 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_309_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p263 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_314_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p264 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_321_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p265 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_322_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p266 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_331_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p267 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_368_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p268 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_370_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p269 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_374_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p270 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_377_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p271 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_394_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p272 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_430_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p273 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_455_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p274 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_471_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p275 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_473_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p276 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_491_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p277 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_605_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p278 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_606_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p279 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA02_608_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p280 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA03_121_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p281 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA03_133_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p282 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA03_138_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p283 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA03_199_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p284 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA03_257_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p285 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA03_265_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p286 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA03_296_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p287 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA03_338_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p288 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA03_375_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p289 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA03_419_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p290 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA03_474_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p291 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA03_498_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p292 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA04_111_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p293 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA04_149_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p294 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA04_192_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p295 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA04_328_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p296 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA04_343_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p297 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA04_361_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p298 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA04_437_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p299 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA04_479_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p300 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA05_277_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p301 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA05_396_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p302 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA05_444_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p303 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA05_478_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p304 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA06_165_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p305 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA06_184_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p306 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA06_211_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p307 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA06_247_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p308 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA06_332_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p309 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA06_372_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p310 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA06_409_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p311 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA06_603_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p312 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA08_105_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p313 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA08_113_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p314 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA08_162_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p315 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA08_167_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p316 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA08_205_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p317 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA08_218_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p318 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA08_234_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p319 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA08_242_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p320 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA08_278_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p321 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA08_280_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p322 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA08_319_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p323 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA08_406_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p324 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA08_436_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p325 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TCIA08_469_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p326 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TMC_06290_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p327 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TMC_06643_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p328 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TMC_11964_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p329 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TMC_12866_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p330 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TMC_15477_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p331 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TMC_21360_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p332 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TMC_27374_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )
    p333 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/remainingHGG/BraTS19_TMC_30014_1_t1ce.nii.gz',
                               mylabel=1),

        diagnosis='I',

    )

    ######################ixi

    p334 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI012-HH-1211-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p335 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI013-HH-1212-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p336 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI014-HH-1236-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p337 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI015-HH-1258-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p338 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI016-Guys-0697-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p339 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI017-Guys-0698-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p340 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI019-Guys-0702-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p341 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI020-Guys-0700-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p342 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI022-Guys-0701-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p343 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI021-Guys-0703-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p344 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI023-Guys-0699-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p345 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI024-Guys-0705-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p346 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI025-Guys-0852-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p347 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI026-Guys-0696-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p348 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI027-Guys-0710-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p349 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI028-Guys-1038-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p350 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI029-Guys-0829-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p351 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI030-Guys-0708-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p352 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI031-Guys-0797-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p353 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI033-HH-1259-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p354 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI034-HH-1260-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p355 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI035-IOP-0873-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p356 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI036-Guys-0736-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p357 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI037-Guys-0704-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p358 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI038-Guys-0729-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p359 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI039-HH-1261-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p360 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI040-Guys-0724-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p361 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI041-Guys-0706-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p362 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI042-Guys-0725-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p363 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI043-Guys-0714-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p364 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI044-Guys-0712-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p365 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI045-Guys-0713-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p366 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI046-Guys-0824-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p367 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI048-HH-1326-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p368 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI049-HH-1358-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p369 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI050-Guys-0711-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p370 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI051-HH-1328-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p371 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI052-HH-1343-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p372 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI053-Guys-0727-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p373 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI054-Guys-0707-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p374 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI055-Guys-0730-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p375 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI056-HH-1327-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p376 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI057-HH-1342-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p377 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI058-Guys-0726-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p378 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI059-HH-1284-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p379 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI060-Guys-0709-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p380 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI061-Guys-0715-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p381 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI062-Guys-0740-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p382 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI063-Guys-0742-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p383 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI064-Guys-0743-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p384 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI065-Guys-0744-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p385 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI066-Guys-0731-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p386 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI067-HH-1356-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p387 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI068-Guys-0756-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p388 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI069-Guys-0769-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p389 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI070-Guys-0767-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p390 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI071-Guys-0770-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p391 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI072-HH-2324-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p392 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI073-Guys-0755-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p393 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI074-Guys-0771-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p394 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI075-Guys-0754-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p395 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI077-Guys-0752-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p396 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI078-Guys-0751-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p397 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI079-HH-1388-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p398 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI080-HH-1341-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p399 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI083-HH-1357-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p400 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI084-Guys-0741-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p401 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI086-Guys-0728-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p402 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI087-Guys-0768-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p403 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI088-Guys-0758-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p404 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI089-Guys-0757-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p405 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI090-Guys-0800-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p406 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI607-Guys-1097-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p407 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI608-HH-2599-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p408 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI609-HH-2600-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p409 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI610-HH-2649-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p410 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI092-HH-1436-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p411 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI093-HH-1359-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p412 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI094-HH-1355-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p413 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI095-HH-1390-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p414 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI096-HH-1391-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p415 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI097-HH-1619-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p416 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI102-HH-1416-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p417 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI104-HH-1450-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    ############################################3
    p418 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI105-HH-1471-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p419 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI126-HH-1437-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p420 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI127-HH-1451-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p421 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI128-HH-1470-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p422 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI130-HH-1528-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    #############

    p423 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI131-HH-1527-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p424 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI132-HH-1415-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p425 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI136-HH-1452-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p426 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI137-HH-1472-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p427 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI146-HH-1389-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p428 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI148-HH-1453-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p429 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI150-HH-1550-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p430 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI159-HH-1549-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p431 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI160-HH-1637-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p432 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI161-HH-2533-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p433 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI162-HH-1548-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p434 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI163-HH-1621-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p435 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI165-HH-1589-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p436 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI167-HH-1569-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p437 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI168-HH-1607-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p438 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI173-HH-1590-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p439 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI174-HH-1571-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p440 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI175-HH-1570-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p441 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI176-HH-1604-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p442 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI180-HH-1605-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p443 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI195-HH-1620-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p444 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI201-HH-1588-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p445 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI202-HH-1526-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p446 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI204-HH-1651-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p447 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI205-HH-1649-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p448 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI206-HH-1650-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p449 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI211-HH-1568-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p450 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI212-HH-1643-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p451 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI213-HH-1642-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p452 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI214-HH-1636-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    #############

    p453 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI216-HH-1635-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p454 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI217-HH-1638-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p455 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI218-HH-1815-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p456 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI221-HH-1606-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p457 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI226-HH-1618-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p458 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI230-IOP-0869-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p459 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI231-IOP-0866-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p460 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI232-IOP-0898-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p461 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI233-IOP-0875-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p462 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI234-IOP-0870-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    #############

    p463 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI238-IOP-0883-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p464 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI239-HH-2296-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p465 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI242-HH-1722-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p466 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI248-HH-1972-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p467 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI252-HH-1693-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    #############

    p468 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI253-HH-1694-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p469 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI254-HH-1705-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p470 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI255-HH-1882-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p471 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI256-HH-1723-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p472 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI257-HH-1724-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p473 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI258-HH-1769-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p474 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI259-HH-1804-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p475 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI260-HH-1805-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p476 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI261-HH-1704-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p477 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI262-HH-1861-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    #############

    p478 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI263-HH-1684-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p479 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI267-HH-1772-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p480 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI274-HH-2294-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p481 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI275-HH-1803-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p482 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI276-HH-1840-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p483 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI277-HH-1770-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p484 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI278-HH-1771-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p485 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI280-HH-1860-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p486 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI282-HH-2025-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p487 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI284-HH-2354-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p488 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI290-IOP-0874-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p489 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI291-IOP-0882-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p490 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI292-IOP-0877-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p491 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI293-IOP-0876-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p492 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI294-IOP-0868-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p493 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI295-HH-1814-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p494 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI296-HH-1970-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p495 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI302-HH-1883-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p496 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI303-IOP-0968-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p497 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI305-IOP-0871-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p498 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI306-IOP-0867-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p499 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI307-IOP-0872-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p500 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI309-IOP-0897-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p501 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI310-IOP-0890-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p502 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI313-HH-2241-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p503 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI314-IOP-0889-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p504 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI315-IOP-0888-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )



    #############

    p504 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI328-HH-2295-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p505 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI329-HH-1908-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p506 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI331-IOP-0892-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p507 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI332-IOP-1134-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p508 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI333-IOP-0926-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p509 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI334-HH-1907-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p510 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI337-IOP-0929-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p511 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI340-IOP-0915-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p512 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI345-IOP-0928-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p513 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI347-IOP-0927-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    #############

    p514 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI371-IOP-0970-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p515 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI372-IOP-0971-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p516 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI373-IOP-0967-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p517 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI378-IOP-0972-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p518 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI382-IOP-1135-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    #############

    p519 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI388-IOP-0973-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p520 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI395-IOP-0969-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p521 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI423-IOP-0974-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p522 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI424-IOP-0991-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p523 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI425-IOP-0988-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p524 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI426-IOP-1011-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p525 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI427-IOP-1012-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p526 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI430-IOP-0990-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p527 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI433-IOP-0989-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p528 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI434-IOP-1010-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p529 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI435-IOP-1040-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p530 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI442-IOP-1041-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p531 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI462-IOP-1042-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p532 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI463-IOP-1043-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p533 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI464-IOP-1029-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p534 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI469-IOP-1136-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p535 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI470-IOP-1030-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p536 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI473-IOP-1137-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p537 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI474-IOP-1138-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p538 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI475-IOP-1139-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p539 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI476-IOP-1140-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p540 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI477-IOP-1141-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p541 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI478-IOP-1142-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p542 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI510-IOP-1143-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p543 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI517-IOP-1144-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    #############

    p544 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI531-Guys-1057-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p545 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI533-Guys-1066-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p546 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI534-Guys-1062-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p547 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI535-Guys-1061-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p548 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI536-Guys-1059-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p549 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI539-Guys-1067-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p550 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI549-Guys-1046-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p551 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI550-Guys-1069-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p552 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI551-Guys-1065-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p553 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI552-Guys-1063-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p554 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI554-Guys-1068-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p555 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI555-Guys-1074-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p556 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI558-Guys-1079-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p557 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI560-Guys-1070-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p558 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI562-Guys-1131-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p559 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI569-Guys-1101-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p560 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI576-Guys-1077-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p561 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI578-Guys-1078-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p562 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI579-Guys-1126-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p563 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI582-Guys-1127-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p564 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI584-Guys-1129-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p565 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI585-Guys-1130-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p566 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI587-Guys-1128-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p567 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI589-Guys-1080-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p568 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI591-Guys-1084-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p569 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI592-Guys-1085-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p570 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI593-Guys-1109-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p571 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI594-Guys-1089-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p572 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI616-Guys-1092-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p573 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI617-Guys-1090-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p574 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI618-Guys-1091-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p575 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI619-Guys-1099-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p576 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI621-Guys-1100-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p577 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI622-Guys-1102-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p578 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI623-Guys-1076-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p579 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI625-Guys-1098-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p580 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI626-Guys-1094-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p581 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI627-Guys-1103-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p582 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI629-Guys-1095-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p583 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI630-Guys-1108-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p584 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI639-Guys-1088-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p585 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI641-Guys-1105-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p586 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI642-Guys-1104-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p587 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI644-Guys-1121-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p588 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI648-Guys-1107-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    #############

    p589 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI651-Guys-1118-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p590 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI652-Guys-1116-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    p591 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI653-Guys-1122-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )
    p592 = torchio.Subject(
        t1=torchio.ScalarImage('/scratch/faraz/Thesis/brats_dataprep/ixi/IXI662-Guys-1120-T1_brain_resampled.nii.gz',
                               mylabel=2),

        diagnosis='I',

    )

    subjects_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15,
                     p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30,
                     p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41, p42, p43, p44, p45,
                     p46, p47, p49, p50, p51, p52, p53, p54, p55, p56, p57, p58, p59, p60,
                     p61, p62, p63, p64, p65, p66, p67, p68, p69, p70, p71, p72, p73, p74, p75,
                     p76, p77, p78, p79, p80, p81, p82, p83, p84, p85, p86, p87, p88, p89, p90,
                     p91, p92, p93, p94, p95, p96, p97, p98, p99, p100, p101, p102, p103, p104, p105,
                     p106, p107, p108, p109, p110, p111, p112, p113, p114, p115, p116, p117, p118, p119, p120,
                     p121, p122, p123, p124, p125, p126, p127, p128, p129, p130, p131, p132, p133, p134, p135,
                     p136, p137, p138, p139, p140, p141, p142, p143, p144, p145, p146, p147, p148, p149, p150, p151,
                     p152,
                     p153, p154, p155, p156, p157, p158, p159, p160, p161, p162, p163, p164, p165, p166, p167, p168,
                     p169, p170,
                     p171, p172, p173, p174, p175, p176, p177, p178, p179, p180, p181, p182, p183, p184, p185, p186,
                     p187, p188, p189,
                     p190, p191, p192, p193, p194, p195, p196, p197, p198, p199, p200, p201, p202, p203, p204, p205,
                     p206, p207, p208,
                     p209, p210, p211, p212, p213, p214, p215, p216, p217, p218, p219, p220, p221, p222, p223, p224,
                     p225, p226, p227, p228,
                     p229, p230, p231, p232, p233, p234, p235, p236, p237, p238, p239, p240, p241, p242, p243, p244,
                     p245, p246, p247, p248, p249,
                     p250, p251, p252, p253, p254, p255, p256, p257, p258, p259, p260, p261, p262, p263, p264, p265,
                     p266, p267, p268, p269, p270,
                     p271, p272, p273, p274, p275, p276, p277, p278, p279, p280, p281, p282, p283, p284, p285, p286,
                     p287, p288, p289, p290, p291,
                     p292, p293, p294, p295, p296, p297, p298, p299, p300, p301, p302, p303, p304, p305, p306, p307,
                     p308, p309, p310, p311, p312,
                     p313, p314, p315, p316, p317, p318, p319, p320, p321, p322, p323, p324, p325, p326, p327, p328,
                     p329, p330, p331, p332, p333, p334, p335, p336, p337, p338, p339, p340, p341, p342,
                     p343, p344, p345, p346, p347, p348, p349, p350, p351, p352, p353, p354, p355, p356, p357, p358,
                     p359, p360, p361, p362, p363, p364, p365, p366, p367, p368, p369, p370, p371, p372,
                     p373, p374, p375, p376, p377, p378, p379, p380, p381, p382, p383, p384, p385, p386, p387, p388,
                     p389, p390, p391, p392, p393, p394, p395, p396, p397, p398, p399, p400, p401, p402, p403,
                     p404, p405, p406, p407, p408, p409, p410, p411, p412, p413, p414, p415, p416, p417, p418, p419,
                     p420,
                     p421, p422, p423, p424, p425, p426, p427, p428, p429, p430, p431, p432, p433, p434, p435, p436,
                     p437, p438,
                     p439, p440, p441, p442, p443, p444, p445, p446, p447, p448, p449, p450, p451, p452, p453, p454,
                     p455, p456,
                     p457, p458, p459, p460, p461, p462, p463, p464, p465, p466, p467, p468, p469, p470, p471, p472,
                     p473, p474,
                     p475, p476, p477, p478, p479, p480, p481, p482, p483, p484, p485, p486, p487, p488, p489, p490,
                     p491, p492,
                     p493, p494, p495, p496, p497, p498, p499, p500, p501, p502, p503, p504, p505, p506, p507, p508,
                     p509, p510,
                     p511, p512, p513, p514, p515, p516, p517, p518, p519, p520, p521, p522, p523, p524, p525, p526,
                     p527, p528,
                     p529, p530, p531, p532, p533, p534, p535, p536, p537, p538, p539, p540, p541, p542, p543, p544,
                     p545, p546,
                     p547, p548, p549, p550, p551, p552, p553, p554, p555, p556, p557, p558, p559, p560, p561, p562,
                     p563, p564,
                     p565, p566, p567, p568, p569, p570, p571, p572, p573, p574, p575, p576, p577, p578, p579, p580,
                     p581, p582,
                     p583, p584, p585, p586, p587, p588, p589, p590, p591, p592

                     ]
    return subjects_list
