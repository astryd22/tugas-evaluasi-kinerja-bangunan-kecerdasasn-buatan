class BuildingPerformance:
    def __init__(self, energy_consumption, building_area, indoor_temp, co2_level, humidity):
        self.energy_consumption = energy_consumption  # kWh per bulan
        self.building_area = building_area  # m²
        self.indoor_temp = indoor_temp  # °C
        self.co2_level = co2_level  # ppm
        self.humidity = humidity  # %

    def evaluate_energy_efficiency(self):
        energy_per_m2 = self.energy_consumption / self.building_area
        if energy_per_m2 < 10:
            return "Efisiensi Energi: Baik"
        elif energy_per_m2 < 20:
            return "Efisiensi Energi: Sedang"
        else:
            return "Efisiensi Energi: Buruk"

    def evaluate_thermal_comfort(self):
        if 22 <= self.indoor_temp <= 26:
            return "Kenyamanan Termal: Nyaman"
        elif 20 <= self.indoor_temp < 22 or 26 < self.indoor_temp <= 28:
            return "Kenyamanan Termal: Sedang"
        else:
            return "Kenyamanan Termal: Tidak Nyaman"

    def evaluate_air_quality(self):
        if self.co2_level < 600 and 30 <= self.humidity <= 60:
            return "Kualitas Udara: Baik"
        elif self.co2_level < 1000 and 20 <= self.humidity <= 70:
            return "Kualitas Udara: Sedang"
        else:
            return "Kualitas Udara: Buruk"

    def evaluate_building_performance(self):
        return {
            "Energy Efficiency": self.evaluate_energy_efficiency(),
            "Thermal Comfort": self.evaluate_thermal_comfort(),
            "Indoor Air Quality": self.evaluate_air_quality()
        }

# Contoh Penggunaan
building = BuildingPerformance(energy_consumption=1200, building_area=100, indoor_temp=30, co2_level=500, humidity=50)
performance = building.evaluate_building_performance()

for aspect, result in performance.items():
    print(f"{aspect}: {result}")
