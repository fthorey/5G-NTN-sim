#!/usr/bin/env python3
import argparse

# Lookup table for ARFCN step sizes in kHz based on 3GPP TS 38.104
ARFCN_STEP_KHZ = {
    # FR1 bands (15 kHz steps)
    1: 15, 3: 15, 7: 15, 20: 15, 28: 15,
    77: 15, 78: 15, 79: 15,
    # FR2 bands (60 kHz steps)
    257: 60, 258: 60, 260: 60, 261: 60,
}

def get_arfcn_step_khz(band):
    if band in ARFCN_STEP_KHZ:
        return ARFCN_STEP_KHZ[band]
    raise ValueError(f"Unsupported band {band}. Please add it to the lookup table.")

def calculate_ssb_offset(arfcn_ssb, arfcn_pointa, scs_khz, band):
    arfcn_step_khz = get_arfcn_step_khz(band)
    delta_arfcn = arfcn_ssb - arfcn_pointa
    delta_freq_khz = delta_arfcn * arfcn_step_khz
    center_subcarrier_offset = delta_freq_khz / scs_khz
    ssb_start_offset = int(round(center_subcarrier_offset - 120))  # SSB width = 240 → 120 subcarriers each side
    return ssb_start_offset

def main():
    parser = argparse.ArgumentParser(
        description="Calculate the --ssb subcarrier offset for OAI UE configuration."
    )
    parser.add_argument("--arfcn-ssb", type=int, required=True, help="AbsoluteFrequencySSB (ARFCN)")
    parser.add_argument("--arfcn-pointa", type=int, required=True, help="AbsoluteFrequencyPointA (ARFCN)")
    parser.add_argument("--scs", type=int, choices=[15, 30, 60, 120], default=30, help="Subcarrier spacing in kHz (default: 30)")
    parser.add_argument("--band", type=int, required=True, help="NR band number (e.g., 78)")

    args = parser.parse_args()

    try:
        offset = calculate_ssb_offset(args.arfcn_ssb, args.arfcn_pointa, args.scs, args.band)
        print(f"✅ Calculated --ssb offset: {offset}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
