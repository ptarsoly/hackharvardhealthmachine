var SerialPort = require('serialport');
var port = new SerialPort('/dev/ttyACM0', {
  baudRate: 115200
});

// Read data that is available but keep the stream from entering "flowing mode"
port.on('readable', function () {
    console.log('Data:', port.read().toString());
  });

  // in /home/pi/hackharvard