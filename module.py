import random
ugen=[]
for agents in range(10000):
		rr = random.randint
		rc = random.choice
		wo = ['CPH1803','CPH1805', '2107113SG','RMX2103','Infinix X655D','SM-A115U','SM-A136W','Infinix X572','RMX3393','21061119AL','RMX1811','CPH2139','CPH2127','V2022','V2023','CPH1943','SM-A260G','Infinix X656','RMX1941','M2004J7BC','CPH1912','M2010J19SI','Infinix X5515F','SM-A305GT','SM-A307FN','RMX3300','SM-A3051','SN-A426B','RMX3357','SM-A500X','SM-J327AZ','M2012K11I','CPH2407','SM-M225FN','X655F','SM-G781B','SM-J330F','SM-A826S']
		ads = random.choice(wo)
		uab = "Mozilla/5.0 (Linux; Android " + ads + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 999)) + " Mobile Safari/537.36"
		uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + ads + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
		ua = str(rc([uab,uaxb]))
		ugen.append(ua)
