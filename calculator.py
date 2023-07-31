import json
from garmin_fit_sdk import Decoder, Stream
from typing import Union

def decodeFITData(filename):
    stream = Stream.from_file(filename)
    decoder = Decoder(stream)
    messages, errors = decoder.read()

    print(messages)
    with open("Parkrun.json", "w") as f:
        json.dump(messages, f, indent=4, default=str) # json.loads is the reverse

def calculateTimingMetrics(dist_miles: Union[int, float, None] = None, dist_kms: Union[int, float, None] = None, dist_ms: Union[int, float, None] = None, time_hours: Union[float, None] = None, time_mins: Union[float, None] = None, time_secs: Union[float, None] = None):
    
    if dist_kms is None and dist_miles is None and dist_ms is None:
        raise ValueError('You must specify a distance.')
    
    if time_hours is None and time_mins is None and time_secs is None:
        raise ValueError('You must specify a time.')
    
    if dist_kms is not None:
        dist_ms = dist_kms * 1000
    elif dist_miles is not None:
        dist_ms = dist_miles * 1609.344

    if time_hours is not None:
        time_secs = time_hours * 60 * 60
    elif time_mins is not None:
        time_secs = time_mins * 60
    
    mps = dist_ms / time_secs
    mpk = (time_secs * 60) / (dist_ms * 1000)
    kph = (dist_ms * 1000) / (time_secs * 60 * 60) 
    mpm = (time_secs * 60) / (dist_ms * 1609.344)
    mph = (dist_ms * 1609.344) / (time_secs * 60 * 60) 

    
    
    # meters/sec,       mins/km,      km/hr,      mins/mile,  miles/hr
    return {'mps': mps, 'mpk': mpk, 'kph': kph, 'mpm': mpm, 'mph': mph}

print(calculateTimingMetrics(dist_ms=4955.32, time_secs=1678.451))
# decodeFITData("Parkrun.fit")
# speed is in m/s




