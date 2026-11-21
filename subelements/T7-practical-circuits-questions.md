# T7 — Practical Circuits
*4 questions on the exam from a pool of 44*

## Group T7A — Station equipment: receivers, transceivers, transmitter amplifiers, RF preamplifiers, transverters; Basic radio circuit concepts and terminology: sensitivity, selectivity, mixers, oscillators, Push-To-Talk (PTT), VFO, modulation

### T7A01
**Which term describes the ability of a receiver to detect the presence of a signal?**
- A) RF gain
- **B) Sensitivity** ✅
- C) Selectivity
- D) Total Harmonic Distortion

> Sensitivity describes a receiver's ability to detect the presence of weak signals. A more sensitive receiver can pick up fainter signals. Sensitivity is typically measured in microvolts — the lower the number, the more sensitive the receiver.

### T7A02
**What is a transceiver?**
- **A) A device that combines a receiver and transmitter** ✅
- B) A device for matching feed line impedance to 50 ohms
- C) A device for automatically sending and decoding Morse code
- D) A device for converting receiver and transmitter frequencies to another band

> A transceiver combines a receiver and a transmitter in one unit, sharing circuits like frequency control and the power supply. Almost all modern amateur radios are transceivers. Matching feed line impedance is the job of an antenna tuner, and converting to another band is what a transverter does.

### T7A03
**Which of the following is used to convert a signal from one frequency to another?**
- A) Phase splitter
- **B) Mixer** ✅
- C) Inverter
- D) Amplifier

> A mixer converts a signal from one frequency to another by combining it with a local oscillator signal. The mixer produces sum and difference frequencies — this frequency conversion is at the heart of the superheterodyne receiver design used in virtually all modern radios.

### T7A04
**Which term describes the ability of a receiver to discriminate between multiple signals?**
- A) Discrimination ratio
- B) Sensitivity
- **C) Selectivity** ✅
- D) Harmonic distortion

> Selectivity is a receiver's ability to separate the signal you want from other signals on nearby frequencies, mostly thanks to its filters. Sensitivity is a different property, the ability to detect weak signals. Discrimination ratio sounds right but isn't the standard term, and harmonic distortion is about signal purity.

### T7A05
**What is the name of a circuit that generates a signal at a specific frequency?**
- A) Reactance modulator
- B) Phase modulator
- C) Low-pass filter
- **D) Oscillator** ✅

> An oscillator is a circuit that generates a signal at a specific frequency, and every transmitter and receiver uses one. Reactance and phase modulators change an existing signal rather than create one, and a low-pass filter only passes or blocks frequencies.

### T7A06
**What device converts the RF input and output of a transceiver to another band?**
- A) High-pass filter
- B) Low-pass filter
- **C) Transverter** ✅
- D) Phase converter

> A transverter converts a transceiver's RF input and output to another band, for example letting a 10-meter or 2-meter radio operate on a higher band. It converts both the transmitted and the received signals. High-pass and low-pass filters only pass or block frequencies without changing them, and a phase converter is electrical power equipment, not a radio device.

### T7A07
**What is the function of a transceiver’s PTT input?**
- A) Input for a key used to send CW
- **B) Switches transceiver from receive to transmit when grounded** ✅
- C) Provides a transmit tuning tone when grounded
- D) Input for a preamplifier tuning tone

> PTT stands for push to talk. Grounding the PTT input, usually by pressing the microphone button, switches the transceiver from receive to transmit. A CW key plugs into a separate key jack, and the PTT line doesn't generate any tuning tones.

### T7A08
**Which of the following describes combining speech with an RF carrier signal?**
- A) Impedance matching
- B) Oscillation
- **C) Modulation** ✅
- D) Low-pass filtering

> Modulation is the process of combining speech, data, or other information with an RF carrier signal. AM, FM, and single sideband are all types of modulation. Oscillation creates the carrier in the first place, impedance matching helps transfer power to the antenna, and low-pass filtering removes higher frequencies.

### T7A09
**What is the function of the switch which selects either SSB or CW-FM on some VHF power amplifiers?**
- A) Change the mode of the transmitted signal
- **B) Set the amplifier for proper operation in the selected mode** ✅
- C) Change the frequency range of the amplifier to operate in the proper segment of the band
- D) Reduce the received signal noise

> The SSB/CW-FM switch on VHF power amplifiers sets the amplifier for proper operation in the selected mode. SSB and CW need linear amplification to preserve the signal's amplitude variations, while FM can use more efficient non-linear amplification.

