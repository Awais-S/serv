import random

ugen = []

for agents in range(10000):
		rr = random.randint
		rc = random.choice
		wo = ['CPH2417','22041216I', 'CPH2419','CPH2459','X689D','RMX1833','X6816C','X665E','M2007J17G','RMX1929','GT-7245','SM-A300H','SM-A3051','SM-A606Y','SM-G6200','SM-A920F','SM-A810S','Infinix X509','SM-A430F','SNE-LX3','Lenovo YT-X705L','SM-J730K','SM-F7110','LM-Q510N','vivo 1938','V2221','V2020','L78121','V2234','M2007J17I','SM-M205F']
		ads = random.choice(wo)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 300)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb]))
		ugen.append(ua)
