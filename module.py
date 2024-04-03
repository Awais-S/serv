import random
ugen = []
for agent in range(100000):
		rr = random.randint
		rc = random.choice
		wo = ['MLA-L13','Infinix X612B','SM-G770F','CPH2199','SM-A037FN', 'NX627J','LM-G710','SM-A600N','SM-A102U1','M2006C3MII','ANG-LX2','RMX3561','SM-A3050','VKY-L29','RMX3612','X6826B','AGS3-W09','TAS-L29','RMX3031','SM-G9810','SM-G781B','RMX3350','RMX3193','CPH2213','SM-X200','SM-T515N','SM-X808U','PAR-LX9','CPH2235','SM-T978U','SM-P620','SM-A225M','S905X','SM-A715F','BQ-5745L','LM-G900TM','SM-N950U','SM-9005','RMX20750','SM-J737T1','SM-F711U1','RMX1931','SM-J600L','LG-US998','TECNO LG8n','J9110','SM-M325F','SM-J3308','SM-J530YM','RMX1807']
		ads = random.choice(wo)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 300)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb]))
		ugen.append(ua)
