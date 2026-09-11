customers = {}
vehicles = {}
class CustomerPannel:
    def __init__(self,vehicles,customers):
        self.vehicles = vehicles
        self.customers = customers
    def register(self,name,number,liscence):
        self.customers[name]={"customer_name": name,
                             "customer_number": number,
                             "customer_liscence": liscence,
                             "rented_status": None
                            }
        print(f"customer : {name},{number} is added successfully")
    def see_available(self):
        for key, value in self.vehicles.items():
            if value["available"]:
                print(f"{key}:type:{value["vehicle_type"]} model:{value["vehicle_model"]} rent:{value["vehicle_rent"]}")
    def rent_vehicle(self,customer_id,vehicle_id):
        if customer_id not in self.customers:
            print("please register first")
        elif not self.vehicles[vehicle_id]["available"]:
            print("that vehicle is rented, please select another vehicle")
        else:
            self.customers[customer_id]["rented_status"] = vehicle_id
            self.vehicles[vehicle_id]["available"] = False
            print(f"customer : {customer_id} rented {vehicle_id}")
    def return_vehicle(self,customer_id):
        if customer_id not in self.customers:
            print("you are not registered")
        elif self.customers[customer_id]["rented_status"] is None :
            print("customer did not rent a vehicle")
        else:
            vehicle_id = self.customers[customer_id]["rented_status"]

            self.customers[customer_id]["rented_status"] = None
            self.vehicles[vehicle_id]["available"] = True

            print(f"customer {customer_id} returned {vehicle_id}")
        
    

if __name__ == "__main__":

    customers ={}
    vehicles ={}
    raju = CustomerPannel(vehicles,customers)
    raju.register("raju",8862307246,"c4664")
    print(customers)
