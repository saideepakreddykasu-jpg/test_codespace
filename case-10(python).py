Python 3.13.17 (tags/v3.13.17:64e080d, Oct 21 2026, 14:08:53) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
venue = 20000
equipment = 10000
... catering_per_person = 250
... transport_per_person = 100
... certificate_per_person = 50
... planned_participants = 100
... sponsorship = 15000
... registration_fee = 500
... 
... fixed_cost = venue + equipment
... variable_per_person = catering_per_person + transport_per_person + certificate_per_person
... total_cost = fixed_cost + variable_per_person * planned_participants
... shortfall = max(0, total_cost - sponsorship)
... 
... # Minimum participants whose registration fees cover costs after sponsorship
... break_even_count = (fixed_cost - sponsorship + registration_fee - 1) // registration_fee
... break_even_count = max(0, break_even_count)
... 
... participant_contribution = planned_participants * registration_fee
... remaining_shortfall = max(0, total_cost - sponsorship - participant_contribution)
... 
... print(f"Total event cost: Rs.{total_cost:.2f}")
... print(f"Sponsorship: Rs.{sponsorship:.2f}")
... print(f"Funding shortfall before registrations: Rs.{shortfall:.2f}")
... print(f"Participant contributions: Rs.{participant_contribution:.2f}")
... print(f"Remaining shortfall: Rs.{remaining_shortfall:.2f}")
