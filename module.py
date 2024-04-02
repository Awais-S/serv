import random
ugen = []
for agent in range(100000):
		rr = random.randint
		rc = random.choice
		wo = ['J8170','SM-T509','J8270','SM-A205S','XQ-BT52','LM-K735','V2102','SM-S906U','J8110','J8210','2201116TG','RMX2205','CTR-LX3','SM-A125FN','V30','RMX1851','LGM-V300L','XQ-AU51','SM-A805N','CPH2413','V1829','SM-F926B','RMO-NX1','SM-A6060','G720C','SM-M022M','S6-KC','X670C','JDN2-L09','T810S','CPH2527','HJC-LX9','X6810','V2070','SM-A305GT','LM-G820N','HRY-LX1T','V2231','BQ-5045L','SM-J701MT','22126RN91Y','SM-S906E','V2239','X627V','SM-G973N']
		ads = random.choice(wo)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 300)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb]))
		ugen.append(ua)
