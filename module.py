import random
ugen = []
for agent in range(100000):
		rr = random.randint
		rc = random.choice
		wo = ['X627V','RMX1903','SM-N7100','SM-A315G','VOG-TL00','CPH2437','SC-51B','SM-S127DL','X689F','XQ-AS52','V2120','T770H','V55','GT-I9505','RMX3242','SM-A245F','LMX06','LGM-V300L','LGM-G600S','TFY-LX2','SM-R880','LLD-L21','GT-I9192','2201117TG','M2007J17G','SM-J600GF','CPH1917','LM-X440ZMW','M2007J3SP','SM-F707B','SM-A525F','LYA-L0C','SM-G892A','CPH2199','SM-A202F','LM-K510','LGM-G600K','SM-J737P','23053RN02Y','X5516B','9060X','CPH2363','POCO X3 NFC','Redmi 9T NFC','V2247','X3 NFC']
		ads = random.choice(wo)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 300)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb]))
		ugen.append(ua)
