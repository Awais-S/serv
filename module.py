import random
ugen=[]
for agent in range(100000):
		rr = random.randint
		rc = random.choice
		wo = ['V2152','SM-F700N', 'SM-X900','SM-A520F','CPH2415','M2007J22C','LMG01','ZTE Blade L130','LM-Q730N','BQ-5540L','SM-A307GN','CPH2461','SM-J600FN','CPH2091','ZTE A2121','SM-N935K','RMX3461','CDY-AN90','TB-Q706F','SM-T860X','XQ-AS52','V2214','LG-D855','CPH1979','SM-M017FN','SM-S115DL','SM-S367VL','220333QAG','CPH2343','SM-A037U1','RMX3201','RMX1991','21121119SG','SM-M546B','LM-K500','SM-X800','SM-J415FN','M2101K6G','BQ-6035L']
		ads = random.choice(wo)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 300)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb]))
		ugen.append(ua)
