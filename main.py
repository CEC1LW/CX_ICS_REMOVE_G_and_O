f = open("target.ics")
data = f.read()

events = []
in_event = False
lines = data.split('\n')
for line in lines:
    if line == 'BEGIN:VEVENT':
        event = {}
        in_event = True
        continue
    if line == 'END:VEVENT':
        events.append(event)
        in_event = False
        continue
    if in_event:
        key, val = line.split(':', 1)
        event[key] = val

for event in reversed(events):
    eventSummary = event["SUMMARY"]
    eventDate, eventType = eventSummary.split(" ", 1)
    if eventType == "O " or eventType == "G ":
        events.remove(event)


# for event in events:
#   print(event)

output = "BEGIN:VCALENDAR\n"
for item in events:
    output += "BEGIN:VEVENT\n"
    for key, value in item.items():
        output += f"{key}:{value}\n"
    output += "END:VEVENT\n"
output += "END:VCALENDAR"

with open("output.ics", "w") as file:
    file.write(output)