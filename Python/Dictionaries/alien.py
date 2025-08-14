#name={'key':'value'}
#access value->print(name['key])->returns value associated with that key
alien_0={'color':'green','points':5 }
print(alien_0['color'])
print(alien_0['points'])

'''new_points=alien_0['points']
print(f"You just earned {new_points} points")'''

#adding more key value pairs to the dictionary
alien_0['x_pos']=0
alien_0['y_pos']=25
print(alien_0)

#modifying dictionry values
alien_0['color']='red'
print(alien_0)
