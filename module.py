import random

ugen = []

for agents in range(10000):
    rr = random.randint
    rc = random.choice
    
    # Oppo device details
    and_oppo = rc(['14', '11', '10'])
    model_oppo = rc(['CPH3837', 'CPH3803', 'CPH2209', 'CPH2271', 'CPH1955', 'CPH2339', 'CPH2095', 'CPH2077', 'CPH2065', 'CPH2069', 'CPH2059', 'CPH1099', 'CPH1091', 'CPH1073', 'CPH1065', 'CPH1979'])
    chrome_oppo = f"{str(rr(80, 444))}.0.{str(rr(3000, 6500))}.{str(rr(11, 499))}"
    
    # Infinix device details
    models_inf = rc(['X559C', 'X559F', 'X606D', 'X604B', 'X5010'])
    ch_inf = f"{str(rr(80, 999))}.0.{str(rr(3200, 6500))}.{str(rr(11, 999))}"
    
    # Facebook Hua device details
    fb_hua = f"{str(rr(100, 490))}.0.0.{str(rr(11, 99))}.{str(rr(11, 990))}"
    
    # Vivo device details
    and_vivo = f"{str(rr(11, 14))}"
    models_vivo = rc(['V1923A', 'V2205', 'V2152', 'V2221', 'V2109', 'vivo 1938', 'vivo 1910', 'V2042', 'V2037', 'V2214', 'V2201', 'V2247', 'V2117', 'V2238A', 'V2241A', 'V2021', 'V1924A'])
    
    # Realme device details
    models_re = rc(['RMX1931', 'RMX2002', 'RMX2032', 'RMX3661', 'RMX3201', 'RMX2051', 'RMX2071', 'RMX2101', 'RMX2163'])
    buld_re = rc(['QP1A.190711.020', 'QKQ1.190918.001', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011', 'UKQ1.230924.001', 'UKQ1.230917.001', 'TP1A.220624.014'])
    ch_re = f"{str(rr(120, 999))}.0.{str(rr(3000, 6500))}.{str(rr(11, 999))}"
    
    # Samsung device details
    ad_sam = rc(['10', '7.0', '14', '11'])
    models_sam = rc(['SM-M136B', 'SM-N975F', 'SM-M325FV', 'SM-J337A', 'SM-A516V', 'SM-G977N', 'SM-A2070', 'SM-A207M', 'SM-S901B', 'SM-A013G', 'SM-T820', 'SM-T555', 'SM-G7810', 'SM-T315', 'SM-S727VL', 'SM-J610F', 'SM-J610F', 'SM-J610G', 'SM-J610FN', 'SM-A736B', 'SM-N915A'])
    ch_sam = f"{str(rr(50, 499))}.0.{str(rr(2200, 6500))}.{str(rr(11, 499))}"
    
    # Generating user-agent strings
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))} {model_oppo} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; Infinix {models_inf} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_inf} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36 VivoBrowser/18.9.0.0"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))} {models_re} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u5 = f"Mozilla/5.0 (Linux; U; Android {str(rr(4, 13))}; zh-CN; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_sam} UCBrowser/11.6.4.950 UCBS/2.11.1.20 Mobile Safari/537.36 AliApp(TB/7.0.2) WindVane/8.0.0 1080X1920"
    
    ua = rc([u1, u2, u3, u4, u5])
    ugen.append(ua)
