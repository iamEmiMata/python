
import mysql.connector 

class restore():

	dbName = input('Enter DbName to restore >>> ')
	saveBackup = f'C:\\Users\\marie\\OneDrive\\Escritorio\\backup\\{dbName}__backup.sql'

	def __init__(self):
		try:
			self.conexion = mysql.connector.connect(
				host = '127.0.0.1',
				port = 3306,
				user = 'root',
				password = '')
		except Exception as e:
			print(e)


	def importDb(self):
		try:
			if self.conexion.is_connected():
				cursor = self.conexion.cursor()
				sql = 'show databases'
				cursor.execute(sql)

				fetch = cursor.fetchall()
				dbList = []
				for lista in fetch:
					dbList.append(lista[0])

				if self.dbName in dbList:
					print(f'\nWARNING : {self.dbName} already exists')
					sql = f'use {self.dbName}'
					cursor.execute(sql)

				else: 
					sql = f'create database {self.dbName}'
					cursor.execute(sql)
					self.conexion.commit()
					print(f'{self.dbName} was created')

					sql = f'use {self.dbName}'
					cursor.execute(sql)

					with open(self.saveBackup) as file:
						readFile = file.read().split(';')

					for db in readFile:
						cursor.execute(db)
						print(db)

					print('\n>>> Database was imported successfully')

		except Exception as e:
			print(e)
		finally:
			if self.conexion.is_connected():
				self.conexion.close()


run = restore()
run.importDb()