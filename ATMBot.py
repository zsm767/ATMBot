import sys

# ATM Bot
# Basic ATM functionality -- assuming that the GUI/Interface for it is handled by others
# REALLY basic functionality, will consist primarily of withdraw function,
# and a basic CLI for it. 

# thinking ahead, within the function itself, the initial block could be made into an initializer func,
# the user input print / loop check could be shrunk down a little, made more readible than just a loop with if/else up the wazoo

# withdrawal in denominations of 20s
def withdrawal( account_balance ):

	print( "Current balance: %f.\n" %account_balance )
	u_input = ''
	valid_options = {'A', 'B', 'C', 'D', 'Exit'}
	withdr_amount = [20.00, 40.00, 60.00, 80.00]
	fee_flag = False
	if( account_balance < 20 ):
		print( "Insufficient funds. $5.00 fee will be charged.\n" )
		fee_flag = True
	
	#user choice: 20/40/60/80 to withdraw out from their account, looping for user error, etc.
	print( "How much would you like to withdraw?\n A) $20.00\n B) $40.00\n C) $60.00\n D) $80.00\n 'Exit' to quit.\n" )
	
		#version checking
	vers = sys.version
	print(vers)
	if (vers < "3.0"):
		print("Currently running an outdated version of python. For potential issues involving changes made with input(), \n")
		print("calling a more outdated version of the functionality...")
		
		while( u_input != 'Exit' ):
			u_input = input( "Select an option: " )
			if( u_input not in valid_options ):
				print( "\nInvalid selection. Try again.\n")
				print( "Current balance: %f.\n" %account_balance )
			else:
				#accounting for extra fee
				if( fee_flag == True ):
					if ( u_input == 'A' ):
						account_balance = account_balance - 25
						print( "Current balance: %f.\n" %account_balance )
					if ( u_input == 'B' ):
						account_balance = account_balance - 45
						print( "Current balance: %f.\n" %account_balance )
					if ( u_input == 'C' ):
						account_balance = account_balance - 65 
						print( "Current balance: %f.\n" %account_balance )
					if ( u_input == 'D' ):
						account_balance = account_balance - 85
						print( "Current balance: %f.\n" %account_balance )
				#without extra fee
				else:
					if ( u_input == 'A' ):
						account_balance = account_balance - 20
						print( "Current balance: %f.\n" %account_balance )
					if ( u_input == 'B' ):
						account_balance = account_balance - 40
						print( "Current balance: %f.\n" %account_balance )
					if ( u_input == 'C' ):
						account_balance = account_balance - 60 
						print( "Current balance: %f.\n" %account_balance )
					if ( u_input == 'D' ):
						account_balance = account_balance - 80
						print( "Current balance: %f.\n" %account_balance )
		
	while( u_input != 'Exit' ):
		u_input = input( "Select an option: " )
		if( u_input not in valid_options ):
			print( "\nInvalid selection. Try again.\n")
			print( "Current balance: %f.\n" %account_balance )
		else:
			#accounting for extra fee
			if( fee_flag == True ):
				if ( u_input == 'A' ):
					account_balance = account_balance - 25
					print( "Current balance: %f.\n" %account_balance )
				if ( u_input == 'B' ):
					account_balance = account_balance - 45
					print( "Current balance: %f.\n" %account_balance )
				if ( u_input == 'C' ):
					account_balance = account_balance - 65 
					print( "Current balance: %f.\n" %account_balance )
				if ( u_input == 'D' ):
					account_balance = account_balance - 85
					print( "Current balance: %f.\n" %account_balance )
			#without extra fee
			else:
				if ( u_input == 'A' ):
					account_balance = account_balance - 20
					print( "Current balance: %f.\n" %account_balance )
				if ( u_input == 'B' ):
					account_balance = account_balance - 40
					print( "Current balance: %f.\n" %account_balance )
				if ( u_input == 'C' ):
					account_balance = account_balance - 60 
					print( "Current balance: %f.\n" %account_balance )
				if ( u_input == 'D' ):
					account_balance = account_balance - 80
					print( "Current balance: %f.\n" %account_balance )
			
	#printing the current balance afterward
	print( "Current balance: %f.\n\n" %account_balance )		
#end withrdawal
	
#---------------------------------------------------------------------#	
	
#some initial stuff (test cases, etc.)
startingBalance = 200

print( "testing...")
withdrawal( startingBalance )
