# User Module:
### User Registration : POST - http://127.0.0.1:8000/user/signup/
body :
         {
         "username" : "roopa",
         "email" : "roopa@gmail.com",
         "password" : "123123123"
         }
    
### User Login : POST - http://127.0.0.1:8000/user/login/

body :
        {
            "email" : "roopa@gmail.com",
            "password" : "123123123"
        }
   
# Reservation Module:
### Hotel Reservation : POST - http://127.0.0.1:8000/reservation/reserve/ 
body : 
        {
            "user":1,
            "hotelname":"idbHotels",
            "checkin":"2024-12-20T14:00:00Z",
            "checkout":"2024-12-21T10:00:00Z",
            "nopersons" : 4
        }
### All Reservation : GET - http://127.0.0.1:8000/reservation/allreservation/

### Reservation By UserId : GET - http://127.0.0.1:8000/reservation/allreservation/1/

### Reservation By UserId and BookingId : GET - http://127.0.0.1:8000/reservation/allreservation/1/1
