import random

ugen = []

for agents in range(10000):
    rr = random.randint
    rc = random.choice
    a_m=rc(['11','13','6.0.1','6.0','7.0','14','12','9'])
    m_m=rc(['MEIZU 17 Pro','V1930A','MEIZU 18 Pro','MEIZU 16Xs','MEIZU 17 Pro','ZTE A2121E','MZ-Infinix X663D','MZ-MEIZU 20 Pro','MX6','Meizu 6T','Infinix X6821','Infinix X687'])
    b_m=rc(['MRA58K','P50-EEA','UKQ1.230917.001','TKQ1.221114.001','NRD90M','SP1A.210812.016','PKQ1.190616.001'])
    c_m=f"{str(rr(42,123))}.0.{str(rr(3200,6500))}.{str(rr(11,199))}"
    f_m=f"{str(rr(100,460))}.0.0.{str(rr(11,99))}.{str(rr(11,360))}"
    a_o=rc(['13','14'])
    m_o=rc(['CPH2219','CPH2207','CPH2099','RMX2189','CPH2499','CPH2337','RMX3261','vivo 1902','RMX2155','LM-G900'])
    b_o=rc(['SP1A.210812.016','UKQ1.230924.001','TP1A.220905.001','UP1A.230620.001'])
    c_o=f"{str(rr(120,123))}.0.{str(rr(6000,6500))}.{str(rr(11,150))}"
    c_h=f"{str(rr(100,122))}.0.{str(rr(6000,6500))}.{str(rr(62,240))}"
    a_w=rc(['5.1.1','12','7.1.1','9','8.1.0'])
    m_w=rc(['V1990A','RMX2155','M2007J1SC','SM-T220','V2131','MOTO G STYLUS 5G','Lenovo TB-X606X','MOTO E20'])
    b_w=rc(['SP1A.210812.016','P00610','O11019','LMY47V','QP1A.190711.020','NMF26F'])
    c_w=f"{str(rr(62,123))}.0.{str(rr(2500,6500))}.{str(rr(20,150))}"
    u1=f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {m_m} Build/{b_m}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c_m} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{f_m};]"
    u2=f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {m_o} Build/{b_o}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c_o} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{f_m};]"
    aV=str(random.choice(range(10,20)))
    u4=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,10)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(111,661)))}.0 Safari/534.{aV}"
    u3=f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {m_w} Build/{b_w}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c_w} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{f_m};]"
    ua=rc([u1,u2,u3,u4])
    ugen.append(ua)
