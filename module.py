import random
ugen=[]
for agents in range(10000):
	rr = random.randint
	rc = random.choice
	and_oppo=rc(['14','11','10'])
	model_oppo=rc(['CPH2201','CPH1917','CPH2421','CPH1937','RMX2170','RMX1831','RMX2117','RMX2156','SO-53C','J9210','XQ-AT51','CPH2359','CPH2185','CPH1979'])
	chrome_oppo=f"{str(rr(80,444))}.0.{str(rr(3000,6500))}.{str(rr(11,499))}"
	models_inf=rc(['X657C','X676C','X6711','X6832','X6525B'])
	ch_inf=f"{str(rr(80,999))}.0.{str(rr(3200,6500))}.{str(rr(11,999))}"
	fb_hua=f"{str(rr(100,490))}.0.0.{str(rr(11,99))}.{str(rr(11,990))}"
	and_vivo=f"{str(rr(11,14))}"
	models_vivo=rc(['V2006','V1914A','V2022','V2002','V2023','V2024','V2026','V2027','V2028','V2030','V2029','V2040'])
	models_re=rc(['RMX1945','RMX3381','RMX1903','RMX2121','RMX3572','RMX3842','RMX3890'])
	buld_re=rc(['QP1A.190711.020','QKQ1.190918.001','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011','UKQ1.230924.001','UKQ1.230917.001','TP1A.220624.014'])
	ad_sam=rc(['10','7.0','14','11'])
	ch_re=f"{str(rr(120,999))}.0.{str(rr(3000,6500))}.{str(rr(11,999))}"
	models_sam=rc(['SM-G781B','SM-A127F','SM-M625F','SM-J530L','SM-G892U','SM-J737VPP','SM-P615N','SM-A202L','SM-G973C','SM-S908N','SM-G525G'])
	ch_sam=f"{str(rr(52,124))}.0.{str(rr(2200,6500))}.{str(rr(11,199))}"
	u1=f"Mozilla/5.0 (Linux; Android {str(rr(4,13))} {model_oppo} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36"
	u2=f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; Infinix {models_inf} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_inf} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
	u3=f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36 VivoBrowser/18.9.0.0"
	u4=f"Mozilla/5.0 (Linux; Android {str(rr(4,13))} {models_re} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
	u5=f"Mozilla/5.0 (Linux; U; Android {str(rr(4,13)); zh-CN; {models_sam} Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_sam} UCBrowser/11.6.4.950 UCBS/2.11.1.20 Mobile Safari/537.36 AliApp(TB/7.0.2) WindVane/8.0.0 1080X1920"
	ua=rc([u1,u2,u3,u4,u5])
	ugen.append(ua)
