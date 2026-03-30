# T4 — Amateur Radio Practices
*2 questions on the exam from a pool of 23*

## Group T4A — Station setup; connecting a transceiver; power source; connecting digital equipment; RF grounding

### T4A01
**Which of the following is an appropriate power supply rating for a typical 50-watt output mobile FM transceiver?**
- A) 24.0 volts at 4 amperes
- B) 13.8 volts at 4 amperes
- C) 24.0 volts at 12 amperes
- **D) 13.8 volts at 12 amperes** ✅

> A typical 50-watt output mobile FM transceiver needs a power supply rated for at least 13.8 VDC at 12 amps or more. At 50 watts of RF output, the radio draws several amps from the DC supply. Using a supply with too low a current rating can cause voltage drops and unreliable operation.

### T4A02
**Which of the following should be considered when selecting an accessory SWR meter?**
- **A) The frequency and power level at which the measurements will be made** ✅
- B) The distance that the meter will be located from the antenna
- C) The maximum SWR anticipated on the transmission line
- D) The ability of the meter to compensate for a poor transmission line match to the antenna

> When selecting an SWR meter, make sure it covers the frequency range you're using and has the appropriate power rating. An SWR meter designed for HF won't necessarily work accurately at VHF or UHF. Frequency range coverage is the key consideration.

### T4A03
**Why are short, heavy-gauge wires used for a transceiver’s DC power connection?**
- **A) To minimize voltage drop when transmitting** ✅
- B) To provide a close match to the power supply output impedance
- C) To avoid RF interference
- D) To minimize radiative losses in the power cable

> Short, heavy-gauge wires minimize voltage drop between the power supply and the transceiver. Long or thin wires have higher resistance, causing voltage to drop under load, which can make the radio malfunction or reduce output power. Keep the power cables short and thick.

### T4A04
**How are the audio input and output of a transceiver connected in a station configured to operate using FT8?**
- A) To a computer running a terminal program and connected to a terminal node controller unit
- **B) To the audio output and input of a computer running FT8 software** ✅
- C) To an FT8 conversion unit, a keyboard, and a computer monitor
- D) To a computer connected to the FT8converter.com website

> For FT8 operation, the transceiver's audio input and output are connected to the audio output and input of a computer running FT8 software (like WSJT-X). The computer generates and decodes the FT8 signals through the audio interface. Modern setups often use a USB audio interface built into the radio.

### T4A05
**Where should an RF power meter be installed?**
- **A) In the feed line, between the transmitter and antenna** ✅
- B) At the power supply output
- C) In parallel with the push-to-talk line and the antenna
- D) In the power supply cable, as close as possible to the radio

> Most modern transceivers connect to a computer through a USB cable for both audio and control. This single connection handles CAT control (frequency, mode), audio in/out for digital modes, and often PTT control. It's much simpler than the multiple cables older setups required.

### T4A06
**What signals are used in a computer-radio interface for digital mode operation?**
- A) Receive and transmit mode, status, and location
- B) Antenna and RF power
- **C) Receive audio, transmit audio, and transmitter keying** ✅
- D) NMEA GPS location and DC power

> An RF power meter installed between the transmitter and antenna monitors the output power level. It tells you exactly how much power is going to the antenna, which is useful for adjusting power levels and troubleshooting.

### T4A07
**Which of the following is one of the connections required between a computer and a transceiver to operate digital modes?**
- A) Computer “line out” to transceiver push-to-talk
- B) Computer “line in” to transceiver push-to-talk
- **C) Computer “line in” to transceiver speaker connector** ✅
- D) Computer “line out” to transceiver speaker connector

> To operate digital modes, one essential connection between the computer and transceiver is an audio interface (speaker/microphone connections or a USB audio codec). This carries the digital mode audio signals between the computer software and the radio.

