import random

def asd():
    rr = random.randint
    rc = random.choice
    wo = ['RMX1831','RMX1919', 'X657C','X662C','M2007J3SG','SM-G770F','SM-T867V','SM-S906U','LM-K735','SM-S908B','SM-G781N','SM-A205GN','J8110','RMX2071','SM-A025AZ','V2031','SM-A105M','Infinix X655B','LM-V350N','M2103K19PG','vivo 1940','BKL-L04','MAR-LX1A','J8210','V2102','SM-N9300','M2103K19PG','H60-L21','CPH2577','RMX3085','V2059','SM-X806B','SM-T540','SM-A528N','SM-T636B','LM-X420N','SM-A320FL','RMX3197','CPH1805']

    ads = random.choice(wo)
    uab = "Mozilla/5.0 (Linux; Android " + wo + " Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
    uaxb = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; " + wo + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 300)) + " Mobile Safari/537.36"
    ua = str(rc([uab,uaxb]))
    return ua
