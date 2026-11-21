# T8 — Signals and Emissions
*4 questions on the exam from a pool of 47*

## Group T8A — Basic characteristics of FM and SSB; Bandwidth of various modulation modes: CW, SSB, FM, fast-scan TV; Choice of emission type: selection of USB vs LSB, use of SSB for weak signal work, use of FM for VHF packet and repeaters

### T8A01
**Which of the following is a form of amplitude modulation?**
- A) Spread spectrum
- B) Packet radio
- **C) Single sideband** ✅
- D) Phase shift keying (PSK)

> Single sideband is a form of amplitude modulation. It starts as an AM signal, then the carrier and one sideband are removed, leaving a single sideband to carry the information. Packet radio is a data protocol, and spread spectrum and phase shift keying are different techniques, not forms of amplitude modulation.

### T8A02
**What type of modulation is commonly used for VHF packet radio transmissions?**
- **A) FM or PM** ✅
- B) SSB
- C) AM
- D) PSK

> VHF packet radio is commonly sent using FM or PM, phase modulation, usually by feeding audio tones from a modem into an ordinary FM radio. FM transceivers are inexpensive and widely available on VHF, so they're a natural fit. SSB and AM aren't commonly used for VHF packet, and PSK is a separate digital mode used mostly on HF.

### T8A03
**Which type of voice mode is often used for long-distance (weak signal) contacts on the VHF and UHF bands?**
- A) FM
- B) DRM
- **C) SSB** ✅
- D) PM

> SSB is the preferred voice mode for long-distance, weak-signal contacts on VHF and UHF. It puts all of the transmitter's power into one narrow sideband with no carrier, so weak signals can still get through. FM and PM are great for local repeater contacts but need a stronger signal, and DRM is a digital broadcasting format, not a common amateur weak-signal mode.

### T8A04
**Which type of modulation is commonly used for VHF and UHF voice repeaters?**
- A) AM
- B) SSB
- C) PSK
- **D) FM or PM** ✅

> VHF and UHF voice repeaters commonly use FM or PM, phase modulation, which is closely related to FM. FM gives clear audio, resists noise, and suits the channelized repeater frequencies. AM and SSB are seldom used on repeaters, and PSK is a digital data mode, not a voice mode.

### T8A05
**Which of the following signal types has the narrowest bandwidth?**
- A) FM voice
- B) SSB voice
- **C) CW** ✅
- D) Slow-scan TV

> CW, or Morse code, has the narrowest bandwidth of the choices listed, about 150 hertz. SSB voice is roughly 3 kilohertz, FM voice is about 10 to 15 kilohertz, and analog slow-scan TV is sent within about the same width as an SSB voice signal. CW's narrow bandwidth is one reason it works so well for weak-signal communication.

### T8A06
**Which sideband is normally used for 10-meter HF, VHF, and UHF single-sideband communications?**
- **A) Upper sideband** ✅
- B) Lower sideband
- C) Suppressed sideband
- D) Inverted sideband

> Upper sideband (USB) is normally used for 10-meter HF, VHF, and UHF single-sideband communications. The convention is USB above 10 MHz. Since 10 meters (28 MHz) is above this threshold, USB is the standard.

### T8A07
**What is one characteristic of single sideband (SSB) compared to FM?**
- A) SSB signals are easier to tune in correctly
- B) SSB signals are less susceptible to interference
- **C) SSB signals have narrower bandwidth** ✅
- D) SSB signals are less susceptible to high SWR

> A key characteristic of SSB compared to FM is that SSB signals have a narrower bandwidth, which means they can be heard under noisier conditions and at greater distances with lower power.

### T8A08
**What is the approximate bandwidth of a typical single sideband (SSB) voice signal?**
- A) 1 kHz
- **B) 3 kHz** ✅
- C) 6 kHz
- D) 15 kHz

> The approximate bandwidth of an SSB voice signal is about 3 kHz. This is much narrower than FM's 10–15 kHz bandwidth, which is one reason SSB is more efficient for long-distance communication.

