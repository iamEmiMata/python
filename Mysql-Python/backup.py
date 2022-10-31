
import mysql.connector
import os

class backup():
	
	dbName = input('Enter DbName to consult >>> ')
	def __init__(self):
		try:
			self.conexion = mysql.connector.connect(
				host = '127.0.0.1',
				port = 3306,
				user = 'root',
				password = '',
				db = self.dbName) # self.dbName

			# validamos
			if self.conexion.is_connected():
				dbInfo = self.conexion.get_server_info()
				print('Connection is working... ', dbInfo)
		except Exception as e:
			print('Connection has failed... ', e)


	def saveDb(self):

		try:
			if self.conexion.is_connected():
				cursor = self.conexion.cursor()
				sql = 'show tables'
				cursor.execute(sql)

				# array to add tables
				dbTables = []
				for tables in cursor.fetchall():
					dbTables.append(tables[0])

				file = f'{self.dbName}__backup' # date : 22 / 10 / 22 
				try:
					#  crea base de datos respaldo
					sql = f'create database {file}'
					cursor.execute(sql)
					self.conexion.commit()

					print(f'Backup > database {file}__backup,  was create ')

				except Exception as e:
					print(e)

				# usa la base de datos que has creado
				sql = f'use {file}'
				cursor.execute(sql)

				for lista in dbTables:
					sql = f'create table {lista} select * from {self.dbName}.{lista}'
					cursor.execute(sql)
					self.conexion.commit()

					print(f'{lista} was attached correctly')

		except Exception as e:
			print(e)
		finally:
			if self.conexion.is_connected():
				cursor.close()


	def saveBackup(self):
		if self.conexion.is_connected():
			try:
				# Direccion de la carpeta en donde guardaremos el respaldo
				saveBackup = f'C:\\Users\\Escritorio\\backup\\{self.dbName}__backup.sql'
				# path > direccion en donde esta mysqldump.exe
				path = 'C:\\xampp\\mysql\\bin\\mysqldump.exe'
				# popen is a method()
				os.popen(path + " -u " + "root" + " " + self.dbName + " > " + saveBackup)

				print(f'\n{self.dbName}__backup.sql, was save correctly')

			except Exception as e:
				print(e)

run = backup()
run.saveDb()
run.saveBackup()
