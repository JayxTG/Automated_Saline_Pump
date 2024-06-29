# Automated Saline Pump System

This repository contains the implementation of an Automated Saline Pump System named FlowGuard. The project was completed as part of the Biomedical Device Designing module by Group D at the Department of Electronic & Telecommunication Engineering, University of Moratuwa, Sri Lanka.

## 👥 Group Members

- 
- 
- 

Special thanks to Lohan, Charels, and Kaveendra for their assistance in transferring and verifying the data.

## 🎯 Objective

The objective of this project is to design, implement, and verify an automated saline pump system that can monitor saline flow rate in patients remotely for enhanced patient management.

## 🔑 Key Features

- 📡 Remote monitoring of saline flow rate using IoT
- 💻 Automated stopping of reverse flow
- 🔔 Notification system for low saline levels
- 🛠️ Integration with hospital control room notifications
- 📊 Design and implementation of PCB and enclosure

## Project Overview

The project is divided into several distinct phases:

### Phase 1: Research and Concept Exploration
- Analyze various approaches and select the most practical one.
- Conduct extensive feasibility studies.

### Phase 2: System Development
- Prototype with components like temperature sensor, peristaltic pump, non-contact water level sensor, and ESP8266 Wi-Fi module.
- Develop software for controlling the system via a web interface.

### Phase 3: Software Integration
- Create a web server for control and monitoring.
- Implement serial communication for data exchange between the server and hardware components.

### Phase 4: Testing and Verification
- Conduct bench testing and simulated use testing to validate system performance.
- Ensure compliance with medical device regulations and standards.

## 🛠️ Hardware and Software Requirements

**Hardware:**
- Temperature sensor
- Peristaltic pump
- Non-contact water level sensor
- ESP8266 Wi-Fi module
- Wireless power supply module

**Software:**
- Web server software for control and monitoring
- Serial communication protocol for data exchange
- Alarm system integration software
- Data logging and analysis tools

## 🚀 How to Use

1. **Clone the Repository:**
```bash
git clone https://github.com/your-username/Automated-Saline-Pump-System.git
```
2. **Hardware Setup:**
- Assemble the hardware components according to the design files in the hardware/ directory.
3. **Software Setup:**
- Deploy the web server software in the software/server directory.
- Configure the monitoring and notification system using the provided software.
4. **System Implementation:**
- Open the project in your preferred development environment.
- Synthesize the design and program the microcontroller or development board.
5. **Testing:**
- Use the provided test environment to verify functionality.
- Perform clinical testing and verify compliance with regulatory standards.
- 
## 📊 Results
- Successful implementation of an automated saline pump system.
- Verified functionality through comprehensive testing and simulation.
- Detailed analysis and documentation available in the project report.
  
## 📚 References
- Paul G. Yock, Stefanos Zenios, Josh Makower, Todd J. Brinton, Uday N. Kumar, "Biodesign: The Process of Innovating Medical Technologies", 2nd edition, New York: Cambridge University Press, 2009.
- Rajveer Shastri, Aparna Shastri, Sarika Shende, Nikita Swami, Rohini Yadav, "Controller Based Automatic Saline Infusion Pump," Department of Electronics and Telecommunication Vidya Pratishthan’s Kamalnayan Bajaj Institute of Engineering and Technology Baramati, India, 2019.
- Achraf Haibi, Kenza Oufaska, Khalid El Yassini, Mohammed Boulmalf, and Mohsine Bouya, "Systematic Mapping Study on RFID Technology," IEEE, 2022.
- O. T. K. N. S. Patrick Loola Bokonda, "Predictive Analysis Using Machine Learning: Review of Trends and Methods," IEEE ISAECT 2020.

## 📄 License
This project is open-source and available under the MIT License.
