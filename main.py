from pedestrianCrossing import PedestrianCrossing
from TrafficLightController import Light
from vehicle import VehicleDetectionHandler

if __name__ == "__main__":
    crossing = PedestrianCrossing()
    crossing.run()

    traffic_light = TrafficLightController()
    traffic_light.control_traffic_lights()

    vehicle_handler = VehicleDetectionHandler()
    # Call methods or perform actions related to the vehicle detection handler
    # For example:
    # vehicle_handler.detect_vehicle()
    # vehicle_handler.perform_actions()
