from homeassistant_api import Client
# import time

with Client(
    'http://192.168.8.148:8123/api',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIyZTZjZmIxMmJlZGY0ODJjOWZkZmRiNDc5NzkxODEzMiIsImlhdCI6MTY5MDgxNTYzOCwiZXhwIjoyMDA2MTc1NjM4fQ.iLLFzvxut7_WJhPIaLZGFLoQObX1F4gGgLcAEM1cU3s'
) as client:
    
    light = client.get_domain("light")
    light.turn_off(entity_id="light.lightbulb")
    light.turn_off(entity_id="light.lightbulb_2")
    # light.turn_on(entity_id="light.lightbulb", rgb_color=[100, 10, 20])
    # time.sleep(1)
    # light.turn_on(entity_id="light.lightbulb_2", rgb_color=[120, 80, 20])
