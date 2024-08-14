#LU RECODE JANGAN APUS NAMA AUTHOR LAH ANJENG LAMMER NOOB
#USE PYTHON 3 ANJENG YA
try:
	import requests as r, os, sys, json, re
	from concurrent.futures import ThreadPoolExecutor as pol
except Exception as e:
	exit("[>] Error: "+str(e)+"\n")

clear = lambda: os.system("clear") if "linux" in sys.platform.lower() else os.system("cls")
header = lambda: {"user-agent": "chrome", "User-Agent": "chrome"}

def writer(name, content):
	try:
		if content.strip() in open(name, "r").read():
			pass
		else:
			open(name, "a+").write(content.strip().replace("\n","")+"\n")
	except FileNotFoundError:
		open(name, "a+").write(content.strip().replace("\n","")+"\n")

def SingleTarget():
	tnya = input("> Ingin massal/single? [M/S]: ")
	while tnya not in list("MmSs"):
		print("*> Pilihan tidak tersedia..")
		tnya = input("> Ingin massal/single? [M/S]: ")
	if tnya in list("Mm"):
		while True:
			file = input("> Masukan file: ")
			try:
				cek = open(file,"r").read().strip().split("\n")
				break
			except:
				print("*> File tidak ditemukan")
		return cek
	else:
		trget = input("> Target site/hostname: ")
		while trget == "":
			trget = input("> Target site/hostname: ")
		return trget.split()

def subScan(url):
	global header
	regs = re.findall(r"(?:(?:https?://)?(?:www\d?\.)?|www\d?\.)?([^\s/]+)", url)[0]
	cek = r.get("https://rapiddns.io/subdomain/"+regs+"?full=1#result", headers=header()).text
	fetch = re.findall("</th>\n<td>(.*?)</td>", str(cek))
	if len(fetch) == 0:
		print("  -> : Subdomain tidak terdeteksi")
	else:
		for x in fetch:
			writer("res_subdo.txt", x)
		print("  -> : "+str(len(fetch))+" subdomain terdeteksi")

def main():
	clear()
	print("""
	    [ SUBDOMAIN SCANNER ]
	    Author : IronHeary_X12 | Mr.Crifty \n\n""")
	ask = SingleTarget()
	print("")
	with pol(max_workers=10) as sub:
		for x in ask:
			sub.submit(subScan, x)
	print("\n! Done.. save: res_subdo.txt\n")


if __name__=="__main__":
	main()
