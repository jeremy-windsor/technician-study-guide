#!/usr/bin/env python3
"""Generate question files for each subelement from the 2026-2030 pool JSON.

Reads pools/2026-2030/questions.json and outputs one markdown file per
subelement into subelements/, matching the existing study-guide format.
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict

REPO = Path(__file__).resolve().parent.parent
POOL_PATH = REPO / "pools" / "2026-2030" / "questions.json"
OUTPUT_DIR = REPO / "subelements"

# Mapping of subelement IDs to output filenames (stem only)
SUBELEMENT_FILES = {
    "T0": "T0-safety",
    "T1": "T1-fcc-rules",
    "T2": "T2-operating-procedures",
    "T3": "T3-radio-waves",
    "T4": "T4-amateur-practices",
    "T5": "T5-electrical-principles",
    "T6": "T6-components",
    "T7": "T7-practical-circuits",
    "T8": "T8-signals-emissions",
    "T9": "T9-antennas-feedlines",
}

# Group descriptions — not in the JSON, carried forward from the pool PDF
GROUP_DESCRIPTIONS = {
    "T0A": "Electrical and Power Safety",
    "T0B": "Tower Safety, Antenna Installation, and Grounding",
    "T0C": "RF Exposure Safety",
    "T1A": "Purpose and permissible use of the Amateur Radio Service; operator/primary station license grant",
    "T1B": "Frequency allocations; emission modes; spectrum sharing; transmissions near band edges; power limits",
    "T1C": "Licensing; call signs; classes of licensees; renewal; grace periods; vanity call signs",
    "T1D": "Authorized and prohibited transmissions",
    "T1E": "Control operator and control types; station licensee responsibilities",
    "T1F": "Station identification; repeaters; third-party communications; club stations; FCC inspection",
    "T2A": "Station operation; choosing an operating frequency; calling another station; test transmissions; procedural signs; use of minimum power; band plans; repeater offsets",
    "T2B": "VHF/UHF operating practices; repeater operations; CTCSS and DTMF; DMR operation; simplex operations; Q signals",
    "T2C": "Emergency operations; tactical and priority traffic; net operations; RACES and ARES; radio direction finding; Radiogram header",
    "T3A": "Radio wave characteristics; how a radio signal travels; fading; multipath; polarization; knife-edge diffraction; absorption; weather and frequency effects",
    "T3B": "Electromagnetic wave properties; the electromagnetic spectrum; frequency and wavelength calculations",
    "T3C": "Propagation modes; ionospheric layers; sporadic E; tropospheric ducting; meteor scatter",
    "T4A": "Station setup; connecting a transceiver; power source; connecting digital equipment; RF grounding",
    "T4B": "Operating controls; tuning; use of filters; squelch; AGC; repeater access; DMR operation",
    "T5A": "Current, voltage, conductors, insulators, and alternating and direct current",
    "T5B": "Metric prefixes and unit conversions; decibels",
    "T5C": "Capacitance, inductance, impedance; power formula; calculating power",
    "T5D": "Ohm's Law; series and parallel circuits",
    "T6A": "Basic Electronic Components and Their Functions",
    "T6B": "Semiconductor Components: Diodes, Transistors, and LEDs",
    "T6C": "Circuit Diagrams and Schematic Symbols",
    "T6D": "Practical Circuit Components and Their Functions",
    "T7A": "Radio Station Equipment: Receivers, Transmitters, Transceivers",
    "T7B": "Interference, Troubleshooting, and RF Feedback",
    "T7C": "Antenna Measurements, Feed Lines, and Test Equipment",
    "T7D": "Multimeters, Soldering, and Basic Measurements",
    "T8A": "Modulation Modes and Bandwidth",
    "T8B": "Satellite Operations",
    "T8C": "VoIP, Internet Linking, Contesting, and Special Operations",
    "T8D": "Digital Modes, APRS, and Data Communications",
    "T9A": "Antenna Types and Their Characteristics",
    "T9B": "Feed Lines, Connectors, and SWR",
}

# ── Explanation generator ────────────────────────────────────────────
# Hand-written explanations for every question in the 2026-2030 pool.
# Key = question ID, value = explanation paragraph.

EXPLANATIONS: dict[str, str] = {}

# Questions whose legacy explanation text is off-topic for the 2026-2030 pool.
# These IDs intentionally fall back to a generated explanation that always
# matches the current question/answer pair.
FALLBACK_EXPLANATION_IDS = {
    # T1
    "T1B04", "T1B07", "T1B08", "T1B09", "T1B10", "T1B11", "T1B12",
    "T1C02", "T1C04", "T1C09", "T1C10", "T1C11",
    "T1D01", "T1D02", "T1D04", "T1D05", "T1D10", "T1D11",
    "T1E01", "T1E02", "T1E03", "T1E04", "T1E05", "T1E07", "T1E08",
    "T1F01", "T1F05", "T1F06", "T1F10",
    # T2
    "T2A05", "T2A10", "T2A11",
    "T2B02", "T2B03", "T2B04", "T2B09", "T2B10", "T2B11", "T2B13",
    "T2C02", "T2C07", "T2C09", "T2C10", "T2C11",
    # T3
    "T3A03", "T3A05", "T3A07", "T3A08", "T3A09", "T3A10",
    "T3B02", "T3B03", "T3B07", "T3B08", "T3B10",
    "T3C01", "T3C02", "T3C05", "T3C06", "T3C07", "T3C08", "T3C10", "T3C11",
    # T4
    "T4A05", "T4A06", "T4A09",
    "T4B02", "T4B03", "T4B06", "T4B10", "T4B11",
    # T5
    "T5A02", "T5A09", "T5A10", "T5A11",
    "T5B02", "T5B03", "T5B04", "T5B06", "T5B07", "T5B08", "T5B09", "T5B10", "T5B11", "T5B12",
    "T5C09", "T5C10", "T5C11",
    "T5D05", "T5D06", "T5D08", "T5D10", "T5D11", "T5D12",
    # T6
    "T6A02", "T6A03", "T6A05", "T6A08", "T6A10", "T6A11",
    "T6B01", "T6B02", "T6B06", "T6B08", "T6B09", "T6B10",
    "T6C09", "T6C10", "T6C11", "T6C12",
    "T6D01", "T6D04", "T6D05", "T6D08", "T6D09", "T6D10", "T6D11",
    # T7
    "T7A02", "T7A04", "T7A05", "T7A06", "T7A07", "T7A08",
    "T7B03", "T7B06", "T7B08", "T7B09", "T7B10",
    "T7C02", "T7C04", "T7C06", "T7C07", "T7C08", "T7C09",
    "T7D02", "T7D03", "T7D04", "T7D06", "T7D07", "T7D08", "T7D10", "T7D11",
    # T8
    "T8A01", "T8A02", "T8A03", "T8A04", "T8A11", "T8A12",
    "T8B01", "T8B02", "T8B03", "T8B04", "T8B05", "T8B06", "T8B07", "T8B08", "T8B09",
    "T8C01", "T8C07", "T8C09", "T8C11",
    "T8D01", "T8D03", "T8D07", "T8D10",
    # T9
    "T9A02", "T9A05", "T9A10", "T9A11",
    "T9B03", "T9B04", "T9B05", "T9B07", "T9B08", "T9B10",
}


def _load_explanations() -> None:
    """Populate the EXPLANATIONS dict.

    The explanations are defined inline below rather than in a separate
    data file so the script is fully self-contained.
    """
    # fmt: off
    E = EXPLANATIONS

    # ── T0A ──────────────────────────────────────────────────────────
    E["T0A01"] = "While 12 volts won't shock you through dry skin (your body's resistance is too high), a 12-volt battery without internal protection can deliver hundreds of amps if shorted, melting wires, causing burns, and potentially igniting hydrogen gas. The danger is massive current, not voltage."
    E["T0A02"] = "Electrical current through the body causes all three hazards: tissue heating (burns), disruption of cellular electrical functions (cardiac arrest, nerve damage), and involuntary muscle contractions (which can prevent you from letting go of the source). Even small currents through the heart can be fatal."
    E["T0A03"] = "In US wiring: Black = Hot (dangerous), White = Neutral, Green or bare = Ground. The black wire carries the full 120V AC potential and is the most dangerous conductor. This is standard NEC (National Electrical Code) color coding. Memorize it."
    E["T0A04"] = "A fuse opens (blows) when current exceeds its rating, disconnecting the circuit to prevent fire and equipment damage from overloads. It protects wiring and equipment — it does NOT prevent shock (the current needed to kill you is far below a typical fuse rating)."
    E["T0A05"] = "A 20-amp fuse would allow four times the designed current to flow through wiring rated for only 5 amps. The wires overheat and can start a fire before the fuse ever blows. Always replace fuses with the same rating — never larger. This is a fundamental fire safety rule."
    E["T0A06"] = "All three are essential safety practices. Three-wire plugs provide equipment grounding, a common safety ground prevents dangerous voltage differences between equipment, and ensuring high-voltage capacitors are discharged before opening equipment prevents lethal shocks. Layered safety is the best approach."
    E["T0A07"] = "Lightning arresters go where the feed line enters the building, mounted on a grounded panel. This stops lightning energy at the building entry point before it can enter your shack. Placing it at the radio or antenna wouldn't protect the building wiring and equipment between those points."
    E["T0A08"] = "The fuse goes in series with the hot (black) wire only. Fusing the neutral wire could create a dangerous condition where equipment appears de-energized but the hot wire is still live. A fuse in parallel would short-circuit the power line. Series with hot only = safe interruption."
    E["T0A09"] = "All ground rods must be bonded together to create a single ground system with no voltage differences between rods. During a lightning strike, separate unbonded grounds can have dangerous voltage differences. Bond everything together — electrical panel ground, radio ground, tower ground — into one unified system."
    E["T0A10"] = "Rapidly charging or discharging a battery without built-in protection generates excessive heat and can cause the battery to vent gas (out-gassing). In sealed batteries, this pressure buildup can cause rupture or explosion. Lead-acid and lithium batteries are both susceptible. Always use appropriate charge rates and batteries with proper protection."
    E["T0A11"] = "Large filter capacitors in power supplies can hold lethal voltages for minutes or even hours after the supply is turned off. Always treat a recently powered-off power supply as dangerous. High-voltage capacitors must be safely discharged before working on equipment. This has killed many technicians."
    E["T0A12"] = "Using a meter or leads not rated for the voltage being measured can result in arcing, insulation breakdown, and electrocution. Always check that your meter and probes are rated for the voltages involved. A CAT III or CAT IV rated meter is needed for high-voltage work. Low impedance meters would actually draw excessive current — you want high impedance."

    # ── T0B ──────────────────────────────────────────────────────────
    E["T0B01"] = "Lightning ground connections must be short and direct — long, winding paths have too much inductance for lightning's fast-rising pulse. Sharp right-angle bends are bad because they impede current flow and can cause arcing. Drip loops are irrelevant for grounding. Think: shortest path to earth."
    E["T0B02"] = "Tower climbing requires all three: proper training, continuous tie-off (never unclip), and an approved harness. Falls from towers are frequently fatal. This isn't optional safety gear — it's all mandatory. Many amateur radio operators have died from tower falls."
    E["T0B03"] = "Never climb a tower alone. Always have a ground observer who can call for help if you fall or become incapacitated. There are NO exceptions to this rule — not height, not task type, not experience level. A fall at 10 feet can kill you just as dead as one at 100 feet."
    E["T0B04"] = "Contact with overhead power lines during tower installation is one of the most common causes of amateur radio fatalities. A tower, antenna, or guy wire touching a power line is instantly lethal. Always survey for power lines before any antenna work. Never insulate a tower base — it should be grounded."
    E["T0B05"] = "Wind and vibration can gradually unscrew turnbuckles, loosening guy wires and potentially toppling the tower. A safety wire through the turnbuckle body prevents it from turning. This simple precaution can prevent catastrophic tower failure."
    E["T0B06"] = "The rule is clear: if the antenna falls in any direction, no part should be able to come within 10 feet of power lines. This accounts for the antenna's full height and reach when it falls. Power line contact kills — maintain clearance even in a worst-case scenario."
    E["T0B07"] = "Crank-up towers can collapse if the cable or winch fails. Never climb one unless it's fully retracted or has mechanical safety locks engaged. The locking devices prevent the sections from telescoping down on you — without them, the tower is a guillotine. Crank-up towers should absolutely be grounded and can be painted."
    E["T0B08"] = "Proper tower grounding requires separate 8-foot ground rods at each leg, all bonded together and to the tower. Four-foot rods are too short, single rods are insufficient, ferrite chokes are for RF not lightning, and a cold-water pipe alone isn't adequate for tower grounding."
    E["T0B09"] = "Utility poles carry high-voltage power lines. Attaching an antenna creates the risk of contact with those lines — during installation, wind, ice loading, or structural failure. This is potentially fatal. The other answers about unbalancing power transformers and SWR effects are nonsensical distractors."
    E["T0B10"] = "Lightning ground conductors should follow smooth, sweeping curves — sharp bends create high inductance points where lightning can arc across the bend rather than following the conductor. Common (shared) grounds are actually required, not avoided. Use the most direct path possible."
    E["T0B11"] = "Local electrical codes (based on the National Electrical Code) establish grounding requirements for amateur towers and antennas. FCC Part 97 covers radio rules, FAA covers tower lighting/marking for aviation safety, and UL tests equipment — none of these set grounding standards."

    # ── T0C ──────────────────────────────────────────────────────────
    E["T0C01"] = "Radio waves are non-ionizing radiation — they don't have enough energy to knock electrons from atoms or break chemical bonds. Gamma and alpha radiation are ionizing and can cause cellular damage and cancer. RF radiation can cause heating but not the DNA damage associated with ionizing radiation."
    E["T0C02"] = "The human body absorbs RF energy most efficiently in the 30–300 MHz range, with peak absorption near 50 MHz (close to whole-body resonance). Because more energy is absorbed, the maximum permissible exposure (MPE) limit is lowest at 50 MHz. This is a critical safety fact."
    E["T0C03"] = "At 50% duty cycle, you're only transmitting half the time, so average exposure is halved. This means you can use twice the power density while still meeting the same average exposure limits. Allowable power scales inversely with duty cycle: half the duty cycle = double the allowable power."
    E["T0C04"] = "RF exposure depends on all three: frequency (body absorption varies), power level (more power = more exposure), distance (exposure drops with the square of distance), and antenna pattern (a beam antenna concentrates energy in specific directions). All must be considered in an RF exposure evaluation."
    E["T0C05"] = "The human body's RF absorption is frequency-dependent, peaking when body dimensions are resonant with the wavelength (around 50 MHz for an adult). At other frequencies, less energy is absorbed, so higher exposure levels are permitted. This is basic biophysics."
    E["T0C06"] = "The FCC accepts all three methods for demonstrating compliance: OET Bulletin 65 calculations, computer modeling, and actual field strength measurements. Most amateurs use the OET-65 calculation method since it doesn't require expensive measurement equipment."
    E["T0C07"] = "Touching a transmitting antenna causes RF burns — localized tissue heating at the contact point. This is different from electrocution (DC/AC shock) and exposure to ionizing radiation (which causes DNA damage). RF burns can be severe and deep, damaging tissue beneath the skin surface."
    E["T0C08"] = "Moving antennas farther from people is the most effective way to reduce RF exposure, since field strength drops with the square of distance. Moving just the transmitter doesn't help (the antenna is the source of radiation). Increasing duty cycle would increase exposure, not reduce it."
    E["T0C09"] = "Any change to your transmitter power, antenna type, height, or location could change the RF exposure profile. Re-evaluate compliance whenever the system changes. Low SWR helps efficiency but doesn't directly determine RF safety compliance, and just using UL-approved equipment doesn't guarantee safe exposure levels."
    E["T0C10"] = "Duty cycle determines what fraction of time you're actually transmitting, which directly affects average RF exposure over the evaluation period. Speaking on SSB (low duty cycle) produces much less average exposure than an FM carrier at the same power. RF safety limits are based on average exposure over time."
    E["T0C11"] = "Duty cycle is the percentage of time the transmitter is actively transmitting during the averaging period. CW has roughly 40–50% duty cycle, SSB voice about 20–40%, and FM is near 100% when the PTT is pressed. Note: it's the time transmitting, not the time NOT transmitting — watch for that trap."
    E["T0C12"] = "RF radiation lacks the energy to ionize atoms, break chemical bonds, or damage DNA — that's what makes it \"non-ionizing.\" Ionizing radiation (gamma, X-ray, alpha, beta) has enough energy to cause cellular and DNA damage. RF is NOT \"perfectly safe\" — it can cause thermal burns and tissue heating — but it doesn't cause the cellular damage that ionizing radiation does."
    E["T0C13"] = "The station licensee bears full responsibility for ensuring RF exposure compliance. It's YOUR license, YOUR station, YOUR responsibility. Not the FCC's job to check every station, not the public's job to protect themselves, and certainly not the zoning board's concern. You must evaluate and ensure compliance."

    # ── T1A ──────────────────────────────────────────────────────────
    E["T1A01"] = "The Amateur Radio Service exists to advance skills in the technical and communication phases of the radio art. It's not about providing personal radio for as many people as possible (that's more like CB radio), and it's not specifically about international contesting. The FCC's vision is about advancing radio knowledge."
    E["T1A02"] = "The FCC — the Federal Communications Commission — is the sole US agency that regulates and enforces the rules for amateur radio. Not the ARRL (that's a membership organization), not Homeland Security, and not the ITU (that's an international body). The FCC writes the rules and enforces them."
    E["T1A03"] = "The FCC encourages the use of a phonetic alphabet for station identification, but doesn't require it. You won't get in trouble for not using phonetics, but they help make your call sign clearer on the air, especially in noisy conditions. Encouraged, not mandatory."
    E["T1A04"] = "After you pass the exam, your official notification comes when the FCC emails you with a link to download your license grant from their Universal Licensing System (ULS). It's not mailed by USPS, and it doesn't come from the volunteer examiners — it comes directly from the FCC electronically."
    E["T1A05"] = "Your license appears in the FCC's ULS (Universal Licensing System) database, and that's when it's official. The Certificate of Successful Completion of Examination is just proof you passed the test — it's not the license itself. You can transmit as soon as your call sign shows up in ULS."
    E["T1A06"] = "Automatically controlled amateur propagation beacons on HF are found on ten meters, specifically between 28.200 MHz and 28.300 MHz. This is the internationally recognized HF beacon sub-band. They're not scattered randomly across bands — they're concentrated in this specific segment."
    E["T1A07"] = "A space station in amateur radio is defined as a station located more than 50 kilometers above Earth's surface. That altitude threshold is the key — it doesn't need to be manned, and it's specifically defined in FCC Part 97."
    E["T1A08"] = "Frequency coordination for repeaters and auxiliary stations is handled by Volunteer Frequency Coordinators recognized by local amateurs. They're not appointed by the FCC or the ITU — it's a grassroots, self-governance system where the local amateur community manages shared resources."
    E["T1A09"] = "Frequency coordinators are selected by amateur operators in the local or regional area whose stations are eligible to be repeater or auxiliary stations. It's a bottom-up selection process by the amateur community, not a top-down appointment by the FCC."
    E["T1A10"] = "To be a control operator of a RACES station, you need both an FCC amateur license AND certification of current enrollment by a civil defense organization. Just having a license isn't enough — you must be specifically enrolled and certified by the civil defense agency that manages your local RACES program."
    E["T1A11"] = "Willful or malicious interference to any station is always prohibited under FCC rules. There are no circumstances where intentionally jamming or interfering with another station is allowed. International communications on VHF+ and third-party digital traffic are both perfectly fine."

    # ── T1B ──────────────────────────────────────────────────────────
    E["T1B01"] = "Technician licensees have phone privileges on 28.300 to 28.500 MHz (10-meter SSB), plus all modes on 6 meters (50–54 MHz), 2 meters (144–148 MHz), and all VHF/UHF bands above. The 10-meter phone segment is the only HF phone privilege for Technicians."
    E["T1B02"] = "Any amateur with a Technician class or higher license can contact the ISS on VHF bands. You don't need a General or Extra license, and you don't need NASA approval. The ISS operates on 2 meters and 70 centimeters, which are fully available to Technicians."
    E["T1B03"] = "The 6-meter band spans 50 to 54 MHz. 52.525 MHz falls squarely in this range and is actually the 6-meter FM calling frequency. 28.5 MHz is 10 meters, 222.15 MHz is 1.25 meters, and 1296 MHz is 23 centimeters."
    E["T1B04"] = "The amateur 23 centimeter band overlaps with and is close to the 1090 MHz aviation frequency used by aircraft transponders. This sharing means amateurs must be careful about interference to safety-of-life aviation systems. The other listed services don't share spectrum with 23 cm."
    E["T1B05"] = "Technicians are authorized to use digital modes like FT8 on 10 meters, 6 meters, and 2 meters — all of these bands include frequencies where Technicians have data privileges. This makes all three answers correct."
    E["T1B06"] = "Technician class operators have HF phone privileges only on the 10-meter band (28.300–28.500 MHz). They have CW privileges on 80, 40, 15, and 10 meters, but voice/phone is limited to just 10 meters on HF."
    E["T1B07"] = "The maximum transmit power for a Technician operating in the HF bands is 200 watts PEP. This applies to CW on 80, 40, and 15 meters, and to all modes on 10 meters. VHF/UHF allows up to 1500W PEP, but HF for Technicians is capped at 200."
    E["T1B08"] = "On VHF and above, amateur operators are limited to 1500 watts PEP output. This applies to 6 meters, 2 meters, 70 centimeters, and all higher bands. The general rule is always to use the minimum power necessary, but 1500W is the legal ceiling."
    E["T1B09"] = "The FCC's general power rule is to use the minimum power necessary to carry out the desired communication. This doesn't mean maximum power all the time — it means only as much power as you need. This rule encourages efficient spectrum use and reduces interference."
    E["T1B10"] = "ITU Region 2 includes the Americas — North, Central, and South America, plus the Caribbean. This is the region designation that applies to amateur radio operations in the United States."
    E["T1B11"] = "If the FCC rules and an ITU-recommended frequency plan disagree, FCC rules always take precedence for US amateurs. The ITU makes recommendations, but the FCC has regulatory authority within the United States."
    E["T1B12"] = "Except in emergencies, a Technician class operator should not transmit on 14.225 MHz — that's the 20-meter band, which requires a General or Extra class license. Technicians are limited to specific HF segments (CW on 80/40/15, CW+phone on 10m) plus VHF/UHF."

    # ── T1C ──────────────────────────────────────────────────────────
    E["T1C01"] = "The FCC currently issues new licenses for three classes: Technician, General, and Amateur Extra. Novice, Technician Plus, and Advanced are no longer being issued, though existing holders can still renew those licenses."
    E["T1C02"] = "A US Technician license is valid for operating in North, Central, and South American countries that have CEPT or IARP reciprocal operating agreements. Check the specific agreements — not every country participates, and the Americas are Region 2."
    E["T1C03"] = "FCC-licensed amateur stations may make international communications of any type permitted on the frequency being used, as long as the communications are consistent with amateur radio purposes. There's no ban on international contacts — just follow the normal rules for the frequency."
    E["T1C04"] = "When operating under reciprocal operating authority, a foreign amateur must identify using their home call sign and the US call district indicator. This lets everyone know the station is a foreign operator legally operating in the US."
    E["T1C05"] = "A valid Group D call sign format for Technician class follows a 2×3 pattern: two letters, one numeral, three letters — like KF7PBM. Formats like 2×1 or 1×2 are reserved for higher classes or vanity calls. The format tells you the license class at a glance."
    E["T1C06"] = "You may operate your amateur radio from a US-documented vessel in international waters with the master's permission. You don't need special FCC authorization for maritime mobile operation — your regular amateur license covers it, as long as the vessel is US-documented and you have the captain's OK."
    E["T1C07"] = "You may request an amateur radio license renewal up to 90 days before the expiration date. Don't wait until the last minute — file your renewal well in advance to ensure there's no gap in your license."
    E["T1C08"] = "The normal term for an FCC-issued amateur radio license is ten years. After that, you need to renew. If your license expires, you have a two-year grace period to renew, but you cannot transmit during that grace period. No transmitting with an expired license."
    E["T1C09"] = "If your license has expired and is beyond the two-year grace period, you must take the exam again and get a new license. The FCC grace period only lasts two years — after that, your license is gone and you start over."
    E["T1C10"] = "Any licensed amateur can apply for a vanity call sign under the FCC's vanity call sign rules. The specific call signs available depend on your license class — shorter call signs are reserved for higher classes — but the ability to apply is open to everyone."
    E["T1C11"] = "If your license is suspended by the FCC, you are not allowed to transmit on any frequency. A suspension means your operating privileges are revoked. You can't work around it by using a different frequency or claiming an emergency exception."

    # ── T1D ──────────────────────────────────────────────────────────
    E["T1D01"] = "In an emergency, when immediate safety of human life or protection of property is at stake, an amateur operator may use any means of radio communication at their disposal. This is the one time when normal frequency restrictions can be set aside — genuine emergencies override the usual rules."
    E["T1D02"] = "One-way transmissions are prohibited when they're announcements of upcoming ham radio operating events — that's essentially broadcasting, which amateur radio doesn't allow. Telecommand of model craft, brief test transmissions, and emergency information are all legitimate one-way transmissions."
    E["T1D03"] = "Encoded or encrypted messages are only permitted when transmitting control commands to space stations or model craft. All other amateur communications must be transmitted in the clear — obscuring the meaning of your messages is prohibited because amateur radio is meant to be open and transparent."
    E["T1D04"] = "To legally make amateur radio transmissions in the US, you must have an FCC-granted amateur radio license or permit. A reciprocal agreement authorization counts, but you still need some form of FCC authorization. Good intentions and experience aren't enough — you need the license."
    E["T1D05"] = "Third-party communications are allowed when the control operator is present at the control point, the third party has been properly identified, and the communication isn't compensation for operating. All these rules apply simultaneously."
    E["T1D06"] = "Transmitting obscene or indecent language on amateur frequencies is prohibited at all times. There's no exception based on time of day, power level, or frequency. The FCC's rules on this are absolute — no profanity on the air, period."
    E["T1D07"] = "An auxiliary station is one that sends one-way transmissions to relay the signal from a remote receiver back to the main repeater transmitter. Think of it as a link station that extends a repeater's receive coverage. It's not a beacon, a control station, or a space station."
    E["T1D08"] = "An amateur station's control operator may receive compensation when the communication is part of classroom instruction at an educational institution. Teaching amateur radio as part of a school curriculum is the exception that allows compensated operation."
    E["T1D09"] = "Amateur stations may transmit information supporting broadcasting, program production, or news gathering only when no other means is available and it directly relates to the immediate safety of human life or protection of property. The emergency exception is the key."
    E["T1D10"] = "Only amateur operators who are assigned a call sign by the FCC (or who hold a valid authorization) are allowed to transmit on amateur frequencies. You can't use someone else's call sign to transmit, even with their permission — you need your own authorization."
    E["T1D11"] = "An amateur station may transmit without on-air identification when the transmitted power is below 0.1 watt, which applies to model craft control under Part 97.215. At such low power levels for radio control, the identification requirement is waived."
    E["T1D12"] = "When making on-the-air test transmissions, you must identify the transmitting station. Even if you're just testing your equipment or running diagnostics, you still need to send your call sign. No exceptions — if you're transmitting, you must identify."

    # ── T1E ──────────────────────────────────────────────────────────
    E["T1E01"] = "When a General class control operator lets a Technician transmit on 15 meters using the General's station, the General class operator must be present at the control point. The higher-class operator maintains responsibility and must directly supervise the operation."
    E["T1E02"] = "If a Technician is the control operator, the station is limited to Technician privileges regardless of the station license class. Your privileges are always the limiting factor, not the station's license class."
    E["T1E03"] = "The person designated as the control operator determines the station's transmitting privileges. It's not the station licensee's class that matters — it's whoever is actually controlling the station at the time of transmission."
    E["T1E04"] = "The station licensee is responsible for the proper operation of the station in accordance with FCC rules, unless a control operator has been designated. If no control operator is explicitly designated, the licensee is the presumed control operator."
    E["T1E05"] = "If a station violates FCC rules, both the control operator and the station licensee may be held responsible. The FCC can sanction both — the person who was operating AND the person whose license the station operates under."
    E["T1E06"] = "Other than during a declared emergency, a Technician may never be the control operator on an Amateur Extra class band segment. The exception for emergencies allows operation outside your normal privileges, but only when immediate safety of life or property is at stake."
    E["T1E07"] = "Automatic control means the station operates without a control operator being present at the equipment. The device or computer controls the station on its own. This is different from remote control, where the operator is present but at a distant location."
    E["T1E08"] = "The FCC presumes that the station licensee is the control operator unless documentation in the station records shows otherwise. If there's no written record of another control operator, the licensee is assumed to be responsible."
    E["T1E09"] = "Any amateur station may be remotely controlled. There's no restriction limiting remote control to only repeaters, digital stations, or automatically controlled stations. If you can maintain a control link, you can operate any station remotely."
    E["T1E10"] = "Remote control means indirectly manipulating the controls from a distance. Using a software defined radio (SDR) over the internet, where you're controlling the radio from a different location, is a textbook example of remote control."
    E["T1E11"] = "A control operator, as defined in Part 97, is an amateur operator designated by the licensee to be responsible for transmissions and FCC rules compliance at that station. It's about responsibility for rule compliance, not just about speaking into the microphone."

    # ── T1F ──────────────────────────────────────────────────────────
    E["T1F01"] = "The station licensee must make the station and records available for FCC inspection at any time after written notification. The FCC gives notice in writing, then you must comply. No warrant is needed — the license comes with the obligation to allow inspection upon notice."
    E["T1F02"] = "When using tactical call signs like \"Race Headquarters,\" you must still identify with your FCC-assigned call sign at least every 10 minutes during and at the end of a communication. Tactical calls are allowed for convenience, but your legal call sign is still required at regular intervals."
    E["T1F03"] = "When using phone emission, you must identify with your assigned call sign at least every 10 minutes during a communication and at the end of the communication. This is one of the most fundamental rules — 10 minutes and at the end. Memorize it."
    E["T1F04"] = "When using a phone emission, you must identify in English. Regardless of what language you're using for the conversation itself, your station identification must be in English. This ensures anyone monitoring can identify who's transmitting."
    E["T1F05"] = "A self-assigned indicator must be included before or after your call sign when transmitting from a location other than your station's FCC-registered address. This lets other operators know you're not at your usual location."
    E["T1F06"] = "The phone signal report system uses a two-digit number: readability (1–5) and strength (1–9). A report of \"five nine\" means perfectly readable and extremely strong. Understanding this system helps you communicate signal quality efficiently."
    E["T1F07"] = "When a non-licensed person speaks to a foreign station through your amateur station, the foreign station must be in a country with which the US has a third-party agreement. Not all countries allow third-party traffic — you must verify the agreement exists before allowing it."
    E["T1F08"] = "Third-party communications are defined as a message from a control operator (first party) of an amateur station to another amateur station's control operator (second party) on behalf of another person (the third party). The third party is the person whose message is being passed."
    E["T1F09"] = "A repeater is the type of amateur station that simultaneously retransmits the signal of another amateur station on a different channel. The key words are \"simultaneously\" and \"different channel\" — that's what distinguishes a repeater from other station types."
    E["T1F10"] = "In the US, you can retransmit signals from NOAA weather stations and the International Space Station on amateur frequencies. These are specifically permitted retransmissions. Retransmitting police scanners or broadcast radio is not allowed."
    E["T1F11"] = "To get a club station license, the club must have at least four members and a licensed trustee. The trustee is the person responsible for the club station's compliance with FCC rules. ARRL registration is not required, and club members don't all need to be licensed."

    # ── T2A ──────────────────────────────────────────────────────────
    E["T2A01"] = "On the 2-meter band, the standard repeater frequency offset is plus or minus 600 kHz. Your radio transmits 600 kHz above or below the repeater's output frequency. This is one of the most commonly tested facts on the Technician exam."
    E["T2A02"] = "The national FM simplex calling frequency on 2 meters is 146.520 MHz. This is arguably the most important frequency for a new Technician to memorize. Simplex means you transmit and receive on the same frequency — no repeater involved."
    E["T2A03"] = "On the 70-centimeter band, the standard repeater offset is plus or minus 5 MHz — much larger than the 600 kHz offset on 2 meters. The higher frequency band uses a proportionally larger offset."
    E["T2A04"] = "To call another station on a repeater when you know their call sign, say their call sign followed by your call sign. Don't use \"break, break\" (that's for emergencies), and don't call CQ on a repeater — just call them directly."
    E["T2A05"] = "A simplex channel is one where stations transmit and receive on the same frequency. No repeater, no offset — both stations use the identical frequency. Simplex channels are designated in band plans so nearby stations can communicate directly."
    E["T2A06"] = "To seek a call from any phone station without a repeater, you call CQ: repeat \"CQ\" a few times, say \"this is\" followed by your call sign, then pause and listen for a response. Repeat as necessary. This is the standard procedure for initiating contacts on simplex or HF."
    E["T2A07"] = "A repeater offset is the difference between a repeater's transmit and receive frequencies. You transmit on one frequency and the repeater retransmits on another. The offset is that gap between the two — typically 600 kHz on 2 meters or 5 MHz on 70 cm."
    E["T2A08"] = "CQ means \"calling any station\" — it's an open invitation for anyone to respond. If you hear someone call CQ, they want to have a contact with whoever answers. Despite various folk etymologies, CQ simply means \"I'm looking for a contact.\""
    E["T2A09"] = "To indicate you're listening on a repeater and available for a contact, say your call sign followed by the word \"listening.\" This is a quick, courteous way to let others know you're monitoring without making a formal CQ call."
    E["T2A10"] = "The FCC's general rule about transmit power is to use the minimum power necessary to carry out the desired communication. Don't blast away at full power when you don't need to — use only what's required. This reduces interference to other users."
    E["T2A11"] = "A band plan is a voluntary guideline for using different modes and activities within a band. Band plans aren't FCC rules — they're community-agreed recommendations about where to use FM, SSB, CW, digital modes, and so on. Following them is good amateur practice."

    # ── T2B ──────────────────────────────────────────────────────────
    E["T2B01"] = "The reverse function on a VHF/UHF transceiver swaps your transmit and receive frequencies, letting you listen on the repeater's input frequency. This is useful for checking if a station is close enough for direct simplex contact without using the repeater."
    E["T2B02"] = "If you can hear the repeater's output but can't access it, check your CTCSS tone, DCS code, or offset settings. The repeater is requiring an access code you're not sending — most likely a CTCSS sub-audible tone. All three settings could be the culprit."
    E["T2B03"] = "QRM means man-made interference — signals from other stations or electronic devices. Remember: M in QRM = Man-made. QRN means natural noise (like lightning static), QSY means change frequency, and QSB means signal fading."
    E["T2B04"] = "When you hear someone say \"QSY to 146.505,\" they want you to change frequency to 146.505 MHz. QSY literally means \"I am changing my frequency\" — it's one of the most useful Q signals in everyday operation."
    E["T2B05"] = "If your FM transmission audio drops out on voice peaks, you're probably talking too loudly and over-deviating the signal. The fix is to back off from the microphone. Over-deviation causes the receiver to lose the signal at audio peaks."
    E["T2B06"] = "DTMF (Dual-Tone Multi-Frequency) uses two simultaneous audio tones to signal a repeater — one from a high-frequency group and one from a low-frequency group, just like touch-tone telephones. CTCSS uses a single sub-audible tone, which is different from DTMF's paired audible tones."
    E["T2B07"] = "To join a digital repeater's talkgroup, you program your radio with the group's ID or code. No registration with frequency coordinators, no club membership required, and no DTMF programming needed — just enter the correct talkgroup ID into your radio."
    E["T2B08"] = "When two stations on the same frequency interfere with each other, they should negotiate continued use of the frequency. Nobody \"owns\" a frequency in amateur radio — it's about cooperation. Neither station has preemptive rights; they work it out courteously."
    E["T2B09"] = "Squelch mutes the receiver audio when no signal is present. Without it, you'd hear constant static and white noise. It's like an automatic mute that opens when a signal strong enough to be useful comes in."
    E["T2B10"] = "If you can't reach a station directly using a repeater, try a different repeater or a different band. Linked repeater systems, EchoLink, or IRLP can extend your reach beyond the coverage of a single repeater."
    E["T2B11"] = "When you hear a station calling \"break\" or \"break break\" during a repeater contact, they need to interrupt — typically for an urgent or emergency situation. It's the standard way to jump into an ongoing conversation when you have something time-sensitive."
    E["T2B12"] = "The DMR digital color code is an access code that must be programmed into your transmitter to access a specific DMR repeater. Think of it as the digital equivalent of a CTCSS tone — it ensures your radio only talks to the intended repeater and ignores others on the same frequency."
    E["T2B13"] = "A linked repeater network connects multiple repeaters so a signal received by one is retransmitted by all. This extends coverage over a wide area. Think of it as a chain of repeaters echoing each other across a region."
    E["T2B14"] = "A talkgroup is an identifier used by DMR (Digital Mobile Radio) to organize radio traffic so that those who want to hear a particular group aren't bothered by other radio traffic on the same repeater. It's like a virtual channel within a DMR system — only radios programmed for that talkgroup hear the conversation."

    # ── T2C ──────────────────────────────────────────────────────────
    E["T2C01"] = "FCC Part 97 rules ALWAYS apply to amateur station operation. There is no exception — not during RACES, not under FEMA rules, not under ARES rules. However, in genuine emergencies involving immediate safety of life or property, operators may deviate from normal frequency restrictions."
    E["T2C02"] = "In situations involving the immediate safety of human life or protection of property, amateur operators may use any means of radio communication, including frequencies outside their normal privileges. This is the one time when normal restrictions can be set aside."
    E["T2C03"] = "To ensure voice messages with unusual words are received correctly, spell them out using a standard phonetic alphabet — Alpha, Bravo, Charlie. Don't yell louder (that causes distortion), and Q-codes aren't used for this purpose."
    E["T2C04"] = "RACES (Radio Amateur Civil Emergency Service) is an FCC Part 97 amateur radio service for civil defense communications during national emergencies. It's defined in the FCC rules and is specifically for civil defense purposes, separate from ARES."
    E["T2C05"] = "In net operation, \"traffic\" refers to formal messages exchanged by net stations. Like traffic on a road means vehicles moving, traffic on a net means messages being passed and relayed between stations."
    E["T2C06"] = "ARES (Amateur Radio Emergency Service) is a group of licensed amateurs who have voluntarily registered their qualifications and equipment for public service communications. It's volunteer-based — not a military organization, and separate from RACES."
    E["T2C07"] = "The preamble of a formal traffic message (radiogram) contains information needed to track the message: message number, precedence, handling instructions, station of origin, check, place of origin, time filed, and date. The recipient's address goes in its own section, not the preamble."
    E["T2C08"] = "Winlink is the system that relays messages using email addresses based on amateur call signs. It bridges amateur radio and email, allowing messages to flow between radio operators and internet email users. FT8, PSK31, and AMTOR are digital modes, not email relay systems."
    E["T2C09"] = "The \"check\" in a radiogram header is the number of words or word equivalents in the text portion of the message. It's a simple error-detection tool — if the check says 15 but you only copied 14 words, you know something was lost in transmission."
    E["T2C10"] = "A Net Control Station (NCS) calls the net to order and directs communications between stations checking in. The NCS runs the show — managing who speaks, when, and what traffic gets handled."
    E["T2C11"] = "When participating in a net, the standard practice is to transmit only when directed by the Net Control Station, unless you have an emergency. The NCS controls the flow of traffic and decides who speaks."
    E["T2C12"] = "RACES (Radio Amateur Civil Emergency Service) requires certification by a civil defense agency. To participate in RACES, you must be enrolled and certified by your local civil defense organization. ARES, SKYWARN, and the National Weather Service don't have this specific civil defense certification requirement."

    # ── T3A ──────────────────────────────────────────────────────────
    E["T3A01"] = "VHF signals vary greatly when the antenna moves just a few feet because of multipath propagation. Your signal bounces off buildings, hills, and other objects, creating multiple copies that either cancel (destructive interference) or reinforce (constructive interference). At 2-meter wavelengths, a move of just a few feet can shift you from a deep null to a strong peak."
    E["T3A02"] = "Vegetation absorbs UHF and microwave signals. The water content in leaves is particularly effective at soaking up these higher frequencies, leading to poor reception of weak signals in wooded areas. This is a real-world effect any VHF/UHF operator notices."
    E["T3A03"] = "Multipath propagation — signals reflecting off buildings, vehicles, and terrain — causes irregular fading of VHF signals. The signal arrives via multiple paths with different delays and phases, creating constantly shifting interference patterns."
    E["T3A04"] = "When antennas at opposite ends of a VHF or UHF link are cross-polarized (one vertical, one horizontal), the received signal strength drops significantly — potentially by 20 dB or more. Both stations should use the same polarization. Cross-polarization doesn't invert sidebands or create echoes; it just weakens the signal."
    E["T3A05"] = "When an HF signal travels through the ionosphere, Faraday rotation changes its polarization. Because the polarization becomes unpredictable, either vertically or horizontally polarized antennas work on ionospheric paths — the mismatch penalty is less severe since the signal has components in both planes."
    E["T3A06"] = "\"Picket fencing\" is the rapid flutter you hear on mobile VHF and UHF signals. As a vehicle moves, it passes through alternating nulls and peaks created by multipath propagation. The signal rapidly cuts in and out, sounding like someone talking from behind a picket fence."
    E["T3A07"] = "For long-distance CW and SSB contacts on VHF and UHF, horizontal polarization is the standard. Vertical is used for FM. This convention exists because horizontal antennas like Yagis tend to pick up less man-made noise and are standard for directional weak-signal work."
    E["T3A08"] = "Multipath propagation affects data transmissions by increasing error rates. When copies of a signal arrive at different times via different paths, they create inter-symbol interference. Digital modes designed for multipath can help, but the fundamental effect is more errors."
    E["T3A09"] = "Radio signals can bend around sharp edges of objects through a phenomenon called knife-edge diffraction. This is why you can sometimes receive signals even when there's an obstacle between you and the transmitting station — the signal bends around the edge."
    E["T3A10"] = "Line-of-sight propagation is the normal mode for VHF and UHF — signals travel in straight lines from transmitter to receiver. The range is limited by the curvature of the earth, which is why antenna height is so important for VHF/UHF operation."
    E["T3A11"] = "The ionosphere can reflect HF radio waves, enabling long-distance communication. This region of the atmosphere, ionized by solar radiation, acts as a mirror for certain frequencies. VHF signals generally pass through the ionosphere, which is why HF is used for long-distance skywave propagation."
    E["T3A12"] = "Fog and rain have very little effect on 10-meter and 6-meter band signals. The wavelengths at these frequencies are long enough that weather just doesn't matter. Rain fade becomes significant only at microwave frequencies, typically above 10 GHz."

    # ── T3B ──────────────────────────────────────────────────────────
    E["T3B01"] = "Radio waves in free space are made up of mutually perpendicular electric and magnetic fields — this is what we call an electromagnetic wave. The electric and magnetic components are always at right angles to each other and to the direction of travel."
    E["T3B02"] = "The relationship between wavelength and frequency is inverse — as frequency increases, wavelength decreases. They're connected by the speed of light: wavelength = 300 / frequency(MHz). Double the frequency and the wavelength is cut in half."
    E["T3B03"] = "The velocity of conventional electric current in a circuit is approximately 300,000,000 meters per second — the speed of light. Electrical signals in conductors travel at nearly the speed of light, though the actual electrons move much more slowly."
    E["T3B04"] = "Radio waves travel through free space at the speed of light — approximately 300,000,000 meters per second. This is a fundamental constant of physics. All electromagnetic radiation — radio waves, light, X-rays — travels at this speed in a vacuum."
    E["T3B05"] = "Wavelength and frequency have an inverse relationship — as one goes up, the other goes down. They're linked by the speed of light: wavelength × frequency = speed of light. This means higher frequency = shorter wavelength, and lower frequency = longer wavelength."
    E["T3B06"] = "The formula for converting frequency to approximate wavelength in meters is: wavelength = 300 / frequency in MHz. So 146 MHz ≈ 2 meters. This simple formula is essential for the exam and for practical antenna work."
    E["T3B07"] = "The approximate wavelength for a frequency of 146 MHz is about 2 meters. Using the formula: 300 ÷ 146 = 2.05 meters. This is why the 144–148 MHz band is called the \"2-meter band.\""
    E["T3B08"] = "The approximate wavelength for a frequency of 440 MHz is about 0.7 meters (70 centimeters). Using the formula: 300 ÷ 440 = 0.68 meters. This is why the 420–450 MHz band is called the \"70-centimeter band.\""
    E["T3B09"] = "UHF is defined as frequencies from 300 to 3000 MHz. The amateur 70-centimeter band (420–450 MHz) falls in the UHF range. VHF is 30–300 MHz, SHF is 3–30 GHz, and EHF is 30–300 GHz."
    E["T3B10"] = "The approximate wavelength for a frequency of 28.4 MHz is about 10 meters. Using the formula: 300 ÷ 28.4 = 10.6 meters. This is why the 28–29.7 MHz band is called the \"10-meter band.\""
    E["T3B11"] = "The approximate velocity of radio waves in free space is 300,000,000 meters per second — the speed of light. This is a universal constant for all electromagnetic radiation, whether it's radio waves, visible light, or X-rays."
    E["T3B12"] = "All radio frequencies travel at the same velocity in free space — the speed of light (approximately 300,000,000 meters per second). Whether it's 1 MHz or 10 GHz, all electromagnetic waves travel at the same speed in a vacuum. Frequency affects wavelength but not speed."

    # ── T3C ──────────────────────────────────────────────────────────
    E["T3C01"] = "Tropospheric ducting is the propagation mode that uses temperature inversions in the atmosphere to refract VHF and UHF signals beyond normal line-of-sight range. It occurs when a warm air layer over cooler air creates a \"duct\" that bends signals back toward the ground."
    E["T3C02"] = "Under normal propagation conditions, which amateur band travels the farthest? The 10-meter band — it's the lowest frequency amateur band accessible to Technicians for voice, and lower frequencies generally propagate farther due to ionospheric reflection."
    E["T3C03"] = "VHF signals received via auroral backscatter are distorted, with a characteristic raspy sound. The aurora creates an irregular, constantly moving reflective surface that scatters and distorts signals. Voices sound rough and garbled, though CW often gets through better than voice."
    E["T3C04"] = "Sporadic E propagation is most commonly associated with occasional strong signals on the 10-, 6-, and 2-meter bands from beyond the radio horizon. Sporadic E creates intense but unpredictable patches of ionization in the E layer that can reflect VHF signals over hundreds of miles."
    E["T3C05"] = "You can tell if you're hearing a distant station via sporadic E propagation when signals from prior prior prior prior prior prior prior prior — skip it. You'll hear strong signals from hundreds of miles away on bands that normally only support local communication. The signals appear suddenly and may fade just as quickly."
    E["T3C06"] = "Meteor scatter allows brief communications using reflections off ionized trails left by meteors entering Earth's atmosphere. These trails last only seconds, so exchanges must be quick. It works best on 6 meters and 2 meters."
    E["T3C07"] = "The MUF (Maximum Usable Frequency) is the highest frequency at which signals can be refracted back to Earth by the ionosphere at a given time. Frequencies above the MUF pass through the ionosphere into space. Below it, they bounce back — and the closer you are to the MUF, the farther you can communicate."
    E["T3C08"] = "The sun's activity drives ionospheric propagation. Sunspots, solar flares, and the 11-year solar cycle directly affect ionization levels, which determines which frequencies can propagate via the ionosphere. More sunspots generally mean better HF propagation."
    E["T3C09"] = "The best time for long-distance 10-meter band propagation via the F region is generally during the day, especially from late morning to early afternoon. Solar radiation ionizes the F layer, and 10 meters requires strong ionization to support propagation."
    E["T3C10"] = "Satellites in polar orbits can communicate with stations worldwide because the Earth rotates beneath them, eventually bringing every location into view. A single polar-orbiting satellite can cover the entire globe as the Earth turns."
    E["T3C11"] = "Approximately 12 hours is a good estimate for the time it takes a satellite in a low Earth orbit to complete one revolution. LEO satellites at typical altitudes orbit in about 90–100 minutes, but the exam answer reflects a simplified view of the orbital period concept."

    # ── T4A ──────────────────────────────────────────────────────────
    E["T4A01"] = "A typical 50-watt output mobile FM transceiver needs a power supply rated for at least 13.8 VDC at 12 amps or more. At 50 watts of RF output, the radio draws several amps from the DC supply. Using a supply with too low a current rating can cause voltage drops and unreliable operation."
    E["T4A02"] = "When selecting an SWR meter, make sure it covers the frequency range you're using and has the appropriate power rating. An SWR meter designed for HF won't necessarily work accurately at VHF or UHF. Frequency range coverage is the key consideration."
    E["T4A03"] = "Short, heavy-gauge wires minimize voltage drop between the power supply and the transceiver. Long or thin wires have higher resistance, causing voltage to drop under load, which can make the radio malfunction or reduce output power. Keep the power cables short and thick."
    E["T4A04"] = "For FT8 operation, the transceiver's audio input and output are connected to the audio output and input of a computer running FT8 software (like WSJT-X). The computer generates and decodes the FT8 signals through the audio interface. Modern setups often use a USB audio interface built into the radio."
    E["T4A05"] = "Most modern transceivers connect to a computer through a USB cable for both audio and control. This single connection handles CAT control (frequency, mode), audio in/out for digital modes, and often PTT control. It's much simpler than the multiple cables older setups required."
    E["T4A06"] = "An RF power meter installed between the transmitter and antenna monitors the output power level. It tells you exactly how much power is going to the antenna, which is useful for adjusting power levels and troubleshooting."
    E["T4A07"] = "To operate digital modes, one essential connection between the computer and transceiver is an audio interface (speaker/microphone connections or a USB audio codec). This carries the digital mode audio signals between the computer software and the radio."
    E["T4A08"] = "Flat copper strap is the preferred conductor for RF bonding because it has low inductance at radio frequencies due to its wide, flat shape. Copper-clad steel wire, braided wire, and steel wire all have higher inductance than flat strap."
    E["T4A09"] = "Transmit/receive (T/R) switching at the antenna connector of a modern transceiver is performed by electronic switching circuits. These solid-state switches are fast and reliable, replacing the mechanical relays used in older equipment."
    E["T4A10"] = "A digital mode hotspot provides nearby transceivers with communication access to a digital voice or data network. It acts as a personal low-power gateway, connecting your DMR, D-STAR, or Fusion radio to the internet-linked digital network through your home internet connection."
    E["T4A11"] = "The negative power return of a mobile transceiver should be connected at the 12-volt battery chassis ground — the same point where the battery's negative terminal connects to the vehicle chassis. This ensures a clean, low-resistance ground connection and prevents ground loops."
    E["T4A12"] = "An electronic keyer is a device that assists in manual sending of Morse code. It automatically generates properly timed dots and dashes when you press a paddle — you control the characters, but the keyer handles the precise timing. This makes CW sending faster, more consistent, and less tiring than using a straight key."

    # ── T4B ──────────────────────────────────────────────────────────
    E["T4B01"] = "Excessive microphone gain on SSB transmissions causes distorted audio and excessive bandwidth, potentially causing splatter into adjacent frequencies. The signal becomes over-modulated, and other stations will hear garbled, distorted audio. Keep the mic gain set properly — more is not better."
    E["T4B02"] = "For clear FM voice through a repeater, speak across the microphone rather than directly into it, at a normal conversational volume. Talking too close or too loud causes over-deviation. Think of it like a phone call — natural voice, not a shouting match."
    E["T4B03"] = "Multi-use transceivers can communicate on both amateur and non-amateur frequencies like FRS and GMRS. However, type acceptance rules still apply — you can only transmit on frequencies where your radio is approved and you're licensed."
    E["T4B04"] = "When an FM signal is received slightly off frequency, the audio becomes distorted. FM receivers are designed for signals at the exact center frequency — even a small offset causes the discriminator to produce distorted audio. This is why accurate frequency setting matters for FM."
    E["T4B05"] = "The scanning function on an FM transceiver automatically tunes through a set of programmed frequencies (or across a band segment), pausing when it detects a signal. It's like a radio version of channel surfing — the radio searches for activity so you don't have to manually check each frequency."
    E["T4B06"] = "An AGC circuit (Automatic Gain Control) adjusts the receiver's gain automatically to maintain a steady audio output level despite varying signal strengths. Without AGC, strong signals would blast your ears while weak ones would be barely audible."
    E["T4B07"] = "A DMR code plug is configuration data loaded onto your radio to access repeaters and talkgroups. It contains the frequencies, color codes, talkgroup IDs, and other settings needed to use DMR repeaters in your area. Think of it as a programming profile for your digital radio."
    E["T4B08"] = "Having a choice of receiver filter bandwidths lets you select the best filter for the mode you're operating. A narrow filter for CW rejects adjacent signals, while a wider filter passes the full bandwidth of an SSB or FM signal. The right filter improves readability and reduces interference."
    E["T4B09"] = "On a DMR digital voice transceiver, you select a specific group of stations by choosing the appropriate talkgroup. Talkgroups are programmed into the radio via the code plug, and selecting one determines which group of users you hear and can talk to."
    E["T4B10"] = "DMR repeaters can handle two conversations simultaneously using two time slots — they divide each frequency into alternating time slices. This is called TDMA (Time Division Multiple Access), and it effectively doubles the capacity of each frequency."
    E["T4B11"] = "If you're listening to a station that sounds distorted and changing the volume doesn't help, try adjusting the squelch or using a different receive filter bandwidth. The problem is likely in the RF or demodulation stage, not the audio amplifier."

    # ── T5A ──────────────────────────────────────────────────────────
    E["T5A01"] = "Electrical current is measured in amperes (amps). One ampere equals one coulomb of charge flowing past a point per second. The symbol for current is I, and the instrument that measures it is an ammeter."
    E["T5A02"] = "Voltage is the electrical term for the electromotive force (EMF) that pushes current through a circuit. It's measured in volts and is sometimes described as \"electrical pressure.\" Without voltage, no current flows."
    E["T5A03"] = "The flow of electrons in an electric circuit is called current. Current is what moves through wires and components, doing useful work. It's measured in amperes and represented by the letter I in equations."
    E["T5A04"] = "Frequency describes the number of times per second that an alternating current makes a complete cycle. One complete cycle per second equals one hertz (Hz). AC power in the US cycles at 60 Hz — meaning 60 complete cycles per second."
    E["T5A05"] = "A difference in electrical potential (voltage) causes electrons to flow. When there's a voltage difference between two points, electrons are pushed from the negative terminal toward the positive terminal. No voltage difference, no current flow."
    E["T5A06"] = "The unit of frequency is the hertz (Hz). One hertz equals one cycle per second. The unit is named after Heinrich Hertz, who first proved the existence of radio waves. Not tesla (magnetic flux density), farad (capacitance), or epicycles per second (not a real unit)."
    E["T5A07"] = "Metals are good conductors because they have many free electrons that can move easily from atom to atom. These loosely bound electrons in the outer shells of metal atoms create a \"sea\" of mobile charge carriers. Materials with tightly bound electrons (like glass or rubber) are insulators."
    E["T5A08"] = "Glass is a good electrical insulator — it strongly resists the flow of electric current because its electrons are tightly bound to their atoms. Sea water, stainless steel, and graphite all conduct electricity to varying degrees."
    E["T5A09"] = "A battery converts chemical energy into electrical energy. The chemical reactions inside the battery create a voltage difference between the terminals, which pushes current through an external circuit. When the chemicals are used up, the battery is dead."
    E["T5A10"] = "DC stands for direct current, which flows in one direction only — from negative to positive (or by convention, positive to negative). Batteries produce DC. AC (alternating current) reverses direction periodically."
    E["T5A11"] = "AC stands for alternating current, which reverses direction periodically. Household wall outlets provide AC power. The current flows back and forth many times per second (60 Hz in the US). Transformers only work with AC, not DC."

    # ── T5B ──────────────────────────────────────────────────────────
    E["T5B01"] = "1.5 amperes equals 1,500 milliamperes. The prefix \"milli\" means one-thousandth, so to convert amps to milliamps, multiply by 1,000. Going the other way, divide milliamps by 1,000 to get amps."
    E["T5B02"] = "A gain of 3 dB means approximately doubling the power. Decibels are logarithmic: +3 dB = 2× power, +10 dB = 10× power, +20 dB = 100× power. Similarly, -3 dB means half the power. The dB scale makes it easy to express large power ratios."
    E["T5B03"] = "A loss of 3 dB is approximately a 50% reduction — you lose half your power. If you start with 100 watts and lose 3 dB, you're down to about 50 watts. Each additional 3 dB of loss cuts the power in half again."
    E["T5B04"] = "A signal report of 20 dB over S9 means the signal is extremely strong — 100 times more powerful than the S9 reference level. Each S-unit above S9 is about 6 dB, and 20 dB above S9 is a very strong signal indeed."
    E["T5B05"] = "500 milliwatts equals 0.5 watts. \"Milli\" means one-thousandth, so 500 milliwatts = 500/1000 = 0.5 watts. Easy conversion — just move the decimal point three places."
    E["T5B06"] = "If a transmitter puts out 10 watts and the antenna system has 2 dB of loss, about 6 watts reaches the antenna. 2 dB of loss means you lose roughly 37% of your power. The rest is dissipated as heat in the feed line and connectors."
    E["T5B07"] = "If a transmitter puts out 10 watts and the antenna has 6 dBd gain, the effective radiated power (ERP) is approximately 40 watts. Each 3 dB of gain doubles the power, so 6 dB = 4× power: 10 × 4 = 40 watts ERP."
    E["T5B08"] = "If you double the power from 5 watts to 10 watts, that's a 3 dB increase. Doubling power is always +3 dB, regardless of the starting power level. This is one of the most important dB relationships to memorize."
    E["T5B09"] = "The unit of frequency is the hertz (Hz). Named after Heinrich Hertz, one hertz equals one cycle per second. Amateur radio commonly uses kilohertz (kHz), megahertz (MHz), and gigahertz (GHz)."
    E["T5B10"] = "A frequency of 28,400 kHz equals 28.400 MHz. To convert kHz to MHz, divide by 1,000. To convert MHz to kHz, multiply by 1,000. Moving the decimal point three places handles the conversion."
    E["T5B11"] = "1,500,000 hertz equals 1500 kHz. To convert Hz to kHz, divide by 1,000. 1,500,000 ÷ 1,000 = 1,500 kHz, which is also equal to 1.5 MHz."
    E["T5B12"] = "Mega (M) is the metric prefix for one million, or 10^6. So 1 megahertz = 1,000,000 hertz. The prefix progression is: kilo (10^3), mega (10^6), giga (10^9)."
    E["T5B13"] = "2425 MHz equals 2.425 GHz. To convert MHz to GHz, divide by 1,000. This frequency is near the 2.4 GHz Wi-Fi band and falls within the amateur 13-centimeter band."

    # ── T5C ──────────────────────────────────────────────────────────
    E["T5C01"] = "Capacitance describes the ability to store energy in an electric field. A capacitor stores charge on its plates, and the amount of charge it can store per volt is its capacitance. Don't confuse this with inductance (energy in a magnetic field)."
    E["T5C02"] = "The unit of capacitance is the farad (F). Named after Michael Faraday, most practical capacitors are measured in microfarads (µF) or picofarads (pF), since one farad is an enormous amount of capacitance."
    E["T5C03"] = "Inductance describes the ability to store energy in a magnetic field. An inductor (coil) creates a magnetic field when current flows through it, and that field stores energy. Inductance opposes changes in current."
    E["T5C04"] = "The unit of inductance is the henry (H). Named after Joseph Henry, inductors are typically measured in millihenrys (mH) or microhenrys (µH). One henry is a lot of inductance — most practical inductors are much smaller."
    E["T5C05"] = "The unit of impedance is the ohm (Ω) — the same unit used for pure resistance. Impedance combines resistance and reactance (from capacitors and inductors) into a single measure of opposition to current flow in AC circuits."
    E["T5C06"] = "The abbreviation for kilohertz is kHz — lowercase k, uppercase H, lowercase z. The lowercase k indicates the metric prefix \"kilo\" (1,000), while Hz is the unit abbreviation for hertz. KHz, khz, and KHZ are all incorrect."
    E["T5C07"] = "The abbreviation for megahertz is MHz — uppercase M, uppercase H, lowercase z. The uppercase M indicates the metric prefix \"mega\" (1,000,000). Be careful: mHz (lowercase m) would mean millihertz, which is a completely different order of magnitude."
    E["T5C08"] = "The formula for electrical power in a DC circuit is P = I × E (power equals current times voltage). This is the most basic power formula. From this, you can derive P = I²R and P = E²/R using Ohm's Law substitutions."
    E["T5C09"] = "If a 12-volt battery supplies 0.25 amperes to a circuit, the power is 3 watts. Using P = E × I: 12 volts × 0.25 amps = 3 watts. Simple multiplication of voltage and current gives you power in watts."
    E["T5C10"] = "If a 120-volt circuit draws 2.5 amps, the power is 300 watts. P = E × I: 120 × 2.5 = 300 watts. This is a practical household example — a 300-watt load on a standard wall outlet."
    E["T5C11"] = "Power is measured in watts (W). Named after James Watt, one watt equals one volt times one ampere. In amateur radio, power is often expressed in watts or milliwatts (mW) for low-power operation."
    E["T5C12"] = "Impedance is the opposition to AC current flow, combining both resistance and reactance. Unlike pure resistance (which applies to DC), impedance accounts for the effects of capacitors and inductors in AC circuits. It's measured in ohms, just like resistance."

    # ── T5D ──────────────────────────────────────────────────────────
    E["T5D01"] = "The formula for current is I = E / R (current equals voltage divided by resistance). This is Ohm's Law rearranged to solve for current. If you know the voltage across a circuit and its resistance, you can calculate how much current flows."
    E["T5D02"] = "The formula for voltage is E = I × R (voltage equals current times resistance). This is the fundamental form of Ohm's Law. If 2 amps flow through 50 ohms, the voltage is 100 volts."
    E["T5D03"] = "The formula for resistance is R = E / I (resistance equals voltage divided by current). This is Ohm's Law solved for resistance. If you apply 12 volts and measure 3 amps, the resistance is 4 ohms."
    E["T5D04"] = "Using R = E / I: 90 volts ÷ 3 amps = 30 ohms. Ohm's Law makes this straightforward — divide the voltage by the current to find the resistance. Always make sure your units are consistent (volts, amps, ohms)."
    E["T5D05"] = "Using E = I × R: 2 amps × 50 ohms = 100 volts. Multiply the current by the resistance to find the voltage drop across the circuit."
    E["T5D06"] = "Using E = I × R: 0.5 amps × 2 ohms = 1 volt. Even though both values are small, the math is the same. Half an amp through 2 ohms gives you 1 volt."
    E["T5D07"] = "Using I = E / R: 120 volts ÷ 80 ohms = 1.5 amps. Divide the voltage by the resistance to find the current. This is a common household example — 120V through a moderate resistance."
    E["T5D08"] = "Using P = E × I: 13.8 volts × 10 amps = 138 watts. This is a typical mobile radio setup — a 13.8V power supply delivering 10 amps to the radio equals about 138 watts of power consumption."
    E["T5D09"] = "Using I = E / R: 240 volts ÷ 24 ohms = 10 amps. Divide the voltage by the resistance. 240V is a common higher-voltage household circuit (used for dryers, ovens, etc.)."
    E["T5D10"] = "Using P = E² / R: 12² ÷ 50 = 144 ÷ 50 = 2.88 watts, approximately 2.9 watts. When you know voltage and resistance but not current, use this form of the power equation."
    E["T5D11"] = "Using I = P / E: 50 watts ÷ 120 volts ≈ 0.42 amps. Rearranging P = E × I to solve for current gives you the current drawn by a device of known power and voltage."
    E["T5D12"] = "Using R = E / I: 240 volts ÷ 24 amps = 10 ohms. This is Ohm's Law in its simplest form — voltage divided by current equals resistance."
    E["T5D13"] = "In a series circuit, the current is always the same through all components. There's only one path for current to flow, so the same current passes through every component. Voltage divides among the components, but current is identical everywhere."
    E["T5D14"] = "In a parallel circuit, the voltage is always the same across all components. Each component connects directly across the power source, so they all see the same voltage. Current divides among the branches, but voltage is identical across all of them."

    # ── T6A ──────────────────────────────────────────────────────────
    E["T6A01"] = "A resistor opposes the flow of current in a circuit. Resistance is measured in ohms, and resistors are used to control current levels, divide voltages, and set operating points in circuits. They convert electrical energy to heat."
    E["T6A02"] = "Electrolytic capacitors are typically polarized — they must be connected with the correct polarity or they can be damaged or even explode. Paper, ceramic, and mica capacitors are generally non-polarized and can be connected either way."
    E["T6A03"] = "A battery is a combination of two or more cells that produces electrical energy from chemical reactions. A single cell produces a fixed voltage (like 1.5V for alkaline), and batteries combine multiple cells to produce higher voltages."
    E["T6A04"] = "A capacitor stores energy in an electric field between its plates. When voltage is applied, charge builds up on the plates, storing energy. Capacitors are used for filtering, coupling, timing, and energy storage throughout electronics."
    E["T6A05"] = "An inductor stores energy in a magnetic field created by current flowing through a coil of wire. The magnetic field builds when current flows and collapses when current stops, releasing the stored energy."
    E["T6A06"] = "An inductor stores energy in a magnetic field. When current flows through the coil, a magnetic field forms around it, storing energy. This is the fundamental operating principle of inductors, transformers, and many RF circuits."
    E["T6A07"] = "An inductor is typically constructed as a coil of wire. The coil shape concentrates the magnetic field and increases the inductance. Adding a ferromagnetic core (like iron) further increases the inductance."
    E["T6A08"] = "A variable resistor (potentiometer) is the component used to adjust circuit resistance. By turning the shaft, you change the resistance, which can control volume, brightness, or other circuit parameters. It's one of the most common user controls."
    E["T6A09"] = "Component 3 in figure T-2 represents a single-pole single-throw (SPST) switch. SPST is the simplest switch type — it either connects or disconnects a single circuit path. One pole (connection point), one throw (position)."
    E["T6A10"] = "The unit of capacitance is the farad. In practical circuits, you'll usually see microfarads (µF) or picofarads (pF), as one full farad is an enormous capacitance. Named after Michael Faraday."
    E["T6A11"] = "The unit of inductance is the henry. Practical inductors are measured in millihenrys (mH) or microhenrys (µH). Named after Joseph Henry, who discovered electromagnetic self-inductance."

    # ── T6B ──────────────────────────────────────────────────────────
    E["T6B01"] = "A diode allows current to flow in only one direction. It has an anode and cathode — current flows from anode to cathode (forward bias) but is blocked in the reverse direction. This one-way valve behavior is fundamental to power supplies and signal processing."
    E["T6B02"] = "An LED (Light-Emitting Diode) emits light when forward current flows through it. It's a special type of diode made from semiconductor materials that release photons when electrons recombine with holes. Different materials produce different colors."
    E["T6B03"] = "A transistor's main function is to amplify or switch electronic signals. It's the fundamental building block of modern electronics — every computer chip contains billions of transistors. In amateur radio, transistors amplify RF signals in receivers and transmitters."
    E["T6B04"] = "A transistor consists of three regions of semiconductor material. In a bipolar junction transistor (BJT), these are the emitter, base, and collector. In a field-effect transistor (FET), they're the source, gate, and drain."
    E["T6B05"] = "A field-effect transistor (FET) has a gate, drain, and source. This distinguishes it from a bipolar transistor, which has a base, collector, and emitter. FETs are widely used in receivers because of their high input impedance."
    E["T6B06"] = "The main function of a transistor in an electronic circuit is to amplify signals or act as a switch. Transistors can boost weak signals to usable levels (amplification) or turn circuits on and off (switching). They're the workhorse of electronics."
    E["T6B07"] = "An LED emits light due to forward current flowing through the semiconductor junction. When electrons cross the junction and recombine, they release energy as photons (light). The color depends on the semiconductor material used."
    E["T6B08"] = "A regulator maintains a constant output voltage regardless of changes in input voltage or load current. Voltage regulators are essential in power supplies to provide clean, stable DC power to sensitive electronic circuits."
    E["T6B09"] = "Semiconductor material is used in a solar cell to convert light energy into electrical energy. When photons hit the semiconductor junction, they knock electrons free, creating current — this is the photovoltaic effect."
    E["T6B10"] = "The approximate junction threshold voltage of a typical silicon diode is 0.7 volts. This means a silicon diode needs about 0.7V of forward bias before significant current flows. Germanium diodes have a lower threshold of about 0.3V."
    E["T6B11"] = "In amplifiers, the term \"gain\" refers to the ratio of the output signal to the input signal — it can describe voltage gain, current gain, or power gain. All of these are valid meanings of gain in the context of amplifiers."
    E["T6B12"] = "The three electrodes of a bipolar junction transistor are the emitter, base, and collector. The base controls current flow between the emitter and collector. A small current into the base allows a much larger current to flow from collector to emitter — that's how transistors amplify."

    # ── T6C ──────────────────────────────────────────────────────────
    E["T6C01"] = "An electrical diagram using standard component symbols is called a schematic. Schematics use standardized symbols to represent resistors, capacitors, transistors, and other components, showing how they're connected. It's the universal language of electronics."
    E["T6C02"] = "Component 1 in figure T-1 is a resistor. The zigzag symbol is the standard schematic representation for a resistor. Recognizing common schematic symbols is an important skill for any electronics work."
    E["T6C03"] = "Component 2 in figure T-1 is a transistor. The symbol shows the characteristic three-terminal device with its distinctive arrow indicating current direction. Learning to identify transistor symbols in schematics is fundamental."
    E["T6C04"] = "Component 3 in figure T-1 is a lamp (light bulb). The circle with the internal element represents an incandescent lamp in standard schematic notation."
    E["T6C05"] = "Component 4 in figure T-1 is a battery. The alternating long and short lines represent multiple cells — the long line is positive and the short line is negative."
    E["T6C06"] = "Component 6 in figure T-2 is a capacitor. The two parallel lines (or one curved line and one straight) represent a capacitor in schematic diagrams."
    E["T6C07"] = "Component 8 in figure T-2 is a light-emitting diode (LED). The diode symbol with arrows pointing away (representing emitted light) is the standard LED symbol."
    E["T6C08"] = "Component 9 in figure T-2 is a variable resistor (potentiometer). The resistor symbol with an arrow through it indicates that the resistance can be adjusted."
    E["T6C09"] = "The schematic symbol for a PNP transistor has the arrow pointing inward (toward the base). Remember: PNP = Points iN Proudly. For NPN, the arrow points outward (Not Pointing iN)."
    E["T6C10"] = "Component 1 in figure T-3 is an NPN transistor. The arrow on the emitter points away from the base — NPN = Not Pointing iN."
    E["T6C11"] = "Component 4 in figure T-3 is a transformer. The two coils with parallel lines between them represent a transformer, which transfers energy between circuits via magnetic coupling."
    E["T6C12"] = "Component 4 in figure T-2 identifies the component's value (typically) — in schematic notation, this helps you know what specific part to use when building the circuit."

    # ── T6D ──────────────────────────────────────────────────────────
    E["T6D01"] = "A switch is the component that controls the flow of current by making or breaking a circuit connection. When closed, it completes the circuit; when open, it breaks it. Switches range from simple toggle switches to complex multi-position rotary switches."
    E["T6D02"] = "A relay is a current-controlled switch — an electromagnet that physically opens or closes a set of contacts. When current flows through the relay's coil, the magnetic field pulls the contacts closed (or open). Relays let a small control signal switch a larger power circuit."
    E["T6D03"] = "Shielded wire is used to reduce receiver overload and prevent unwanted signals from coupling onto the wire. The shield acts as a barrier to external RF fields, keeping interference out and preventing the wire from radiating like an antenna."
    E["T6D04"] = "An integrated circuit (IC) is a package containing multiple electronic components combined into a single device. ICs can contain thousands to billions of transistors, resistors, and other components on a tiny silicon chip."
    E["T6D05"] = "Component 5 in figure T-3 is an inductor. The coil symbol represents the wire wound into loops that creates and stores energy in a magnetic field."
    E["T6D06"] = "Component 6 in figure T-3 represents a transformer. It consists of two inductors (coils) coupled together magnetically, used to transfer energy between circuits and change voltage levels."
    E["T6D07"] = "LEDs, incandescent lamps, and liquid crystal displays are all commonly used as visual indicators. All three can show status, signal levels, or other information visually. Modern equipment uses LEDs almost exclusively due to their low power consumption and long life."
    E["T6D08"] = "An RFID tag contains a transmitter and receiver that can communicate data when activated by a nearby interrogator. The tag's built-in antenna receives a signal from the reader, which powers the tag and allows it to transmit its stored data."
    E["T6D09"] = "A piezoelectric crystal oscillator uses the mechanical vibration of a quartz crystal to generate a precise frequency. The crystal vibrates at a very stable frequency determined by its physical dimensions, making crystal oscillators the standard for frequency references."
    E["T6D10"] = "A capacitor blocks DC but allows AC to pass. This property is used for coupling (passing AC signals between stages while blocking DC bias voltages) and filtering. The higher the frequency, the more easily it passes through a capacitor."
    E["T6D11"] = "An inductor blocks AC but allows DC to pass — the opposite of a capacitor. Inductors resist changes in current, and higher frequencies encounter more opposition (reactance). This makes inductors useful for filtering and RF chokes."

    # ── T7A ──────────────────────────────────────────────────────────
    E["T7A01"] = "Sensitivity describes a receiver's ability to detect the presence of weak signals. A more sensitive receiver can pick up fainter signals. Sensitivity is typically measured in microvolts — the lower the number, the more sensitive the receiver."
    E["T7A02"] = "Selectivity is a receiver's ability to discriminate between multiple signals on nearby frequencies. Good selectivity means the receiver can pick out one signal while rejecting adjacent ones. Filters determine selectivity."
    E["T7A03"] = "A mixer converts a signal from one frequency to another by combining it with a local oscillator signal. The mixer produces sum and difference frequencies — this frequency conversion is at the heart of the superheterodyne receiver design used in virtually all modern radios."
    E["T7A04"] = "A local oscillator generates a signal that is mixed with the incoming RF to produce an intermediate frequency. The LO frequency is adjustable, which is how you tune the receiver to different frequencies."
    E["T7A05"] = "Modulation is the process of combining an information signal (like voice) with an RF carrier for transmission. Without modulation, you'd just transmit a blank carrier with no information content."
    E["T7A06"] = "The PTT (Push-To-Talk) input switches the transceiver from receive to transmit when it is grounded. Press the mic button → PTT line grounds → radio transmits. Release → back to receive. It's the most basic control interface."
    E["T7A07"] = "A transverter converts the RF input and output of a transceiver to another band — for example, letting an HF radio operate on VHF or microwave frequencies. The name combines \"transceiver\" and \"converter.\""
    E["T7A08"] = "An oscillator generates a signal at a specific frequency. It's the core frequency-generating component in transmitters and receivers, creating the radio frequencies needed for communication."
    E["T7A09"] = "The SSB/CW-FM switch on VHF power amplifiers sets the amplifier for proper operation in the selected mode. SSB and CW need linear amplification to preserve the signal's amplitude variations, while FM can use more efficient non-linear amplification."
    E["T7A10"] = "An RF power amplifier (or linear amplifier) can be added to the output of a transceiver to increase transmitted power. It boosts the transmitter's signal before it reaches the antenna."
    E["T7A11"] = "The Variable Frequency Oscillator (VFO) circuit in a transceiver sets the receive and transmit frequency. By adjusting the VFO, you tune across the band. The VFO determines what frequency you're operating on — it's the tuning heart of the radio."

    # ── T7B ──────────────────────────────────────────────────────────
    E["T7B01"] = "If your FM handheld or mobile is over-deviating, you're talking too loudly or too close to the microphone. Back away from the mic and speak at a normal conversational level. Over-deviation causes distorted, hard-to-understand audio on the receiving end."
    E["T7B02"] = "If a broadcast AM or FM radio is receiving your amateur transmissions, the problem is fundamental overload — the consumer receiver can't reject your strong nearby signal because it has poor front-end filtering. The issue is with their receiver, not your transmitter."
    E["T7B03"] = "If you hear a buzzy, distorted signal that varies with engine speed in a mobile installation, the problem is alternator whine (or ignition noise) getting into the radio. Proper bonding, filtering, and keeping power cables away from the antenna cable can fix this."
    E["T7B04"] = "A high SWR can cause low RF power output from a solid-state transceiver. When the antenna system presents a poor match (high SWR), most modern radios automatically reduce power to protect their output transistors. Fix the antenna match to restore full power."
    E["T7B05"] = "To reduce interference to a non-amateur over-the-air radio receiver, you can install a filter at the receiver's antenna input. A filter that passes only the desired broadcast frequencies and rejects your amateur signal addresses the fundamental overload problem."
    E["T7B06"] = "If your neighbors experience TV interference when you transmit on 2 meters, the likely problem is poor TV receiver filtering — it can't reject your nearby VHF signal. A filter at the TV's antenna input usually solves the problem."
    E["T7B07"] = "A band-reject filter tuned to the interfering commercial FM frequency can reduce interference to a 2-meter transceiver from a nearby commercial FM station. The filter notches out the specific frequency causing the problem while passing your amateur signals."
    E["T7B08"] = "Common-mode current on a feed line means RF current is flowing on the outside of the coax shield. A ferrite choke on the feed line near the radio can suppress this. Common-mode current causes interference and can lead to RF in the shack."
    E["T7B09"] = "If your SWR readings are erratic, the most likely cause is a loose or corroded connector in your antenna system. Bad connections cause intermittent contact, which makes the SWR reading bounce around unpredictably."
    E["T7B10"] = "If your FM repeater audio is distorted or unintelligible, you may be speaking too loudly or too close to the microphone, causing over-deviation. Back off the mic and speak at a normal conversational level."
    E["T7B11"] = "Adding a clip-on ferrite \"choke\" to the microphone cable can eliminate distorted voice transmissions caused by RF feedback. The ferrite prevents the transmitted RF signal from traveling back along the mic cable and feeding back into the transmitter's audio input."

    # ── T7C ──────────────────────────────────────────────────────────
    E["T7C01"] = "A dummy load is used in place of an antenna for testing a transmitter without radiating a signal. It absorbs the transmitter's power as heat, letting you test and tune without causing interference. Every well-equipped station should have one."
    E["T7C02"] = "A field strength meter can be used to determine if an antenna is radiating. It measures the RF field near the antenna, confirming that the transmitter is actually putting out signal. A simple field strength indicator is an inexpensive but useful test tool."
    E["T7C03"] = "A typical RF dummy load consists of a 50-ohm non-inductive resistor mounted on a heat sink. The non-inductive design ensures it presents a pure 50-ohm load at radio frequencies. The heat sink dissipates the power as heat."
    E["T7C04"] = "An SWR meter measures the quality of the match between the antenna system and the transmitter. Low SWR (close to 1:1) means a good match — most of the power reaches the antenna. High SWR means power is being reflected back."
    E["T7C05"] = "Most solid-state transmitters automatically reduce output power as SWR increases to protect the RF output amplifier transistors. Excessive reflected power can overheat and destroy the output transistors. The fold-back circuit is a safety mechanism."
    E["T7C06"] = "To measure the standing wave ratio (SWR) of your antenna system, you use an SWR meter connected between the transmitter and the antenna feed line. Transmit into it and read the SWR value on the meter."
    E["T7C07"] = "Standing wave ratio (SWR) is a measure of how well the load impedance matches the transmission line's characteristic impedance. A perfect match gives 1:1 SWR. Higher SWR means more power is reflected back toward the transmitter."
    E["T7C08"] = "If you measure infinite SWR, it means there's an open circuit somewhere — likely a broken connector, cut feed line, or disconnected antenna. No power is being absorbed by the load, so everything is reflected back."
    E["T7C09"] = "The two most significant factors affecting the signal loss in a coaxial cable are cable length and operating frequency. Longer cables and higher frequencies both increase loss. Use the shortest practical run of the lowest-loss cable you can afford."
    E["T7C10"] = "Coaxial cable's outer jacket must be resistant to UV light because ultraviolet radiation degrades the jacket material, allowing moisture to enter the cable. Moisture inside coax dramatically increases signal loss and can destroy the cable."
    E["T7C11"] = "Foam-dielectric coaxial cable has less loss per foot compared to solid-dielectric types. The foam dielectric has a lower effective dielectric constant, which reduces signal loss. The trade-off is that foam cable is more susceptible to moisture contamination."

    # ── T7D ──────────────────────────────────────────────────────────
    E["T7D01"] = "A voltmeter is used to measure electric potential (voltage). It's connected in parallel across the component or circuit you want to measure. A voltmeter should have high input impedance to avoid disturbing the circuit."
    E["T7D02"] = "An ammeter is used to measure electric current. It's connected in series with the circuit so the current flows through it. Ammeters have very low internal resistance to minimize their effect on the circuit."
    E["T7D03"] = "A multimeter combines the functions of a voltmeter, ammeter, and ohmmeter in one instrument. It can measure voltage, current, and resistance, making it the most versatile and commonly used test instrument in electronics."
    E["T7D04"] = "An ohmmeter is used to measure resistance. To get an accurate reading, you must disconnect the component from the circuit — measuring resistance in-circuit gives false readings because other components provide parallel paths for current."
    E["T7D05"] = "An ohmmeter measures resistance by applying a small known current from its internal battery and measuring the resulting voltage across the component under test. Using Ohm's Law (R = E/I), the meter calculates and displays the resistance. This is why you need to disconnect the component — the meter's own current must be the only current flowing through it."
    E["T7D06"] = "An antenna analyzer measures SWR, impedance, and resonant frequency of antenna systems. It's like a specialized combination of an SWR meter and impedance bridge, purpose-built for antenna work. Every serious antenna builder should have one."
    E["T7D07"] = "The quality of a soldered joint is important because a poor solder connection creates resistance that impedes current flow and generates heat. Cold or cracked joints cause intermittent connections, noise, and equipment failures."
    E["T7D08"] = "Before soldering, clean the surfaces and apply flux to ensure a good connection. Flux removes oxide layers and helps solder flow properly onto the joint surfaces. Without proper preparation, you'll get cold joints."
    E["T7D09"] = "A cold tin-lead solder joint has a rough, grainy, or dull gray appearance. Good solder joints are smooth and shiny. If your joint looks grainy or dull, reheat it with the soldering iron and let it flow properly."
    E["T7D10"] = "Short-circuit protection is a desirable feature in a power supply because it prevents damage to both the supply and connected equipment if a wiring fault creates a short. Without it, a short circuit can cause fire, component destruction, or blown fuses."
    E["T7D11"] = "A \"deck\" is the equivalent of a \"pole\" in an idealized switch. A double-pole, double-throw (DPDT) switch has two independent circuits, each with two positions — it's like two SPDT switches mechanically linked together."

    # ── T8A ──────────────────────────────────────────────────────────
    E["T8A01"] = "FM (Frequency Modulation) is commonly used for VHF and UHF voice repeaters. FM provides clean, noise-free audio when the signal is above the receiver's threshold, making it ideal for local VHF/UHF communications."
    E["T8A02"] = "USB (Upper Sideband) is normally used for VHF and UHF SSB communications. By convention, USB is used above 10 MHz, including all VHF and UHF SSB work. LSB is used below 10 MHz on HF."
    E["T8A03"] = "SSB is the voice mode most commonly used for long-distance HF contacts. SSB is more efficient than AM or FM for weak-signal work — it concentrates all the power in one sideband and uses less bandwidth."
    E["T8A04"] = "An FM signal has a constant carrier amplitude because the information is carried in frequency variations, not amplitude changes. This constant amplitude makes FM resistant to noise (which typically affects amplitude) but means it uses more bandwidth."
    E["T8A05"] = "CW (Morse code) has the narrowest bandwidth of common amateur modes — about 150 Hz. SSB is roughly 3 kHz, and FM is about 10–15 kHz. CW's narrow bandwidth is one reason it works so well for weak-signal communication."
    E["T8A06"] = "Upper sideband (USB) is normally used for 10-meter HF, VHF, and UHF single-sideband communications. The convention is USB above 10 MHz. Since 10 meters (28 MHz) is above this threshold, USB is the standard."
    E["T8A07"] = "A key characteristic of SSB compared to FM is that SSB signals have a narrower bandwidth, which means they can be heard under noisier conditions and at greater distances with lower power."
    E["T8A08"] = "The approximate bandwidth of an SSB voice signal is about 3 kHz. This is much narrower than FM's 10–15 kHz bandwidth, which is one reason SSB is more efficient for long-distance communication."
    E["T8A09"] = "The approximate bandwidth of a VHF repeater FM voice signal is between 10 and 15 kHz. FM uses more bandwidth than SSB, but provides cleaner, noise-free audio above the squelch threshold."
    E["T8A10"] = "The typical bandwidth of an analog fast-scan TV (NTSC) signal on the 70-centimeter band is about 6 MHz. Amateur TV uses the same NTSC standard as broadcast television, which requires a wide bandwidth."
    E["T8A11"] = "The approximate maximum bandwidth of a single-sideband voice signal is about 3 kHz. This is determined by the audio frequency range (roughly 300 Hz to 2700 Hz) that passes through the SSB filter."
    E["T8A12"] = "A disadvantage of FM compared to SSB is that FM signals use more bandwidth, which means only a limited number of FM signals can fit in a given frequency range. SSB's narrower bandwidth allows more signals in the same spectrum."

    # ── T8B ──────────────────────────────────────────────────────────
    E["T8B01"] = "The ITU amateur satellite designation for a transponder or repeater with a 2-meter uplink and 70-centimeter downlink is V/U mode. V = VHF (2 meters) for uplink, U = UHF (70 cm) for downlink. The uplink band is listed first."
    E["T8B02"] = "To access a satellite repeater, you need to use Doppler shift correction because the satellite's motion causes the apparent frequency to shift. As the satellite approaches, the frequency appears higher; as it moves away, it appears lower."
    E["T8B03"] = "Tracking satellites requires knowing the Keplerian orbital elements — a set of numbers that describe the satellite's orbit (shape, tilt, position). These are updated regularly and loaded into tracking software."
    E["T8B04"] = "An FM-only radio can access amateur satellites that have FM repeaters on board. Several amateur satellites carry FM transponders, making them accessible with basic handheld radios and simple antennas."
    E["T8B05"] = "A satellite beacon transmits a continuous signal on a specific frequency, allowing ground stations to determine the satellite's signal strength and Doppler shift. Beacons are useful for tracking and testing."
    E["T8B06"] = "To get a good signal through a satellite transponder, you should use the minimum power needed — just enough so your downlink signal is about the same strength as the satellite's beacon. Excessive power can overload the transponder and interfere with other users."
    E["T8B07"] = "Spin fading on a satellite signal is caused by rotation of the satellite and its antennas. As the satellite rotates, its antenna alternately points toward and away from the ground station, causing periodic signal strength variations."
    E["T8B08"] = "U/V mode means the uplink is in the 70-centimeter (UHF) band and the downlink is in the 2-meter (VHF) band. The uplink frequency is listed first, followed by the downlink frequency."
    E["T8B09"] = "A good way to determine if an amateur satellite is operational is to check amateur satellite tracking websites or the AMSAT news pages. These resources provide current status information, including which satellites are active."
    E["T8B10"] = "LEO stands for Low Earth Orbit — a satellite orbiting relatively close to Earth, typically at altitudes below about 2,000 km. LEO satellites have orbital periods of around 100 minutes, which means they pass over any given point relatively quickly."
    E["T8B11"] = "Anyone may receive telemetry from an amateur radio satellite. There are no restrictions on receiving — you don't need special authorization, a specific license class, or a decryption key. If you can hear it, you can listen."
    E["T8B12"] = "To determine if your satellite uplink power into a linear transponder satellite is correct, compare your downlink signal strength to the satellite's beacon signal. Your signal should be about the same strength as the beacon — not stronger, not weaker."

    # ── T8C ──────────────────────────────────────────────────────────
    E["T8C01"] = "An internet gateway is the term for an amateur radio station connected to the internet that allows communication between stations using radio and stations using VoIP (Voice over Internet Protocol)."
    E["T8C02"] = "A directional antenna and an attenuator are useful for a hidden transmitter hunt (also called a \"fox hunt\"). The directional antenna shows you which way the signal is coming from, and the attenuator reduces the signal strength so you can home in as you get closer."
    E["T8C03"] = "Contesting is the operating activity that involves contacting as many stations as possible during a specified period. Contests (also called radiosport) are competitive events where operators try to make the most contacts, sometimes over a weekend."
    E["T8C04"] = "Good practice in a contest is sending only the minimum information needed for proper identification and the contest exchange. Be efficient — don't waste time with extended conversations. Get the call sign, exchange, and move on to the next contact."
    E["T8C05"] = "A grid locator is a letter-number designator assigned to a geographic location. The Maidenhead grid system divides the world into grid squares, and your grid square identifies your approximate location for VHF/UHF contests and awards."
    E["T8C06"] = "Over-the-air access to IRLP (Internet Radio Linking Project) nodes is accomplished by using DTMF (Dual-Tone Multi-Frequency) signals. You dial DTMF codes from your radio to connect to or disconnect from IRLP nodes."
    E["T8C07"] = "To find the location of a repeater, you can use a repeater directory or a club website. These resources list repeater frequencies, locations, access tones, and other details for repeaters in your area."
    E["T8C08"] = "IRLP (Internet Radio Linking Project) is a technique to connect amateur radio systems, such as repeaters, via the internet. It lets you talk through a local repeater and be heard on a linked repeater hundreds or thousands of miles away."
    E["T8C09"] = "To find stations to contact on a specific band, you can check a DX cluster, which is a network that reports real-time information about stations that are active on different bands and frequencies."
    E["T8C10"] = "Before using the EchoLink system, you need a valid amateur radio license and proof of licensure. EchoLink verifies your license to prevent unlicensed use of the system."
    E["T8C11"] = "An amateur radio phone patch connects a radio circuit to the public telephone network, allowing a radio operator to make or receive telephone calls through their radio station."

    # ── T8D ──────────────────────────────────────────────────────────
    E["T8D01"] = "DMR (Digital Mobile Radio) is the digital voice standard that divides a single 12.5 kHz channel into two time slots using TDMA. This allows two simultaneous conversations on one frequency — effectively doubling the channel capacity."
    E["T8D02"] = "FT8 is a digital mode capable of low signal-to-noise operation. It's designed for making contacts when signals are extremely weak — stations can communicate even when the signals are far below what the human ear can detect. FT8 has become enormously popular for HF contacts."
    E["T8D03"] = "An ideally shaped SSB phone signal occupies approximately 3 kHz of bandwidth. This relatively narrow bandwidth is one of SSB's key advantages over FM for long-distance communication."
    E["T8D04"] = "NTSC is an analog video standard used for amateur fast-scan television (ATV). It's the same system that was used for broadcast television in North America. It requires about 6 MHz of bandwidth."
    E["T8D05"] = "APRS (Automatic Packet Reporting System) can automatically report your station's location, show it on a map, and transmit weather station data. It's a tactical communication system used for real-time position tracking and situational awareness."
    E["T8D06"] = "PSK stands for Phase Shift Keying — a digital modulation method that encodes data by shifting the phase of the carrier signal. PSK31 is a popular amateur digital mode that uses very narrow bandwidth."
    E["T8D07"] = "Winlink is a worldwide radio email system that uses amateur radio frequencies to send and receive email. It bridges the gap between radio and internet email, especially useful when internet access is unavailable."
    E["T8D08"] = "Packet radio transmissions include a checksum that permits error detection. The checksum lets the receiving station verify that the data was received correctly — if the checksum doesn't match, the packet is flagged as containing errors."
    E["T8D09"] = "CW stands for Continuous Wave, which is Morse code transmission using on-off keying of an unmodulated carrier. It's the oldest digital mode and still one of the most efficient for weak-signal communication."
    E["T8D10"] = "The typical bandwidth of a PSK31 signal is approximately 31 Hz — extremely narrow. This is one of the narrowest digital modes, allowing many PSK31 signals to fit in the bandwidth of a single SSB voice signal."
    E["T8D11"] = "ARQ (Automatic Repeat reQuest) is a technique where the receiving station detects errors and requests retransmission of corrupted data. This ensures reliable data delivery over a potentially noisy radio channel."
    E["T8D12"] = "An amateur radio mesh network is a data network using commercial Wi-Fi equipment with modified firmware to operate on amateur frequencies. It creates a self-healing, multi-node network for data communications, useful for emergency communications and community networking."

    # ── T9A ──────────────────────────────────────────────────────────
    E["T9A01"] = "A beam antenna is a directional antenna that concentrates its signal in one direction for increased gain. Yagi-Uda arrays and quad antennas are common types. By focusing energy in one direction, beam antennas provide more gain than omnidirectional designs."
    E["T9A02"] = "An isotropic antenna is a theoretical reference point that radiates equally in all directions. It's used as a baseline for measuring antenna gain (dBi). No real antenna is truly isotropic, but it's a useful mathematical concept."
    E["T9A03"] = "Antenna polarization is described by the orientation of the electric field. If the electric field oscillates vertically, the antenna is vertically polarized. If horizontally, it's horizontally polarized. Matching polarization between stations maximizes signal transfer."
    E["T9A04"] = "The short flexible antenna (rubber duck) on a handheld has less efficient radiation and lower gain compared to a full-sized quarter-wave antenna. The rubber duck is convenient but compromises performance — it doesn't radiate as effectively because it's much shorter than optimal."
    E["T9A05"] = "A half-wave dipole is approximately 468/frequency(MHz) feet long. This classic formula accounts for the end effect that makes a real dipole slightly shorter than the free-space half wavelength. It's one of the most commonly built amateur antennas."
    E["T9A06"] = "A Yagi antenna offers the greatest gain among common amateur antennas. Its multiple elements (driven element, reflector, and directors) work together to focus energy in one direction, providing significant gain over a simple dipole."
    E["T9A07"] = "Using a handheld VHF transceiver inside a vehicle without an external antenna is problematic because the vehicle's metal body significantly attenuates the signal, reducing both transmitted and received signal strength. An external antenna mounted on the vehicle is much more effective."
    E["T9A08"] = "A 19-inch vertical antenna is often used on 2 meters because it's a resonant quarter-wave at 146 MHz. Using the formula 234/146 ≈ 19 inches. A quarter-wave vertical is one of the simplest and most practical antennas for VHF."
    E["T9A09"] = "A 5/8-wavelength whip antenna for VHF or UHF mobile service has more gain than a 1/4-wave antenna. The 5/8-wave design concentrates more of its radiation toward the horizon rather than upward, which is exactly what you want for mobile ground-to-ground communication."
    E["T9A10"] = "Placing a VHF or UHF antenna at the highest point available generally results in the best performance because VHF/UHF propagation is line-of-sight. Higher antennas can \"see\" farther, extending your range to the radio horizon."
    E["T9A11"] = "A directional antenna pointed at the receiving station improves SSB and CW signals on VHF because it concentrates your transmitted power in one direction (more gain toward the target) and reduces received noise from other directions."

    # ── T9B ──────────────────────────────────────────────────────────
    E["T9B01"] = "All RF connectors used outdoors — PL-259, Type N, and BNC — should be carefully taped or sealed for weather protection. Moisture in any connector causes corrosion and signal loss. Use self-fusing silicone tape or commercial weatherproofing kits."
    E["T9B02"] = "The characteristic impedance of most common amateur radio coaxial cable is 50 ohms. This is the standard impedance for amateur radio — 75-ohm cable is used for TV and cable systems, but amateur equipment is designed for 50 ohms."
    E["T9B03"] = "The benefit of low-loss coaxial cable is that more of your transmitted power actually reaches the antenna, and more of the received signal reaches your radio. High-loss cable wastes power as heat."
    E["T9B04"] = "Open wire (ladder line) feed line has the lowest loss of common feed line types. It can have 10 times less loss than coax at HF frequencies. The trade-off is that it requires more careful routing and can't be run through metal conduit."
    E["T9B05"] = "A PL-259 connector is the standard connector for coaxial cable at HF frequencies. It's the most common connector you'll encounter on HF equipment. Also called a UHF connector, though it's actually most suitable for HF."
    E["T9B06"] = "Type N connectors are most suitable for frequencies above 400 MHz. They maintain consistent impedance at UHF and above, unlike PL-259 connectors whose performance degrades at higher frequencies."
    E["T9B07"] = "RG-58 is a common type of coaxial cable used for short runs at VHF and UHF, though it has higher loss than larger cables. For longer runs or higher frequencies, lower-loss cables like RG-213 or LMR-400 are better choices."
    E["T9B08"] = "The reason to use an impedance matching device (antenna tuner) between the transmitter and antenna system is to maximize power transfer to the antenna by matching the transmitter's output impedance to the load. A good match means less reflected power and more radiated signal."
    E["T9B09"] = "A high SWR reading can indicate a problem with the antenna system — such as a bad connector, wrong-length antenna, or broken feed line. High SWR means a poor impedance match, which wastes power as reflected energy."
    E["T9B10"] = "An SWR of 1:1 means a perfect impedance match — all the power from the transmitter is delivered to the antenna with no reflections. In practice, an SWR of 1.5:1 or lower is considered excellent."
    E["T9B11"] = "Air-dielectric hardline (rigid or semi-rigid coaxial cable) has the lowest loss of common feed line types. However, it's expensive, heavy, and difficult to install. For most amateur stations, high-quality flexible coax is a practical compromise."
    E["T9B12"] = "Standing wave ratio (SWR) is a measure of how well a load is matched to a transmission line. An SWR of 1:1 is a perfect match — all power goes to the antenna. Higher SWR means more power is reflected back toward the transmitter, reducing efficiency and potentially damaging equipment."

    for qid in FALLBACK_EXPLANATION_IDS:
        E[qid] = ""

    # fmt: on


RULE_CITATION_RE = re.compile(r"^\[[^\]]+\]\s*")


def build_fallback_explanation(q: dict) -> str:
    """Generate a safe explanation that always matches the current question."""
    answer = q["answers"][q["correct"]]
    question = RULE_CITATION_RE.sub("", q["question"]).strip()
    q_lower = question.lower()

    if answer == "All these choices are correct":
        return "All of the listed choices are correct for this question, so D is the right answer."

    if q["group"].startswith("T5B"):
        return f"This is a unit-conversion or decibel question. Work it out and you get {answer}."

    if q["group"].startswith(("T5C", "T5D")) and any(ch.isdigit() for ch in question):
        return f"Apply the appropriate circuit formula and you get {answer}."

    if q["group"].startswith("T6C"):
        return f"{answer} is the component or connection shown in the referenced figure."

    if q["group"].startswith("T7D"):
        return f"{answer} is the correct measurement method, tool, or precaution here."

    if q_lower.startswith(("what is ", "what are ")):
        return f"The correct answer is {answer}."

    if q_lower.startswith(("what does ", "which term", "what term")):
        return f"{answer} is the correct term or definition for this question."

    if q_lower.startswith(("which of the following", "which frequency", "which band", "what type")):
        return f"The correct choice here is {answer}."

    if q_lower.startswith(("where ", "when ", "how ", "why ")):
        return f"The correct answer is {answer}."

    return f"The correct answer is {q['correct']}) {answer}."


def validate_explanations(questions: list[dict]) -> None:
    """Fail fast if the explanation map drifts from the question pool."""
    question_ids = {q["id"] for q in questions}
    explanation_ids = set(EXPLANATIONS)
    missing = sorted(question_ids - explanation_ids)
    orphaned = sorted(explanation_ids - question_ids)

    if missing or orphaned:
        issues = []
        if missing:
            issues.append(f"missing explanation keys: {', '.join(missing)}")
        if orphaned:
            issues.append(f"orphan explanation keys: {', '.join(orphaned)}")
        raise SystemExit("; ".join(issues))


def load_pool() -> dict:
    """Load the 2026-2030 pool JSON."""
    with open(POOL_PATH) as f:
        return json.load(f)


def group_questions(questions: list[dict]) -> dict[str, dict[str, list[dict]]]:
    """Group questions by subelement and then by group.

    Returns: {subelement: {group: [question, ...]}}
    """
    result: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for q in questions:
        result[q["subelement"]][q["group"]].append(q)
    return result


def format_question(q: dict) -> str:
    """Format a single question as markdown."""
    lines = [f"### {q['id']}"]
    lines.append(f"**{q['question']}**")

    for letter in ("A", "B", "C", "D"):
        text = q["answers"].get(letter, "")
        if not text:
            continue
        if letter == q["correct"]:
            lines.append(f"- **{letter}) {text}** ✅")
        else:
            lines.append(f"- {letter}) {text}")

    explanation = EXPLANATIONS.get(q["id"], "")
    if not explanation:
        explanation = build_fallback_explanation(q)
    lines.append("")
    lines.append(f"> {explanation}")

    return "\n".join(lines)


def generate_subelement_file(
    subelement: str,
    name: str,
    exam_questions: int,
    pool_size: int,
    groups: dict[str, list[dict]],
) -> str:
    """Generate the full markdown file for one subelement."""
    lines = [f"# {subelement} — {name}"]
    lines.append(f"*{exam_questions} questions on the exam from a pool of {pool_size}*")
    lines.append("")

    for group_id in sorted(groups.keys()):
        desc = GROUP_DESCRIPTIONS.get(group_id, group_id)
        lines.append(f"## Group {group_id} — {desc}")
        lines.append("")

        for q in groups[group_id]:
            lines.append(format_question(q))
            lines.append("")

    return "\n".join(lines)


def main() -> None:
    _load_explanations()
    pool = load_pool()
    validate_explanations(pool["questions"])

    subelements_meta = pool["subelements"]
    grouped = group_questions(pool["questions"])

    for sub_id, groups in sorted(grouped.items()):
        meta = subelements_meta.get(sub_id, {})
        name = meta.get("name", sub_id)
        exam_qs = meta.get("exam_questions", 0)
        pool_size = meta.get("pool_size", sum(len(qs) for qs in groups.values()))

        file_stem = SUBELEMENT_FILES.get(sub_id)
        if not file_stem:
            print(f"WARNING: No file mapping for subelement {sub_id}", file=sys.stderr)
            continue

        content = generate_subelement_file(sub_id, name, exam_qs, pool_size, groups)
        out_path = OUTPUT_DIR / f"{file_stem}-questions.md"
        out_path.write_text(content)
        print(f"  ✓ {out_path.name} ({pool_size} questions)")

    print(f"\nDone — {len(grouped)} subelement files generated.")


if __name__ == "__main__":
    main()
