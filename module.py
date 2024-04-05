import random
ugen = []
for agent in range(100000):
		rr = random.randint
		rc = random.choice
		wo = ['SM-J320H','SM-T561','SM-P7300','GT-I9301I','CPH3809', 'CPH2203','CPH2069','CPH2009','CPH3983','RMX2193','RMX2155','RMX2117','RMX2072','RMX2051','RMX1993','Infinix X687','CPH2121','M2012K11AG','SM-A127G','SM-N986W','SM-A102U1','M2006C3MII','SM-A037U1','SM-A520F','VKY-L29','RMX3612','V2207','CMA-LX2','SM-A705GM','SM-J500FN','RMX1945','SM-M546B','V2072','BNE-LX1','Infinix X655C','V2157','SM-A202K','CDY-NX9A','SM-S908N','V2025','SM-A7070','SM-J337W','SM-A032M','V2028','LG-H933','LM-X440IM','V2012','YAL-L21','SM-J415FN','BND-L21']
		ads = random.choice(wo)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 300)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb]))
		ugen.append(uab)
