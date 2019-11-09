import ftplib

connect = ftplib.FTP("www.ishyiga.net")
connect.login("ishyiga", "Jkejdjh51463")
data = []
connect.dir(data.append)
connect.quit()
for line in data:
   print(line)
