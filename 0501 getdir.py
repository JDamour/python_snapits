import ftplib

connect = ftplib.FTP("www.ioy.net")
connect.login("ioy", "oi")
data = []
connect.dir(data.append)
connect.quit()
for line in data:
   print(line)
