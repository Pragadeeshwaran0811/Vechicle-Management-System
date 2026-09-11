from src.admin import AdminPannel
from src.customer import CustomerPannel
def main():
    vehicles= {}
    customers = {}
    admin_pannel = AdminPannel(vehicles)
    customer_pannel = CustomerPannel(vehicles,customers)
    print("<>"*10)
    print("welcome to kumar rentals")
    print("<>"*10)

   # while condition 
    while True:
        print("select an option : ")
        print("1,admin panel")
        print("2,customer panel")
        print("3,exit")
        user =input("select the option: ")

        if user =="3":
            print("thank you,visit again")
            break
        elif user =="1":
            print("welcome to admin panel")
            while True:
                print("="*10)
                print("welcome admin")
                print("="*10)
                print("select an option: ")
                print("1.add a new vehicle")
                print("2.see inventory")
                print("3.exit admin panel")
                admin = input("enter  the option: ")

                if admin =="3":
                    print("exiting the admin pannel")
                    break
                elif admin =="2":
                    print("accesing the inventory")
                    admin_pannel.view_inventory()
                elif admin == "1":
                    vehicle_id = input("enter the vehicle id: ")
                    vehicle_type = input("enter the vehicle type: ")
                    vehicle_model = input("enter the vehicle model: ")
                    vehicle_rent = float(input("enter the vehicle rent: "))
                    admin_pannel.add_new_vehicle(
                        vehicle_id,vehicle_type,vehicle_model,vehicle_rent
                        )
                    print("vehicle added successfully")
                else:
                    print("invalid option.select the valid option ")
              
                
        elif user =="2":
            print("you are inside the customer panel")
            while True:
                print("="*10)
                print("welcome to customer pannel")
                print("="*10)
                print("select an option: ")
                print("1.registering for bike")
                print("2.see available bikes")
                print("3.rent a vehicle")
                print("4.return a vechile")
                print("5.exit the customer pannel")
                customer = input("enter  the option: ")

                if customer == "5":
                    print("exiting the cuustomer pannel")
                    break
                elif customer =="1":
                    customer_name = input("enter your name: ")
                    customer_number = int(input("enter you number: "))
                    customer_liscense = input("enter your liscense number: ")
                    customer_pannel.register(customer_name,customer_number,customer_liscense)
                    print("registering the detail of customer")
                elif customer =="2":
                    print(vehicles)
                    customer_pannel.see_available()
                    print("displaying the available vehicles")
                elif customer =="3":
                    customer_id = input("enter the customer id: ")
                    vehicle_id = input("enter the vehicle id: ")
                    customer_pannel.rent_vehicle(customer_id,vehicle_id)
                    print("selecting a bike for rent")
                elif customer =="4":
                    customer_id=input("enter the customer id: ")
                    customer_pannel.return_vehicle(customer_id)
                    print("returning the rented vehicle")
                else:
                    print("invalid option,select an appropriate option")
            
        else:
            print("invalid option.please select valid option")

# for importing
if __name__ == "__main__":
    main()