### T7A10
**What can be added to the output of a transceiver to increase the transmitted output power?**
- A) A potentiometer
- **B) An RF power amplifier** ✅
- C) An impedance multiplier
- D) All these choices are correct

> An RF power amplifier (or linear amplifier) can be added to the output of a transceiver to increase transmitted power. It boosts the transmitter's signal before it reaches the antenna.

### T7A11
**What is the function of the Variable Frequency Oscillator (VFO) circuit in a transceiver?**
- **A) Set the receive and transmit frequency** ✅
- B) Provide automatic frequency control
- C) Inject a variable frequency to allow CW reception
- D) Generate and demodulate single sideband signals

> The Variable Frequency Oscillator (VFO) circuit in a transceiver sets the receive and transmit frequency. By adjusting the VFO, you tune across the band. The VFO determines what frequency you're operating on — it's the tuning heart of the radio.

## Group T7B — Symptoms, causes, and cures of common transmitter and receiver problems: overload and overdrive, distortion, interference and consumer electronics, RF feedback

### T7B01
**What can you do if you are told your FM handheld or mobile transceiver is over-deviating?**
- A) Talk louder into the microphone
- B) Let the transceiver cool off
- C) Change to a higher power level
- **D) Talk farther away from the microphone** ✅

> If your FM handheld or mobile is over-deviating, you're talking too loudly or too close to the microphone. Back away from the mic and speak at a normal conversational level. Over-deviation causes distorted, hard-to-understand audio on the receiving end.

### T7B02
**What would cause a broadcast AM or FM radio to receive an amateur radio transmission unintentionally?**
- **A) The receiver is unable to reject strong signals outside the AM or FM band** ✅
- B) The microphone gain of the transmitter is turned up too high
- C) The audio amplifier of the transmitter is overloaded
- D) The deviation of an FM transmitter is set too low

> If a broadcast AM or FM radio is receiving your amateur transmissions, the problem is fundamental overload — the consumer receiver can't reject your strong nearby signal because it has poor front-end filtering. The issue is with their receiver, not your transmitter.

### T7B03
**Which of the following can cause radio frequency interference?**
- A) Fundamental overload
- B) Harmonics
- C) Spurious emissions
- **D) All these choices are correct** ✅

> All three can cause radio frequency interference. Fundamental overload happens when a strong signal overwhelms a nearby receiver, harmonics are multiples of your transmit frequency that can land on other services, and spurious emissions are other unwanted signals from a transmitter. Since all three apply, D is correct.

### T7B04
**Which of the following might be the cause of low RF power output from a solid-state transceiver?**
- A) Poor amplifier noise figure
- B) Poor amplifier linearity
- C) Low SWR
- **D) High SWR** ✅

> A high SWR can cause low RF power output from a solid-state transceiver. When the antenna system presents a poor match (high SWR), most modern radios automatically reduce power to protect their output transistors. Fix the antenna match to restore full power.

### T7B05
**Which of the following might reduce interference by an amateur station to a non-amateur over-the-air radio receiver?**
- **A) Block the amateur signal with a filter at the antenna input of the affected receiver** ✅
- B) Block the interfering signal with a filter on the amateur transmitter
- C) Switch the transmitter from FM to SSB
- D) Switch the transmitter to a narrow-band mode

> To reduce interference to a non-amateur over-the-air radio receiver, you can install a filter at the receiver's antenna input. A filter that passes only the desired broadcast frequencies and rejects your amateur signal addresses the fundamental overload problem.

### T7B06
**Which of the following actions should you take if a neighbor tells you that your station’s transmissions are interfering with their radio or TV reception?**
- **A) Make sure that your station is functioning properly and that it does not cause interference to your own radio or television when it is tuned to the same channel** ✅
- B) Immediately turn off your transmitter and contact the nearest FCC office for assistance
- C) Install a harmonic doubler on the output of your transmitter and tune it until the interference is eliminated
- D) All these choices are correct

> Start by checking your own station. Make sure it's working properly, and see whether it interferes with your own radio or TV tuned to the same channel. If your own equipment is clean, the problem may be in the neighbor's receiver. There's no need to shut down and call the FCC right away, and a harmonic doubler would make interference worse, not better.

### T7B07
**Which of the following can reduce interference to a 2-meter band transceiver from a nearby commercial FM station?**
- A) Installing an RF preamplifier
- B) Using double-shielded coaxial cable
- C) Installing bypass capacitors on the microphone cable
- **D) Installing a band-reject filter** ✅

