from firebase import firebase

firebase = firebase.FirebaseApplication("", None)
result = firebase.get('merenja','')
print(result)