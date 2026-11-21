# T9 — Antennas and Feed Lines
*2 questions on the exam from a pool of 23*

## Group T9A — Antennas: vertical and horizontal polarization, concept of antenna gain, definition and types of beam antennas, antenna loading, common portable and mobile antennas, relationships between resonant length and frequency, dipole pattern

### T9A01
**What is a beam antenna?**
- A) An antenna built from square aluminum beams
- B) An omnidirectional antenna invented by Clarence Beam
- **C) An antenna that concentrates signals in one direction** ✅
- D) An antenna that focuses the signal into two intense rays

> A beam antenna is a directional antenna that concentrates its signal in one direction for increased gain. Yagi-Uda arrays and quad antennas are common types. By focusing energy in one direction, beam antennas provide more gain than omnidirectional designs.

### T9A02
**Which of the following describes a type of antenna loading?**
- **A) Electrically lengthening by inserting inductors in radiating elements** ✅
- B) Inserting a resistor in the radiating portion of the antenna to make it resonant
- C) Installing a spring in the base of a mobile vertical antenna to make it more flexible
- D) Strengthening the radiating elements of a beam antenna to better resist wind damage

> Antenna loading means adding a coil (an inductor) to the radiating element so a physically short antenna acts electrically longer and becomes resonant at a lower frequency. That is how short mobile HF whips work on bands where a full-size antenna would be far too long. A resistor would just waste power as heat, and a base spring or stronger elements are mechanical changes, not loading.

### T9A03
**How is the polarization of an antenna described?**
- A) By the shape of the driven element
- **B) By the orientation of the electric field** ✅
- C) By the orientation of the magnetic field
- D) By the direction of radiation

> Antenna polarization is described by the orientation of the electric field. If the electric field oscillates vertically, the antenna is vertically polarized. If horizontally, it's horizontally polarized. Matching polarization between stations maximizes signal transfer.

### T9A04
**What is a disadvantage of a handheld radio transceiver’s short flexible antenna compared to a full-sized quarter-wave antenna?**
- **A) It has low efficiency** ✅
- B) It transmits only circularly polarized signals
- C) It is more susceptible to receiver desensitization
- D) It only works on analog signals, not digital ones

> The short flexible antenna (rubber duck) on a handheld has less efficient radiation and lower gain compared to a full-sized quarter-wave antenna. The rubber duck is convenient but compromises performance — it doesn't radiate as effectively because it's much shorter than optimal.

### T9A05
**Which of the following increases the resonant frequency of a dipole antenna?**
- A) Lengthening it
- B) Inserting coils in series with radiating wires
- **C) Shortening it** ✅
- D) Adding capacitive loading to the ends of the radiating wires

> A dipole's resonant frequency goes up as it gets shorter, because frequency and length are inversely related. With the dipole formula, length in feet equals 468 divided by frequency in megahertz, so a 33-foot dipole resonates near 14.2 megahertz, and trimming it to 32 feet raises that to about 14.6 megahertz. Lengthening it, adding series coils, or adding capacitive loading at the ends all make it electrically longer, which lowers the resonant frequency instead.

### T9A06
**Which of the following types of antennas offers the greatest gain?**
- A) 5/8 wave vertical
- B) Isotropic
- C) J pole
- **D) Yagi** ✅

> A Yagi antenna offers the greatest gain among common amateur antennas. Its multiple elements (driven element, reflector, and directors) work together to focus energy in one direction, providing significant gain over a simple dipole.

### T9A07
**What is a potential drawback of using a handheld VHF transceiver inside a vehicle that lacks an externally mounted antenna?**
- **A) Signal strength is reduced due to the shielding effect of the vehicle** ✅
- B) The bandwidth of the antenna will decrease, increasing SWR
- C) The SWR might decrease, decreasing the signal strength
- D) The handheld will overheat due to reflected power in the vehicle

> Using a handheld VHF transceiver inside a vehicle without an external antenna is problematic because the vehicle's metal body significantly attenuates the signal, reducing both transmitted and received signal strength. An external antenna mounted on the vehicle is much more effective.

### T9A08
**Why is a 19-inch-long vertical antenna often used on 2 meters?**
- A) It has high gain
- B) It is a resonant half-wave
- **C) It is a resonant quarter-wave** ✅
- D) It has low RF radiation exposure