> A band-reject filter tuned to the interfering commercial FM frequency can reduce interference to a 2-meter transceiver from a nearby commercial FM station. The filter notches out the specific frequency causing the problem while passing your amateur signals.

### T7B08
**What should you do if something in a neighbor’s home is causing harmful interference to your amateur station?**
- A) Work with your neighbor to identify the offending device
- B) Politely inform your neighbor that FCC rules prohibit the use of devices that cause interference
- C) Make sure your station meets the standards of good amateur practice
- **D) All these choices are correct** ✅

> All three are correct. Work with your neighbor to find the offending device, politely explain that FCC rules prohibit using devices that cause harmful interference, and make sure your own station meets the standards of good amateur practice. A friendly, cooperative approach works far better than confrontation.

### T7B09
**What should be the first step to resolve non-fiber optic cable TV interference caused by your amateur radio transmission?**
- A) Add a low-pass filter to the TV antenna input
- B) Add a high-pass filter to the TV antenna input
- C) Add a preamplifier to the TV antenna input
- **D) Be sure all TV feed line coaxial connectors are installed properly** ✅

> The first step is to make sure all the TV feed line coaxial connectors are installed properly. Loose or poorly installed connectors let RF leak into the cable system, which is a common cause of cable TV interference. Check that easy fix before adding filters, and never add a preamplifier, which would only amplify the problem.

### T7B10
**What might be a problem if you receive a report that your audio signal through an FM repeater is distorted or unintelligible?**
- A) Your transmitter is slightly off frequency
- B) You are speaking too loudly or too close to the microphone
- C) You are in a bad location
- **D) All these choices are correct** ✅

> All three can cause distorted FM audio through a repeater. Being slightly off frequency can distort your signal in the repeater's receiver, speaking too loudly or too close to the microphone over-deviates your signal, and a bad location causes multipath or weak-signal problems. Since all three apply, D is correct.

### T7B11
**Which of the following can eliminate distorted voice transmissions?**
- A) Adding extra feedline to the antenna to lower SWR
- B) Turning the radio on and off to reset the computer-controlled circuitry
- **C) Adding a clip-on ferrite “choke” to the microphone cable to prevent the transmitted signal from feeding back into the transmitter** ✅
- D) Turning the squelch control fully clockwise to prevent the transmitted signal from triggering the squelch circuit

> Adding a clip-on ferrite "choke" to the microphone cable can eliminate distorted voice transmissions caused by RF feedback. The ferrite prevents the transmitted RF signal from traveling back along the mic cable and feeding back into the transmitter's audio input.

## Group T7C — Antenna and transmission line measurements and troubleshooting: measuring SWR, effects of high SWR, causes of feed line failures; Basic coaxial cable characteristics; Use of dummy loads when testing

### T7C01
**What is the primary purpose of a dummy load?**
- **A) To prevent transmitting signals over the air when making tests** ✅
- B) To prevent over-modulation of a transmitter
- C) To improve the efficiency of an antenna
- D) To improve the signal-to-noise ratio of a receiver

> A dummy load is used in place of an antenna for testing a transmitter without radiating a signal. It absorbs the transmitter's power as heat, letting you test and tune without causing interference. Every well-equipped station should have one.

### T7C02
**Which of the following is used to determine if an antenna is resonant at the desired operating frequency?**
- A) A VTVM
- **B) An antenna analyzer** ✅
- C) A Q meter
- D) A frequency counter

> An antenna analyzer measures an antenna's impedance and SWR across a range of frequencies, so it shows you where the antenna is resonant. A frequency counter only measures the frequency of a signal, a VTVM is a type of voltmeter, and a Q meter tests components, not antennas.

### T7C03
**What does a typical RF dummy load consist of?**
- A) A low-voltage power supply and an AC relay
- **B) A 50-ohm non-inductive resistor mounted on a heat sink** ✅
- C) A low-voltage power supply and a DC relay
- D) A 50-ohm inductive reactance mounted in a shielded enclosure

> A typical RF dummy load consists of a 50-ohm non-inductive resistor mounted on a heat sink. The non-inductive design ensures it presents a pure 50-ohm load at radio frequencies. The heat sink dissipates the power as heat.

### T7C04
**What reading on an SWR meter indicates a perfect impedance match between the antenna and the feed line?**
- A) 50:50
- B) Zero
- **C) 1:1** ✅
- D) Full Scale

