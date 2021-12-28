while True: 
 cursor = con.cursor() 
 lineBytes = ser.readline) 
 line = lineBytes.decode('utf-8') 
 data_ayam = line.split("\r')[0][1:] 
 cursor.execute('SELECT kondisi FROM warungmakan WHERE idayam = "!+data_ayam+'"') 
 data db = cursor.fetchone() 
 if data db: 
   if data_db [0] == "IN": 
     print ("Ayam didalam") 
     cursor.execute('UPDATE warungmakan SET kondisi = "OUT" WHERE idayam = "+data_ayam+'"') 
   else: 
     print ("Ayam diluar")
     cursor.execute('UPDATE warungmakan SET kondisi = "IN" WHERE idayam = "!+data_ayam+'"')
   con.commit()
 else: 
   cursor.execute('INSERT INTO warungmakan (idayam, kondisi) VALUES ("! + data_ayam +'", "IN")')
   print ("No in databases")
   con.commit()