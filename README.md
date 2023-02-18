# Hosec

Hosec is a IoT Project that utilizes opencv for facial recognition and create a additional layer of secuity for its residence.

When connected to Line's Messaging API, the user is able to send messages directly to Line group chat's when recognized / unrecognized faces are captured. It can easily be connected to any number of IP cameras / webcams.

## Installation

###  requirements.txt

- Install required dependencies
```
npm install
```

### dataset/__usernamehere__
- create folder with desired persons name

### headshots.py
- Take around 10-20 photos of face with diverse angles
```
python3 headshots.py __usernamehere__
```

### encode_faces.py
- Allow opencv to encode faces for facial recognition
```
python3 encode_faces.py
```

### headshots.py
- check if camera recognizes face
```
python3 facial_req.py
```

### info.json
- create info.json file in src directory and insert line channel_access_token & user_id
```
{
    "CHANNEL_ACCESS_TOKEN": "TOKEN_HERE",
    "USER_ID": "USER_ID HERE"
}
```