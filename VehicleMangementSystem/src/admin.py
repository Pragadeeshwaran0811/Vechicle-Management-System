vehicles = {}
class AdminPannel:
    def __init__(self,vehicles):
        self.vehicles = vehicles
        
    def add_new_vehicle(self,id,type,model,rent):
        self.vehicles [id] = {
            "vehicle_id":id,
            "vehicle_rent":rent,
            "vehicle_type":type,
            "vehicle_model":model,
            "available" : True
        }

    def view_inventory(self):
        for key, value in self.vehicles.items():
            print(f'{key}:type:{value["vehicle_type"]} model:{value["vehicle_model"]} rent:{value["vehicle_rent"]}')

    def save_vehicles(self):
        with open("vehicles_details.txt","w")as file:
            file.write(str(self.vehicles))





if __name__ == "__main__":
    vehicles ={}
    admin = AdminPannel(vehicles)
    admin.add_new_vehicle("ct5250","Bike","classic","1000")
    admin.add_new_vehicle("ak5500","car","swift","2000")
    admin.view_inventory()
    admin.save_vehicles()
    print(vehicles)