> A 19-inch vertical is a resonant quarter-wave on 2 meters. The quarter-wave formula gives length in feet: 234 divided by 146 megahertz is about 1.6 feet, and 1.6 feet times 12 is about 19 inches. A half-wave would be about twice that long, and the length has nothing to do with high gain or low RF exposure. A quarter-wave vertical is one of the simplest and most practical antennas for VHF.

### T9A09
**What is an advantage of a 5/8-wavelength whip antenna for VHF or UHF mobile service compared to a 1/4-wave antenna?**
- **A) It has more gain** ✅
- B) It radiates at a higher angle
- C) It has lower SWR
- D) It has lower impedance

> A 5/8-wavelength whip antenna for VHF or UHF mobile service has more gain than a 1/4-wave antenna. The 5/8-wave design concentrates more of its radiation toward the horizon rather than upward, which is exactly what you want for mobile ground-to-ground communication.

### T9A10
**In which direction does a half-wave dipole antenna radiate the strongest signal?**
- A) Equally in all directions
- B) Off the ends of the antenna
- C) In the direction of the feed line
- **D) Broadside to the antenna** ✅

> A half-wave dipole radiates most strongly broadside, meaning at right angles to the wire. Its pattern looks like a donut around the wire, with deep nulls off the ends. So it is not equally strong in all directions, it is weakest off the ends, and the feed line direction has nothing to do with it.

### T9A11
**What is antenna gain?**
- A) The additional power that is added to the transmitter power
- B) The additional power that is required in the antenna when transmitting on a higher frequency
- **C) The increase in signal strength in a specified direction compared to a reference antenna** ✅
- D) The increase in impedance on receive or transmit compared to a reference antenna

> Antenna gain is the increase in signal strength in a particular direction compared to a reference antenna, such as an isotropic radiator (dBi) or a dipole (dBd). An antenna can't add power; it gets gain by concentrating the power it already has toward some directions and away from others. That is why the answers about added power or increased impedance are wrong.

## Group T9B — Feed lines: types, attenuation vs frequency, selecting; SWR concepts; Antenna tuners (couplers); RF Connectors: selecting, weather protection

### T9B01
**Which of the following connectors should be carefully taped for weather protection when used outdoors?**
- A) PL259
- B) BNC
- C) Type N
- **D) All these choices are correct** ✅

> All RF connectors used outdoors — PL-259, Type N, and BNC — should be carefully taped or sealed for weather protection. Moisture in any connector causes corrosion and signal loss. Use self-fusing silicone tape or commercial weatherproofing kits.

### T9B02
**What is the most common impedance of coaxial cables used in amateur radio?**
- A) 8 ohms
- **B) 50 ohms** ✅
- C) 600 ohms
- D) 12 ohms

> The characteristic impedance of most common amateur radio coaxial cable is 50 ohms. This is the standard impedance for amateur radio — 75-ohm cable is used for TV and cable systems, but amateur equipment is designed for 50 ohms.

### T9B03
**Why is coaxial cable the most common feed line for amateur radio antenna systems?**
- **A) It is easy to use and requires few special installation considerations** ✅
- B) It has less loss than any other type of feed line
- C) It can handle more power than any other type of feed line
- D) It is less expensive than any other type of feed line

> Coax is the most popular feed line because it's easy to use: you can run it along walls, through windows, near metal, or bundle it with other cables without the careful spacing that open-wire line needs. It is not the lowest-loss feed line; open-wire and ladder line have much less loss than ordinary flexible coax. It doesn't handle the most power, and it isn't always the cheapest either. Convenience is the reason.

### T9B04
**What is the major function of an antenna tuner (antenna coupler)?**
- **A) It matches the antenna system impedance to the transceiver's output impedance** ✅
- B) It helps a receiver automatically tune in weak stations
- C) It allows an antenna to be used on both transmit and receive
- D) It automatically selects the proper antenna for the frequency band being used

> An antenna tuner, or antenna coupler, transforms the impedance of the antenna system into the 50 ohms your transceiver expects, so the radio sees a good match and can deliver full power. It doesn't fix the antenna itself; the mismatch is still there on the antenna side of the tuner. It doesn't tune in weak stations, switch between transmit and receive, or pick antennas for you.

