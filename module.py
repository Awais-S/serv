import random
ugen=[]
for agent in range(100000):
		rr = random.randint
		rc = random.choice
		wo = ['RMX1901','SC-04C', 'RMX1931','V2026','RMX1941','G630-U10','X663','SM-G930F','GT-I9500','SM-T231','MLA-L11','SM-P613','SM-E225F','SM-A725F','SM-S901N','LM-X420','CPH2161','SM-A600P','SM-A105F','Redmi Note 9 Pro','V2029','V2020','V2028','SM-N981N','Lenovo L19041','DLT-A0','T21-EEA','ZTE 8010RU','CPH2473','SM-J737T','M2011K2G','CPH2353']
		ads = random.choice(wo)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 300)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb]))
		ugen.append(ua)
