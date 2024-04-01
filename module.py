import random

def asd():
		uas = ['SM-A125F','SM-A125M','SM-A125U','SM-A125U1','SM-A125N','SM-A125W']
		ft = ['V2061A','CPH2145', 'SM-S901B','FLA-LX3','M2012K11AC','LG-F800K','RMX3472','SM-J610G','RMX3381','SM-A025V','Ivivo 1951','HMA-AL00','SM-T595','SM-X205','V2041','HRY-LX1','SM-N970U1','Cyber X','RX4505','JEF-NX9','STK-L22','CPH2205','RMO-NX3','SM-A600U','Nokia C10','SO-03K','V2040','SM-A326K','CPH1933','S9-KC','SM-G6200','RMX3430','vivo X21UD A','ONEPLUS A5000','SM-M105M']
		an = ['9','8']
		su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
		xg = ['armeabi-v7a:armeabi','arm64-v8a','armeabi-v8a:armeabi','arm64-v8a:armeabi']
		fr = ['pt-BR','en_US','en_GB','es_LA','fr_FR','en_PK']
		cv = ['Banglalink','Vodafone','airtel','IND airtel','Nepal Telecom','Jio 4G','Jio']
		aw = random.choice(['2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9','30'])
		ap = random.choice(fr)
		fd = random.choice(cv)
		ux = random.choice(an)
		fo = random.choice(xg)
		ub = random.choice(uas)
		efg = random.choice(aw)
		se = random.choice(ft)
		so = random.choice(su)
		ua = "Dalvik/2.1.0 (Linux; U; Android "+str(rr(4,13))+"; "+se+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,300))+str(random.randint(11,555)) +";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/FB4A;FBAV/153.0.0.32.85;FBBV/797856764;FBDM/{density=3.0,width=720,height=1600};FBLC/"+ap+";FBRV/164956341;FBCR/"+fd+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+ub+";FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
		return ua
