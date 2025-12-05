from part_2.project.clients.business_client import BusinessClient
from part_2.project.clients.regular_client import RegularClient
from part_2.project.clients.base_client import BaseClient
from part_2.project.plants.base_plant import BasePlant
from part_2.project.plants.flower import Flower
from part_2.project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    VALID_PLANT_TYPES = Flower, LeafPlant
    VALID_CLIENT_TYPES = BusinessClient, RegularClient

    def __init__(self):
        self.income: float = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str) -> str:
        plant_class = next((p for p in self.VALID_PLANT_TYPES if p.__name__ == plant_type), None)

        if plant_class is None:
            raise ValueError("Unknown plant type!")

        plant = plant_class(plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str) -> str:
        client_class = next((c for c in self.VALID_CLIENT_TYPES if c.__name__ == client_type), None)

        if client_class is None:
            raise ValueError("Unknown client type!")

        if any(c.phone_number == client_phone_number for c in self.clients):
            raise ValueError("This phone number has been used!")

        client = client_class(client_name, client_phone_number)
        self.clients.append(client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int) -> str:
        client = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        plant = [p for p in self.plants if p.name == plant_name]
        if client is None:
            raise ValueError("Client not found!")

        if not plant:
            raise ValueError("Plants not found!")

        if len(plant) < plant_quantity:
            return "Not enough plant quantity."

        order_amount = 0
        for index in range(plant_quantity):
            current_plant = plant[index]
            self.plants.remove(current_plant)
            current_discount = client.discount / 100
            order_amount += (current_plant.price - current_plant.price * current_discount)

        self.income += order_amount
        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self, plant_name: str) -> str:
        plant = [p for p in self.plants if p.name == plant_name]
        if not plant:
            return "No such plant name."

        self.plants.remove(plant[0])
        return f"Removed {plant[0].plant_details()}"

    def remove_clients(self) -> str:
        clients_without_orders = [c for c in self.clients if c.total_orders == 0]
        for index in range(len(clients_without_orders)):
            self.clients.remove(clients_without_orders[index])

        return f"{len(clients_without_orders)} client/s removed."

    def shop_report(self):
        result = []
        flowers_count = {}
        for flower in self.plants:
            flowers_count[flower.name] = len([p for p in self.plants if p.name == flower.name])
        sorted_flowers = sorted(flowers_count.items(), key=lambda kvp: (-kvp[1], kvp[0]))
        sorted_clients = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))

        all_orders = sum([c.total_orders for c in self.clients])
        result.append(f"~Flower Shop Report~\nIncome: {self.income:.2f}")
        result.append(f"Count of orders: {all_orders}")
        result.append(f"~~Unsold plants: {len(self.plants)}~~")
        for plant_name, plant_count in sorted_flowers:
            result.append(f"{plant_name}: {plant_count}")
        result.append(f"~~Clients number: {len(self.clients)}~~")
        for client in sorted_clients:
            result.append(client.client_details())

        return '\n'.join(result)



