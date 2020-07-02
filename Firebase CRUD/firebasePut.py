from firebase import firebase

firebase = firebase.FirebaseApplication("", None)
data = {
    "lokacija": "Homolj",
    "id": "15",
    "vrednost": "855"
}

result = firebase.post('merenja', data)


print(result)