### T8A09
**What is the approximate bandwidth of an FM voice signal on VHF repeaters?**
- A) Less than 500 Hz
- B) About 150 kHz
- **C) Between 10 and 15 kHz** ✅
- D) Between 50 and 125 kHz

> The approximate bandwidth of a VHF repeater FM voice signal is between 10 and 15 kHz. FM uses more bandwidth than SSB, but provides cleaner, noise-free audio above the squelch threshold.

### T8A10
**What is the approximate bandwidth of AM fast-scan TV transmissions?**
- A) More than 10 MHz
- **B) About 6 MHz** ✅
- C) About 3 MHz
- D) About 1 MHz

> The typical bandwidth of an analog fast-scan TV (NTSC) signal on the 70-centimeter band is about 6 MHz. Amateur TV uses the same NTSC standard as broadcast television, which requires a wide bandwidth.

### T8A11
**What is the approximate bandwidth required to transmit a CW signal?**
- A) 2.4 kHz
- **B) 150 Hz** ✅
- C) 1000 Hz
- D) 15 kHz

> A CW signal needs only about 150 hertz of bandwidth, much narrower than any voice mode. About 2.4 kilohertz is what an SSB voice signal uses, and 15 kilohertz is the width of an FM voice signal. 1000 hertz is also far more than a clean CW signal needs.

### T8A12
**Which of the following is a disadvantage of FM compared with single sideband?**
- A) Voice quality is poorer
- **B) Only one signal can be received at a time** ✅
- C) FM signals are harder to tune
- D) FM signals are more susceptible to high SWR

> Because of FM's capture effect, the strongest signal on a frequency takes over the receiver and weaker ones are suppressed, so only one signal can be received at a time. With SSB, you can hear several stations on the same frequency at once. FM's voice quality is generally good, and FM is actually easier to tune in than SSB.

## Group T8B — Amateur satellite operation: Doppler shift, basic orbits, operating protocols, modulation mode selection, transmitter power considerations, telemetry, satellite tracking programs, beacons, uplink and downlink mode definitions, spin fading, definition of “LEO”, setting uplink power

### T8B01
**What telemetry information is typically transmitted by satellite beacons?**
- A) The signal strength of received signals
- B) Time of day accurate to plus or minus 1/10 second
- **C) Health and status of the satellite** ✅
- D) All these choices are correct

> Satellite beacons typically send telemetry about the health and status of the satellite, such as battery voltage, temperatures, and the condition of its systems. Ground stations use this data to keep an eye on the spacecraft. Reporting the strength of your signal and sending precise time are not what beacons are typically for, so all these choices is wrong.

### T8B02
**What is the impact of using excessive effective radiated power on a satellite uplink?**
- A) Possibility of commanding the satellite to an improper mode
- **B) Blocking access by other users** ✅
- C) Overloading the satellite batteries
- D) Possibility of rebooting the satellite control computer

> Using too much effective radiated power on a satellite uplink can block access by other users. A satellite's transponder shares its limited power among everyone using it, so an overly strong signal takes more than its share and drowns out others. Use only enough power to be heard. Too much uplink power doesn't overload the satellite's batteries or reboot its computer.

### T8B03
**Which of the following are provided by satellite tracking programs?**
- A) Maps showing the real-time position of the satellite track over Earth
- B) The time, azimuth, and elevation of the start, maximum altitude, and end of a pass
- C) The apparent frequency of the satellite transmission, including effects of Doppler shift
- **D) All these choices are correct** ✅

> Satellite tracking programs provide all three. They show a map of the satellite's real-time position over Earth, the time, azimuth, and elevation for the start, highest point, and end of each pass, and the apparent frequency corrected for Doppler shift. Since all three apply, D is correct.

### T8B04
**What mode of transmission is commonly used by amateur radio satellites?**
- A) SSB
- B) FM
- C) CW/data
- **D) All these choices are correct** ✅

