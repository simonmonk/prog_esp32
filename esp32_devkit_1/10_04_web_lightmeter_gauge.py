from network import WLAN, STA_IF
from microdot import Microdot
from machine import ADC, Pin
from time import sleep

ssid = 'network'      # CHANGE ME
password = 'password' # CHANGE ME

index_page = '''
<!DOCTYPE html>
<html>
<head>
  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js" type="text/javascript" charset="utf-8"></script>
  <script src="http://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script> 
  <script src="https://cdnjs.cloudflare.com/ajax/libs/justgage/1.6.1/justgage.min.js"></script>
  <script>
  function callback(lightStr, status){
    if (status == "success") {
      light = parseFloat(lightStr).toFixed(2);
      g.refresh(light);
      setTimeout(getReading, 1000);
    }
    else {
      alert("There was a problem");
    }
  }
  function getReading(){
    $.get('/light', callback);
  }
</script>
</head>

<body>
<h1>Light Level (Percent)</h1>
<div id="gauge" class="200x160px"></div>

<script>
var g = new JustGage({
    id: "gauge",
    value: 0,
    min: 0,
    max: 100,
});
getReading();
</script>
</body>
</html>
'''

max_reading = 58000

sensor = ADC(Pin(32), atten=ADC.ATTN_11DB)

def connect_wifi(ssid, password):
    wlan = WLAN(STA_IF)
    wlan.active(True)
    print('connecting to ' + ssid)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('.', end='')
        sleep(1)
    print('IP address:', wlan.ifconfig()[0])

def read_light():
    reading = sensor.read_u16()
    percent = int(reading / max_reading * 100)
    if percent > 100:
        percent = 100
    return percent


app = Microdot()  
connect_wifi(ssid, password)

@app.route('/')
def index(request):
    return index_page, 400, {'Content-Type': 'text/html'}

@app.route('/light')
def temp(request):
    return str(read_light())

app.run(port=80)