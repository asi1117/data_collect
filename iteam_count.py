import csv
import time
from functools import reduce
import os
# with open("",'rt',encoding='utf-8_sig') as f:
#     reder = csv.DictReader(f)
#

count = []
worry_list = []
# id_list = ['1279952315376503', '969815736436279', '1498526623509747', '827294127398133', '942006482530009',
#            '1198492796853678', '1251787591581936', '1164252963696830', '1176652609059507', '940410229366998',
#            '1063691710368492', '1130312973723945', '1190441294377640', '941837879186570', '1261331807302580',
#            '1155364627825721', '1124164450939641', '814885695293688', '927672977351617', '970225196383135',
#            '869694586482674', '970981526326393', '977115909056929', '779304552192363', '2247877368571344',
#            '1341671792523028', '1035061809913798', '859807967457408', '1135654449807002', '1028359287211728',
#            '1111432215631156', '1246280708824029', '1389161184521528', '1383189711751416', '1238852986197676',
#            '1250268818411608', '1401343996605343', '948175608590153', '2027653017260426', '1232181650154576',
#            '1402084486500779', '1407846952568081', '1257988667656584', '2865608840146763', '994229133962087',
#            '1159244034143439', '1311119432246338', '1363125447085111', '1723271804396968', '1458129140982015',
#            '1039551732766812', '893462057375013', '1179587862133850', '1750042515043543', '1129567930394285',
#            '869062649886828', '1076393782417282', '1564071926993433', '1265881140114780', '978858615575041',
#            '1585261441509589', '1490394380970763', '1085190581588500', '1157662374252543', '890562797701371',
#            '888655704564160', '2182380691837266', '1148894061844063', '1163301273699318', '1423686654360310',
#            '1533717109978548', '1206152689481565', '835782169860964', '1644126292264565', '855607711227110',
#            '1884542518224310', '1358025144231073', '1742740612417684', '1168200286607832', '1256687334386627',
#            '797549690323260', '1116787541697912', '1077649088989110', '1246460702066816', '1418093681546023',
#            '1230799313655858', '975419542492586', '1483105368478205', '1599089200204462', '702313006537899',
#            '1245015338916107', '994223077313205', '909222225797509', '1692800674095423', '1096547647026443',
#            '967457083325115', '1476883939049726', '984128001677065', '2515738525108145', '1093678027375678',
#            '962797827179803', '1316393138403817', '1845987428750183', '2108210925919661', '922519877806282',
#            '731949250255823', '839725332767068', '1327971593879954', '999953676712829', '2252817104759749',
#            '646891152077200', '1115223751871877', '945657588886188', '1397570263626312', '869485659814410',
#            '906577009374541', '1152440564774310', '1514501481946313', '929143807179080', '1745900872117882',
#            '1175172312522689', '2098235286868577', '1656522077759220', '1165889830098769', '1792865820758773',
#            '2600000103359534', '1272280566205677', '1272636489423125', '2187469658010419', '693852360737481',
#            '743301119132072', '985740968178995', '1040150542725228', '1309677705722446', '1769193356487183',
#            '1506375586042095', '839109046206257', '1016573058409292', '1329467047134070', '442303342561096',
#            '1692021557498395', '1458184060862256', '1192938717388849', '1784608534936050', '1001318569947582',
#            '908567785851774', '1613977911951627', '1662599157093813', '1105507662843899', '1220361218019062',
#            '1308431799167967', '1082826128464888', '2084588764916379', '820253268102944', '1317796131632528',
#            '1152938968151435', '1645146858877576', '1136466006397282', '2151654038193242', '1210834605638180',
#            '1151852774921213', '1311702362213668', '1475724512535901', '1559571227451352', '1308274785931781',
#            '1397503436990351', '937155399709711', '1705533536145044', '1433607290033029', '1994117610669719',
#            '1236726999709837', '1015802351839289', '1010026535719776', '953048504789375', '1096173157163965',
#            '1055629531142378', '1051452461583340', '1458677940864975', '1430068307034578', '2057813437660352',
#            '1176281109085323', '1596151970428159', '1213715582017059', '1138465426283227', '1039052029463099',
#            '815449458566728', '1002899163116852', '764544883656394', '1107766839328808', '1330308093710823',
#            '1274071716010063', '1149523025079174', '1188183857876754', '1150151301762838', '1094257107281857',
#            '1408045589285371', '1900868696672010', '1237598576314376', '1282459145111104', '1165266710246286',
#            '1073856559366835', '1326195317491993', '1666153080144269', '1228338660532183', '1068419409885057',
#            '1094315670658189', '1834522029951979', '957887340986022', '1161055827278470', '1170793196320382',
#            '1880730948683634', '942681562482500', '1297352360374984', '1827480957263521', '1416383481777117',
#            '1079053475440244', '1065433633539161', '1093617717347270', '1052195828241004', '1115959265146824',
#            '1519842891421902', '1442492449205817', '1086522398130218', '1411919038919717', '1237657979662216',
#            '817961768314571', '1032865413439300', '939287339491032', '916630401745678', '1193386440728067',
#            '967592450025614', '1179052298807928', '1783939024969036', '1350225515008434', '697506160349280',
#            '1593975777342062', '796067960495193', '1383443071767092', '1231125970313284', '1199482320162285',
#            '1134330346692366', '1457959427660729', '872167559579148', '888915797823449', '2264650486940997',
#            '1789588554444599', '1233703053312346', '1491907854175850', '798584850248075', '1028739740522755',
#            '1535771263167868', '1172102179510632', '1360994720682508', '2625633214114324', '936326553110906',
#            '750441971724977', '1326984544089099', '1694892783918007', '1027265264008428', '1830914413625836',
#            '1514862561912745', '1118136401544593', '1059251330800683', '1447414238628186', '1135979366469525',
#            '1274880599305742', '1805572406228951', '704783576291313', '1117186341654722', '974420059288856',
#            '955341724542883', '899401630172187', '1240594359359841', '1896659680406341', '971517676219009',
#            '1046954465328733', '913133022131504', '1876666982349412', '637999199658181', '1219562808069896',
#            '1488036287899838', '1195599640458896', '1462012723846452', '1009578569110975', '1523573664385045',
#            '1071493689558158', '2217620391643401', '1497597723606634', '1324679164310094', '1168388049887478',
#            '1072311739534695', '1433153263377039', '764533217004821', '1188879784477485', '1748557301886748',
#            '1454501874624337', '924173877658832', '1130513737020611', '1139013382857601', '1723715221033555',
#            '2176642949027006', '1268902426499564', '1087059131366738', '1147672638577288', '1617001221678467',
#            '1036701589724698', '1419924494723130', '1300263013349763', '1045211762197999', '983261678442712',
#            '1277243192403413', '1471880979518893', '1834973373242178', '914641785316114', '982771795100769',
#            '892968027463189', '1467388843347781', '1436166546433138', '1381620821905816', '1376933662397923',
#            '1509267782486482', '1073687572742391', '1648291811865437', '992805010809326', '1134135246646346',
#            '976046909159185', '2276703325689158', '1045447662230249', '963915370322399', '918156718271999',
#            '1723398854346437', '803125203132875', '1542475959125207', '1174459059254863', '546512902140409',
#            '1371929766155309', '1124492254298555', '2620140564669029', '934674339915892', '2007297379312180',
#            '1489708541098941', '1938563662840722', '1598126356885122', '1465981820197033', '1100747383337483',
#            '1290744591003482', '1441572095934452', '2129805820435611', '1040690412651736', '2154723571220481',
#            '1178115748953782', '2090322207665366', '1292530930842918', '749068321865534', '1462960343734947',
#            '1198601433526554', '1034202093295063', '1214529118674771', '1426618267355919', '1884563648283280',
#            '1029139517196048', '1329982467106352', '1736022076426765', '1339156882838156', '1391548304284983',
#            '1871718786197152', '1688130367976502', '2364870590252749', '1809897762383106', '1163920993632145',
#            '1973899416041933', '1612181508893550', '1932627993464423', '1932183776797079', '1929308520523460',
#            '2190785931001625', '1312559188845495', '1962660437148780', '1964504246901982', '2055672164475811',
#            '1675594145812400', '2365079196906504', '2365251143563517', '1925714304166869', '2424698784271861',
#            '1709238782523826', '2452699524755696', '1163285000441874', '1207916199241348', '1239388509475291',
#            '1607027939327680', '1684580334920669', '1010228079090313', '1013248532088752', '1532533733438338',
#            '1169318969854411', '1581112278669461', '1428287320528005', '1476293569079509', '2185901951459621',
#            '1464810520216368', '2002118589833747', '1242900092425846', '1426119180771781', '1678578035508341',
#            '1267959529922459', '2893734833988477', '1392230570811021', '1612336165492390', '1308960369180690',
#            '1426313427425846', '1900559300017262', '1480250182029706', '1898302430210613', '1513516468676920',
#            '1443717742338698', '1759430264082060', '1317137055078757', '1534966199966470', '2228185307227987',
#            '1787446041296195', '1520039134732158', '1325747684190991', '1928612897204217', '1899081083467955',
#            '1152853434785277', '1641698295876186', '1548818075148912', '1075078902529655', '1091395807610779',
#            '1378834245571358', '2512152512128560', '1580086868693812', '1978400832224524', '1317308518366695',
#            '2389460644427627', '2029486033737792', '1158666007581635', '1466906033365597', '2129964383789845',
#            '1544656912313859', '1181750045204379', '992503684170594', '1700097443425061', '2799914226690358',
#            '1284669471561141', '1491256844278639', '1637576082944853', '878262692296965', '1212238368891470',
#            '2306542396125503', '1599103100154572', '1153993427965181', '1368262083207740', '1645503818802339',
#            '1175048312616465', '1432145000151577', '1162516107186541', '1091161604315290', '974760535972181',
#            '1090623134367376', '1524331530931445', '1322966301106903', '999890153455291', '1666667546723525',
#            '1174624452648980', '1395533030506291', '1301310243262546', '1285913318105808', '1333194773387958',
#            '1270657409683040', '2438115112900489', '1678720028842346', '1272105756135847', '2412287618791781',
#            '1852276078160450', '1516314451794036', '2675214445841036', '1807979115894017', '2391154734289067',
#            '909419709141137', '1297121060348906', '1328569307244888', '1623020254404709', '1063671847025811',
#            '1355030521256699', '1283121388441343', '1078418522275392', '1399736556800852', '1732459530190629',
#            '1950944974977236', '2256634431075894', '1204582006269925', '1114519575315555', '2480220705384651',
#            '2111625568951409', '1512111082174635', '822155747901570', '1242229392548045', '1649832118468834',
#            '1314654188601310', '1834306356618900', '1440250926052355', '1715760008453818', '1698906030200300',
#            '1176414735748031', '1839107082770503', '1431590396875280', '1393634417388939', '2039233006118981',
#            '1135979879802552', '1169711473101637', '1491651084285291', '1144207145676653', '1301430849952300',
#            '1001187066635036', '1102200389827613', '1177986715634360', '1882301038538245', '1910679155667222',
#            '1057308294366167', '1908181425937092', '1123268427742395', '1507202936002141', '1712701125524929',
#            '1268267383280759', '1229011070478055', '1166921553428197', '957997940977508', '1465353230246194',
#            '1452559921492021', '1325781514215661', '1283593541663549', '2276532692364976', '2186133398134464',
#            '2379075352124947', '981318185303176', '1225987560770270', '1794758713929287', '1110609692373708',
#            '1280948248695306', '1196489400366340', '1597871153556553', '2870922692924167', '1308265182572962',
#            '1367312796675079', '1017219438375731', '893710327423160', '1121696511262288', '1286670651462332',
#            '2130603867065604', '1232027913518496', '921656151286079', '1385997328128629', '2275610949145387',
#            '1339795772708323', '995866223865093', '1330247323730249', '2255622867842087', '1836211156444019',
#            '1445165342164827', '1594384107291611', '1411964078835842', '1498710846915554', '1262864070467421',
#            '1439818472776831', '1226084887518288', '1351386438251845', '1626597084076889', '1812156665514011',
#            '2210735768999489', '982319468556497', '1254142181323692', '954104248027422', '1525706217501664',
#            '1635424006496446', '1319349118175460', '2708876125851246', '2099304230107998', '1235740319862860',
#            '814352192025674', '1396595220453211', '1554308144580814', '1624825357552159', '1836237233067947',
#            '1204677752953729', '1221498017906287', '1538140602922694', '1162552413848721', '1749644671743547',
#            '1546565872084156', '1303645319717831', '1634724596608007', '1833979673378882', '1420999057968520',
#            '1440520392683206', '1640145679355737', '1317775404987235', '1233634056684177', '2092748130793752',
#            '1059403080823692', '1242874882435434', '655763911214228', '1701947649841720', '2327882720555378',
#            '1218769578217782', '1312271805535530', '1818308048290175', '1440760322656158', '2164564576948581',
#            '1345279855519886', '1079794805481691', '1484333328284811', '1588326037848832', '1702109373193083',
#            '1625218054204184', '1754893891296534', '1784196901608145', '2351409044933732', '1278997645522490',
#            '1554030881307119', '2054882794628533', '1469400176440180', '1793760207315627', '1689879184370118',
#            '1035656763205647', '1992910510749351', '1281474908540066', '1565988873492912', '2063823487045619',
#            '1584063351668198', '1770956259651277', '1655485311168943', '1846476648763111', '1046051945517101',
#            '1171685502873385', '1303554596363883', '1206286042744297', '1787978867893011', '2079355438825794',
#            '1267305453346375', '1548442951878869', '1143782212362210', '1348481425226688', '1478011548974390',
#            '1602299743220506', '2043845889041446', '951652424934219', '1061163433982769', '1881627821956963',
#            '1363598240361842', '1262694413787430', '1115233775178991', '2204872436205921', '1509620452468804',
#            '1879753195405538', '893040984131487', '1461025750594133', '1698492586827840', '1715978015184865',
#            '1198578316858824', '1890936197643447', '1663834653648968', '2616991518375078', '2289190954438865',
#            '1705352709495577', '1264133353659580', '1659646724105274', '1480767155334570', '2037076092976380',
#            '1031509710236946', '1520619047980648', '1525053574253194', '1546529198754283', '1099387316842405',
#            '2227827680579719', '1260323640676193', '1383422391726922', '1684208744953935', '1583221581750963',
#            '1171944206201442', '2221462354582950', '1395092607226958', '1637176539706668', '1437540826270922',
#            '1152045714894454', '1265645153528817', '1368909253170494', '1718957224836022', '1695627687128904',
#            '1442836775781939', '1916562741759022', '1413956321996878', '1492645400790931', '1427713014002514',
#            '1188615264582268', '352531731537848', '1528347857223593', '1549664095083678', '1205339442875040',
#            '1887659707932041', '1377453642353176', '1224996980954613', '1428450880592282', '1504340412919363',
#            '1463424230375092', '1451786331579849', '1790296634334754', '1529642327114669', '1272734082822892',
#            '1386589188087777', '1442483992493834', '1122106037877975', '1739742929422865', '1876389955711118',
#            '1216567281785099', '1124928977555956', '2281308988561276', '1814074872024230', '1019232254855150',
#            '2207792252593533', '1322583501119472', '1260639860676726', '1599493453504097', '1808488179169635',
#            '1732706276770632', '1814064888639379', '2107904142590556', '1951143931639691', '1556971604391491',
#            '1539172346125255', '1873054289414848', '2230094230387678', '1283814471725720', '1585928168128663',
#            '1845107052196187', '1600117476706680', '1509935985716959', '2129434773773128', '1515747085158115',
#            '1479723692118508', '674020082723155', '2434293676641131', '2424567997609061', '1780456281988243',
#            '2838977819461711', '1042339359226757', '1923796041074350', '1791499370922235', '1827923633931956',
#            '2051824278233919', '1745721745474016', '1455980924414702', '2511854118886031', '1465930903478165',
#            '1687447334632333', '1940786632644691', '2166598490113728', '1857813284259418', '1351920194853562',
#            '1809903285787051', '2087296411294473', '1940525362686304', '2311355522261825', '2049465185091157',
#            '1371395432934029', '1315782518472243', '1625574517548862', '2321213081230191', '1399933736741689',
#            '1833871373366446', '1544852308893316', '2018808911513771', '2351348738262431', '2572765362752733',
#            '1170221253080258', '1793876507292640', '1597710370263546', '2500224536702304', '2447104348661495',
#            '2525056534179120', '1670711503018722', '2415663465145235', '2162812570409727', '2234270353278570',
#            '2275042335871751', '2115815695179272', '1938387136198556', '2233797386689323', '1725243257523071',
#            '1890484677736105', '2016525948452071', '1935956886455445', '1930601700380887', '2870120766391290',
#            '2307438049345010', '2727455957282664', '3013336705359381', '2439690532723888', '1715311011903661',
#            '1869628566461582', '1806945789372143', '1482943268401046', '2163722966974633', '3072886712783728',
#            '1795066593933270', '1715044728551108', '2286096021428390', '2184457871596608', '2117304188387042',
#            '2117987304980708', '2376557319093072', '2244781828973040', '2072766929487859', '1626660900737280',
#            '2169403016480893', '2001216633317459', '2129647710395917', '2190360741012796', '2471769576279885',
#            '2326620234111426', '2855012877858033', '2394684733881252', '2698267323547921', '1781891121939968',
#            '1320861371371231', '2356579607738482', '2334378369971067', '2234167176698693', '3796241227140288',
#            '3743290205690918', '3693047404070061', '3632968493433188', '3625594330795389', '3582676451774250',
#            '3581017328608162', '3576690055731387', '3527944777223297', '3523133864461049', '3510484932332486',
#            '3491172367656653', '3466107356802122', '3462840753766714', '3451512821630610', '3449579278491049',
#            '3439106192779539', '3417785331650285', '3397874170224145', '3396804017029127', '3359474554075670',
#            '3348817661895379', '3347465252036603', '3337373606296486', '3334227066666320', '3289830014445026',
#            '3284357228291769', '3278269668948846', '3265352356867038', '3264201193655001', '3258252620946042',
#            '3253542344664743', '3089033354457696', '3045219882236038', '3037861916323709', '3015671768522195',
#            '3005463392867501', '3002596863131752', '2994652293988472', '2993602733993881', '2990946714347209',
#            '2990091407692747', '2990066157760608', '2985166154833426', '2981904405208593', '2981498431864819',
#            '2964746063538386', '2955928654482306', '3165818406825516', '3157815160909601', '3152675004789593',
#            '3136589733030838', '3119522461437940', '3117882944962986', '3107328052712285', '3106370362755398',
#            '3097547357007160', '3089189254482303', '2751826864934523', '2745449288824134', '2714882785290545',
#            '2689829444436027', '2681266795216749', '2655780594543750', '2654569334651872', '2616254075157692',
#            '2610169122379924', '2602487059828596', '2584242601671594', '2561621967292018', '2557714124311431',
#            '2528862540515417', '2501676163286296', '2477239819049341', '2464167103618398', '2451721584863689',
#            '2451393778316809', '2450127795040322', '2438672549555541', '2410039175769990', '2383473281757389',
#            '2307438349367687', '2301106566668122', '2152278711475458', '2085468338152617', '2035531256550083',
#            '2008190295965331', '1958844807478336', '1859994844050876', '1847929188664915']
filepath = 'C:/Users/Admi/Desktop/detasets/Oculus/GearVR/Iteam_reviews'
id_list = os.listdir(filepath)
print(id_list)
print(len(id_list))
id_count = 1
for id in id_list:
    try:
        #filename = 'C:/Users/Admi/Desktop/oculus/go/iteam_reviews/' + str(id) + '.csv'
        filename = 'C:/Users/Admi/Desktop/detasets/Oculus/GearVR/Iteam_reviews/'+id
        #total = sum(1 for line in open(filename))-1
        #total = len(open(filename).readlines())-1
        first = 0
        with open(filename, 'r', encoding='UTF-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    first += 1
        count.append(first-1)
        print('这个', id, '有', first-1)
    except:
        print('这个id没有评论', id)
        worry_list.append(id)
    id_count = id_count+1
print(id_count)
print(worry_list)
print(len(worry_list))
print(reduce(lambda x, y: x + y, count))
