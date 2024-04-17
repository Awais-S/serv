import random
ugen=[]
for agents in range(10000):
		rr = random.randint
		rc = random.choice
		wo = ['SM-A025A','vivo 1909', 'V2023','V2020','V2027','V1930','SM-G885F','RMX3571','V1938CT','RMX2002','LIO-AL00','LM-Q520N','SM-M515F','SM-A515X','RMX3286','V2202','V2205','2112123AG','J9110','M2103K19PG','SM-A105FN','SM-X706B','CPH1871','LLD-L31','SM-G975F','LM-V409N','2201117SI','RMX1901','MAR-LX1A','V2145','SM-N960F','22101316UG','CPH2213','LM-V500N','SM-T517P','SM-A115M','M2102K1C','LIO-L29','SM-A217N']
		ads = random.choice(wo)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 999)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb]))
		ugen.append(ua)
