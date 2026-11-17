from enum import StrEnum


class DiffractionPlanExperimentType(StrEnum):
    COMMISSIONING = "Commissioning"
    DEFAULT = "Default"
    FIXED = "Fixed"
    LIGAND_BINDING = "Ligand binding"
    MAD = "MAD"
    MAD_INVERSE_BEAM = "MAD - Inverse Beam"
    MESH = "MESH"
    METAL_ID = "Metal ID"
    MXPRESSE = "MXPressE"
    MXPRESSE_SAD = "MXPressE_SAD"
    MXPRESSM = "MXPressM"
    MXPRESSO = "MXPressO"
    MXSCORE = "MXScore"
    OSC = "OSC"
    REFINEMENT = "Refinement"
    SAD = "SAD"
    SAD_INVERSE_BEAM = "SAD - Inverse Beam"
    STEPPED_TRANSMISSION = "Stepped transmission"
    XCHEM_HIGH_SYMMETRY = "XChem High Symmetry"
    XCHEM_LOW_SYMMETRY = "XChem Low Symmetry"
    XFE = "XFE"

    def __str__(self) -> str:
        return str(self.value)