> An SWR reading of 1 to 1 means a perfect match. The antenna's impedance equals the feed line's, and no power is reflected back toward the transmitter. SWR can never be less than 1 to 1, so a reading of zero isn't possible, and 50 to 50 isn't how SWR is expressed.

### T7C05
**Why do most solid-state transmitters reduce output power as SWR increases beyond a certain level?**
- **A) To protect the RF output amplifier transistors** ✅
- B) To comply with FCC rules on spectral purity
- C) Because power supplies cannot supply enough current at high SWR
- D) To lower the SWR on the transmission line

> Most solid-state transmitters automatically reduce output power as SWR increases to protect the RF output amplifier transistors. Excessive reflected power can overheat and destroy the output transistors. The fold-back circuit is a safety mechanism.

### T7C06
**What does an SWR reading of 4:1 indicate?**
- A) Loss of -4 dB
- B) Good impedance match
- C) Gain of +4 dB
- **D) Impedance mismatch** ✅

> An SWR of 4 to 1 indicates an impedance mismatch between the antenna system and the feed line. A good match is close to 1 to 1. SWR is a ratio, not a gain or loss in decibels, so the choices with dB values are wrong.

### T7C07
**What happens to power lost in a feed line?**
- A) It increases the SWR
- B) It is radiated as harmonics
- **C) It is converted into heat** ✅
- D) It distorts the signal

> Power lost in a feed line is converted into heat in the conductors and the insulating material. It isn't radiated as harmonics, and feed line loss doesn't increase the SWR. In fact, loss makes the SWR measured at the transmitter look better than it really is at the antenna.

### T7C08
**Which instrument can be used to determine SWR?**
- A) Voltmeter
- B) Ohmmeter
- C) Iambic pentameter
- **D) Directional wattmeter** ✅

> A directional wattmeter measures both forward and reflected power, and from those two readings you can determine the SWR. A voltmeter and an ohmmeter can't separate forward power from reflected power. Iambic pentameter is a joke answer. It's a rhythm used in poetry, not a radio instrument.

### T7C09
**Which of the following causes failure of coaxial cables?**
- **A) Moisture contamination** ✅
- B) Solder flux contamination
- C) Rapid fluctuation in transmitter output power
- D) Operation at 100% duty cycle for an extended period

> Moisture contamination is the main cause of coaxial cable failure. Water gets in through a damaged jacket or a poorly sealed connector, increases the cable's loss, and corrodes the conductors. That's why outdoor connectors should always be weatherproofed. Power changes and long transmissions don't harm coax that's used within its ratings.

### T7C10
**Why should the outer jacket of coaxial cable be resistant to ultraviolet light?**
- A) Ultraviolet light can increase the resistance of the conductors
- B) Ultraviolet light can increase losses in the cable’s jacket
- C) Ultraviolet and RF signals can mix, causing interference
- **D) Ultraviolet light can damage the jacket and allow water to enter the cable** ✅

> Coaxial cable's outer jacket must be resistant to UV light because ultraviolet radiation degrades the jacket material, allowing moisture to enter the cable. Moisture inside coax dramatically increases signal loss and can destroy the cable.

### T7C11
**What is an advantage of foam-dielectric versus solid-dielectric coaxial cable?**
- A) It is more resistant to moisture contamination
- B) It has higher voltage breakdown
- **C) It has less loss per foot** ✅
- D) It has a better impedance match to 50 ohms

> Foam-dielectric coaxial cable has less loss per foot compared to solid-dielectric types. The foam dielectric has a lower effective dielectric constant, which reduces signal loss. The trade-off is that foam cable is more susceptible to moisture contamination.

## Group T7D — Using basic test instruments: voltmeter, ammeter, and ohmmeter; Soldering

### T7D01
**Which instrument would you use to measure electric potential?**
- A) An ammeter
- **B) A voltmeter** ✅
- C) A potentiometer
- D) An ohmmeter

> A voltmeter is used to measure electric potential (voltage). It's connected in parallel across the component or circuit you want to measure. A voltmeter should have high input impedance to avoid disturbing the circuit.

### T7D02
**How is a voltmeter connected to a component to measure applied voltage?**
- A) In series
- **B) In parallel** ✅
- C) In quadrature
- D) In phase

> A voltmeter is connected in parallel, which means across the component, so it can measure the voltage difference between its two ends. A good voltmeter draws very little current, so it barely disturbs the circuit. A series connection is used for measuring current, and in quadrature and in phase describe the timing between AC signals, not how meters are connected.

