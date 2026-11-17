from enum import StrEnum


class DataCollectionGroupInExperimentTypeType0(StrEnum):
    BRAGG = "Bragg"
    BURN = "Burn"
    CHARACTERIZATION = "Characterization"
    COLLECT_MULTIWEDGE = "Collect - Multiwedge"
    CUSTOM = "Custom"
    DEHYDRATION = "Dehydration"
    DIAMOND_ANVIL_HIGH_PRESSURE = "Diamond Anvil High Pressure"
    EM = "EM"
    ENERGY_SCAN = "Energy scan"
    EXPERIMENT = "experiment"
    HELICAL = "Helical"
    MAD = "MAD"
    MAD_INVERSE_BEAM = "MAD - Inverse Beam"
    MESH = "Mesh"
    MESH3D = "Mesh3D"
    MULTI_POSITIONAL = "Multi-positional"
    OSC = "OSC"
    PDF = "PDF"
    PDFBRAGG = "PDF+Bragg"
    SAD = "SAD"
    SAD_INVERSE_BEAM = "SAD - Inverse Beam"
    SCREENING = "Screening"
    SERIAL_FIXED = "Serial Fixed"
    SERIAL_JET = "Serial Jet"
    SINGLE_PARTICLE = "single particle"
    STANDARD = "Standard"
    TIME_RESOLVED = "Time Resolved"
    TOMO = "tomo"
    XRF_MAP = "XRF map"
    XRF_MAP_XAS = "XRF map xas"
    XRF_SPECTRUM = "XRF spectrum"

    def __str__(self) -> str:
        return str(self.value)