> Amateur satellites use many modes. Linear transponders carry SSB and CW, many satellites have FM repeaters, and others relay digital data. Since all three apply, D is correct.

### T8B05
**What is a satellite beacon?**
- A) The primary transmit antenna on the satellite
- B) An indicator light that shows where to point your antenna
- C) A reflective surface on the satellite
- **D) A transmission from a satellite that contains status information** ✅

> A satellite beacon is a transmission from a satellite that contains status information, such as telemetry about its batteries and temperatures. Hearing the beacon also tells you the satellite is in range and working. A beacon isn't an antenna, an indicator light, or a reflective surface.

### T8B06
**Which of the following are inputs to a satellite tracking program?**
- A) The satellite transmitted power
- **B) The Keplerian elements** ✅
- C) The last observed time of zero Doppler shift
- D) All these choices are correct

> Satellite tracking programs need the Keplerian elements, a set of numbers that describe the satellite's orbit. They're published regularly, often in a format called two-line elements, and should be updated from time to time because orbits slowly change. The program doesn't need the satellite's transmit power or past Doppler observations.

### T8B07
**What is Doppler shift in reference to satellite communications?**
- A) A change in the satellite orbit
- B) A mode where the satellite receives signals on one band and transmits on another
- **C) An observed change in signal frequency caused by relative motion between the satellite and Earth station** ✅
- D) A special digital communications mode for some satellites

> Doppler shift is an observed change in signal frequency caused by relative motion between the satellite and your Earth station. As a satellite approaches, its signal appears higher in frequency, and as it moves away, the frequency drops, much like the pitch of a passing siren. It isn't an orbit change, a band mode, or a digital mode, and you adjust your frequency during a pass to compensate.

### T8B08
**What does it mean if a satellite is operating in U/V mode?**
- A) The satellite uplink is in the 15-meter band and the downlink is in the 10-meter band
- **B) The satellite uplink is in the 70-centimeter band and the downlink is in the 2-meter band** ✅
- C) The satellite operates using ultraviolet frequencies
- D) The satellite frequencies are usually variable

> In U/V mode, the satellite's uplink is in the 70-centimeter band, which is UHF, and its downlink is in the 2-meter band, which is VHF. The first letter is the uplink and the second is the downlink. It has nothing to do with ultraviolet light, and the 15- and 10-meter bands are HF, which use different letters.

### T8B09
**What causes spin fading of satellite signals?**
- A) Circular polarized noise interference radiated from the sun
- **B) Rotation of the satellite and its antennas** ✅
- C) Doppler shift of the received signal
- D) Interfering signals within the satellite uplink band

> Spin fading is caused by rotation of the satellite and its antennas. As the satellite spins or tumbles, its antennas point toward you and then away, so the signal fades in and out in a regular rhythm. It's different from Doppler shift, which changes the frequency, and it isn't caused by noise from the sun.

### T8B10
**What does the term LEO mean in reference to communication satellites?**
- A) Low Energy Orbit, which conserves battery power
- B) Low Elevation Orbit, which appears close to the horizon from the earth station
- C) Low Equilibrium Orbit, which has a slightly unstable period
- **D) Low Earth Orbit, which has a period of around 100 minutes** ✅

> LEO stands for Low Earth Orbit — a satellite orbiting relatively close to Earth, typically at altitudes below about 2,000 km. LEO satellites have orbital periods of around 100 minutes, which means they pass over any given point relatively quickly.

### T8B11
**Who is permitted to receive telemetry from an amateur radio satellite?**
- **A) Anyone** ✅
- B) Only the satellite control operator
- C) Only the control operator or a licensed radio amateur who has received the encryption key from the control operator
- D) Only a licensed radio amateur who has received the encryption key from AMSAT

> Anyone may receive telemetry from an amateur radio satellite. There are no restrictions on receiving — you don't need special authorization, a specific license class, or a decryption key. If you can hear it, you can listen.