### T7D03
**When configured to measure current, how is a multimeter connected to a component?**
- **A) In series** ✅
- B) In parallel
- C) In quadrature
- D) In phase

> To measure current, the multimeter is connected in series, so all the current flowing through the component also flows through the meter. That usually means opening the circuit and inserting the meter. A meter set for current has very low resistance, so connecting it in parallel can short the circuit and blow the meter's fuse.

### T7D04
**Which instrument is used to measure electric current?**
- A) An ohmmeter
- B) An electrometer
- C) A voltmeter
- **D) An ammeter** ✅

> An ammeter measures electric current, in amperes, and is connected in series with the circuit. A voltmeter measures voltage and an ohmmeter measures resistance. An electrometer is a specialized laboratory instrument for measuring charge and tiny currents or voltages in very high-impedance circuits; it isn't the everyday tool for measuring current.

### T7D05
**How does an ohmmeter measure the resistance of a circuit or component?**
- **A) By applying a small current and measuring the resulting voltage** ✅
- B) By placing a variable resistor in parallel with the circuit
- C) By placing a variable resistor in series with the circuit
- D) By applying a variable voltage and measuring the resulting current change

> An ohmmeter measures resistance by applying a small known current from its internal battery and measuring the resulting voltage across the component under test. Using Ohm's Law (R = E/I), the meter calculates and displays the resistance. This is why you need to disconnect the component — the meter's own current must be the only current flowing through it.

### T7D06
**Which of the following can damage a multimeter?**
- A) Attempting to measure resistance using the voltage setting
- B) Failing to connect one of the probes to ground
- **C) Attempting to measure voltage when using the resistance setting** ✅
- D) Not allowing it to warm up properly

> Measuring voltage with the meter set to resistance can damage a multimeter. In resistance mode the meter sends its own small current through the circuit, and an outside voltage can overload those sensitive circuits. The reverse mistake, measuring resistance on a voltage setting, just gives a useless reading. Multimeters don't need to warm up, and neither probe has to be connected to ground.

### T7D07
**Which of the following measurements are made using a multimeter?**
- A) Signal strength and noise
- B) Impedance and reactance
- **C) Voltage and resistance** ✅
- D) All these choices are correct

> A multimeter measures voltage, current, and resistance, so voltage and resistance is the right choice. Signal strength and noise need a receiver or spectrum analyzer, and impedance and reactance at radio frequencies need an instrument like an antenna analyzer. Because those two choices are wrong, all these choices is wrong too.

### T7D08
**Which of the following types of solder should not be used for radio and electronic applications?**
- **A) Acid-core solder** ✅
- B) Lead-tin solder
- C) Rosin-core solder
- D) Tin-copper solder

> Acid-core solder should never be used for radio and electronics work. Its acid flux is corrosive and will eat away at wires, components, and circuit boards over time. Use rosin-core solder instead. Lead-tin and tin-copper describe the solder metal itself, and both are used in electronics.

### T7D09
**What is the characteristic appearance of a cold tin-lead solder joint?**
- A) Dark black spots
- B) A bright or shiny surface
- **C) A rough or lumpy surface** ✅
- D) A greenish tinge

> A cold tin-lead solder joint has a rough, grainy, or dull gray appearance. Good solder joints are smooth and shiny. If your joint looks grainy or dull, reheat it with the soldering iron and let it flow properly.

### T7D10
**What reading indicates that an ohmmeter is connected across a large, discharged capacitor?**
- **A) Increasing resistance with time** ✅
- B) Decreasing resistance with time
- C) Steady full-scale reading
- D) Alternating between open and short circuit

> When you connect an ohmmeter across a large, discharged capacitor, the reading starts low and the resistance increases with time. The meter's internal battery charges the capacitor, so current flows freely at first and then tapers off as the capacitor charges. This makes a handy quick check that a capacitor is charging normally.

### T7D11
**Which of the following precautions should be taken when measuring in-circuit resistance with an ohmmeter?**
- A) Ensure that the applied voltages are correct
- **B) Ensure that the circuit is not powered** ✅
- C) Ensure that the circuit is grounded
- D) Ensure that the circuit is operating at the correct frequency

> Before you measure resistance in a circuit, make sure the circuit is not powered. An ohmmeter uses its own internal battery, so any voltage already present will throw off the reading and could damage the meter. Grounding the circuit or checking its voltages or frequency doesn't solve that problem.
