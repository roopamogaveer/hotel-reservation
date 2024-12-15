# User Module:
### User Registration : POST - http://127.0.0.1:8000/user/signup/
body :</br>
         { </br>
           "username" : "roopa",</br>
           "email" : "roopa@gmail.com",</br>
           "password" : "123123123"</br>
         }
    
### User Login : POST - http://127.0.0.1:8000/user/login/

body :  </br>
        { </br>
           "email" : "roopa@gmail.com",</br>
           "password" : "123123123"</br>
        }
   
# Reservation Module:
### Hotel Reservation : POST - http://127.0.0.1:8000/reservation/reserve/ 
body : </br>
        {</br>
           "user":1,</br>
           "hotelname":"idbHotels",</br>
           "checkin":"2024-12-20T14:00:00Z",</br>
           "checkout":"2024-12-21T10:00:00Z",</br>
           "nopersons" : 4</br>
        }
### All Reservation : GET - http://127.0.0.1:8000/reservation/allreservation/

### Reservation By UserId : GET - http://127.0.0.1:8000/reservation/allreservation/1/

### Reservation By UserId and BookingId : GET - http://127.0.0.1:8000/reservation/allreservation/1/1
