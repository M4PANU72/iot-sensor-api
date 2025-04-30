#bronnen
# https://canvas.kdg.be/courses/49875/pages/wekcollge-zelf-een-api-aanmaken?module_item_id=1139858
# https://canvas.kdg.be/courses/49875/assignments/221530?module_item_id=1139859
# https://fastapi.tiangolo.com/


from fastapi import FastAPI

# Maak een nieuwe FastAPI-applicatie
app = FastAPI()

# Root route om te controleren of de API werkt
@app.get("/")
def root():
    return {"message": "Welkom bij de Sensor-API!"}




# Route om alle taken op te halen
@app.get("/sensors")
def get_sensors():
    return sensors

@app.get("/sensors/{sensor_id}")
def get_sensor(sensor_id: int):
    # Zoek de sensor met het gegeven ID
    for t in sensors:
        if t["id"] == sensor_id:
            return t
    # Geef een bericht als de sensor niet gevonden is
    return {"message": "sensor niet gevonden"}


@app.get("/sensors/status/{status}")
def get_sensorstatus(sensor_status: str):
# Verzamel alle sensoren met de opgegeven status
    matching_sensors = [t for t in sensors if t["status"] == sensor_status]
    
    # Controleer of er sensoren zijn gevonden
    if matching_sensors:
        return matching_sensors
    
    # Geef een bericht als er geen sensoren zijn gevonden
    return {"message": "Geen sensoren gevonden met de opgegeven status"}


@app.post("/sensors")
def create_sensor(input: dict):
    # Maak een nieuwe sensor met een uniek ID
    new_sensor = {
        "id": len(sensors) + 1,
        "sensor": input["sensor"],
        "location": input["location"],
        "status": "Inactive",
    }
    # Voeg de nieuwe sensor toe aan de lijst
    sensors.append(new_sensor)
    return new_sensor


# Route om een sensor als actief te markeren

@app.put("/sensors/activate/{sensor_id}")
def update_sensor(sensor_id: int):
    for t in sensors:
        if t["id"] == sensor_id:
            t["status"] = "Active"
            return t
    return {"message": "sensor niet gevonden"}

# Route om een sensor als inactief te markeren
@app.put("/sensors/deactivate/{sensor_id}")
def update_sensor(sensor_id: int):
    for t in sensors:
        if t["id"] == sensor_id:
            t["status"] = "Inactive"
            return t
    return {"message": "sensor niet gevonden"}


# Route om een sensor te verwijderen
@app.delete("/sensors/{sensor_id}")
def delete_sensor(sensor_id: int):
    global sensors
    new_sensors = []
    for t in sensors:
        if t["id"] != sensor_id:
            new_sensors.append(t)
    sensors = new_sensors
    return {"message": "sensor verwijderd"}