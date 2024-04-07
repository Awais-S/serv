import random
ugen = []
for agents in range(100000):
	rr = random.randint
	rc = random.choice
	
	# Oppo device details
	and_oppo = rc(['14', '11', '10'])
	model_oppo = rc(['CPH2035', 'CPH2235', 'CPH1831','CPH2211','CPH2415', 'CPH2411', 'CMA-LX3', 'SNE-LX3', 'RKY-LX2', 'INE-LX2', 'CPH2023', 'LM-X510L', 'SM-A750F', 'CPH1933', 'LM-X220N', 'M2007J20CI','SM-F721B'])
	chrome_oppo = f"{str(rr(80, 444))}.0.{str(rr(3000, 6500))}.{str(rr(11, 499))}"
	
	# Infinix device details
	models_inf = rc(['X658E', 'X666', 'X693', 'X652A', 'X612','X6820','X627V'])
	ch_inf = f"{str(rr(80, 999))}.0.{str(rr(3200, 6500))}.{str(rr(11, 999))}"
	
	# Facebook Hua device details
	fb_hua = f"{str(rr(100, 490))}.0.0.{str(rr(11, 99))}.{str(rr(11, 990))}"
	
	# Vivo device details
	and_vivo = f"{str(rr(11, 14))}"
	models_vivo = rc(['V2190A', 'V1981A', 'V1916A','V2202', 'V2061', 'V2162','V2144','V2129', 'V2050', 'V2164A', 'V2220A', 'V2020A', 'V2156A', 'V350C', 'V2178A','V2036','V2069'])
	
	# Realme device details
	models_re = rc(['RMX3710', 'RMX2040', 'RMX2020','RMX2083','RMX1991', 'RMX3350', 'RMX2050', 'RMX3474', 'RMX3471','RMX1825','RMX3263','RMX2151'])
	buld_re = rc(['QP1A.190711.020', 'QKQ1.190918.001', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011', 'UKQ1.230924.001', 'UKQ1.230917.001', 'TP1A.220624.014'])
	ch_re = f"{str(rr(120, 999))}.0.{str(rr(3000, 6500))}.{str(rr(11, 999))}"
	
	# Samsung device details
	ad_sam = rc(['10', '7.0', '14', '11'])
	models_sam = rc(['22011211C', 'LM-Q730','SM-J260AZ','SM-A505YN','SM-N9700','SM-A605FN','2201116SG','M2101K6P','SM-T290', 'SM-J737S', 'SM-A908N', 'SM-X700','2201116TI', 'SM-A346E','FRL-L23', 'STK-L22', 'M2012K11C', 'JR-J71','GM1900','SM-S901U1','SM-S506DL','J9210','SM-T830'])
	ch_sam = f"{str(rr(52, 124))}.0.{str(rr(2200, 6500))}.{str(rr(11, 199))}"
	
	# Generating user-agent strings
	u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))} {model_oppo} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36"
	u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; Infinix {models_inf} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_inf} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
	u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36 VivoBrowser/18.9.0.0"
	u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))} {models_re} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
	u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
	
	ua = rc([u1, u2, u3, u4, u5])
	ugen.append(ua)