### T8B12
**Which of the following is a way to determine whether your satellite uplink power into a linear transponder satellite is neither too low nor too high?**
- A) Check your signal strength report in the telemetry data
- B) Listen for distortion on your downlink signal
- **C) Your signal strength on the downlink should be about the same as the beacon** ✅
- D) Compare your signal to others on the downlink using an internet SDR receiver

> To determine if your satellite uplink power into a linear transponder satellite is correct, compare your downlink signal strength to the satellite's beacon signal. Your signal should be about the same strength as the beacon — not stronger, not weaker.

## Group T8C — Operating activities: radio direction finding, contests, linking over the internet, exchanging grid locators

### T8C01
**Which of the following methods is used to locate sources of noise interference or jamming?**
- A) Echolocation
- B) Doppler radar
- **C) Radio direction finding** ✅
- D) Phase locking

> Radio direction finding is used to locate sources of noise interference or jamming. With a directional antenna, you take bearings on the signal from different spots and follow it back to the source. Echolocation and Doppler radar detect objects with reflected signals, and phase locking is a way to keep an oscillator on frequency.

### T8C02
**Which of these items would be useful for a hidden transmitter hunt?**
- A) Calibrated SWR meter
- **B) A directional antenna** ✅
- C) A directional wattmeter
- D) All these choices are correct

> A directional antenna is the key tool for a hidden transmitter hunt, also called a fox hunt. Turning the antenna shows you the direction where the signal is strongest, and bearings taken from several spots lead you to the transmitter. An SWR meter and a directional wattmeter measure your own antenna system, not the direction of an incoming signal, so all these choices is wrong.

### T8C03
**What operating activity involves contacting as many stations as possible during a specified period?**
- A) Simulated emergency exercises
- B) Net operations
- C) Hidden transmitter hunts
- **D) Contesting** ✅

> Contesting is the operating activity that involves contacting as many stations as possible during a specified period. Contests (also called radiosport) are competitive events where operators try to make the most contacts, sometimes over a weekend.

### T8C04
**Which of the following is good practice when contacting another station in a contest?**
- A) Signing only the last two letters of your call if there are many other stations calling
- B) Contacting the station twice to be sure that you are in his log
- **C) Sending only the minimum information needed for proper identification and the contest exchange** ✅
- D) Adding “Please copy” before your exchange

> Good practice in a contest is sending only the minimum information needed for proper identification and the contest exchange. Be efficient — don't waste time with extended conversations. Get the call sign, exchange, and move on to the next contact.

### T8C05
**What is a grid locator?**
- **A) A letter-number designator assigned to a geographic location** ✅
- B) A letter-number designator assigned to an azimuth and elevation
- C) An instrument for locating faults in power amplifiers
- D) An instrument for radio direction finding

> A grid locator is a letter-number designator assigned to a geographic location. The Maidenhead grid system divides the world into grid squares, and your grid square identifies your approximate location for VHF/UHF contests and awards.

### T8C06
**How is over the air access to Internet Radio Linking Project (IRLP) nodes accomplished?**
- A) By obtaining a password that is sent via voice to the node
- **B) By using Dual-Tone Multi-Frequency (DTMF) signals** ✅
- C) By entering the proper internet password
- D) By using Continuous Tone-Coded Squelch System (CTCSS) tone codes

> Over-the-air access to IRLP (Internet Radio Linking Project) nodes is accomplished by using DTMF (Dual-Tone Multi-Frequency) signals. You dial DTMF codes from your radio to connect to or disconnect from IRLP nodes.

### T8C07
**What is Voice Over Internet Protocol (VoIP)?**
- A) A set of rules specifying how to identify your station when linked over the internet to another station
- B) A technique employed to “spot” DX stations via the internet
- C) A technique for measuring the modulation quality of a transmitter using remote sites monitored via the internet
- **D) A method of delivering voice communications over the internet using digital techniques** ✅

