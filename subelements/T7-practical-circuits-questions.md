# T7 — Practical Circuits
*4 questions on the exam from a pool of 44*

## Group T7A — Radio Station Equipment: Receivers, Transmitters, Transceivers

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

> The correct answer is A device that combines a receiver and transmitter.

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

> Selectivity is the correct term or definition for this question.

### T7A05
**What is the name of a circuit that generates a signal at a specific frequency?**
- A) Reactance modulator
- B) Phase modulator
- C) Low-pass filter
- **D) Oscillator** ✅

> The correct answer is Oscillator.

### T7A06
**What device converts the RF input and output of a transceiver to another band?**
- A) High-pass filter
- B) Low-pass filter
- **C) Transverter** ✅
- D) Phase converter

> The correct answer is C) Transverter.

### T7A07
**What is the function of a transceiver’s PTT input?**
- A) Input for a key used to send CW
- **B) Switches transceiver from receive to transmit when grounded** ✅
- C) Provides a transmit tuning tone when grounded
- D) Input for a preamplifier tuning tone

> The correct answer is Switches transceiver from receive to transmit when grounded.

### T7A08
**Which of the following describes combining speech with an RF carrier signal?**
- A) Impedance matching
- B) Oscillation
- **C) Modulation** ✅
- D) Low-pass filtering

> The correct choice here is Modulation.

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

## Group T7B — Interference, Troubleshooting, and RF Feedback

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

> All of the listed choices are correct for this question, so D is the right answer.

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

> The correct choice here is Make sure that your station is functioning properly and that it does not cause interference to your own radio or television when it is tuned to the same channel.

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

> All of the listed choices are correct for this question, so D is the right answer.

### T7B09
**What should be the first step to resolve non-fiber optic cable TV interference caused by your amateur radio transmission?**
- A) Add a low-pass filter to the TV antenna input
- B) Add a high-pass filter to the TV antenna input
- C) Add a preamplifier to the TV antenna input
- **D) Be sure all TV feed line coaxial connectors are installed properly** ✅

> The correct answer is D) Be sure all TV feed line coaxial connectors are installed properly.

### T7B10
**What might be a problem if you receive a report that your audio signal through an FM repeater is distorted or unintelligible?**
- A) Your transmitter is slightly off frequency
- B) You are speaking too loudly or too close to the microphone
- C) You are in a bad location
- **D) All these choices are correct** ✅

> All of the listed choices are correct for this question, so D is the right answer.

### T7B11
**Which of the following can eliminate distorted voice transmissions?**
- A) Adding extra feedline to the antenna to lower SWR
- B) Turning the radio on and off to reset the computer-controlled circuitry
- **C) Adding a clip-on ferrite “choke” to the microphone cable to prevent the transmitted signal from feeding back into the transmitter** ✅
- D) Turning the squelch control fully clockwise to prevent the transmitted signal from triggering the squelch circuit

> Adding a clip-on ferrite "choke" to the microphone cable can eliminate distorted voice transmissions caused by RF feedback. The ferrite prevents the transmitted RF signal from traveling back along the mic cable and feeding back into the transmitter's audio input.

## Group T7C — Antenna Measurements, Feed Lines, and Test Equipment

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

> The correct choice here is An antenna analyzer.

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

> The correct answer is C) 1:1.

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

> Impedance mismatch is the correct term or definition for this question.

### T7C07
**What happens to power lost in a feed line?**
- A) It increases the SWR
- B) It is radiated as harmonics
- **C) It is converted into heat** ✅
- D) It distorts the signal

> The correct answer is C) It is converted into heat.

### T7C08
**Which instrument can be used to determine SWR?**
- A) Voltmeter
- B) Ohmmeter
- C) Iambic pentameter
- **D) Directional wattmeter** ✅

> The correct answer is D) Directional wattmeter.

### T7C09
**Which of the following causes failure of coaxial cables?**
- **A) Moisture contamination** ✅
- B) Solder flux contamination
- C) Rapid fluctuation in transmitter output power
- D) Operation at 100% duty cycle for an extended period

> The correct choice here is Moisture contamination.

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

## Group T7D — Multimeters, Soldering, and Basic Measurements

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

> In parallel is the correct measurement method, tool, or precaution here.

### T7D03
**When configured to measure current, how is a multimeter connected to a component?**
- **A) In series** ✅
- B) In parallel
- C) In quadrature
- D) In phase

> In series is the correct measurement method, tool, or precaution here.

### T7D04
**Which instrument is used to measure electric current?**
- A) An ohmmeter
- B) An electrometer
- C) A voltmeter
- **D) An ammeter** ✅

> An ammeter is the correct measurement method, tool, or precaution here.

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

> Attempting to measure voltage when using the resistance setting is the correct measurement method, tool, or precaution here.

### T7D07
**Which of the following measurements are made using a multimeter?**
- A) Signal strength and noise
- B) Impedance and reactance
- **C) Voltage and resistance** ✅
- D) All these choices are correct

> Voltage and resistance is the correct measurement method, tool, or precaution here.

### T7D08
**Which of the following types of solder should not be used for radio and electronic applications?**
- **A) Acid-core solder** ✅
- B) Lead-tin solder
- C) Rosin-core solder
- D) Tin-copper solder

> Acid-core solder is the correct measurement method, tool, or precaution here.

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

> Increasing resistance with time is the correct measurement method, tool, or precaution here.

### T7D11
**Which of the following precautions should be taken when measuring in-circuit resistance with an ohmmeter?**
- A) Ensure that the applied voltages are correct
- **B) Ensure that the circuit is not powered** ✅
- C) Ensure that the circuit is grounded
- D) Ensure that the circuit is operating at the correct frequency

> Ensure that the circuit is not powered is the correct measurement method, tool, or precaution here.
