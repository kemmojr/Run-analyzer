import json
from garmin_fit_sdk import Decoder, Stream

stream = Stream.from_file("Parkrun.fit")
decoder = Decoder(stream)
messages, errors = decoder.read()

print(messages)
with open("Parkrun.json", "w") as f:
    json.dump(messages, f, indent=4, default=str) # json.loads is the reverse

# speed is in m/s