### T4A08
**Which of the following conductors is preferred for bonding at RF?**
- A) Copper braid removed from coaxial cable
- B) Copper-clad steel wire
- C) Twisted-pair cable
- **D) Flat copper strap** ✅

> Flat copper strap is the preferred conductor for RF bonding because it has low inductance at radio frequencies due to its wide, flat shape. Copper-clad steel wire, braided wire, and steel wire all have higher inductance than flat strap.

### T4A09
**How can you determine the length of time that equipment can be powered from a battery?**
- A) Divide the watt-hour rating of the battery by the peak power consumption of the equipment
- **B) Divide the battery ampere-hour rating by the average current draw of the equipment** ✅
- C) Multiply the watts per hour consumed by the equipment by the battery power rating
- D) Multiply the square of the current rating of the battery by the input resistance of the equipment

> Transmit/receive (T/R) switching at the antenna connector of a modern transceiver is performed by electronic switching circuits. These solid-state switches are fast and reliable, replacing the mechanical relays used in older equipment.

### T4A10
**What function does a digital mode hotspot perform for nearby transceivers?**
- **A) Communication with a digital voice or data network** ✅
- B) FT8 digital communications via AFSK using a smartphone connected to the internet
- C) RTTY encoding and decoding without a computer
- D) High-speed digital communications for meteor scatter

> A digital mode hotspot provides nearby transceivers with communication access to a digital voice or data network. It acts as a personal low-power gateway, connecting your DMR, D-STAR, or Fusion radio to the internet-linked digital network through your home internet connection.

### T4A11
**Where should the negative power return of a mobile transceiver be connected in a vehicle?**
- **A) At the 12-volt battery chassis ground** ✅
- B) To the shell of the power connector
- C) To any metal part of the vehicle
- D) Through the transceiver’s mounting bracket

> The negative power return of a mobile transceiver should be connected at the 12-volt battery chassis ground — the same point where the battery's negative terminal connects to the vehicle chassis. This ensures a clean, low-resistance ground connection and prevents ground loops.

### T4A12
**What is an electronic keyer?**
- A) A device for switching antennas from transmit to receive
- B) A device for voice activated switching from receive to transmit
- **C) A device that assists in manual sending of Morse code** ✅
- D) An interlock to prevent unauthorized use of a radio

> The correct answer is C) A device that assists in manual sending of Morse code.

## Group T4B — Operating controls; tuning; use of filters; squelch; AGC; repeater access; DMR operation

### T4B01
**What is the effect of excessive microphone gain on SSB transmissions?**
- A) Frequency instability
- **B) Distorted transmitted audio** ✅
- C) Increased SWR
- D) Sideband inversion

> Excessive microphone gain on SSB transmissions causes distorted audio and excessive bandwidth, potentially causing splatter into adjacent frequencies. The signal becomes over-modulated, and other stations will hear garbled, distorted audio. Keep the mic gain set properly — more is not better.

### T4B02
**Which of the following can be used to enter a transceiver’s operating frequency?**
- **A) The keypad or VFO knob** ✅
- B) The CTCSS or DTMF encoder
- C) The Automatic Frequency Control
- D) All these choices are correct

> For clear FM voice through a repeater, speak across the microphone rather than directly into it, at a normal conversational volume. Talking too close or too loud causes over-deviation. Think of it like a phone call — natural voice, not a shouting match.

### T4B03
**How is squelch adjusted so that a weak FM signal can be heard?**
- **A) Set the squelch threshold so that receiver output audio is on all the time** ✅
- B) Turn up the audio level until it overcomes the squelch threshold
- C) Turn on the anti-squelch function
- D) Enable squelch enhancement

> Multi-use transceivers can communicate on both amateur and non-amateur frequencies like FRS and GMRS. However, type acceptance rules still apply — you can only transmit on frequencies where your radio is approved and you're licensed.

### T4B04
**What does an FM signal sound like when received slightly off frequency?**
- A) The audio increases in pitch
- B) The audio decrease in pitch
- C) There is no effect except for reduction in amplitude
- **D) The audio becomes distorted** ✅

