import random
ugen = []
for agent in range(100000):
		rr = random.randint
		rc = random.choice
		wo = ['M2007J3SG','LM-X510S', 'CPH2199','LM-G710','KSA-LX9','CRT-LX1','SM-T705','22041219PI','CPH2337','ELS-NX9','CPH2113','V1916','220733SL','V1981','V2131','SM-X806B','SM-T540','ABR-AL80','M2007J20CI','SM-A528N','SM-S767VL','V2068','22041219NY','M2010J19SL','Lenovo TB-J616F','22011211C','MGA-LX9','V2143','BMM431B','V1922','RMX1925','XQ-BC52','vivo 1804','SM-M225FV','DBY-W09','SM-A505FM','SM-J330L']
		ads = random.choice(wo)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 300)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb]))
		ugen.append(uab)
