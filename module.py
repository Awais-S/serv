import random
ugen=[]
for agents in range(10000):
	rr = random.randint
	rc = random.choice
	
	# Oppo device details
	and_oppo = rc(['14', '11', '10'])
	model_oppo = rc(['CPH1717', 'CPH1915', 'CPH1987','CPH2213','CPH1609', 'CPH1725', 'CPH1825', 'CPH2025', 'CPH2173', 'CPH1719', 'CPH1877', 'CPH1611', 'CPH2043', 'CPH2036', 'CPH2091', 'CPH2089'])
	chrome_oppo = f"{str(rr(80, 444))}.0.{str(rr(3000, 6500))}.{str(rr(11, 499))}"
	
	# Infinix device details
	models_inf = rc(['X606D', 'X620', 'X627V', 'X690B', 'X571','X5514D'])
	ch_inf = f"{str(rr(80, 999))}.0.{str(rr(3200, 6500))}.{str(rr(11, 999))}"
	
	# Facebook Hua device details
	fb_hua = f"{str(rr(100, 490))}.0.0.{str(rr(11, 99))}.{str(rr(11, 990))}"
	
	# Vivo device details
	and_vivo = f"{str(rr(11, 14))}"
	models_vivo = rc(['V2207A', 'vivo 1904', 'V2055A','vivo 2006', 'vivo 1910', 'V2132A','vivo 2010','V2126', 'V2040', 'V2238','vivo X21UD A','vivo X21A','V2073A','V1963A'])
	
	# Realme device details
	models_re = rc(['RMX2170', 'RMX2163', 'RMX3085','RMX3521','RMX3472', 'RMX3491', 'RMX2185','RMX2189','RMX2195', 'RMX2180', 'RMX1941','RMX3203'])
	buld_re = rc(['QP1A.190711.020', 'QKQ1.190918.001', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011', 'UKQ1.230924.001', 'UKQ1.230917.001', 'TP1A.220624.014'])
	ch_re = f"{str(rr(120, 999))}.0.{str(rr(3000, 6500))}.{str(rr(11, 999))}"
	
	# Samsung device details
	ad_sam = rc(['10', '7.0', '14', '11'])
	models_sam = rc(['SM-G887F', 'SM-G885S','SM-A530N','SM-A810YZ','SM-A320FL','SM-A225M','SM-A215U1','SM-A205GN','SM-M105G','SM-J701F','SM-J710FN','SM-J737T1','SM-J730FM', 'SM-S727VL', 'SM-N770F', 'SM-N975X','SM-A326K', 'Y300-0100','Y221-U12','NEO-L29','MHA-L09','NXT-AL10','CET-LX9','OCE-AN50,'22101316UG','M2101K9AG','2109119DG','M2102K1G','21081111RG'])
	ch_sam = f"{str(rr(52, 124))}.0.{str(rr(2200, 6500))}.{str(rr(11, 199))}"
	
	# Generating user-agent strings
	u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {model_oppo} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36"
	u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; Infinix {models_inf} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_inf} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
	u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36 VivoBrowser/18.9.0.0"
	u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_re} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
	u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
	
	ua = rc([u1, u2, u3, u4, u5])
	ugen.append(ua)
