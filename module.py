import random
ugen=[]
for agents in range(10000):
	rr = random.randint
	rc = random.choice
	
	# Oppo device details
	and_oppo = rc(['14', '11', '10'])
	model_oppo = rc(['CPH2069', 'CPH2131', 'CPH2239','CPH2273','CPH2309', 'CPH1701', 'CPH1912', 'CPH1905', 'CPH2067', 'CPH2099', 'CPH2263', 'CPH1729', 'CPH1939', 'CPH2059', 'CPH2121', 'CPH2203'])
	chrome_oppo = f"{str(rr(80, 444))}.0.{str(rr(3000, 6500))}.{str(rr(11, 499))}"
	
	# Infinix device details
	models_inf = rc(['X401', 'X652A', 'X5010', 'X690B', 'X604','X6819'])
	ch_inf = f"{str(rr(80, 999))}.0.{str(rr(3200, 6500))}.{str(rr(11, 999))}"
	
	# Facebook Hua device details
	fb_hua = f"{str(rr(100, 490))}.0.0.{str(rr(11, 99))}.{str(rr(11, 990))}"
	
	# Vivo device details
	and_vivo = f"{str(rr(11, 14))}"
	models_vivo = rc(['V2021', 'V2023', 'V2027','V2025', 'V2006', 'V2080A','vivoX9L','V2206', 'V2072A', 'V1914A','vivo 1940','vivo 1935','V2126','V2012A'])
	
	# Realme device details
	models_re = rc(['RMX3388', 'RMX1809', 'RMX1803','RMX1827','RMX2032', 'RMX2063', 'RMX2151','RMX3241','RMX1811', 'RMX2180', 'RMX3201','RMX2021'])
	buld_re = rc(['QP1A.190711.020', 'QKQ1.190918.001', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011', 'UKQ1.230924.001', 'UKQ1.230917.001', 'TP1A.220624.014'])
	ch_re = f"{str(rr(120, 999))}.0.{str(rr(3000, 6500))}.{str(rr(11, 999))}"
	
	# Samsung device details
	ad_sam = rc(['10', '7.0', '14', '11'])
	models_sam = rc(['SM-A013G', 'SM-A022M','SM-G950F','SM-A202F','SM-S124DL','SM-A025A','SM-A037U','SM-A105FN','SM-A115AZ','SM-A136U','SM-A205GN','SM-A300H','SM-A336E', 'SM-A5009', 'SM-A500XZ', 'SM-A520W','SM-A516V', 'SM-A536V','SM-G6200','SM-A700YD','M2006C3LVG','M2006C3LII','21061119AL','M2105K81AC'])
	ch_sam = f"{str(rr(52, 124))}.0.{str(rr(2200, 6500))}.{str(rr(11, 199))}"
	
	# Generating user-agent strings
	u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {model_oppo} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36"
	u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; Infinix {models_inf} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_inf} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
	u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36 VivoBrowser/18.9.0.0"
	u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_re} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
	u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
	
	ua = rc([u1, u2, u3, u4, u5])
	ugen.append(ua)
