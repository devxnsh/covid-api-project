import querywriter

# UserCity=input("Enter Name of City") --Can be updated in next version with proper database of district code to city name
UserDistrictCode=input("Enter District Code: ")
UserAge=int(input("Enter your Age: "))
UserDate=input("Enter Date to search: (in DD-MM-YYYY format) ")
UserVaccinated=input("Have you been Vaccinated before? ")

querywriter.show_data(distcode=UserDistrictCode,age=UserAge,dose=UserVaccinated,date=UserDate)