
import mysql.connector
from datetime import datetime
import os

class conexion():

	# dbName = input('Enter DbName to consult >>> ')
	dbName = 'library'
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

	def commandLine(self):
		try:
			if self.conexion.is_connected():
				cursor = self.conexion.cursor()
				# Sql commands
				print('Command Line is active')
				sqlCommands = input('>>> ')
				commandIndex = sqlCommands.split() # ['show','tables'] 
				cursor.execute(sqlCommands)

				# If fetch : Lista resultados else commit()
				if commandIndex[0] == 'show' or commandIndex[0] == 'select' or commandIndex[0] == 'describe' :
					fetch = cursor.fetchall()
					if fetch == []:
						print(cursor.rowcount, ' rows found ')

					for results in fetch:
						print(results)
				else: 
					try:
						self.conexion.commit()
						print('>>> Commit ', cursor.rowcount+1, ' affected ')
					except Exception as e:
						print(e)

		except:
			self.conexion.rollback()
		finally:
			cursor.close()

	def backup(self):
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

# exit
run = conexion()

continuar = True
while continuar :
	# choose an option to start
	print('\n1. Command Line\n2. Backup')
	op = input('>>>  ')
	if op == '1':
		run.commandLine()
	elif op == '2':
		run.backup()
		run.saveBackup()
	else: 
		print('\nERR : Option you entered does not exist')
		op = input('>>>  ')

	# option to finish
	exit = input('\nEnter to continue. . . To exit 0  >>>  ')
	if exit == '0':
		continuar = False
	else:
		continuar = True

print('Connection is closed')