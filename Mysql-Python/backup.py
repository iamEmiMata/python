
import mysql.connector
from datetime import datetime
import os

class conexion():

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
		# finally:
		# 	# Cerramos conexion
		# 	if self.conexion.is_connected():
		# 		self.conexion.close()
		# 		print('Connection is closed')

	def backUp(self):
		try:
			if self.conexion.is_connected():
				cursor = self.conexion.cursor()
				# Sql commands
				sqlCommands = 'show tables'
				cursor.execute(sqlCommands)

				# array Tables in DB used
				dbTables = []
				for record in cursor.fetchall():
					# add tables from array here
					dbTables.append(record[0])

				backupName = f'{self.dbName}_Backup'
				try:
					# create a new db and use backupname as name
					sql = f'create database {backupName}'
					cursor.execute(sql)

					print(f'>>> {backupName} was successfully create!\n')
				except:
					passs

				# use current db you create
				sql = f'use {backupName}'
				cursor.execute(sql)
				# count row you added in dbTables and use it in
				for  tableName in dbTables:
					# use here... create tables with that array
					sql = f'create table {tableName} select * from {self.dbName}.{tableName}'
					cursor.execute(sql)
					# Prompt
					print(f'{self.dbName}.{tableName} \n>>> attached table successfully')
		except:
			pass
		finally:
			cursor.close()

	def saveBackup(self):
		if self.conexion.is_connected():
			try:
				# save file in local C:
				currentDate = datetime.today().strftime('%Y_%m_%d_%H_%M')# day, month, year, hour, min
				saveBackup = f'C:\\Users\\marie\\OneDrive\\Escritorio\\backup\\{self.dbName}_backup_{currentDate}.sql'
				path = 'C:\\xampp\\mysql\\bin\\mysqldump.exe'
				os.popen(path + " -u " + "root" + " " + self.dbName + " > " + saveBackup)

				print(f'\n>>> File {self.dbName}_backup_{currentDate}.sql\n\
>>> Backup completed successfully')
			except Exception as e:
				print(e)

run = conexion()
run.backUp()
run.saveBackup()