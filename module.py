import random
ugen=[]
for agent in range(100000):
		rr = random.randint
		rc = random.choice
		wo = ['RMX1919','SC-02C', 'CPH2145','CPH2201','X662B','MHA-L29','TRT-LX2','SM-A500H','2209116AG','OCE-AN50','SM-9005','SM-A115U1','SM-G611FN','SM-M115G','SM-G990B2','SM-A4260','SM-N975C','SM-A307GT','V2126','SM-G355M','SM-J415GN','SM-J530FM','V341U','TFY-LX2','V2105','Lenovo L38111','Lenovo YT-J706X','SM-A405FN','V2060','V2048','Lava Z66','X671B','V1829','SM-G892A','SM-F907FN','CPH2199','SM-T825Y','SM-F700U','M2012K11AC']
		ads = random.choice(wo)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 300)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb]))
		ugen.append(ua)
