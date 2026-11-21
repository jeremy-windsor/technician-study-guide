# T4 — Amateur Radio Practices
*2 questions on the exam from a pool of 23*

## Group T4A — Station setup: connecting a microphone, RF power meter, a power source, a computer, digital equipment, an SWR meter; RF grounding; Mobile radio installation

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

> When selecting an SWR meter, consider both the frequency and the power level at which you'll make measurements. The meter must be designed for your frequency range, since one built for HF won't necessarily read accurately at VHF or UHF. It also must be rated for the power you'll run through it. Where it sits in the feed line and the highest SWR you expect aren't the deciding factors, and no meter can fix a poor antenna match.

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

> An RF power meter goes in the feed line, between the transmitter and the antenna, because that's where the RF power flows. The power supply output and the power cable carry only DC, so a meter there can't measure RF output. Connecting it in parallel with the push-to-talk line and the antenna doesn't put it in the RF path at all.

### T4A06
**What signals are used in a computer-radio interface for digital mode operation?**
- A) Receive and transmit mode, status, and location
- B) Antenna and RF power
- **C) Receive audio, transmit audio, and transmitter keying** ✅
- D) NMEA GPS location and DC power

> A computer-radio interface for digital modes carries three signals: receive audio from the radio to the computer, transmit audio from the computer to the radio, and transmitter keying to switch the radio into transmit. Many modern radios send all three over a single USB cable. The antenna and RF power don't go through the interface. GPS location data, DC power, and status or location information aren't the required signals.

### T4A07
**Which of the following is one of the connections required between a computer and a transceiver to operate digital modes?**
- A) Computer “line out” to transceiver push-to-talk
- B) Computer “line in” to transceiver push-to-talk
- **C) Computer “line in” to transceiver speaker connector** ✅
- D) Computer “line out” to transceiver speaker connector

> One connection a digital mode setup needs is from the computer's line in to the transceiver's speaker or audio output connector. That's how received audio gets into the computer so the software can decode it. The computer's line out feeds the transceiver's microphone or data input, not its speaker, and push-to-talk is a keying signal, not an audio line. Many modern radios handle these connections through a single USB cable.

### T4A08
**Which of the following conductors is preferred for bonding at RF?**
- A) Copper braid removed from coaxial cable
- B) Copper-clad steel wire
- C) Twisted-pair cable
- **D) Flat copper strap** ✅

> Flat copper strap is the preferred conductor for RF bonding because its wide, flat shape gives it low inductance, and so low impedance, at radio frequencies. Copper-clad steel wire and twisted-pair cable are thin round conductors with much higher inductance. Copper braid removed from coaxial cable is a poor choice because its strands corrode where they touch, which raises its resistance, especially outdoors.

### T4A09
**How can you determine the length of time that equipment can be powered from a battery?**
- A) Divide the watt-hour rating of the battery by the peak power consumption of the equipment
- **B) Divide the battery ampere-hour rating by the average current draw of the equipment** ✅
- C) Multiply the watts per hour consumed by the equipment by the battery power rating
- D) Multiply the square of the current rating of the battery by the input resistance of the equipment

> To estimate how long a battery will last, divide its ampere-hour rating by the equipment's average current draw. For example, a 20 amp-hour battery running a radio that averages 2 amps lasts about 10 hours. Use the average current, not the peak, because a radio draws heavy current only while transmitting. The other choices multiply or square things in ways that don't give you time.

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

> An electronic keyer is a device that assists in manual sending of Morse code. It automatically generates properly timed dots and dashes when you press a paddle — you control the characters, but the keyer handles the precise timing. This makes CW sending faster, more consistent, and less tiring than using a straight key.

## Group T4B — Operating controls: frequency tuning, use of filters, squelch function, AGC, memory channels, noise blanker, microphone gain, receiver incremental tuning (RIT), bandwidth selection, scanning function; Digital transceiver configuration; DMR code plugs and talk groups

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

> You enter a transceiver's operating frequency with the keypad, by typing it in directly, or with the VFO knob, by tuning to it. CTCSS and DTMF encoders generate tones for accessing repeaters and sending control signals. Automatic Frequency Control keeps a receiver locked onto a signal that drifts slightly. Neither one sets the frequency you want.

### T4B03
**How is squelch adjusted so that a weak FM signal can be heard?**
- **A) Set the squelch threshold so that receiver output audio is on all the time** ✅
- B) Turn up the audio level until it overcomes the squelch threshold
- C) Turn on the anti-squelch function
- D) Enable squelch enhancement

> To hear a weak FM signal, set the squelch threshold so the receiver audio is on all the time, which means opening the squelch fully. You'll hear background noise, but weak signals won't be cut off by the squelch. Turning up the volume doesn't change the squelch threshold. Anti-squelch and squelch enhancement aren't real radio controls.

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

> If an SSB voice sounds too high or too low in pitch, adjust the RIT, which stands for receiver incremental tuning and is also called the clarifier. It shifts your receive frequency slightly without moving your transmit frequency, so the voice sounds natural again. AGC and limiters control signal level, not pitch. Bandwidth selection changes the filter width, and tone squelch is an FM feature.

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

> A 2400 hertz filter gives the best signal-to-noise ratio for SSB reception because it matches the bandwidth of an SSB voice signal. It passes the voice but keeps out extra noise. 500 and 1000 hertz filters are too narrow for voice and are meant for CW. A 5000 hertz filter is wider than needed, so it lets in more noise and nearby interference.

### T4B11
**Which of the following must be programmed into a D-STAR digital transceiver before transmitting?**
- **A) Your call sign** ✅
- B) Your output power
- C) The codec type being used
- D) All these choices are correct

> Before you transmit on a D-STAR transceiver, you must program in your call sign. D-STAR sends your call sign in its digital data stream for identification and for routing through repeaters and networks. Output power is an ordinary setting with a default value, and D-STAR uses a single built-in voice codec, so there's no codec type to choose.
