import random

ugen = []

for agents in range(10000):
    rr = random.randint
    rc = random.choice
    
    # Oppo device details
    and_oppo = rc(['14', '11', '10'])
    model_oppo = rc(['CPH2269', 'CPH2271', 'CPH2081','CPH2137','CPH2309', 'CPH1701', 'CPH1909', 'CPH1969', 'CPH1727', 'CPH1725', 'CPH1821', 'CPH2223', 'CPH1911', 'CPH2121', 'CPH2091'])
    chrome_oppo = f"{str(rr(80, 444))}.0.{str(rr(3000, 6500))}.{str(rr(11, 499))}"
    
    # Infinix device details
    models_inf = rc(['X6511E', 'X6823C', 'X503', 'X352', 'X676C','X509'])
    ch_inf = f"{str(rr(80, 999))}.0.{str(rr(3200, 6500))}.{str(rr(11, 999))}"
    
    # Facebook Hua device details
    fb_hua = f"{str(rr(100, 490))}.0.0.{str(rr(11, 99))}.{str(rr(11, 990))}"
    
    # Vivo device details
    and_vivo = f"{str(rr(11, 14))}"
    models_vivo = rc(['V2069', 'vivo Y85', 'V2136A','V2036', 'V2131', 'V2178A','V350C','vivo 1937', 'V2156A', 'V2020A','V2220A','V2164A','V2050','V1916A'])
    
    # Realme device details
    models_re = rc(['RMX3551', 'RMX2202', 'RMX3360','RMX3357','RMX2193', 'RMX2117', 'RMX3041','RMX3475','RMX1992', 'RMX1993', 'RMX2083','RMX2144'])
    buld_re = rc(['QP1A.190711.020', 'QKQ1.190918.001', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011', 'UKQ1.230924.001', 'UKQ1.230917.001', 'TP1A.220624.014'])
    ch_re = f"{str(rr(120, 999))}.0.{str(rr(3000, 6500))}.{str(rr(11, 999))}"
    
    # Samsung device details
    ad_sam = rc(['10', '7.0', '14', '11'])
    et = rc(['U','U1','F','G','S','N','FN'])
    model_sam_et = f"SM-A705{et}"
    models_sam = rc([model_sam_et, f"SM-A707{et}", f"SM-A715{et}", f"SM-A716{et}", f"SM-A810{et}", f"SM-A805{et}", f"SM-A536{et}", "SM-A205GN", f"SM-M205{et}", f"SM-J710{et}", f"SM-J737{et}", f"SM-J730{et}", "STK-AL00", "RMO-NX3", "JAT-LX3", "CLT-L09", f"SM-A307{et}", "LM-X510L", "INE-LX2", "M2004J7BC", "M2011K2C", "220233L2G", "21061119AG", "21051182G"])
    ch_sam = f"{str(rr(52, 124))}.0.{str(rr(2200, 6500))}.{str(rr(11, 199))}"
    ewg = rc([models_sam,models_re,models_vivo,"Infinix" models_inf,model_oppo])
    
    # Generating user-agent strings
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {model_oppo} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; Infinix {models_inf} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_inf} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36 VivoBrowser/18.9.0.0"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_re} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; Android {ewg} Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
    
    ua = rc([u1, u2, u3, u4, u5, u6])
    ugen.append(ua)
