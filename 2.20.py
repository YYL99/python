from urllib import request
import re

#https://user.qzone.qq.com/1462007458/infocenter
'''
cookie: welcomeflash=1462007458_77031; \
1462007458_totalcount=14329; 1462007458_todaycount=0; \
x-stgw-ssl-info=a1ed66158afd7dcc8773992c9ac2cbda|0.227|1589768908.476|1|.\
|Y|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|52500|h2|0; RK=exAQ5m3mf/; ptcz\
=742ceb627d1082695ebf61a82a68909e65293f2b4d28ff4531eefe21ac7f80a1; \
pgv_pvid=5986277190; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; pgv_pvi=\
9436036096; __Q_w_s_hat_seed=1; ptui_loginuin=937534704; uin=o1462007458; \
p_uin=o1462007458; Loading=Yes; pgv_info=ssid=s6813133944; _qpsvr_localtk=\
0.6762845749007409; pgv_si=s9478807552; skey=@lyuNYtEU6; pt4_token=AEx1Kwo5\
qvR546G6PBGQII6QrUv2bzuWBr*h-ajy6Qk_; p_skey=F6G0YT95MxB3HUAFpOXWfo4dZWrw0it\
vOpuR5Td8wpo_; cpu_performance_v8=7
'''
url = "https://user.qzone.qq.com/1462007458/infocenter"
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
	"Cookie": "welcomeflash=1462007458_77031; \
	1462007458_totalcount=14329; 1462007458_todaycount=0; \
	x-stgw-ssl-info=a1ed66158afd7dcc8773992c9ac2cbda|0.227|1589768908.476|1|.\
	|Y|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|52500|h2|0; RK=exAQ5m3mf/; ptcz\
	=742ceb627d1082695ebf61a82a68909e65293f2b4d28ff4531eefe21ac7f80a1; \
	pgv_pvid=5986277190; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; pgv_pvi=\
	9436036096; __Q_w_s_hat_seed=1; ptui_loginuin=937534704; uin=o1462007458; \
	p_uin=o1462007458; Loading=Yes; pgv_info=ssid=s6813133944; _qpsvr_localtk=\
	0.6762845749007409; pgv_si=s9478807552; skey=@lyuNYtEU6; pt4_token=AEx1Kwo5\
	qvR546G6PBGQII6QrUv2bzuWBr*h-ajy6Qk_; p_skey=F6G0YT95MxB3HUAFpOXWfo4dZWrw0it\
	vOpuR5Td8wpo_; cpu_performance_v8=7"
}
req = request.Request(url, headers=headers)
res = request.urlopen(req).read().decode()
t = r'>(.*?)</span>'
d = re.findall(t, res)
print(d)