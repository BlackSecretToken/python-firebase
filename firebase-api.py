import firebase_admin
from firebase_admin import credentials, firestore

# Use the private key JSON file you downloaded
cred = credentials.Certificate('key/chartbot-e623d-firebase-adminsdk-hgz7f-55bb826078.json')
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

def addData(ID, CA, Interval):
    doc_ref = db.collection('setting').document(ID)
    doc_ref.set({
        'CA': CA,
        'Interval': Interval
    })

def getData(ID):
    doc_ref = db.collection('setting').document(ID)
    doc = doc_ref.get()
    if doc.exists:
        return True, doc.to_dict()
    else:
        return False, ''

def updateData(ID, Attr, Value):
    doc_ref = db.collection('setting').document(ID)
    doc_ref.update({
        Attr: Value
    })

def deleteData(ID):
    doc_ref = db.collection('setting').document(ID)
    doc_ref.delete()


if __name__=="__main__":
    # addData('12345678', '0x234678','7D')

    # [exists, data] = getData('1234567')
    # if (exists) :
    #     print('CA:', data['CA'])
    #     print('Interval:', data['Interval'])

    # updateData('1234567', 'CA', '0x23423sdfsdf')

    deleteData('1234567')    