> When an FM signal is received slightly off frequency, the audio becomes distorted. FM receivers are designed for signals at the exact center frequency — even a small offset causes the discriminator to produce distorted audio. This is why accurate frequency setting matters for FM.

### T4B05
**What does the scanning function of an FM transceiver do?**
- A) Checks incoming signal deviation
- B) Prevents interference to nearby repeaters
- **C) Tunes through a range of frequencies to check for activity** ✅
- D) Tunes through a range of frequencies to determine the antenna’s resonant frequency

> The scanning function on an FM transceiver automatically tunes through a set of programmed frequencies (or across a band segment), pausing when it detects a signal. It's like a radio version of channel surfing — the radio searches for activity so you don't have to manually check each frequency.

### T4B06
**Which of the following controls could be used if the voice pitch of a single-sideband signal returning to your CQ call seems too high or low?**
- A) The AGC or limiter
- B) The bandwidth selection
- C) The tone squelch
- **D) The RIT or Clarifier** ✅

> An AGC circuit (Automatic Gain Control) adjusts the receiver's gain automatically to maintain a steady audio output level despite varying signal strengths. Without AGC, strong signals would blast your ears while weak ones would be barely audible.

### T4B07
**What is a DMR “code plug”?**
- A) An adapter cable used to connect a DMR radio to a computer for internet access
- **B) Configuration data loaded onto your radio to access repeaters and talkgroups** ✅
- C) An upgrade to DMR programming software provided by the radio manufacturer to accommodate new radio models
- D) A Coder-Decoder (CODEC) that converts analog voice data to DMR digital data and vice versa

> A DMR code plug is configuration data loaded onto your radio to access repeaters and talkgroups. It contains the frequencies, color codes, talkgroup IDs, and other settings needed to use DMR repeaters in your area. Think of it as a programming profile for your digital radio.

### T4B08
**What is the advantage of having a choice of receiver filter bandwidths in a multimode transceiver?**
- A) Permits monitoring several modes simultaneously by selecting a separate filter for each mode
- **B) Permits noise or interference reduction by selecting a bandwidth matching the mode** ✅
- C) Increases the number of frequencies that can be stored in memory
- D) Increases the amount of offset between receive and transmit frequencies

> Having a choice of receiver filter bandwidths lets you select the best filter for the mode you're operating. A narrow filter for CW rejects adjacent signals, while a wider filter passes the full bandwidth of an SSB or FM signal. The right filter improves readability and reduces interference.

### T4B09
**How is a specific group of stations selected on a DMR digital voice transceiver?**
- A) By retrieving the frequencies from transceiver memory
- B) By enabling the group’s CTCSS tone
- **C) By entering the group’s identification code** ✅
- D) By inserting a five-pin, pre-programmed code plug

> On a DMR digital voice transceiver, you select a specific group of stations by choosing the appropriate talkgroup. Talkgroups are programmed into the radio via the code plug, and selecting one determines which group of users you hear and can talk to.

### T4B10
**Which of the following receiver filter bandwidths provides the best signal-to-noise ratio for SSB reception?**
- A) 500 Hz
- B) 1000 Hz
- **C) 2400 Hz** ✅
- D) 5000 Hz

> DMR repeaters can handle two conversations simultaneously using two time slots — they divide each frequency into alternating time slices. This is called TDMA (Time Division Multiple Access), and it effectively doubles the capacity of each frequency.

### T4B11
**Which of the following must be programmed into a D-STAR digital transceiver before transmitting?**
- **A) Your call sign** ✅
- B) Your output power
- C) The codec type being used
- D) All these choices are correct

> If you're listening to a station that sounds distorted and changing the volume doesn't help, try adjusting the squelch or using a different receive filter bandwidth. The problem is likely in the RF or demodulation stage, not the audio amplifier.
