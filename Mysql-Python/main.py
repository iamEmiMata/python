
import mysql.connector

class conexion():

	# dbName = input('Enter DbName to consult >>> ')
	def __init__(self):
		try:
			self.conexion = mysql.connector.connect(
				host = '127.0.0.1',
				port = 3306,
				user = 'root',
				password = '',
				db = 'library') # self.dbName

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

run = conexion()

continuar = True
while continuar :
	run.commandLine()

	exit = input('\nEnter to continue. . . To exit 0  >>>  ')
	if exit == '0':
		continuar = False
	else:
		continuar = True

print('Connection is closed')