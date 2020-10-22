#calculate wait times based off the data that jetblue provides
#for demo purposes we tested information from postman
def jet_blue_lines(num_flights, flight_occupancy, kiosk_check_in, luggage_check_in, tsa, non_luggage):
   luggage_wait_line = kiosk_check_in - luggage_check_in
   luggage_wait_time = luggage_wait_line / 4

   tsa_line = (luggage_check_in + non_luggage) - tsa
   tsa_line_time = (tsa_line * 5)/3
   total_wait = tsa_line_time + luggage_wait_time
   people_before_u = luggage_wait_line + tsa_line
   more_people = flight_occupancy - kiosk_check_in
   dictionary = {"Jet_Blue_Luggage_Time_Minutes" : luggage_wait_time,"TSA_Time_Minutes" : tsa_line_time,"Total_Wait_Time_Minutes" : total_wait,"Number_Of_People_Before_You_On_Line" : people_before_u, "Number_Of_People_Expected_To_Arrive" : more_people};
   return dictionary

   

   

   

   

    

    
