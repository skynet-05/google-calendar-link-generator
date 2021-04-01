import optparse
import re
from discord_webhook import DiscordWebhook
from datetime import datetime

URL = "https://www.google.com/calendar/render?action=TEMPLATE&text="

def urlify(s):
    s = re.sub(r",+", '%2C', s)
    s = re.sub(r"[^[0-9a-zA-Z\s%]", '', s)
    s = re.sub(r"\s+", '+', s)
    return s

parser = optparse.OptionParser()
parser.set_defaults(verbose=False)
parser.add_option("-n", "--name", dest="name", help="Event name (Required)")
parser.add_option("-l", "--location", dest="location", help="Where is the event taking place")
parser.add_option("-d", "--details", dest="details", help="Extra details about the event")
parser.add_option("-D", "--start-date", dest="start_date", help="When does the event start in the format YYYYMMDD (Required)")
parser.add_option("-s", "--start-time", dest="start_time", help="What time does the event start in the format HH:MM (Required)")
parser.add_option("-E", "--end-date", dest="end_date", help="When does the event end in the format YYYYMMDD (Required)")
parser.add_option("-e", "--end-time", dest="end_time", help="What time does the event end in the format HH:MM (Required)")
parser.add_option("-c", "--discord", action="store_true",dest="verbose", help="Do you want to send this link to discord")

(options, arguments) = parser.parse_args()

name = urlify(options.name)
location = urlify(str(options.location))
details = urlify(str(options.details))
start_date = options.start_date
start_time = urlify(options.start_time)
end_date = options.end_date
end_time = urlify(options.end_time)
location=location.replace("None",'')
details=details.replace("None",'')

urlt = URL + name + "&details=" + details + "&location=" + location + "&dates=" + start_date + "T" + start_time + "%2F" + end_date + "T" + end_time
print(urlt)

if options.verbose is True:
    try:
        webhook = DiscordWebhook(url='PUT YOUR DISCORD WEBHOOK URL HERE', content=urlt)
        response = webhook.execute()
        print("Message sent to Discord")
    except:
        print("Discord Webhook URL Not Found!")