> VoIP, or Voice over Internet Protocol, is a method of delivering voice communications over the internet using digital techniques. Amateur linking systems such as EchoLink, IRLP, and AllStar use VoIP to connect repeaters and stations around the world. It isn't an identification rule, a DX spotting method, or a way to measure modulation quality.

### T8C08
**What is the Internet Radio Linking Project (IRLP)?**
- **A) A technique to connect amateur radio systems, such as repeaters, via the internet** ✅
- B) A system for providing access to websites via amateur radio
- C) A system for informing amateurs in real time of the frequency of active DX stations
- D) A technique for measuring signal strength of an amateur transmitter via the internet

> IRLP (Internet Radio Linking Project) is a technique to connect amateur radio systems, such as repeaters, via the internet. It lets you talk through a local repeater and be heard on a linked repeater hundreds or thousands of miles away.

### T8C09
**Which of the following protocols enables an amateur station to transmit through a repeater without using a radio to initiate the transmission?**
- A) IRLP
- B) D-STAR
- C) DMR
- **D) EchoLink** ✅

> EchoLink lets you connect to repeaters and other stations from a computer or smartphone, so you can transmit through a repeater without using a radio to start the transmission. IRLP users get on the system over the air with a radio. D-STAR and DMR are digital voice modes that are normally used with radios.

### T8C10
**What is required before using the EchoLink system?**
- A) Complete the required EchoLink training
- B) Purchase a license to use the EchoLink software
- **C) Register your call sign and provide proof of license** ✅
- D) At least a General Class license

> Before using the EchoLink system, you need a valid amateur radio license and proof of licensure. EchoLink verifies your license to prevent unlicensed use of the system.

### T8C11
**What is an amateur radio station that connects other amateur stations to the internet?**
- **A) A gateway** ✅
- B) A repeater
- C) A digipeater
- D) A beacon

> A gateway is an amateur station that connects other amateur stations to the internet, acting as a bridge between radio and the internet. A repeater retransmits signals on another frequency, a digipeater relays digital packets over the air, and a beacon transmits so others can check propagation or equipment.

## Group T8D — Non-voice and digital communications: image signals and definition of NTSC, CW, packet radio, PSK, APRS, error detection and correction, amateur radio networking, DMR, WSJT modes, Broadband-Hamnet

### T8D01
**Which of the following is a digital communications mode?**
- A) Packet radio
- B) IEEE 802.11
- C) FT8
- **D) All these choices are correct** ✅

> All three are digital communications modes. Packet radio sends data in packets, IEEE 802.11 is the Wi-Fi standard that hams use in mesh networks, and FT8 is a popular weak-signal digital mode. Since all three are digital, D is correct.

### T8D02
**What is FT8?**
- A) A wideband FM voice mode
- **B) A digital mode capable of low signal-to-noise operation** ✅
- C) An eight-channel multiplex mode for FM repeaters
- D) A digital slow-scan TV mode with forward error correction and automatic color compensation

> FT8 is a digital mode capable of low signal-to-noise operation. It's designed for making contacts when signals are extremely weak — stations can communicate even when the signals are far below what the human ear can detect. FT8 has become enormously popular for HF contacts.

### T8D03
**What kind of data can be transmitted by APRS?**
- A) GPS position data
- B) Text messages
- C) Weather data
- **D) All these choices are correct** ✅

> APRS, the Automatic Packet Reporting System, can carry all of these: GPS position data, short text messages, and weather data from weather stations. That's what makes it so useful for tracking and public service events. Since all three apply, D is correct.

### T8D04
**What is meant by the term "NTSC?"**
- A) A digital transmission standard for encrypting data
- B) A special mode for satellite uplink
- **C) An analog fast-scan color TV signal** ✅
- D) A frame compression scheme for TV signals

> NTSC is an analog video standard used for amateur fast-scan television (ATV). It's the same system that was used for broadcast television in North America. It requires about 6 MHz of bandwidth.

