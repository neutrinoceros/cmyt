# The "kelp" colormap was originally created by John ZuHone within the yt-project
import numpy as np

# Used to reconstruct the colormap in viscm
viscm_parameters = {
    "xp": [
        -2.3569023569023386,
        29.24031986531989,
        21.948653198653204,
        -25.44718013468011,
        -4.78745791245791,
    ],
    "yp": [
        -27.604166666666657,
        -30.642361111111086,
        24.652777777777771,
        -13.6284722222222,
        23.4375,
    ],
    "min_Jp": 15,
    "max_Jp": 95,
}

luts = np.transpose(
    (
        [
            0.07873808,
            0.08503098,
            0.09119215,
            0.09725944,
            0.10324966,
            0.10914691,
            0.1149903,
            0.12076614,
            0.12647234,
            0.13214487,
            0.13775951,
            0.14331952,
            0.14885405,
            0.15434127,
            0.15978387,
            0.16520148,
            0.17058327,
            0.17592717,
            0.1812416,
            0.18653223,
            0.19178949,
            0.19701509,
            0.20221806,
            0.20739605,
            0.21254477,
            0.21766522,
            0.22276163,
            0.22783646,
            0.232884,
            0.23790477,
            0.24289917,
            0.24786997,
            0.25281796,
            0.25773939,
            0.26263436,
            0.26750288,
            0.27234491,
            0.27716076,
            0.28195253,
            0.28671682,
            0.29145343,
            0.29616211,
            0.30084257,
            0.30549451,
            0.31011758,
            0.31471143,
            0.31927567,
            0.32380992,
            0.32831456,
            0.3327882,
            0.33723043,
            0.34164086,
            0.34601907,
            0.35036466,
            0.35467722,
            0.35895634,
            0.36320162,
            0.36741265,
            0.37158905,
            0.37573041,
            0.37983636,
            0.38390652,
            0.38794052,
            0.391938,
            0.3958986,
            0.39982199,
            0.40370783,
            0.40755579,
            0.41136559,
            0.41513702,
            0.41886962,
            0.42256312,
            0.42621724,
            0.42983171,
            0.43340628,
            0.43694071,
            0.44043477,
            0.44388826,
            0.44730096,
            0.4506727,
            0.4540033,
            0.45729265,
            0.46054056,
            0.46374691,
            0.4669116,
            0.47003456,
            0.47311572,
            0.47615505,
            0.47915255,
            0.48210822,
            0.48502208,
            0.4878942,
            0.49072469,
            0.49351365,
            0.49626124,
            0.49896763,
            0.50163303,
            0.50425765,
            0.50684177,
            0.50938571,
            0.51188977,
            0.51435433,
            0.51677977,
            0.5191665,
            0.52151498,
            0.52382573,
            0.52609922,
            0.52833601,
            0.53053664,
            0.53270171,
            0.53483184,
            0.53692768,
            0.53898991,
            0.54101933,
            0.54301655,
            0.5449823,
            0.54691736,
            0.54882248,
            0.55069849,
            0.55254618,
            0.55436641,
            0.55616019,
            0.55792828,
            0.55967151,
            0.56139081,
            0.56308707,
            0.56476124,
            0.56641427,
            0.56804712,
            0.56966078,
            0.57125625,
            0.57283474,
            0.5743971,
            0.57594437,
            0.57747763,
            0.578998,
            0.58050659,
            0.58200457,
            0.58349311,
            0.58497344,
            0.58644679,
            0.58791447,
            0.58937777,
            0.59083808,
            0.59229669,
            0.59375499,
            0.59521431,
            0.59667599,
            0.5981412,
            0.59961095,
            0.60108588,
            0.60256604,
            0.60405059,
            0.60553731,
            0.60702199,
            0.60849757,
            0.60995371,
            0.61137672,
            0.61275043,
            0.61405949,
            0.61529472,
            0.61645863,
            0.61756755,
            0.6186476,
            0.61972621,
            0.62082374,
            0.62195065,
            0.62310898,
            0.62429421,
            0.62549895,
            0.62671518,
            0.62793547,
            0.62915284,
            0.63036156,
            0.63155892,
            0.63274216,
            0.63390941,
            0.63505915,
            0.6361885,
            0.63730024,
            0.63839517,
            0.63947435,
            0.64053552,
            0.64158527,
            0.64262677,
            0.64365947,
            0.64469056,
            0.6457271,
            0.6467694,
            0.6478306,
            0.64891699,
            0.65003829,
            0.65120839,
            0.65243764,
            0.6537444,
            0.65514254,
            0.65665209,
            0.65829045,
            0.66007696,
            0.66202922,
            0.66416348,
            0.66649284,
            0.66902763,
            0.67177387,
            0.67473363,
            0.6779068,
            0.68128823,
            0.68487229,
            0.68865042,
            0.69261428,
            0.69675486,
            0.70106274,
            0.7055261,
            0.71013753,
            0.71488908,
            0.71977295,
            0.72478197,
            0.72990967,
            0.73515031,
            0.74049508,
            0.74593782,
            0.75147747,
            0.75711082,
            0.76283528,
            0.76864883,
            0.77453293,
            0.78049489,
            0.78653899,
            0.79266478,
            0.7988389,
            0.80509156,
            0.81142348,
            0.81779745,
            0.82424433,
            0.83076477,
            0.83731914,
            0.84395228,
            0.85063328,
            0.8573683,
            0.86417388,
            0.87100664,
            0.87792232,
            0.88485711,
            0.89186942,
            0.898911,
            0.90601831,
            0.91316089,
            0.92036241,
            0.92760063,
            0.93489628,
            0.94222522,
            0.94961559,
            0.95703072,
            0.96451696,
            0.97201416,
            0.97959794,
        ],
        [
            0.02380049,
            0.02762946,
            0.0314955,
            0.03538367,
            0.03929263,
            0.04314916,
            0.04681625,
            0.05034685,
            0.05376738,
            0.05706764,
            0.06028584,
            0.06343363,
            0.06649987,
            0.06951333,
            0.0724811,
            0.07539619,
            0.07827446,
            0.0811238,
            0.08394364,
            0.08673511,
            0.08950972,
            0.0922702,
            0.09501404,
            0.0977463,
            0.10047279,
            0.10319545,
            0.10591402,
            0.10862929,
            0.11134673,
            0.11406773,
            0.11679361,
            0.11952425,
            0.12226063,
            0.12500588,
            0.12776095,
            0.13052669,
            0.13330389,
            0.13609311,
            0.13889411,
            0.1417089,
            0.14453802,
            0.14738192,
            0.15024103,
            0.15311572,
            0.15600633,
            0.15891314,
            0.1618364,
            0.16477634,
            0.16773294,
            0.17070662,
            0.17369747,
            0.17670558,
            0.17973101,
            0.18277379,
            0.18583395,
            0.18891149,
            0.19200641,
            0.19511868,
            0.19824828,
            0.20139517,
            0.20455931,
            0.20774066,
            0.21093915,
            0.21415474,
            0.21738737,
            0.22063697,
            0.22390351,
            0.22718691,
            0.23048713,
            0.23380417,
            0.23713792,
            0.24048832,
            0.2438553,
            0.24723882,
            0.25063881,
            0.25405521,
            0.25748797,
            0.26093702,
            0.26440229,
            0.26788372,
            0.27138123,
            0.27489488,
            0.27842445,
            0.28196986,
            0.28553099,
            0.28910775,
            0.29270002,
            0.29630767,
            0.29993058,
            0.30356863,
            0.30722174,
            0.31088964,
            0.31457215,
            0.3182691,
            0.32198029,
            0.32570551,
            0.32944456,
            0.33319721,
            0.33696322,
            0.34074232,
            0.34453424,
            0.34833872,
            0.35215547,
            0.35598423,
            0.35982468,
            0.36367647,
            0.36753933,
            0.37141294,
            0.37529698,
            0.37919113,
            0.38309506,
            0.38700843,
            0.39093088,
            0.394862,
            0.39880154,
            0.40274917,
            0.40670453,
            0.41066731,
            0.41463715,
            0.41861372,
            0.42259669,
            0.4265856,
            0.43058022,
            0.43458024,
            0.43858535,
            0.44259523,
            0.44660955,
            0.45062802,
            0.45465032,
            0.45867614,
            0.46270517,
            0.466737,
            0.47077145,
            0.47480823,
            0.47884705,
            0.48288761,
            0.48692962,
            0.4909728,
            0.49501685,
            0.49906149,
            0.50310643,
            0.5071514,
            0.51119613,
            0.51524033,
            0.51928381,
            0.52332635,
            0.52736778,
            0.531408,
            0.53544701,
            0.53948493,
            0.54352212,
            0.54755923,
            0.55159738,
            0.55563825,
            0.55968439,
            0.56373935,
            0.56780781,
            0.57189523,
            0.57600725,
            0.58014816,
            0.58431885,
            0.58851523,
            0.59272844,
            0.59694739,
            0.6011624,
            0.6053679,
            0.60956269,
            0.61374861,
            0.61792946,
            0.62210956,
            0.62629294,
            0.63048304,
            0.63468291,
            0.63889495,
            0.64312026,
            0.64735999,
            0.65161492,
            0.65588577,
            0.66017389,
            0.66447826,
            0.66879882,
            0.67313546,
            0.67748957,
            0.68185887,
            0.68624266,
            0.69064192,
            0.69505448,
            0.69947837,
            0.70391466,
            0.70835911,
            0.71281063,
            0.71726683,
            0.72172374,
            0.72617917,
            0.73062754,
            0.73506547,
            0.73948684,
            0.74388673,
            0.74825915,
            0.7525986,
            0.75689972,
            0.76115802,
            0.76536957,
            0.76953177,
            0.77364343,
            0.77770289,
            0.78171225,
            0.78567138,
            0.78958223,
            0.79344761,
            0.79726965,
            0.80105066,
            0.8047929,
            0.80849913,
            0.81217164,
            0.81581257,
            0.81942391,
            0.82300747,
            0.82656492,
            0.83009816,
            0.83360887,
            0.83709793,
            0.84056637,
            0.844015,
            0.84744449,
            0.85085836,
            0.85425577,
            0.85763616,
            0.8609997,
            0.8643531,
            0.86769067,
            0.87101222,
            0.87432566,
            0.87762463,
            0.88090892,
            0.88418748,
            0.88745026,
            0.89070437,
            0.89394846,
            0.89717856,
            0.90040525,
            0.90361483,
            0.90682325,
            0.91001579,
            0.9132048,
            0.91638083,
            0.9195519,
            0.92271171,
            0.92586627,
            0.92900992,
            0.93214934,
            0.93527665,
            0.93840226,
            0.94151285,
            0.9446259,
            0.94771918,
        ],
        [
            0.45890713,
            0.46137905,
            0.46384563,
            0.46630529,
            0.46875421,
            0.4711862,
            0.47360008,
            0.47599069,
            0.47835461,
            0.48068977,
            0.48299219,
            0.4852595,
            0.48748847,
            0.48967699,
            0.49182306,
            0.49392292,
            0.4959753,
            0.49797881,
            0.4999306,
            0.50182767,
            0.50367037,
            0.5054572,
            0.50718436,
            0.50885097,
            0.51045736,
            0.51200237,
            0.51348338,
            0.51489809,
            0.51624834,
            0.51753338,
            0.51875253,
            0.51990356,
            0.52098523,
            0.52199968,
            0.52294672,
            0.52382624,
            0.52463824,
            0.52538248,
            0.52605675,
            0.52666444,
            0.52720607,
            0.52768224,
            0.5280937,
            0.5284413,
            0.52872599,
            0.52894886,
            0.52911108,
            0.5292139,
            0.52925736,
            0.52924451,
            0.5291769,
            0.52905617,
            0.52888406,
            0.52866235,
            0.5283929,
            0.52807762,
            0.52771851,
            0.52731757,
            0.52687689,
            0.52639856,
            0.52588473,
            0.52533756,
            0.52475925,
            0.524152,
            0.52351804,
            0.5228596,
            0.52217891,
            0.5214782,
            0.52075951,
            0.52002465,
            0.51927646,
            0.51851715,
            0.51774891,
            0.51697393,
            0.51619438,
            0.5154124,
            0.5146301,
            0.51384958,
            0.51307291,
            0.51230212,
            0.51153923,
            0.51078544,
            0.51004343,
            0.50931521,
            0.50860267,
            0.50790763,
            0.50723191,
            0.50657725,
            0.50594539,
            0.50533791,
            0.50475611,
            0.50420208,
            0.50367737,
            0.50318346,
            0.50272179,
            0.50229376,
            0.50190069,
            0.5015438,
            0.50122435,
            0.50094363,
            0.50070274,
            0.50050273,
            0.50034459,
            0.50022925,
            0.50015758,
            0.50013055,
            0.50014881,
            0.50021302,
            0.50032381,
            0.50048172,
            0.50068726,
            0.50094086,
            0.50124298,
            0.50159412,
            0.50199429,
            0.50244368,
            0.50294243,
            0.50349062,
            0.5040883,
            0.50473544,
            0.50543197,
            0.50617805,
            0.5069733,
            0.50781742,
            0.50871016,
            0.5096512,
            0.51064021,
            0.51167679,
            0.51276051,
            0.5138909,
            0.51506743,
            0.51628978,
            0.51755709,
            0.51886873,
            0.52022401,
            0.52162216,
            0.52306241,
            0.52454388,
            0.52606564,
            0.52762668,
            0.5292259,
            0.53086207,
            0.53253385,
            0.53423975,
            0.53597803,
            0.53774675,
            0.53954371,
            0.54136636,
            0.54321177,
            0.54507652,
            0.54695667,
            0.54884775,
            0.55074476,
            0.55264242,
            0.55453558,
            0.55642011,
            0.55829453,
            0.56016223,
            0.56203375,
            0.56392814,
            0.56587122,
            0.56788936,
            0.57000019,
            0.57220545,
            0.57449055,
            0.57683063,
            0.57919892,
            0.58157275,
            0.58393538,
            0.58627588,
            0.58858776,
            0.59086745,
            0.59311274,
            0.59532221,
            0.59749564,
            0.59963222,
            0.60173091,
            0.60379008,
            0.60580649,
            0.60777924,
            0.6097056,
            0.61158212,
            0.61340237,
            0.6151645,
            0.61686366,
            0.61849128,
            0.62004292,
            0.62151305,
            0.62288934,
            0.62416816,
            0.62533879,
            0.62639158,
            0.62731938,
            0.6281096,
            0.62875725,
            0.62925097,
            0.62958736,
            0.62976024,
            0.62976899,
            0.62961438,
            0.62930119,
            0.62883586,
            0.62822926,
            0.62749232,
            0.62663432,
            0.62567778,
            0.62461908,
            0.62348256,
            0.62227864,
            0.621005,
            0.6196701,
            0.61828149,
            0.61685751,
            0.61539115,
            0.61388335,
            0.61233673,
            0.61075292,
            0.60913269,
            0.607476,
            0.60579314,
            0.60408651,
            0.60234546,
            0.60056748,
            0.59874959,
            0.59688839,
            0.59502121,
            0.59312158,
            0.59117279,
            0.58917064,
            0.58718501,
            0.58514178,
            0.58303558,
            0.58094288,
            0.57879227,
            0.5765793,
            0.57438349,
            0.57210749,
            0.56981243,
            0.56748232,
            0.56508082,
            0.56269289,
            0.56020367,
            0.55773849,
            0.5551784,
            0.55261699,
            0.54997983,
            0.54732492,
            0.54460356,
            0.54185741,
            0.53904386,
            0.53620824,
            0.53329363,
            0.53036982,
            0.52734442,
            0.52433316,
            0.52118636,
        ],
    )
)
