# rtl_433_discoverandsubmit

A command-line utility to connect to an MQTT server, listen to `rtl_433` events, and allow users to generate auto-discovery configurations for Home Assistant for the devices they choose.

## Features
- Connects to an MQTT server.
- Listens to `rtl_433` events in real-time.
- Provides an interactive CLI to let users choose devices.
- Generates Home Assistant auto-discovery configurations for chosen devices.

Screenshot of devices listed
![img.png](Screenshots/img.png)

Detailed device view and opportunity to add to Home Assistant
![img.png](Screenshots/img1.png)

Device added to Home Assistant
![img_2.png](Screenshots/img_2.png)
## Installation

You can install `rtl_433_discoverandsubmit` directly from PyPI:

```bash
pip install rtl_433_discoverandsubmit
```
##Usage
After installation, you can run the tool using:

```rtl_433_discoverandsubmit```

##Command Line Arguments
You can specify the MQTT server, username, and password (if applicable) as well as the topic via command-line arguments. More details can be found in the help documentation:

```rtl_433_discoverandsubmit --help```

##Contributing
Feedback, bug reports, and pull requests are super welcome on this project. If you face any issues, please raise them in the issue tracker.

##License
This project is licensed under the MIT License. See the LICENSE file for more details.

