from urllib import request
from ipware import get_client_ip
import httpagentparser
import geoip2.database
from .models import UserData, UserUrlData, UserDataSeen
import socket
import getpass




def urlfunction(url, data):
    save_user_url_visited = UserUrlData(
        userdata = data,
        url = url
    )
    save_user_url_visited.save()

def useros(request):
    agent = request.META["HTTP_USER_AGENT"]
    os = httpagentparser.detect(agent)["os"]
    return os["name"]


def usersysteminfo(request):
    user_agent = request.user_agent
    browser = user_agent.browser.family + " " + user_agent.browser.version_string
    return  browser


def getlication(ip, url, request):
    try:
        device = ""
        user_agent = request.user_agent
        if user_agent.is_mobile == True:
            device = "Mobile"
        elif user_agent.is_tablet == True:
            device = "Tablet"
        elif user_agent.is_touch_capable == True:
            device = "Touch Capable"
        elif user_agent.is_pc == True:
            device = "PC"
        else:
            device = "Bot"

        browser = user_agent.browser.family + " " + user_agent.browser.version_string
        operating_system = user_agent.os.family + " " + user_agent.os.version_string
        with geoip2.database.Reader('/home/zamaniramin/personalwebiste/home/geoip/data/GeoLite2-City.mmdb') as reader:
            response = reader.city(ip)
            if len(UserData.objects.filter(ip = ip, device = device, browser = browser, operating_system = operating_system)) == 1:
                update_data = UserData.objects.get(ip = ip, device = device, browser = browser, operating_system = operating_system)
                update_seen = UserDataSeen.objects.get(userdata = update_data)
                update_data.city = response.city.name
                update_data.state = response.subdivisions.most_specific.name
                update_data.iso_code = response.subdivisions.most_specific.iso_code
                update_data.country = response.country.name
                update_data.postalcode = response.postal.code
                update_data.latitude = response.location.latitude
                update_data.longitude = response.location.longitude
                update_data.traits_network = response.traits.network
                update_data.operating_system = operating_system
                update_data.browser = browser
                update_data.device_family = user_agent.device.family
                update_data.host_name = socket.gethostname()
                update_data.device = device
                update_data.user_name = getpass.getuser()
                update_data.save()
                update_seen.seen = False
                update_seen.save()
                urlfunction(url, update_data)
            else:
                save_data = UserData(
                    city = response.city.name,
                    state = response.subdivisions.most_specific.name,
                    iso_code = response.subdivisions.most_specific.iso_code,
                    country = response.country.name,
                    postalcode = response.postal.code,
                    latitude = response.location.latitude,
                    longitude = response.location.longitude,
                    host_name = socket.gethostname(),
                    user_name = getpass.getuser(),
                    ip = ip, 
                    traits_network = response.traits.network,
                    operating_system = operating_system,
                    browser = browser,
                    device_family = user_agent.device.family,
                    device = device
                )
                save_data.save()
                save_data_seen = UserDataSeen(
                    userdata = save_data,
                    seen = False
                )
                save_data_seen.save()
                urlfunction(url, save_data)
    except:
        pass

       


def getip(request, url):
    ip, is_routable = get_client_ip(request)
    if ip is None:
        return "IP address is private"
    else:
        if is_routable:
            getlication(ip, url, request)
        else:
            return "IP address is private"

        