### T8D05
**Which of the following is an application of APRS?**
- **A) Providing real-time tactical digital communications in conjunction with a map showing the locations of stations** ✅
- B) Automatically showing the number of packets transmitted via PACTOR during a specific time interval
- C) Providing voice over internet connection between repeaters
- D) Providing information on the number of stations signed into a repeater

> APRS (Automatic Packet Reporting System) can automatically report your station's location, show it on a map, and transmit weather station data. It's a tactical communication system used for real-time position tracking and situational awareness.

### T8D06
**What does the abbreviation "PSK" mean?**
- A) Pulse Shift Keying
- **B) Phase Shift Keying** ✅
- C) Packet Sampled Keying
- D) Power Sampled Keying

> PSK stands for Phase Shift Keying — a digital modulation method that encodes data by shifting the phase of the carrier signal. PSK31 is a popular amateur digital mode that uses very narrow bandwidth.

### T8D07
**Which of the following describes DMR?**
- **A) A technique for time-multiplexing two digital voice signals on a single 12.5 kHz repeater channel** ✅
- B) An automatic position tracking mode for FM mobiles communicating through repeaters
- C) An automatic computer logging technique for hands-off logging when communicating while operating a vehicle
- D) A digital technique for transmitting on two repeater inputs simultaneously for automatic error correction

> DMR, or Digital Mobile Radio, uses time-division multiplexing to carry two separate digital voice signals on a single 12.5 kilohertz repeater channel. The two time slots alternate rapidly, so one repeater can carry two conversations at once. It isn't a position tracking system, a logging method, or a way to transmit on two repeater inputs.

### T8D08
**Which of the following is included in packet radio transmissions?**
- A) A checksum that permits error detection
- B) A header that contains the call sign of the station to which the information is being sent
- C) Automatic repeat request in case of error
- **D) All these choices are correct** ✅

> Packet radio transmissions include all three. A checksum lets the receiving station detect errors, a header carries the call sign of the station the data is going to, and automatic repeat request, or ARQ, asks for any packet received with errors to be sent again. Since all three apply, D is correct.

### T8D09
**What is CW?**
- A) A type of electromagnetic propagation
- B) A digital mode used primarily on 2-meter FM
- C) Error correction for digital transmission using code words
- **D) Another name for a Morse code transmission** ✅

> CW stands for Continuous Wave, which is Morse code transmission using on-off keying of an unmodulated carrier. It's the oldest digital mode and still one of the most efficient for weak-signal communication.

### T8D10
**Which of the following operating activities is supported by digital mode software in the WSJT-X software suite?**
- A) Earth-Moon-Earth
- B) Weak signal propagation beacons
- C) Meteor scatter
- **D) All these choices are correct** ✅

> The WSJT-X software suite supports all three activities. It has modes for Earth-Moon-Earth contacts, such as JT65 and Q65, for weak signal propagation beacons, such as WSPR, and for meteor scatter, such as MSK144. Since all three are supported, D is correct.

### T8D11
**What is the role of ARQ in a transmission system?**
- A) A special transmission format limited to video signals
- B) A system used to encrypt command signals to an amateur radio satellite
- **C) An error correction method in which the receiving station detects errors and sends a request for retransmission** ✅
- D) A method of compressing data using autonomous reiterative Q codes prior to final encoding

> ARQ (Automatic Repeat reQuest) is a technique where the receiving station detects errors and requests retransmission of corrupted data. This ensures reliable data delivery over a potentially noisy radio channel.

### T8D12
**Which of the following best describes an amateur radio mesh network?**
- **A) An amateur-radio data network using commercial Wi-Fi equipment with modified firmware** ✅
- B) A wide-bandwidth digital voice mode employing DMR protocols
- C) An amateur-radio satellite communications network using modified commercial satellite TV hardware
- D) An internet linking protocol allowing communication through repeaters around the world

> An amateur radio mesh network is a data network using commercial Wi-Fi equipment with modified firmware to operate on amateur frequencies. It creates a self-healing, multi-node network for data communications, useful for emergency communications and community networking.