### T9B05
**What happens as the frequency of a signal in coaxial cable is increased?**
- A) The characteristic impedance decreases
- B) The loss decreases
- C) The characteristic impedance increases
- **D) The loss increases** ✅

> As frequency goes up, the loss in coaxial cable goes up too. Conductor losses from skin effect and losses in the insulating dielectric both grow with frequency, which is why the same cable that's fine on HF can be quite lossy at 440 megahertz. The characteristic impedance, such as 50 ohms, is set by the cable's dimensions and dielectric and stays essentially the same, so the impedance choices are wrong.

### T9B06
**Which of the following connector types is most suitable as an RF connector for frequencies above 400 MHz?**
- A) PL-259
- **B) Type N** ✅
- C) RS-213
- D) DB-25

> Type N connectors are most suitable for frequencies above 400 MHz. They maintain consistent impedance at UHF and above, unlike PL-259 connectors whose performance degrades at higher frequencies.

### T9B07
**Which of the following is true of PL-259 type coax connectors?**
- A) They are preferred for microwave operation
- B) They are watertight
- **C) They are commonly used at HF and VHF frequencies** ✅
- D) They are a bayonet-type connector

> PL-259 plugs and their SO-239 sockets are the most common connectors on amateur gear, and they're widely used at HF and VHF. They are not preferred for microwaves because their impedance isn't constant, so Type N or SMA connectors are used up there. They aren't watertight, so they must be sealed outdoors, and they screw on with a threaded coupling rather than the bayonet twist-lock of a BNC.

### T9B08
**Which of the following is a source of loss in coaxial feed line?**
- A) Water intrusion into coaxial connectors
- B) High SWR
- C) Multiple connectors in the line
- **D) All these choices are correct** ✅

> All three are real sources of loss in a coax feed line. Water that gets into connectors soaks into the cable and sharply increases loss. High SWR adds loss because reflected power travels back and forth through the lossy cable. And every connector or adapter in the line adds a little loss of its own, so the best answer is all of these.

### T9B09
**What can cause erratic changes in SWR?**
- A) Local thunderstorm
- **B) Loose connection in the antenna or feed line** ✅
- C) Over-modulation
- D) Overload from a strong local station

> Erratic SWR, meaning readings that jump around, points to a loose or intermittent connection in the antenna or feed line, such as a loose connector, a broken conductor, or a bad solder joint that makes and breaks contact. As the contact changes, the impedance the transmitter sees changes, so the SWR reading changes with it. A fault that doesn't change, such as a wrong-length antenna, gives a steady high SWR instead. Thunderstorms, over-modulation, and a strong local station don't change the antenna's match.

### T9B10
**What is the electrical difference between RG-58 and RG-213 coaxial cable?**
- A) There is no significant difference between the two types
- B) RG-58 cable has two shields
- **C) RG-213 cable has less loss at a given frequency** ✅
- D) RG-58 cable can handle higher power levels

> RG-213 has less loss than RG-58 at any given frequency, because it's a much thicker cable with a larger center conductor and more dielectric between the conductors. Both are 50-ohm cables with a single braided shield, so the claim that RG-58 has two shields is false. RG-213 also handles more power, not RG-58. RG-58 is thinner and more flexible, which is fine for short runs.

### T9B11
**Which of the following types of feed line has the lowest loss?**
- A) 50-ohm flexible coax
- B) Multi-conductor unbalanced cable
- **C) Air-insulated hardline** ✅
- D) 75-ohm flexible coax

> Air-dielectric hardline (rigid or semi-rigid coaxial cable) has the lowest loss of common feed line types. However, it's expensive, heavy, and difficult to install. For most amateur stations, high-quality flexible coax is a practical compromise.

### T9B12
**What is standing wave ratio (SWR)?**
- **A) A measure of how well a load is matched to a transmission line** ✅
- B) The ratio of amplifier power output to input
- C) The transmitter efficiency ratio
- D) An indication of the quality of your station’s ground connection

> Standing wave ratio (SWR) is a measure of how well a load is matched to a transmission line. An SWR of 1:1 is a perfect match — all power goes to the antenna. Higher SWR means more power is reflected back toward the transmitter, reducing efficiency and potentially damaging equipment.
