import random
ugen=[]
for agent in range(1):
		rr = random.randint
		rc = random.choice
		wo = ['V2120','SM-G973C', 'SM-A217N','M2006J10C','V2065','RMX1821','SM-T970','NAM-LX9','SM-T547U','LG-H870S','BQ-4030G','SPH-L720','LYA-L0C','SM-N9760','CPH1937','SM-T387W','SM-T503','M2010J19SG','LGV36','SM-A9200','RMX1809','CPH2063','SM-J810M','LG-RS988','CPH2495','SM-A505FN','SM-X205','V2110','EVR-L29','RMX2156','CPH3987','PPA-LX1','LDN-AL20','SM-M426B','BQ-5519G','V2118','LM-F100','SM-J701M','SM-T976B']
		ads = random.choice(wo)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 300)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb]))
		ugen.append(ua)
