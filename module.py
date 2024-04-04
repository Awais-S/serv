import random
ugen = []
for agent in range(100000):
		rr = random.randint
		rc = random.choice
		wo = ['SM-J105Y','CPH2293','RMX2193','SM-A505GN','SM-J337V', 'SM-N980F','LM-Q630','vivo 1910','M2012K10C','M2002J9G','V2022','V2023','V2027','V2026','SM-N976N','SM-G525F','PE-TL10','CPH2137','SJ-R21','SM-A526B','CPH1877','Infinix X665C','CPH2251','ART-L28','SM-A805FN','X626','LM-X120','LG-H931','RMX2180','CPH2015','STF-AL10','J9210','M2104K10I','MH-T6000','SM-J530YN','CPH2493','SM-G965T','CPH1907','Y1000','FLA-LX2','LM-V405EBW','SM-T387T','CPH2173','VOG-L09','VIA X20','TA-1012','LH9931','M2007J20CI','22041219NY','K30-T','SM-A320FL','JAT-L41','MGA-LX9']
		ads = random.choice(wo)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 300)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb]))
		ugen.append(ua)
