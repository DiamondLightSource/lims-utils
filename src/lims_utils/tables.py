# type: ignore
# ruff: noqa: E501

import datetime
import decimal
from typing import List, Optional

from sqlalchemy import (
    BINARY,
    TIMESTAMP,
    CheckConstraint,
    Column,
    Computed,
    Date,
    DateTime,
    Double,
    Enum,
    Float,
    ForeignKeyConstraint,
    Index,
    Integer,
    LargeBinary,
    SmallInteger,
    String,
    Table,
    Text,
    Time,
    text,
)
from sqlalchemy.dialects.mysql import (
    ENUM,
    INTEGER,
    LONGBLOB,
    LONGTEXT,
    MEDIUMINT,
    MEDIUMTEXT,
    SMALLINT,
    TINYINT,
    VARCHAR,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class AdminActivity(Base):
    __tablename__ = "AdminActivity"
    __table_args__ = (
        Index("AdminActivity_FKAction", "action"),
        Index("username", "username", unique=True),
    )

    adminActivityId: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(45), server_default=text("''"))
    action: Mapped[Optional[str]] = mapped_column(String(45))
    comments: Mapped[Optional[str]] = mapped_column(String(100))
    dateTime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class AdminVar(Base):
    __tablename__ = "AdminVar"
    __table_args__ = (
        Index("AdminVar_FKIndexName", "name"),
        Index("AdminVar_FKIndexValue", "value"),
        {"comment": "ISPyB administration values"},
    )

    varId: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(32))
    value: Mapped[Optional[str]] = mapped_column(String(1024))


class Aperture(Base):
    __tablename__ = "Aperture"

    apertureId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    sizeX: Mapped[Optional[float]] = mapped_column(Float)


class AutoProc(Base):
    __tablename__ = "AutoProc"
    __table_args__ = (
        Index("AutoProc_FKIndex1", "autoProcProgramId"),
        Index(
            "AutoProc_refined_unit_cell",
            "refinedCell_a",
            "refinedCell_b",
            "refinedCell_c",
            "refinedCell_alpha",
            "refinedCell_beta",
            "refinedCell_gamma",
            "spaceGroup",
        ),
    )

    autoProcId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcProgramId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Related program item"
    )
    spaceGroup: Mapped[Optional[str]] = mapped_column(String(45), comment="Space group")
    refinedCell_a: Mapped[Optional[float]] = mapped_column(
        Float, comment="Refined cell"
    )
    refinedCell_b: Mapped[Optional[float]] = mapped_column(
        Float, comment="Refined cell"
    )
    refinedCell_c: Mapped[Optional[float]] = mapped_column(
        Float, comment="Refined cell"
    )
    refinedCell_alpha: Mapped[Optional[float]] = mapped_column(
        Float, comment="Refined cell"
    )
    refinedCell_beta: Mapped[Optional[float]] = mapped_column(
        Float, comment="Refined cell"
    )
    refinedCell_gamma: Mapped[Optional[float]] = mapped_column(
        Float, comment="Refined cell"
    )
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Creation or last update date/time"
    )

    AutoProcScaling: Mapped[List["AutoProcScaling"]] = relationship(
        "AutoProcScaling", back_populates="AutoProc_"
    )


class AutoProcProgram(Base):
    __tablename__ = "AutoProcProgram"
    __table_args__ = (
        ForeignKeyConstraint(
            ["processingJobId"],
            ["ProcessingJob.processingJobId"],
            name="AutoProcProgram_FK2",
        ),
        Index("AutoProcProgram_FK2", "processingJobId"),
    )

    autoProcProgramId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    processingCommandLine: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Command line for running the automatic processing"
    )
    processingPrograms: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Processing programs (comma separated)"
    )
    processingStatus: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), comment="success (1) / fail (0)"
    )
    processingMessage: Mapped[Optional[str]] = mapped_column(
        String(255), comment="warning, error,..."
    )
    processingStartTime: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Processing start time"
    )
    processingEndTime: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Processing end time"
    )
    processingEnvironment: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Cpus, Nodes,..."
    )
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Creation or last update date/time"
    )
    processingJobId: Mapped[Optional[int]] = mapped_column(INTEGER)

    ProcessingJob: Mapped["ProcessingJob"] = relationship(
        "ProcessingJob", back_populates="AutoProcProgram_"
    )
    Screening: Mapped[List["Screening"]] = relationship(
        "Screening", back_populates="AutoProcProgram_"
    )
    AutoProcIntegration: Mapped[List["AutoProcIntegration"]] = relationship(
        "AutoProcIntegration", back_populates="AutoProcProgram_"
    )
    AutoProcProgramAttachment: Mapped[List["AutoProcProgramAttachment"]] = relationship(
        "AutoProcProgramAttachment", back_populates="AutoProcProgram_"
    )
    AutoProcProgramMessage: Mapped[List["AutoProcProgramMessage"]] = relationship(
        "AutoProcProgramMessage", back_populates="AutoProcProgram_"
    )
    PDBEntry: Mapped[List["PDBEntry"]] = relationship(
        "PDBEntry", back_populates="AutoProcProgram_"
    )
    Tomogram: Mapped[List["Tomogram"]] = relationship(
        "Tomogram", back_populates="AutoProcProgram_"
    )
    zc_ZocaloBuffer: Mapped[List["ZcZocaloBuffer"]] = relationship(
        "ZcZocaloBuffer", back_populates="AutoProcProgram_"
    )
    MXMRRun: Mapped[List["MXMRRun"]] = relationship(
        "MXMRRun", back_populates="AutoProcProgram_"
    )
    MotionCorrection: Mapped[List["MotionCorrection"]] = relationship(
        "MotionCorrection", back_populates="AutoProcProgram_"
    )
    PDBEntry_has_AutoProcProgram: Mapped[
        List["PDBEntryHasAutoProcProgram"]
    ] = relationship("PDBEntryHasAutoProcProgram", back_populates="AutoProcProgram_")
    CTF: Mapped[List["CTF"]] = relationship("CTF", back_populates="AutoProcProgram_")
    ParticlePicker: Mapped[List["ParticlePicker"]] = relationship(
        "ParticlePicker", back_populates="AutoProcProgram_"
    )
    RelativeIceThickness: Mapped[List["RelativeIceThickness"]] = relationship(
        "RelativeIceThickness", back_populates="AutoProcProgram_"
    )
    ParticleClassificationGroup: Mapped[
        List["ParticleClassificationGroup"]
    ] = relationship("ParticleClassificationGroup", back_populates="AutoProcProgram_")
    XRFFluorescenceMapping: Mapped[List["XRFFluorescenceMapping"]] = relationship(
        "XRFFluorescenceMapping", back_populates="AutoProcProgram_"
    )


class BFAutomationError(Base):
    __tablename__ = "BF_automationError"

    automationErrorId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    errorType: Mapped[str] = mapped_column(String(40))
    solution: Mapped[Optional[str]] = mapped_column(Text)

    BF_automationFault: Mapped[List["BFAutomationFault"]] = relationship(
        "BFAutomationFault", back_populates="BF_automationError"
    )


class BFSystem(Base):
    __tablename__ = "BF_system"

    systemId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(200))

    BF_component: Mapped[List["BFComponent"]] = relationship(
        "BFComponent", back_populates="BF_system"
    )
    BF_system_beamline: Mapped[List["BFSystemBeamline"]] = relationship(
        "BFSystemBeamline", back_populates="BF_system"
    )


class BLSample(Base):
    __tablename__ = "BLSample"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSubSampleId"], ["BLSubSample.blSubSampleId"], name="BLSample_ibfk4"
        ),
        ForeignKeyConstraint(
            ["containerId"],
            ["Container.containerId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSample_ibfk_1",
        ),
        ForeignKeyConstraint(
            ["crystalId"],
            ["Crystal.crystalId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSample_ibfk_2",
        ),
        ForeignKeyConstraint(
            ["diffractionPlanId"],
            ["DiffractionPlan.diffractionPlanId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSample_ibfk_3",
        ),
        ForeignKeyConstraint(
            ["screenComponentGroupId"],
            ["ScreenComponentGroup.screenComponentGroupId"],
            name="BLSample_fk5",
        ),
        Index("BLSampleImage_idx1", "blSubSampleId"),
        Index("BLSample_FKIndex1", "containerId"),
        Index("BLSample_FKIndex3", "diffractionPlanId"),
        Index("BLSample_FKIndex_Status", "blSampleStatus"),
        Index("BLSample_Index1", "name"),
        Index("BLSample_fk5", "screenComponentGroupId"),
        Index("crystalId", "crystalId", "containerId"),
    )

    blSampleId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Creation or last update date/time",
    )
    diffractionPlanId: Mapped[Optional[int]] = mapped_column(INTEGER)
    crystalId: Mapped[Optional[int]] = mapped_column(INTEGER)
    containerId: Mapped[Optional[int]] = mapped_column(INTEGER)
    name: Mapped[Optional[str]] = mapped_column(String(45))
    code: Mapped[Optional[str]] = mapped_column(String(45))
    location: Mapped[Optional[str]] = mapped_column(String(45))
    holderLength: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    loopLength: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    loopType: Mapped[Optional[str]] = mapped_column(String(45))
    wireWidth: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    comments: Mapped[Optional[str]] = mapped_column(String(1024))
    completionStage: Mapped[Optional[str]] = mapped_column(String(45))
    structureStage: Mapped[Optional[str]] = mapped_column(String(45))
    publicationStage: Mapped[Optional[str]] = mapped_column(String(45))
    publicationComments: Mapped[Optional[str]] = mapped_column(String(255))
    blSampleStatus: Mapped[Optional[str]] = mapped_column(String(20))
    isInSampleChanger: Mapped[Optional[int]] = mapped_column(TINYINT(1))
    lastKnownCenteringPosition: Mapped[Optional[str]] = mapped_column(String(255))
    POSITIONID: Mapped[Optional[int]] = mapped_column(INTEGER)
    SMILES: Mapped[Optional[str]] = mapped_column(
        String(400),
        comment="the symbolic description of the structure of a chemical compound",
    )
    blSubSampleId: Mapped[Optional[int]] = mapped_column(INTEGER)
    lastImageURL: Mapped[Optional[str]] = mapped_column(String(255))
    screenComponentGroupId: Mapped[Optional[int]] = mapped_column(INTEGER)
    volume: Mapped[Optional[float]] = mapped_column(Float)
    dimension1: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    dimension2: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    dimension3: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    shape: Mapped[Optional[str]] = mapped_column(String(15))
    packingFraction: Mapped[Optional[float]] = mapped_column(Float)
    preparationTemeprature: Mapped[Optional[int]] = mapped_column(
        MEDIUMINT, comment="Sample preparation temperature, Units: kelvin"
    )
    preparationHumidity: Mapped[Optional[float]] = mapped_column(
        Float, comment="Sample preparation humidity, Units: %"
    )
    blottingTime: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Blotting time, Units: sec"
    )
    blottingForce: Mapped[Optional[float]] = mapped_column(
        Float, comment="Force used when blotting sample, Units: N?"
    )
    blottingDrainTime: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Time sample left to drain after blotting, Units: sec"
    )
    support: Mapped[Optional[str]] = mapped_column(
        String(50), comment="Sample support material"
    )
    subLocation: Mapped[Optional[int]] = mapped_column(
        SMALLINT,
        comment="Indicates the sample's location on a multi-sample pin, where 1 is closest to the pin base",
    )
    staffComments: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Any staff comments on the sample"
    )

    BLSubSample: Mapped["BLSubSample"] = relationship(
        "BLSubSample", foreign_keys=[blSubSampleId], back_populates="BLSample_"
    )
    Container: Mapped["Container"] = relationship(
        "Container", back_populates="BLSample_"
    )
    Crystal: Mapped["Crystal"] = relationship("Crystal", back_populates="BLSample_")
    DiffractionPlan: Mapped["DiffractionPlan"] = relationship(
        "DiffractionPlan", back_populates="BLSample_"
    )
    ScreenComponentGroup: Mapped["ScreenComponentGroup"] = relationship(
        "ScreenComponentGroup", back_populates="BLSample_"
    )
    Project: Mapped[List["Project"]] = relationship(
        "Project", secondary="Project_has_BLSample", back_populates="BLSample_"
    )
    BLSampleImage: Mapped[List["BLSampleImage"]] = relationship(
        "BLSampleImage", back_populates="BLSample_"
    )
    BLSubSample_: Mapped[List["BLSubSample"]] = relationship(
        "BLSubSample",
        foreign_keys="[BLSubSample.blSampleId]",
        back_populates="BLSample1",
    )
    BLSample_has_Positioner: Mapped[List["BLSampleHasPositioner"]] = relationship(
        "BLSampleHasPositioner", back_populates="BLSample_"
    )
    XRFFluorescenceMappingROI: Mapped[List["XRFFluorescenceMappingROI"]] = relationship(
        "XRFFluorescenceMappingROI", back_populates="BLSample_"
    )
    BLSampleGroup_has_BLSample: Mapped[List["BLSampleGroupHasBLSample"]] = relationship(
        "BLSampleGroupHasBLSample", back_populates="BLSample_"
    )
    BLSample_has_DataCollectionPlan: Mapped[
        List["BLSampleHasDataCollectionPlan"]
    ] = relationship("BLSampleHasDataCollectionPlan", back_populates="BLSample_")
    DataCollectionGroup: Mapped[List["DataCollectionGroup"]] = relationship(
        "DataCollectionGroup", back_populates="BLSample_"
    )
    EnergyScan: Mapped[List["EnergyScan"]] = relationship(
        "EnergyScan", back_populates="BLSample_"
    )
    RobotAction: Mapped[List["RobotAction"]] = relationship(
        "RobotAction", back_populates="BLSample_"
    )
    SampleComposition: Mapped[List["SampleComposition"]] = relationship(
        "SampleComposition", back_populates="BLSample_"
    )
    XFEFluorescenceSpectrum: Mapped[List["XFEFluorescenceSpectrum"]] = relationship(
        "XFEFluorescenceSpectrum", back_populates="BLSample_"
    )
    BLSample_has_EnergyScan: Mapped[List["BLSampleHasEnergyScan"]] = relationship(
        "BLSampleHasEnergyScan", back_populates="BLSample_"
    )
    ContainerQueueSample: Mapped[List["ContainerQueueSample"]] = relationship(
        "ContainerQueueSample", back_populates="BLSample_"
    )


class BLSampleImage(Base):
    __tablename__ = "BLSampleImage"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleId"], ["BLSample.blSampleId"], name="BLSampleImage_fk1"
        ),
        ForeignKeyConstraint(
            ["blSampleImageScoreId"],
            ["BLSampleImageScore.blSampleImageScoreId"],
            onupdate="CASCADE",
            name="BLSampleImage_fk3",
        ),
        ForeignKeyConstraint(
            ["containerInspectionId"],
            ["ContainerInspection.containerInspectionId"],
            name="BLSampleImage_fk2",
        ),
        Index("BLSampleImage_fk2", "containerInspectionId"),
        Index("BLSampleImage_fk3", "blSampleImageScoreId"),
        Index("BLSampleImage_idx1", "blSampleId"),
        Index("BLSampleImage_imageFullPath", "imageFullPath", unique=True),
    )

    blSampleImageId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    blSampleId: Mapped[int] = mapped_column(INTEGER)
    offsetX: Mapped[int] = mapped_column(
        Integer,
        server_default=text("'0'"),
        comment="The x offset of the image relative to the canvas",
    )
    offsetY: Mapped[int] = mapped_column(
        Integer,
        server_default=text("'0'"),
        comment="The y offset of the image relative to the canvas",
    )
    micronsPerPixelX: Mapped[Optional[float]] = mapped_column(Float)
    micronsPerPixelY: Mapped[Optional[float]] = mapped_column(Float)
    imageFullPath: Mapped[Optional[str]] = mapped_column(String(255))
    blSampleImageScoreId: Mapped[Optional[int]] = mapped_column(INTEGER)
    comments: Mapped[Optional[str]] = mapped_column(String(255))
    blTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    containerInspectionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    modifiedTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    BLSample_: Mapped["BLSample"] = relationship(
        "BLSample", back_populates="BLSampleImage"
    )
    BLSampleImageScore: Mapped["BLSampleImageScore"] = relationship(
        "BLSampleImageScore", back_populates="BLSampleImage_"
    )
    ContainerInspection: Mapped["ContainerInspection"] = relationship(
        "ContainerInspection", back_populates="BLSampleImage_"
    )
    BLSubSample: Mapped[List["BLSubSample"]] = relationship(
        "BLSubSample", back_populates="BLSampleImage_"
    )
    BLSampleImageAnalysis: Mapped[List["BLSampleImageAnalysis"]] = relationship(
        "BLSampleImageAnalysis", back_populates="BLSampleImage_"
    )
    BLSampleImageMeasurement: Mapped[List["BLSampleImageMeasurement"]] = relationship(
        "BLSampleImageMeasurement", back_populates="BLSampleImage_"
    )
    BLSampleImage_has_Positioner: Mapped[
        List["BLSampleImageHasPositioner"]
    ] = relationship("BLSampleImageHasPositioner", back_populates="BLSampleImage_")
    BLSampleImage_has_AutoScoreClass: Mapped[
        List["BLSampleImageHasAutoScoreClass"]
    ] = relationship("BLSampleImageHasAutoScoreClass", back_populates="BLSampleImage_")


class BLSampleImageAutoScoreSchema(Base):
    __tablename__ = "BLSampleImageAutoScoreSchema"
    __table_args__ = {"comment": "Scoring schema name and whether it is enabled"}

    blSampleImageAutoScoreSchemaId: Mapped[int] = mapped_column(
        TINYINT, primary_key=True
    )
    schemaName: Mapped[str] = mapped_column(
        String(25), comment="Name of the schema e.g. Hampton, MARCO"
    )
    enabled: Mapped[Optional[int]] = mapped_column(
        TINYINT(1),
        server_default=text("'1'"),
        comment="Whether this schema is enabled (could be configurable in the UI)",
    )

    BLSampleImageAutoScoreClass: Mapped[
        List["BLSampleImageAutoScoreClass"]
    ] = relationship(
        "BLSampleImageAutoScoreClass",
        back_populates="BLSampleImageAutoScoreSchema_",
    )


class BLSampleImageScore(Base):
    __tablename__ = "BLSampleImageScore"

    blSampleImageScoreId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(45))
    score: Mapped[Optional[float]] = mapped_column(Float)
    colour: Mapped[Optional[str]] = mapped_column(String(15))

    BLSampleImage_: Mapped[List["BLSampleImage"]] = relationship(
        "BLSampleImage", back_populates="BLSampleImageScore"
    )


class BLSampleType(Base):
    __tablename__ = "BLSampleType"

    blSampleTypeId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    proposalType: Mapped[Optional[str]] = mapped_column(String(10))
    active: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), server_default=text("'1'"), comment="1=active, 0=inactive"
    )

    BLSampleGroup_has_BLSample: Mapped[List["BLSampleGroupHasBLSample"]] = relationship(
        "BLSampleGroupHasBLSample", back_populates="BLSampleType_"
    )


class BLSubSample(Base):
    __tablename__ = "BLSubSample"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleId"],
            ["BLSample.blSampleId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSubSample_blSamplefk_1",
        ),
        ForeignKeyConstraint(
            ["blSampleImageId"],
            ["BLSampleImage.blSampleImageId"],
            name="BLSubSample_blSampleImagefk_1",
        ),
        ForeignKeyConstraint(
            ["diffractionPlanId"],
            ["DiffractionPlan.diffractionPlanId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSubSample_diffractionPlanfk_1",
        ),
        ForeignKeyConstraint(
            ["motorPositionId"],
            ["MotorPosition.motorPositionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSubSample_motorPositionfk_1",
        ),
        ForeignKeyConstraint(
            ["position2Id"],
            ["Position.positionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSubSample_positionfk_2",
        ),
        ForeignKeyConstraint(
            ["positionId"],
            ["Position.positionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSubSample_positionfk_1",
        ),
        Index("BLSubSample_FKIndex1", "blSampleId"),
        Index("BLSubSample_FKIndex2", "diffractionPlanId"),
        Index("BLSubSample_FKIndex3", "positionId"),
        Index("BLSubSample_FKIndex4", "motorPositionId"),
        Index("BLSubSample_FKIndex5", "position2Id"),
        Index("BLSubSample_blSampleImagefk_1", "blSampleImageId"),
    )

    blSubSampleId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    blSampleId: Mapped[int] = mapped_column(INTEGER, comment="sample")
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Creation or last update date/time",
    )
    diffractionPlanId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="eventually diffractionPlan"
    )
    blSampleImageId: Mapped[Optional[int]] = mapped_column(INTEGER)
    positionId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="position of the subsample"
    )
    position2Id: Mapped[Optional[int]] = mapped_column(INTEGER)
    motorPositionId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="motor position"
    )
    blSubSampleUUID: Mapped[Optional[str]] = mapped_column(
        String(45), comment="uuid of the blsubsample"
    )
    imgFileName: Mapped[Optional[str]] = mapped_column(
        String(255), comment="image filename"
    )
    imgFilePath: Mapped[Optional[str]] = mapped_column(
        String(1024), comment="url image"
    )
    comments: Mapped[Optional[str]] = mapped_column(String(1024), comment="comments")
    source: Mapped[Optional[str]] = mapped_column(
        Enum("manual", "auto"), server_default=text("'manual'")
    )
    type: Mapped[Optional[str]] = mapped_column(
        String(10),
        comment="The type of subsample, i.e. roi (region), poi (point), loi (line)",
    )

    BLSample_: Mapped[List["BLSample"]] = relationship(
        "BLSample",
        foreign_keys="[BLSample.blSubSampleId]",
        back_populates="BLSubSample",
    )
    BLSample1: Mapped["BLSample"] = relationship(
        "BLSample", foreign_keys=[blSampleId], back_populates="BLSubSample_"
    )
    BLSampleImage_: Mapped["BLSampleImage"] = relationship(
        "BLSampleImage", back_populates="BLSubSample"
    )
    DiffractionPlan: Mapped["DiffractionPlan"] = relationship(
        "DiffractionPlan", back_populates="BLSubSample_"
    )
    MotorPosition: Mapped["MotorPosition"] = relationship(
        "MotorPosition", back_populates="BLSubSample_"
    )
    Position: Mapped["Position"] = relationship(
        "Position", foreign_keys=[position2Id], back_populates="BLSubSample_"
    )
    Position_: Mapped["Position"] = relationship(
        "Position", foreign_keys=[positionId], back_populates="BLSubSample1"
    )
    DataCollection: Mapped[List["DataCollection"]] = relationship(
        "DataCollection", back_populates="BLSubSample_"
    )
    BLSampleImageMeasurement: Mapped[List["BLSampleImageMeasurement"]] = relationship(
        "BLSampleImageMeasurement", back_populates="BLSubSample_"
    )
    BLSubSample_has_Positioner: Mapped[List["BLSubSampleHasPositioner"]] = relationship(
        "BLSubSampleHasPositioner", back_populates="BLSubSample_"
    )
    EnergyScan: Mapped[List["EnergyScan"]] = relationship(
        "EnergyScan", back_populates="BLSubSample_"
    )
    XFEFluorescenceSpectrum: Mapped[List["XFEFluorescenceSpectrum"]] = relationship(
        "XFEFluorescenceSpectrum", back_populates="BLSubSample_"
    )
    ContainerQueueSample: Mapped[List["ContainerQueueSample"]] = relationship(
        "ContainerQueueSample", back_populates="BLSubSample_"
    )


class BeamCalendar(Base):
    __tablename__ = "BeamCalendar"

    beamCalendarId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    run: Mapped[str] = mapped_column(String(7))
    beamStatus: Mapped[str] = mapped_column(String(24))
    startDate: Mapped[datetime.datetime] = mapped_column(DateTime)
    endDate: Mapped[datetime.datetime] = mapped_column(DateTime)

    BLSession: Mapped[List["BLSession"]] = relationship(
        "BLSession", back_populates="BeamCalendar_"
    )


class BeamlineStats(Base):
    __tablename__ = "BeamlineStats"

    beamlineStatsId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    beamline: Mapped[Optional[str]] = mapped_column(String(10))
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ringCurrent: Mapped[Optional[float]] = mapped_column(Float)
    energy: Mapped[Optional[float]] = mapped_column(Float)
    gony: Mapped[Optional[float]] = mapped_column(Float)
    beamW: Mapped[Optional[float]] = mapped_column(Float)
    beamH: Mapped[Optional[float]] = mapped_column(Float)
    flux: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    scanFileW: Mapped[Optional[str]] = mapped_column(String(255))
    scanFileH: Mapped[Optional[str]] = mapped_column(String(255))

    BeamApertures: Mapped[List["BeamApertures"]] = relationship(
        "BeamApertures", back_populates="BeamlineStats_"
    )
    BeamCentres: Mapped[List["BeamCentres"]] = relationship(
        "BeamCentres", back_populates="BeamlineStats_"
    )


class CalendarHash(Base):
    __tablename__ = "CalendarHash"
    __table_args__ = {
        "comment": "Lets people get to their calendars without logging in using a "
        "private (hash) url"
    }

    calendarHashId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    ckey: Mapped[Optional[str]] = mapped_column(String(50))
    hash: Mapped[Optional[str]] = mapped_column(String(128))
    beamline: Mapped[Optional[int]] = mapped_column(TINYINT(1))


class ComponentSubType(Base):
    __tablename__ = "ComponentSubType"

    componentSubTypeId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(String(31))
    hasPh: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text("'0'"))
    proposalType: Mapped[Optional[str]] = mapped_column(String(10))
    active: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), server_default=text("'1'"), comment="1=active, 0=inactive"
    )

    Protein: Mapped[List["Protein"]] = relationship(
        "Protein", secondary="Component_has_SubType", back_populates="ComponentSubType_"
    )


class ComponentType(Base):
    __tablename__ = "ComponentType"
    __table_args__ = (Index("name", "name", unique=True),)

    componentTypeId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(String(31))

    Component: Mapped[List["Component"]] = relationship(
        "Component", back_populates="ComponentType_"
    )
    Protein: Mapped[List["Protein"]] = relationship(
        "Protein", back_populates="ComponentType_"
    )


class ConcentrationType(Base):
    __tablename__ = "ConcentrationType"

    concentrationTypeId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(String(31))
    symbol: Mapped[str] = mapped_column(String(8))
    proposalType: Mapped[Optional[str]] = mapped_column(String(10))
    active: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), server_default=text("'1'"), comment="1=active, 0=inactive"
    )

    Protein: Mapped[List["Protein"]] = relationship(
        "Protein", back_populates="ConcentrationType_"
    )
    SampleComposition: Mapped[List["SampleComposition"]] = relationship(
        "SampleComposition", back_populates="ConcentrationType_"
    )
    CrystalComposition: Mapped[List["CrystalComposition"]] = relationship(
        "CrystalComposition", back_populates="ConcentrationType_"
    )


class ContainerRegistry(Base):
    __tablename__ = "ContainerRegistry"
    __table_args__ = (Index("ContainerRegistry_uniq_barcode", "barcode", unique=True),)

    containerRegistryId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    barcode: Mapped[str] = mapped_column(String(20))
    comments: Mapped[Optional[str]] = mapped_column(String(255))
    recordTimestamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    ContainerReport: Mapped[List["ContainerReport"]] = relationship(
        "ContainerReport", back_populates="ContainerRegistry_"
    )
    ContainerRegistry_has_Proposal: Mapped[
        List["ContainerRegistryHasProposal"]
    ] = relationship(
        "ContainerRegistryHasProposal", back_populates="ContainerRegistry_"
    )
    Container: Mapped[List["Container"]] = relationship(
        "Container", back_populates="ContainerRegistry_"
    )


class ContainerType(Base):
    __tablename__ = "ContainerType"
    __table_args__ = {"comment": "A lookup table for different types of containers"}

    containerTypeId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    proposalType: Mapped[Optional[str]] = mapped_column(String(10))
    active: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), server_default=text("'1'"), comment="1=active, 0=inactive"
    )
    capacity: Mapped[Optional[int]] = mapped_column(Integer)
    wellPerRow: Mapped[Optional[int]] = mapped_column(SmallInteger)
    dropPerWellX: Mapped[Optional[int]] = mapped_column(SmallInteger)
    dropPerWellY: Mapped[Optional[int]] = mapped_column(SmallInteger)
    dropHeight: Mapped[Optional[float]] = mapped_column(Float)
    dropWidth: Mapped[Optional[float]] = mapped_column(Float)
    dropOffsetX: Mapped[Optional[float]] = mapped_column(Float)
    dropOffsetY: Mapped[Optional[float]] = mapped_column(Float)
    wellDrop: Mapped[Optional[int]] = mapped_column(SmallInteger)

    Screen: Mapped[List["Screen"]] = relationship(
        "Screen", back_populates="ContainerType_"
    )
    Container: Mapped[List["Container"]] = relationship(
        "Container", back_populates="ContainerType_"
    )


class CryoemInitialModel(Base):
    __tablename__ = "CryoemInitialModel"
    __table_args__ = {"comment": "Initial cryo-EM model generation results"}

    cryoemInitialModelId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    resolution: Mapped[Optional[float]] = mapped_column(
        Float, comment="Unit: Angstroms"
    )
    numberOfParticles: Mapped[Optional[int]] = mapped_column(INTEGER)

    ParticleClassification: Mapped[List["ParticleClassification"]] = relationship(
        "ParticleClassification",
        secondary="ParticleClassification_has_CryoemInitialModel",
        back_populates="CryoemInitialModel_",
    )


class DataAcquisition(Base):
    __tablename__ = "DataAcquisition"

    dataAcquisitionId: Mapped[int] = mapped_column(Integer, primary_key=True)
    sampleCellId: Mapped[int] = mapped_column(Integer)
    framesCount: Mapped[Optional[str]] = mapped_column(String(45))
    energy: Mapped[Optional[str]] = mapped_column(String(45))
    waitTime: Mapped[Optional[str]] = mapped_column(String(45))
    detectorDistance: Mapped[Optional[str]] = mapped_column(String(45))


class DataCollection(Base):
    __tablename__ = "DataCollection"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSubSampleId"],
            ["BLSubSample.blSubSampleId"],
            name="DataCollection_ibfk_8",
        ),
        ForeignKeyConstraint(
            ["dataCollectionGroupId"],
            ["DataCollectionGroup.dataCollectionGroupId"],
            name="DataCollection_ibfk_3",
        ),
        ForeignKeyConstraint(
            ["dataCollectionPlanId"],
            ["DiffractionPlan.diffractionPlanId"],
            name="DataCollection_dataCollectionPlanId",
        ),
        ForeignKeyConstraint(
            ["detectorId"], ["Detector.detectorId"], name="DataCollection_ibfk_2"
        ),
        ForeignKeyConstraint(
            ["endPositionId"],
            ["MotorPosition.motorPositionId"],
            name="DataCollection_ibfk_7",
        ),
        ForeignKeyConstraint(
            ["startPositionId"],
            ["MotorPosition.motorPositionId"],
            name="DataCollection_ibfk_6",
        ),
        ForeignKeyConstraint(
            ["strategySubWedgeOrigId"],
            ["ScreeningStrategySubWedge.screeningStrategySubWedgeId"],
            name="DataCollection_ibfk_1",
        ),
        Index("DataCollection_FKIndex0", "BLSAMPLEID"),
        Index("DataCollection_FKIndex00", "SESSIONID"),
        Index("DataCollection_FKIndex1", "dataCollectionGroupId"),
        Index("DataCollection_FKIndex2", "strategySubWedgeOrigId"),
        Index("DataCollection_FKIndex3", "detectorId"),
        Index("DataCollection_FKIndexDCNumber", "dataCollectionNumber"),
        Index("DataCollection_FKIndexImageDirectory", "imageDirectory"),
        Index("DataCollection_FKIndexImagePrefix", "imagePrefix"),
        Index("DataCollection_FKIndexStartTime", "startTime"),
        Index(
            "DataCollection_dataCollectionGroupId_startTime",
            "dataCollectionGroupId",
            "startTime",
        ),
        Index("DataCollection_dataCollectionPlanId", "dataCollectionPlanId"),
        Index("blSubSampleId", "blSubSampleId"),
        Index("endPositionId", "endPositionId"),
        Index("startPositionId", "startPositionId"),
    )

    dataCollectionId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    dataCollectionGroupId: Mapped[int] = mapped_column(
        Integer, comment="references DataCollectionGroup table"
    )
    BLSAMPLEID: Mapped[Optional[int]] = mapped_column(INTEGER)
    SESSIONID: Mapped[Optional[int]] = mapped_column(
        INTEGER, server_default=text("'0'")
    )
    experimenttype: Mapped[Optional[str]] = mapped_column(String(24))
    dataCollectionNumber: Mapped[Optional[int]] = mapped_column(INTEGER)
    startTime: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Start time of the dataCollection"
    )
    endTime: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="end time of the dataCollection"
    )
    runStatus: Mapped[Optional[str]] = mapped_column(String(45))
    axisStart: Mapped[Optional[float]] = mapped_column(Float)
    axisEnd: Mapped[Optional[float]] = mapped_column(Float)
    axisRange: Mapped[Optional[float]] = mapped_column(Float)
    overlap: Mapped[Optional[float]] = mapped_column(Float)
    numberOfImages: Mapped[Optional[int]] = mapped_column(INTEGER)
    startImageNumber: Mapped[Optional[int]] = mapped_column(INTEGER)
    numberOfPasses: Mapped[Optional[int]] = mapped_column(INTEGER)
    exposureTime: Mapped[Optional[float]] = mapped_column(Float)
    imageDirectory: Mapped[Optional[str]] = mapped_column(
        String(255),
        comment="The directory where files reside - should end with a slash",
    )
    imagePrefix: Mapped[Optional[str]] = mapped_column(String(45))
    imageSuffix: Mapped[Optional[str]] = mapped_column(String(45))
    imageContainerSubPath: Mapped[Optional[str]] = mapped_column(
        String(255),
        comment="Internal path of a HDF5 file pointing to the data for this data collection",
    )
    fileTemplate: Mapped[Optional[str]] = mapped_column(String(255))
    wavelength: Mapped[Optional[float]] = mapped_column(Float)
    resolution: Mapped[Optional[float]] = mapped_column(Float)
    detectorDistance: Mapped[Optional[float]] = mapped_column(Float)
    xBeam: Mapped[Optional[float]] = mapped_column(Float)
    yBeam: Mapped[Optional[float]] = mapped_column(Float)
    comments: Mapped[Optional[str]] = mapped_column(String(1024))
    printableForReport: Mapped[Optional[int]] = mapped_column(
        TINYINT, server_default=text("'1'")
    )
    CRYSTALCLASS: Mapped[Optional[str]] = mapped_column(String(20))
    slitGapVertical: Mapped[Optional[float]] = mapped_column(Float)
    slitGapHorizontal: Mapped[Optional[float]] = mapped_column(Float)
    transmission: Mapped[Optional[float]] = mapped_column(Float)
    synchrotronMode: Mapped[Optional[str]] = mapped_column(String(20))
    xtalSnapshotFullPath1: Mapped[Optional[str]] = mapped_column(String(255))
    xtalSnapshotFullPath2: Mapped[Optional[str]] = mapped_column(String(255))
    xtalSnapshotFullPath3: Mapped[Optional[str]] = mapped_column(String(255))
    xtalSnapshotFullPath4: Mapped[Optional[str]] = mapped_column(String(255))
    rotationAxis: Mapped[Optional[str]] = mapped_column(Enum("Omega", "Kappa", "Phi"))
    phiStart: Mapped[Optional[float]] = mapped_column(Float)
    kappaStart: Mapped[Optional[float]] = mapped_column(Float)
    omegaStart: Mapped[Optional[float]] = mapped_column(Float)
    chiStart: Mapped[Optional[float]] = mapped_column(Float)
    resolutionAtCorner: Mapped[Optional[float]] = mapped_column(Float)
    detector2Theta: Mapped[Optional[float]] = mapped_column(Float)
    DETECTORMODE: Mapped[Optional[str]] = mapped_column(String(255))
    undulatorGap1: Mapped[Optional[float]] = mapped_column(Float)
    undulatorGap2: Mapped[Optional[float]] = mapped_column(Float)
    undulatorGap3: Mapped[Optional[float]] = mapped_column(Float)
    beamSizeAtSampleX: Mapped[Optional[float]] = mapped_column(Float)
    beamSizeAtSampleY: Mapped[Optional[float]] = mapped_column(Float)
    centeringMethod: Mapped[Optional[str]] = mapped_column(String(255))
    averageTemperature: Mapped[Optional[float]] = mapped_column(Float)
    ACTUALSAMPLEBARCODE: Mapped[Optional[str]] = mapped_column(String(45))
    ACTUALSAMPLESLOTINCONTAINER: Mapped[Optional[int]] = mapped_column(INTEGER)
    ACTUALCONTAINERBARCODE: Mapped[Optional[str]] = mapped_column(String(45))
    ACTUALCONTAINERSLOTINSC: Mapped[Optional[int]] = mapped_column(INTEGER)
    actualCenteringPosition: Mapped[Optional[str]] = mapped_column(String(255))
    beamShape: Mapped[Optional[str]] = mapped_column(String(45))
    POSITIONID: Mapped[Optional[int]] = mapped_column(INTEGER)
    detectorId: Mapped[Optional[int]] = mapped_column(
        Integer, comment="references Detector table"
    )
    FOCALSPOTSIZEATSAMPLEX: Mapped[Optional[float]] = mapped_column(Float)
    POLARISATION: Mapped[Optional[float]] = mapped_column(Float)
    FOCALSPOTSIZEATSAMPLEY: Mapped[Optional[float]] = mapped_column(Float)
    APERTUREID: Mapped[Optional[int]] = mapped_column(INTEGER)
    screeningOrigId: Mapped[Optional[int]] = mapped_column(INTEGER)
    startPositionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    endPositionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    flux: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    strategySubWedgeOrigId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="references ScreeningStrategySubWedge table"
    )
    blSubSampleId: Mapped[Optional[int]] = mapped_column(INTEGER)
    flux_end: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="flux measured after the collect"
    )
    bestWilsonPlotPath: Mapped[Optional[str]] = mapped_column(String(255))
    processedDataFile: Mapped[Optional[str]] = mapped_column(String(255))
    datFullPath: Mapped[Optional[str]] = mapped_column(String(255))
    magnification: Mapped[Optional[float]] = mapped_column(
        Float, comment="Calibrated magnification, Units: dimensionless"
    )
    totalAbsorbedDose: Mapped[Optional[float]] = mapped_column(
        Float, comment="Unit: e-/A^2 for EM"
    )
    binning: Mapped[Optional[int]] = mapped_column(
        TINYINT(1),
        server_default=text("'1'"),
        comment="1 or 2. Number of pixels to process as 1. (Use mean value.)",
    )
    particleDiameter: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: nm")
    boxSize_CTF: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: pixels")
    minResolution: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: A")
    minDefocus: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: A")
    maxDefocus: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: A")
    defocusStepSize: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: A")
    amountAstigmatism: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: A")
    extractSize: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: pixels")
    bgRadius: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: nm")
    voltage: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: kV")
    objAperture: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: um")
    c1aperture: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: um")
    c2aperture: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: um")
    c3aperture: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: um")
    c1lens: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: %")
    c2lens: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: %")
    c3lens: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: %")
    totalExposedDose: Mapped[Optional[float]] = mapped_column(
        Float, comment="Units: e-/A^2"
    )
    nominalMagnification: Mapped[Optional[float]] = mapped_column(
        Float, comment="Nominal magnification: Units: dimensionless"
    )
    nominalDefocus: Mapped[Optional[float]] = mapped_column(
        Float, comment="Nominal defocus, Units: A"
    )
    imageSizeX: Mapped[Optional[int]] = mapped_column(
        MEDIUMINT, comment="Image size in x, incase crop has been used, Units: pixels"
    )
    imageSizeY: Mapped[Optional[int]] = mapped_column(
        MEDIUMINT, comment="Image size in y, Units: pixels"
    )
    pixelSizeOnImage: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="Pixel size on image, calculated from magnification, duplicate? Units: um?",
    )
    phasePlate: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), comment="Whether the phase plate was used"
    )
    dataCollectionPlanId: Mapped[Optional[int]] = mapped_column(INTEGER)

    BLSubSample_: Mapped["BLSubSample"] = relationship(
        "BLSubSample", back_populates="DataCollection"
    )
    DataCollectionGroup: Mapped["DataCollectionGroup"] = relationship(
        "DataCollectionGroup", back_populates="DataCollection_"
    )
    DiffractionPlan: Mapped["DiffractionPlan"] = relationship(
        "DiffractionPlan", back_populates="DataCollection_"
    )
    Detector: Mapped["Detector"] = relationship(
        "Detector", back_populates="DataCollection_"
    )
    MotorPosition: Mapped["MotorPosition"] = relationship(
        "MotorPosition", foreign_keys=[endPositionId], back_populates="DataCollection_"
    )
    MotorPosition_: Mapped["MotorPosition"] = relationship(
        "MotorPosition",
        foreign_keys=[startPositionId],
        back_populates="DataCollection1",
    )
    ScreeningStrategySubWedge: Mapped["ScreeningStrategySubWedge"] = relationship(
        "ScreeningStrategySubWedge", back_populates="DataCollection_"
    )
    ProcessingJob: Mapped[List["ProcessingJob"]] = relationship(
        "ProcessingJob", back_populates="DataCollection_"
    )
    Screening: Mapped[List["Screening"]] = relationship(
        "Screening", back_populates="DataCollection_"
    )
    AutoProcIntegration: Mapped[List["AutoProcIntegration"]] = relationship(
        "AutoProcIntegration", back_populates="DataCollection_"
    )
    DataCollectionFileAttachment: Mapped[
        List["DataCollectionFileAttachment"]
    ] = relationship("DataCollectionFileAttachment", back_populates="DataCollection_")
    EventChain: Mapped[List["EventChain"]] = relationship(
        "EventChain", back_populates="DataCollection_"
    )
    GridImageMap: Mapped[List["GridImageMap"]] = relationship(
        "GridImageMap", back_populates="DataCollection_"
    )
    Image: Mapped[List["Image"]] = relationship(
        "Image", back_populates="DataCollection_"
    )
    Movie: Mapped[List["Movie"]] = relationship(
        "Movie", back_populates="DataCollection_"
    )
    ProcessingJobImageSweep: Mapped[List["ProcessingJobImageSweep"]] = relationship(
        "ProcessingJobImageSweep", back_populates="DataCollection_"
    )
    Tomogram: Mapped[List["Tomogram"]] = relationship(
        "Tomogram", back_populates="DataCollection_"
    )
    DataCollectionComment: Mapped[List["DataCollectionComment"]] = relationship(
        "DataCollectionComment", back_populates="DataCollection_"
    )
    MotionCorrection: Mapped[List["MotionCorrection"]] = relationship(
        "MotionCorrection", back_populates="DataCollection_"
    )
    GridInfo: Mapped[List["GridInfo"]] = relationship(
        "GridInfo", back_populates="DataCollection_"
    )


class Detector(Base):
    __tablename__ = "Detector"
    __table_args__ = (
        Index(
            "Detector_FKIndex1",
            "detectorType",
            "detectorManufacturer",
            "detectorModel",
            "detectorPixelSizeHorizontal",
            "detectorPixelSizeVertical",
        ),
        Index("Detector_ibuk1", "detectorSerialNumber", unique=True),
        {"comment": "Detector table is linked to a dataCollection"},
    )

    detectorId: Mapped[int] = mapped_column(
        Integer, primary_key=True, comment="Primary key (auto-incremented)"
    )
    detectorType: Mapped[Optional[str]] = mapped_column(String(255))
    detectorManufacturer: Mapped[Optional[str]] = mapped_column(String(255))
    detectorModel: Mapped[Optional[str]] = mapped_column(String(255))
    detectorPixelSizeHorizontal: Mapped[Optional[float]] = mapped_column(Float)
    detectorPixelSizeVertical: Mapped[Optional[float]] = mapped_column(Float)
    DETECTORMAXRESOLUTION: Mapped[Optional[float]] = mapped_column(Float)
    DETECTORMINRESOLUTION: Mapped[Optional[float]] = mapped_column(Float)
    detectorSerialNumber: Mapped[Optional[str]] = mapped_column(String(30))
    detectorDistanceMin: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    detectorDistanceMax: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    trustedPixelValueRangeLower: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    trustedPixelValueRangeUpper: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    sensorThickness: Mapped[Optional[float]] = mapped_column(Float)
    overload: Mapped[Optional[float]] = mapped_column(Float)
    XGeoCorr: Mapped[Optional[str]] = mapped_column(String(255))
    YGeoCorr: Mapped[Optional[str]] = mapped_column(String(255))
    detectorMode: Mapped[Optional[str]] = mapped_column(String(255))
    density: Mapped[Optional[float]] = mapped_column(Float)
    composition: Mapped[Optional[str]] = mapped_column(String(16))
    numberOfPixelsX: Mapped[Optional[int]] = mapped_column(
        MEDIUMINT, comment="Detector number of pixels in x"
    )
    numberOfPixelsY: Mapped[Optional[int]] = mapped_column(
        MEDIUMINT, comment="Detector number of pixels in y"
    )
    detectorRollMin: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="unit: degrees"
    )
    detectorRollMax: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="unit: degrees"
    )
    localName: Mapped[Optional[str]] = mapped_column(
        String(40), comment="Colloquial name for the detector"
    )
    numberOfROIPixelsX: Mapped[Optional[int]] = mapped_column(
        MEDIUMINT, comment="Detector number of pixels in x in ROI mode"
    )
    numberOfROIPixelsY: Mapped[Optional[int]] = mapped_column(
        MEDIUMINT, comment="Detector number of pixels in y in ROI mode"
    )

    DataCollection_: Mapped[List["DataCollection"]] = relationship(
        "DataCollection", back_populates="Detector"
    )
    BeamLineSetup: Mapped[List["BeamLineSetup"]] = relationship(
        "BeamLineSetup", back_populates="Detector_"
    )
    DiffractionPlan: Mapped[List["DiffractionPlan"]] = relationship(
        "DiffractionPlan", back_populates="Detector_"
    )
    DataCollectionPlan_has_Detector: Mapped[
        List["DataCollectionPlanHasDetector"]
    ] = relationship("DataCollectionPlanHasDetector", back_populates="Detector_")


class DewarLocation(Base):
    __tablename__ = "DewarLocation"
    __table_args__ = {"comment": "ISPyB Dewar location table"}

    eventId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    dewarNumber: Mapped[str] = mapped_column(String(128), comment="Dewar number")
    userId: Mapped[Optional[str]] = mapped_column(
        String(128), comment="User who locates the dewar"
    )
    dateTime: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Date and time of locatization"
    )
    locationName: Mapped[Optional[str]] = mapped_column(
        String(128), comment="Location of the dewar"
    )
    courierName: Mapped[Optional[str]] = mapped_column(
        String(128), comment="Carrier name who's shipping back the dewar"
    )
    courierTrackingNumber: Mapped[Optional[str]] = mapped_column(
        String(128), comment="Tracking number of the shippment"
    )


class DewarLocationList(Base):
    __tablename__ = "DewarLocationList"
    __table_args__ = {"comment": "List of locations for dewars"}

    locationId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    locationName: Mapped[str] = mapped_column(
        String(128), server_default=text("''"), comment="Location"
    )


class EventType(Base):
    __tablename__ = "EventType"
    __table_args__ = (
        Index("name", "name", unique=True),
        {
            "comment": "Defines the list of event types which can occur during a data "
            "collection."
        },
    )

    eventTypeId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(String(30, "utf8mb4_general_ci"))

    Event: Mapped[List["Event"]] = relationship("Event", back_populates="EventType_")


class ExperimentType(Base):
    __tablename__ = "ExperimentType"
    __table_args__ = {"comment": "A lookup table for different types of experients"}

    experimentTypeId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    proposalType: Mapped[Optional[str]] = mapped_column(String(10))
    active: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), server_default=text("'1'"), comment="1=active, 0=inactive"
    )

    DiffractionPlan: Mapped[List["DiffractionPlan"]] = relationship(
        "DiffractionPlan", back_populates="ExperimentType_"
    )
    DataCollectionGroup: Mapped[List["DataCollectionGroup"]] = relationship(
        "DataCollectionGroup", back_populates="ExperimentType_"
    )
    Container: Mapped[List["Container"]] = relationship(
        "Container", back_populates="ExperimentType_"
    )


class GeometryClassname(Base):
    __tablename__ = "GeometryClassname"

    geometryClassnameId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    geometryOrder: Mapped[int] = mapped_column(Integer)
    geometryClassname: Mapped[Optional[str]] = mapped_column(String(45))

    SpaceGroup: Mapped[List["SpaceGroup"]] = relationship(
        "SpaceGroup", back_populates="GeometryClassname_"
    )


class ImageQualityIndicators(Base):
    __tablename__ = "ImageQualityIndicators"

    dataCollectionId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    imageNumber: Mapped[int] = mapped_column(MEDIUMINT, primary_key=True)
    imageId: Mapped[Optional[int]] = mapped_column(Integer)
    autoProcProgramId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Foreign key to the AutoProcProgram table"
    )
    spotTotal: Mapped[Optional[int]] = mapped_column(
        Integer, comment="Total number of spots"
    )
    inResTotal: Mapped[Optional[int]] = mapped_column(
        Integer, comment="Total number of spots in resolution range"
    )
    goodBraggCandidates: Mapped[Optional[int]] = mapped_column(
        Integer, comment="Total number of Bragg diffraction spots"
    )
    iceRings: Mapped[Optional[int]] = mapped_column(
        Integer, comment="Number of ice rings identified"
    )
    method1Res: Mapped[Optional[float]] = mapped_column(
        Float, comment="Resolution estimate 1 (see publication)"
    )
    method2Res: Mapped[Optional[float]] = mapped_column(
        Float, comment="Resolution estimate 2 (see publication)"
    )
    maxUnitCell: Mapped[Optional[float]] = mapped_column(
        Float, comment="Estimation of the largest possible unit cell edge"
    )
    pctSaturationTop50Peaks: Mapped[Optional[float]] = mapped_column(
        Float, comment="The fraction of the dynamic range being used"
    )
    inResolutionOvrlSpots: Mapped[Optional[int]] = mapped_column(
        Integer, comment="Number of spots overloaded"
    )
    binPopCutOffMethod2Res: Mapped[Optional[float]] = mapped_column(
        Float, comment="Cut off used in resolution limit calculation"
    )
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Creation or last update date/time"
    )
    totalIntegratedSignal: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    dozor_score: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="dozor_score"
    )
    driftFactor: Mapped[Optional[float]] = mapped_column(
        Float, comment="EM movie drift factor"
    )


class Imager(Base):
    __tablename__ = "Imager"

    imagerId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(String(45))
    temperature: Mapped[Optional[float]] = mapped_column(Float)
    serial: Mapped[Optional[str]] = mapped_column(String(45))
    capacity: Mapped[Optional[int]] = mapped_column(SmallInteger)

    Container: Mapped[List["Container"]] = relationship(
        "Container", foreign_keys="[Container.imagerId]", back_populates="Imager_"
    )
    Container_: Mapped[List["Container"]] = relationship(
        "Container",
        foreign_keys="[Container.requestedImagerId]",
        back_populates="Imager1",
    )
    ContainerInspection: Mapped[List["ContainerInspection"]] = relationship(
        "ContainerInspection", back_populates="Imager_"
    )


class InspectionType(Base):
    __tablename__ = "InspectionType"

    inspectionTypeId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(45))

    ScheduleComponent: Mapped[List["ScheduleComponent"]] = relationship(
        "ScheduleComponent", back_populates="InspectionType_"
    )
    ContainerInspection: Mapped[List["ContainerInspection"]] = relationship(
        "ContainerInspection", back_populates="InspectionType_"
    )


class IspybCrystalClass(Base):
    __tablename__ = "IspybCrystalClass"
    __table_args__ = {"comment": "ISPyB crystal class values"}

    crystalClassId: Mapped[int] = mapped_column(Integer, primary_key=True)
    crystalClass_code: Mapped[str] = mapped_column(String(20))
    crystalClass_name: Mapped[str] = mapped_column(String(255))


class IspybReference(Base):
    __tablename__ = "IspybReference"

    referenceId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    referenceName: Mapped[Optional[str]] = mapped_column(
        String(255), comment="reference name"
    )
    referenceUrl: Mapped[Optional[str]] = mapped_column(
        String(1024), comment="url of the reference"
    )
    referenceBibtext: Mapped[Optional[bytes]] = mapped_column(
        LargeBinary, comment="bibtext value of the reference"
    )
    beamline: Mapped[Optional[str]] = mapped_column(
        Enum("All", "ID14-4", "ID23-1", "ID23-2", "ID29", "XRF", "AllXRF", "Mesh"),
        comment="beamline involved",
    )


class LDAPSearchParameters(Base):
    __tablename__ = "LDAPSearchParameters"
    __table_args__ = {
        "comment": "All necessary parameters to run an LDAP search, except the search "
        "base"
    }

    ldapSearchParametersId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    accountType: Mapped[str] = mapped_column(
        ENUM("group_member", "staff_account", "functional_account"),
        comment="The entity type returned by the search",
    )
    oneOrMany: Mapped[str] = mapped_column(
        ENUM("one", "many"), comment="Expected number of search results"
    )
    hostURL: Mapped[str] = mapped_column(
        String(200, "utf8mb4_general_ci"), comment="URL for the LDAP host"
    )
    attributes: Mapped[str] = mapped_column(
        String(255, "utf8mb4_general_ci"),
        comment="Comma-separated list of search attributes",
    )
    accountTypeGroupName: Mapped[Optional[str]] = mapped_column(
        String(100, "utf8mb4_general_ci"),
        comment="all accounts of this type must be members of this group",
    )
    filter: Mapped[Optional[str]] = mapped_column(
        String(200, "utf8mb4_general_ci"), comment="A filter string for the search"
    )

    LDAPSearchBase: Mapped[List["LDAPSearchBase"]] = relationship(
        "LDAPSearchBase", back_populates="LDAPSearchParameters_"
    )
    UserGroup_has_LDAPSearchParameters: Mapped[
        List["UserGroupHasLDAPSearchParameters"]
    ] = relationship(
        "UserGroupHasLDAPSearchParameters", back_populates="LDAPSearchParameters_"
    )


class Laboratory(Base):
    __tablename__ = "Laboratory"

    laboratoryId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Creation or last update date/time",
    )
    laboratoryUUID: Mapped[Optional[str]] = mapped_column(String(45))
    name: Mapped[Optional[str]] = mapped_column(String(45))
    address: Mapped[Optional[str]] = mapped_column(String(255))
    city: Mapped[Optional[str]] = mapped_column(String(45))
    country: Mapped[Optional[str]] = mapped_column(String(45))
    url: Mapped[Optional[str]] = mapped_column(String(255))
    organization: Mapped[Optional[str]] = mapped_column(String(45))
    laboratoryPk: Mapped[Optional[int]] = mapped_column(Integer)
    postcode: Mapped[Optional[str]] = mapped_column(String(15))
    EORINumber: Mapped[Optional[str]] = mapped_column(
        String(17),
        comment="An EORI number consists of an ISO Country code from an EU Member State  (2 characters) + a maximum of 15 characters",
    )

    Person: Mapped[List["Person"]] = relationship(
        "Person", back_populates="Laboratory_"
    )


class MotorPosition(Base):
    __tablename__ = "MotorPosition"

    motorPositionId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Creation or last update date/time",
    )
    phiX: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    phiY: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    phiZ: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    sampX: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    sampY: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    omega: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    kappa: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    phi: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    chi: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    gridIndexY: Mapped[Optional[int]] = mapped_column(Integer)
    gridIndexZ: Mapped[Optional[int]] = mapped_column(Integer)

    BLSubSample_: Mapped[List["BLSubSample"]] = relationship(
        "BLSubSample", back_populates="MotorPosition"
    )
    DataCollection_: Mapped[List["DataCollection"]] = relationship(
        "DataCollection",
        foreign_keys="[DataCollection.endPositionId]",
        back_populates="MotorPosition",
    )
    DataCollection1: Mapped[List["DataCollection"]] = relationship(
        "DataCollection",
        foreign_keys="[DataCollection.startPositionId]",
        back_populates="MotorPosition_",
    )
    Image: Mapped[List["Image"]] = relationship(
        "Image", back_populates="MotorPosition_"
    )


class PDB(Base):
    __tablename__ = "PDB"

    pdbId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    contents: Mapped[Optional[str]] = mapped_column(MEDIUMTEXT)
    code: Mapped[Optional[str]] = mapped_column(String(4))
    source: Mapped[Optional[str]] = mapped_column(
        String(30), comment="Could be e.g. AlphaFold or RoseTTAFold"
    )

    Protein_has_PDB: Mapped[List["ProteinHasPDB"]] = relationship(
        "ProteinHasPDB", back_populates="PDB_"
    )


class Permission(Base):
    __tablename__ = "Permission"

    permissionId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    type: Mapped[str] = mapped_column(String(15))
    description: Mapped[Optional[str]] = mapped_column(String(100))

    UserGroup: Mapped[List["UserGroup"]] = relationship(
        "UserGroup", secondary="UserGroup_has_Permission", back_populates="Permission_"
    )


class PhasingAnalysis(Base):
    __tablename__ = "PhasingAnalysis"

    phasingAnalysisId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Creation or last update date/time"
    )

    ModelBuilding: Mapped[List["ModelBuilding"]] = relationship(
        "ModelBuilding", back_populates="PhasingAnalysis_"
    )
    Phasing: Mapped[List["Phasing"]] = relationship(
        "Phasing", back_populates="PhasingAnalysis_"
    )
    Phasing_has_Scaling: Mapped[List["PhasingHasScaling"]] = relationship(
        "PhasingHasScaling", back_populates="PhasingAnalysis_"
    )
    PreparePhasingData: Mapped[List["PreparePhasingData"]] = relationship(
        "PreparePhasingData", back_populates="PhasingAnalysis_"
    )
    SubstructureDetermination: Mapped[List["SubstructureDetermination"]] = relationship(
        "SubstructureDetermination", back_populates="PhasingAnalysis_"
    )


class PhasingProgramRun(Base):
    __tablename__ = "PhasingProgramRun"

    phasingProgramRunId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingCommandLine: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Command line for phasing"
    )
    phasingPrograms: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Phasing programs (comma separated)"
    )
    phasingStatus: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), comment="success (1) / fail (0)"
    )
    phasingMessage: Mapped[Optional[str]] = mapped_column(
        String(255), comment="warning, error,..."
    )
    phasingStartTime: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Processing start time"
    )
    phasingEndTime: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Processing end time"
    )
    phasingEnvironment: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Cpus, Nodes,..."
    )
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    PhasingProgramAttachment: Mapped[List["PhasingProgramAttachment"]] = relationship(
        "PhasingProgramAttachment", back_populates="PhasingProgramRun_"
    )
    ModelBuilding: Mapped[List["ModelBuilding"]] = relationship(
        "ModelBuilding", back_populates="PhasingProgramRun_"
    )
    Phasing: Mapped[List["Phasing"]] = relationship(
        "Phasing", back_populates="PhasingProgramRun_"
    )
    PhasingStep: Mapped[List["PhasingStep"]] = relationship(
        "PhasingStep", back_populates="PhasingProgramRun_"
    )
    PreparePhasingData: Mapped[List["PreparePhasingData"]] = relationship(
        "PreparePhasingData", back_populates="PhasingProgramRun_"
    )
    SubstructureDetermination: Mapped[List["SubstructureDetermination"]] = relationship(
        "SubstructureDetermination", back_populates="PhasingProgramRun_"
    )


class Position(Base):
    __tablename__ = "Position"
    __table_args__ = (
        ForeignKeyConstraint(
            ["relativePositionId"],
            ["Position.positionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Position_relativePositionfk_1",
        ),
        Index("Position_FKIndex1", "relativePositionId"),
    )

    positionId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    relativePositionId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="relative position, null otherwise"
    )
    posX: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    posY: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    posZ: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    scale: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Creation or last update date/time"
    )
    X: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), Computed("(`posX`)", persisted=False)
    )
    Y: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), Computed("(`posY`)", persisted=False)
    )
    Z: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), Computed("(`posZ`)", persisted=False)
    )

    BLSubSample_: Mapped[List["BLSubSample"]] = relationship(
        "BLSubSample",
        foreign_keys="[BLSubSample.position2Id]",
        back_populates="Position",
    )
    BLSubSample1: Mapped[List["BLSubSample"]] = relationship(
        "BLSubSample",
        foreign_keys="[BLSubSample.positionId]",
        back_populates="Position_",
    )
    Position: Mapped["Position"] = relationship(
        "Position", remote_side=[positionId], back_populates="Position_reverse"
    )
    Position_reverse: Mapped[List["Position"]] = relationship(
        "Position", remote_side=[relativePositionId], back_populates="Position"
    )


class Positioner(Base):
    __tablename__ = "Positioner"
    __table_args__ = {
        "comment": "An arbitrary positioner and its value, could be e.g. a motor. "
        "Allows for instance to store some positions with a sample or "
        "subsample"
    }

    positionerId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    positioner: Mapped[str] = mapped_column(String(50))
    value: Mapped[float] = mapped_column(Float)

    BLSampleImage_has_Positioner: Mapped[
        List["BLSampleImageHasPositioner"]
    ] = relationship("BLSampleImageHasPositioner", back_populates="Positioner_")
    BLSample_has_Positioner: Mapped[List["BLSampleHasPositioner"]] = relationship(
        "BLSampleHasPositioner", back_populates="Positioner_"
    )
    BLSubSample_has_Positioner: Mapped[List["BLSubSampleHasPositioner"]] = relationship(
        "BLSubSampleHasPositioner", back_populates="Positioner_"
    )


class ProcessingJob(Base):
    __tablename__ = "ProcessingJob"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dataCollectionId"],
            ["DataCollection.dataCollectionId"],
            name="ProcessingJob_ibfk1",
        ),
        Index("ProcessingJob_ibfk1", "dataCollectionId"),
        {"comment": "From this we get both job times and lag times"},
    )

    processingJobId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    recordTimestamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="When job was submitted",
    )
    dataCollectionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    displayName: Mapped[Optional[str]] = mapped_column(
        String(80), comment="xia2, fast_dp, dimple, etc"
    )
    comments: Mapped[Optional[str]] = mapped_column(
        String(255),
        comment="For users to annotate the job and see the motivation for the job",
    )
    recipe: Mapped[Optional[str]] = mapped_column(
        String(50), comment="What we want to run (xia, dimple, etc)."
    )
    automatic: Mapped[Optional[int]] = mapped_column(
        TINYINT(1),
        comment="Whether this processing job was triggered automatically or not",
    )

    AutoProcProgram_: Mapped[List["AutoProcProgram"]] = relationship(
        "AutoProcProgram", back_populates="ProcessingJob"
    )
    DataCollection_: Mapped["DataCollection"] = relationship(
        "DataCollection", back_populates="ProcessingJob"
    )
    ProcessingJobImageSweep: Mapped[List["ProcessingJobImageSweep"]] = relationship(
        "ProcessingJobImageSweep", back_populates="ProcessingJob_"
    )
    ProcessingJobParameter: Mapped[List["ProcessingJobParameter"]] = relationship(
        "ProcessingJobParameter", back_populates="ProcessingJob_"
    )


class ProcessingPipelineCategory(Base):
    __tablename__ = "ProcessingPipelineCategory"
    __table_args__ = {
        "comment": "A lookup table for the category of processing pipeline"
    }

    processingPipelineCategoryId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(String(20))

    ProcessingPipeline: Mapped[List["ProcessingPipeline"]] = relationship(
        "ProcessingPipeline", back_populates="ProcessingPipelineCategory_"
    )


class PurificationColumn(Base):
    __tablename__ = "PurificationColumn"
    __table_args__ = {
        "comment": "Size exclusion chromotography (SEC) lookup table for BioSAXS"
    }

    purificationColumnId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    active: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), server_default=text("'1'"), comment="1=active, 0=inactive"
    )

    DiffractionPlan: Mapped[List["DiffractionPlan"]] = relationship(
        "DiffractionPlan", back_populates="PurificationColumn_"
    )


class ScanParametersService(Base):
    __tablename__ = "ScanParametersService"

    scanParametersServiceId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(45))
    description: Mapped[Optional[str]] = mapped_column(String(45))

    ScanParametersModel: Mapped[List["ScanParametersModel"]] = relationship(
        "ScanParametersModel", back_populates="ScanParametersService_"
    )


class Schedule(Base):
    __tablename__ = "Schedule"

    scheduleId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(45))

    ScheduleComponent: Mapped[List["ScheduleComponent"]] = relationship(
        "ScheduleComponent", back_populates="Schedule_"
    )
    Container: Mapped[List["Container"]] = relationship(
        "Container", back_populates="Schedule_"
    )


class SchemaStatus(Base):
    __tablename__ = "SchemaStatus"
    __table_args__ = (Index("scriptName", "scriptName", unique=True),)

    schemaStatusId: Mapped[int] = mapped_column(Integer, primary_key=True)
    scriptName: Mapped[str] = mapped_column(String(100))
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    schemaStatus: Mapped[Optional[str]] = mapped_column(String(10))


class Screening(Base):
    __tablename__ = "Screening"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcProgramId"],
            ["AutoProcProgram.autoProcProgramId"],
            ondelete="SET NULL",
            onupdate="CASCADE",
            name="Screening_fk_autoProcProgramId",
        ),
        ForeignKeyConstraint(
            ["dataCollectionGroupId"],
            ["DataCollectionGroup.dataCollectionGroupId"],
            name="Screening_ibfk_1",
        ),
        ForeignKeyConstraint(
            ["dataCollectionId"],
            ["DataCollection.dataCollectionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="_Screening_ibfk2",
        ),
        Index("Screening_FKIndexDiffractionPlanId", "diffractionPlanId"),
        Index("Screening_fk_autoProcProgramId", "autoProcProgramId"),
        Index("_Screening_ibfk2", "dataCollectionId"),
        Index("dcgroupId", "dataCollectionGroupId"),
    )

    screeningId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    bltimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    dataCollectionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    programVersion: Mapped[Optional[str]] = mapped_column(String(45))
    comments: Mapped[Optional[str]] = mapped_column(String(255))
    shortComments: Mapped[Optional[str]] = mapped_column(String(20))
    diffractionPlanId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="references DiffractionPlan"
    )
    dataCollectionGroupId: Mapped[Optional[int]] = mapped_column(Integer)
    xmlSampleInformation: Mapped[Optional[bytes]] = mapped_column(LONGBLOB)
    autoProcProgramId: Mapped[Optional[int]] = mapped_column(INTEGER)

    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="Screening"
    )
    DataCollectionGroup: Mapped["DataCollectionGroup"] = relationship(
        "DataCollectionGroup", back_populates="Screening_"
    )
    DataCollection_: Mapped["DataCollection"] = relationship(
        "DataCollection", back_populates="Screening"
    )
    ScreeningOutput: Mapped[List["ScreeningOutput"]] = relationship(
        "ScreeningOutput", back_populates="Screening_"
    )
    ScreeningInput: Mapped[List["ScreeningInput"]] = relationship(
        "ScreeningInput", back_populates="Screening_"
    )
    ScreeningRank: Mapped[List["ScreeningRank"]] = relationship(
        "ScreeningRank", back_populates="Screening_"
    )


class ScreeningOutput(Base):
    __tablename__ = "ScreeningOutput"
    __table_args__ = (
        ForeignKeyConstraint(
            ["screeningId"],
            ["Screening.screeningId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ScreeningOutput_ibfk_1",
        ),
        Index("ScreeningOutput_FKIndex1", "screeningId"),
    )

    screeningOutputId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    screeningId: Mapped[int] = mapped_column(INTEGER, server_default=text("'0'"))
    mosaicityEstimated: Mapped[int] = mapped_column(
        TINYINT(1), server_default=text("'0'")
    )
    indexingSuccess: Mapped[int] = mapped_column(TINYINT(1), server_default=text("'0'"))
    strategySuccess: Mapped[int] = mapped_column(TINYINT(1), server_default=text("'0'"))
    alignmentSuccess: Mapped[int] = mapped_column(
        TINYINT(1), server_default=text("'0'")
    )
    statusDescription: Mapped[Optional[str]] = mapped_column(String(1024))
    rejectedReflections: Mapped[Optional[int]] = mapped_column(INTEGER)
    resolutionObtained: Mapped[Optional[float]] = mapped_column(Float)
    spotDeviationR: Mapped[Optional[float]] = mapped_column(Float)
    spotDeviationTheta: Mapped[Optional[float]] = mapped_column(Float)
    beamShiftX: Mapped[Optional[float]] = mapped_column(Float)
    beamShiftY: Mapped[Optional[float]] = mapped_column(Float)
    numSpotsFound: Mapped[Optional[int]] = mapped_column(INTEGER)
    numSpotsUsed: Mapped[Optional[int]] = mapped_column(INTEGER)
    numSpotsRejected: Mapped[Optional[int]] = mapped_column(INTEGER)
    mosaicity: Mapped[Optional[float]] = mapped_column(Float)
    iOverSigma: Mapped[Optional[float]] = mapped_column(Float)
    diffractionRings: Mapped[Optional[int]] = mapped_column(TINYINT(1))
    SCREENINGSUCCESS: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), server_default=text("'0'"), comment="Column to be deleted"
    )
    rankingResolution: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    program: Mapped[Optional[str]] = mapped_column(String(45))
    doseTotal: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    totalExposureTime: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    totalRotationRange: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    totalNumberOfImages: Mapped[Optional[int]] = mapped_column(Integer)
    rFriedel: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))

    Screening_: Mapped["Screening"] = relationship(
        "Screening", back_populates="ScreeningOutput"
    )
    ScreeningStrategy: Mapped[List["ScreeningStrategy"]] = relationship(
        "ScreeningStrategy", back_populates="ScreeningOutput_"
    )
    ScreeningOutputLattice: Mapped[List["ScreeningOutputLattice"]] = relationship(
        "ScreeningOutputLattice", back_populates="ScreeningOutput_"
    )


class ScreeningRankSet(Base):
    __tablename__ = "ScreeningRankSet"

    screeningRankSetId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    rankEngine: Mapped[Optional[str]] = mapped_column(String(255))
    rankingProjectFileName: Mapped[Optional[str]] = mapped_column(String(255))
    rankingSummaryFileName: Mapped[Optional[str]] = mapped_column(String(255))

    ScreeningRank: Mapped[List["ScreeningRank"]] = relationship(
        "ScreeningRank", back_populates="ScreeningRankSet_"
    )


class ScreeningStrategy(Base):
    __tablename__ = "ScreeningStrategy"
    __table_args__ = (
        ForeignKeyConstraint(
            ["screeningOutputId"],
            ["ScreeningOutput.screeningOutputId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ScreeningStrategy_ibfk_1",
        ),
        Index("ScreeningStrategy_FKIndex1", "screeningOutputId"),
    )

    screeningStrategyId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    screeningOutputId: Mapped[int] = mapped_column(INTEGER, server_default=text("'0'"))
    anomalous: Mapped[int] = mapped_column(TINYINT(1), server_default=text("'0'"))
    phiStart: Mapped[Optional[float]] = mapped_column(Float)
    phiEnd: Mapped[Optional[float]] = mapped_column(Float)
    rotation: Mapped[Optional[float]] = mapped_column(Float)
    exposureTime: Mapped[Optional[float]] = mapped_column(Float)
    resolution: Mapped[Optional[float]] = mapped_column(Float)
    completeness: Mapped[Optional[float]] = mapped_column(Float)
    multiplicity: Mapped[Optional[float]] = mapped_column(Float)
    program: Mapped[Optional[str]] = mapped_column(String(45))
    rankingResolution: Mapped[Optional[float]] = mapped_column(Float)
    transmission: Mapped[Optional[float]] = mapped_column(
        Float, comment="Transmission for the strategy as given by the strategy program."
    )

    ScreeningOutput_: Mapped["ScreeningOutput"] = relationship(
        "ScreeningOutput", back_populates="ScreeningStrategy"
    )
    ScreeningStrategyWedge: Mapped[List["ScreeningStrategyWedge"]] = relationship(
        "ScreeningStrategyWedge", back_populates="ScreeningStrategy_"
    )


class ScreeningStrategySubWedge(Base):
    __tablename__ = "ScreeningStrategySubWedge"
    __table_args__ = (
        ForeignKeyConstraint(
            ["screeningStrategyWedgeId"],
            ["ScreeningStrategyWedge.screeningStrategyWedgeId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ScreeningStrategySubWedge_FK1",
        ),
        Index("ScreeningStrategySubWedge_FK1", "screeningStrategyWedgeId"),
    )

    screeningStrategySubWedgeId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key"
    )
    screeningStrategyWedgeId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Foreign key to parent table"
    )
    subWedgeNumber: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="The number of this subwedge within the wedge"
    )
    rotationAxis: Mapped[Optional[str]] = mapped_column(
        String(45), comment="Angle where subwedge starts"
    )
    axisStart: Mapped[Optional[float]] = mapped_column(
        Float, comment="Angle where subwedge ends"
    )
    axisEnd: Mapped[Optional[float]] = mapped_column(
        Float, comment="Exposure time for subwedge"
    )
    exposureTime: Mapped[Optional[float]] = mapped_column(
        Float, comment="Transmission for subwedge"
    )
    transmission: Mapped[Optional[float]] = mapped_column(Float)
    oscillationRange: Mapped[Optional[float]] = mapped_column(Float)
    completeness: Mapped[Optional[float]] = mapped_column(Float)
    multiplicity: Mapped[Optional[float]] = mapped_column(Float)
    RESOLUTION: Mapped[Optional[float]] = mapped_column(Float)
    doseTotal: Mapped[Optional[float]] = mapped_column(
        Float, comment="Total dose for this subwedge"
    )
    numberOfImages: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Number of images for this subwedge"
    )
    comments: Mapped[Optional[str]] = mapped_column(String(255))

    DataCollection_: Mapped[List["DataCollection"]] = relationship(
        "DataCollection", back_populates="ScreeningStrategySubWedge"
    )
    ScreeningStrategyWedge: Mapped["ScreeningStrategyWedge"] = relationship(
        "ScreeningStrategyWedge", back_populates="ScreeningStrategySubWedge_"
    )


class ScreeningStrategyWedge(Base):
    __tablename__ = "ScreeningStrategyWedge"
    __table_args__ = (
        ForeignKeyConstraint(
            ["screeningStrategyId"],
            ["ScreeningStrategy.screeningStrategyId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ScreeningStrategyWedge_IBFK_1",
        ),
        Index("ScreeningStrategyWedge_IBFK_1", "screeningStrategyId"),
    )

    screeningStrategyWedgeId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key"
    )
    screeningStrategyId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Foreign key to parent table"
    )
    wedgeNumber: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="The number of this wedge within the strategy"
    )
    resolution: Mapped[Optional[float]] = mapped_column(Float)
    completeness: Mapped[Optional[float]] = mapped_column(Float)
    multiplicity: Mapped[Optional[float]] = mapped_column(Float)
    doseTotal: Mapped[Optional[float]] = mapped_column(
        Float, comment="Total dose for this wedge"
    )
    numberOfImages: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Number of images for this wedge"
    )
    phi: Mapped[Optional[float]] = mapped_column(Float)
    kappa: Mapped[Optional[float]] = mapped_column(Float)
    chi: Mapped[Optional[float]] = mapped_column(Float)
    comments: Mapped[Optional[str]] = mapped_column(String(255))
    wavelength: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )

    ScreeningStrategySubWedge_: Mapped[
        List["ScreeningStrategySubWedge"]
    ] = relationship(
        "ScreeningStrategySubWedge", back_populates="ScreeningStrategyWedge"
    )
    ScreeningStrategy_: Mapped["ScreeningStrategy"] = relationship(
        "ScreeningStrategy", back_populates="ScreeningStrategyWedge"
    )


class Sleeve(Base):
    __tablename__ = "Sleeve"
    __table_args__ = {
        "comment": "Registry of ice-filled sleeves used to cool plates whilst on the "
        "goniometer"
    }

    sleeveId: Mapped[int] = mapped_column(
        TINYINT,
        primary_key=True,
        comment="The unique sleeve id 1...255 which also identifies its home location in the freezer",
    )
    lastMovedToFreezer: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    location: Mapped[Optional[int]] = mapped_column(
        TINYINT, comment="NULL == freezer, 1...255 for local storage locations"
    )
    lastMovedFromFreezer: Mapped[Optional[datetime.datetime]] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )


class UserGroup(Base):
    __tablename__ = "UserGroup"
    __table_args__ = (Index("UserGroup_idx1", "name", unique=True),)

    userGroupId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(String(31))

    Permission_: Mapped[List["Permission"]] = relationship(
        "Permission", secondary="UserGroup_has_Permission", back_populates="UserGroup"
    )
    Person: Mapped[List["Person"]] = relationship(
        "Person", secondary="UserGroup_has_Person", back_populates="UserGroup_"
    )
    UserGroup_has_LDAPSearchParameters: Mapped[
        List["UserGroupHasLDAPSearchParameters"]
    ] = relationship("UserGroupHasLDAPSearchParameters", back_populates="UserGroup_")


class VRun(Base):
    __tablename__ = "v_run"
    __table_args__ = (Index("v_run_idx1", "startDate", "endDate"),)

    runId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    run: Mapped[str] = mapped_column(String(7), server_default=text("''"))
    startDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    endDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class AutoProcIntegration(Base):
    __tablename__ = "AutoProcIntegration"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcProgramId"],
            ["AutoProcProgram.autoProcProgramId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="AutoProcIntegration_ibfk_2",
        ),
        ForeignKeyConstraint(
            ["dataCollectionId"],
            ["DataCollection.dataCollectionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="AutoProcIntegration_ibfk_1",
        ),
        Index("AutoProcIntegrationIdx1", "dataCollectionId"),
        Index("AutoProcIntegration_FKIndex1", "autoProcProgramId"),
    )

    autoProcIntegrationId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    dataCollectionId: Mapped[int] = mapped_column(
        INTEGER, comment="DataCollection item"
    )
    autoProcProgramId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Related program item"
    )
    startImageNumber: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="start image number"
    )
    endImageNumber: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="end image number"
    )
    refinedDetectorDistance: Mapped[Optional[float]] = mapped_column(
        Float, comment="Refined DataCollection.detectorDistance"
    )
    refinedXBeam: Mapped[Optional[float]] = mapped_column(
        Float, comment="Refined DataCollection.xBeam"
    )
    refinedYBeam: Mapped[Optional[float]] = mapped_column(
        Float, comment="Refined DataCollection.yBeam"
    )
    rotationAxisX: Mapped[Optional[float]] = mapped_column(
        Float, comment="Rotation axis"
    )
    rotationAxisY: Mapped[Optional[float]] = mapped_column(
        Float, comment="Rotation axis"
    )
    rotationAxisZ: Mapped[Optional[float]] = mapped_column(
        Float, comment="Rotation axis"
    )
    beamVectorX: Mapped[Optional[float]] = mapped_column(Float, comment="Beam vector")
    beamVectorY: Mapped[Optional[float]] = mapped_column(Float, comment="Beam vector")
    beamVectorZ: Mapped[Optional[float]] = mapped_column(Float, comment="Beam vector")
    cell_a: Mapped[Optional[float]] = mapped_column(Float, comment="Unit cell")
    cell_b: Mapped[Optional[float]] = mapped_column(Float, comment="Unit cell")
    cell_c: Mapped[Optional[float]] = mapped_column(Float, comment="Unit cell")
    cell_alpha: Mapped[Optional[float]] = mapped_column(Float, comment="Unit cell")
    cell_beta: Mapped[Optional[float]] = mapped_column(Float, comment="Unit cell")
    cell_gamma: Mapped[Optional[float]] = mapped_column(Float, comment="Unit cell")
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Creation or last update date/time"
    )
    anomalous: Mapped[Optional[int]] = mapped_column(
        TINYINT(1),
        server_default=text("'0'"),
        comment="boolean type:0 noanoum - 1 anoum",
    )

    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="AutoProcIntegration"
    )
    DataCollection_: Mapped["DataCollection"] = relationship(
        "DataCollection", back_populates="AutoProcIntegration"
    )
    AutoProcScaling_has_Int: Mapped[List["AutoProcScalingHasInt"]] = relationship(
        "AutoProcScalingHasInt", back_populates="AutoProcIntegration_"
    )
    AutoProcStatus: Mapped[List["AutoProcStatus"]] = relationship(
        "AutoProcStatus", back_populates="AutoProcIntegration_"
    )


class AutoProcProgramAttachment(Base):
    __tablename__ = "AutoProcProgramAttachment"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcProgramId"],
            ["AutoProcProgram.autoProcProgramId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="AutoProcProgramAttachmentFk1",
        ),
        Index("AutoProcProgramAttachmentIdx1", "autoProcProgramId"),
    )

    autoProcProgramAttachmentId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcProgramId: Mapped[int] = mapped_column(
        INTEGER, comment="Related autoProcProgram item"
    )
    fileType: Mapped[Optional[str]] = mapped_column(
        Enum("Log", "Result", "Graph", "Debug", "Input"),
        comment="Type of file Attachment",
    )
    fileName: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Attachment filename"
    )
    filePath: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Attachment filepath to disk storage"
    )
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Creation or last update date/time"
    )
    importanceRank: Mapped[Optional[int]] = mapped_column(
        TINYINT,
        comment="For the particular autoProcProgramId and fileType, indicate the importance of the attachment. Higher numbers are more important",
    )

    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="AutoProcProgramAttachment"
    )


class AutoProcProgramMessage(Base):
    __tablename__ = "AutoProcProgramMessage"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcProgramId"],
            ["AutoProcProgram.autoProcProgramId"],
            name="AutoProcProgramMessage_fk1",
        ),
        Index("AutoProcProgramMessage_fk1", "autoProcProgramId"),
    )

    autoProcProgramMessageId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    autoProcProgramId: Mapped[Optional[int]] = mapped_column(INTEGER)
    severity: Mapped[Optional[str]] = mapped_column(Enum("ERROR", "WARNING", "INFO"))
    message: Mapped[Optional[str]] = mapped_column(String(200))
    description: Mapped[Optional[str]] = mapped_column(Text)

    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="AutoProcProgramMessage"
    )


class AutoProcScaling(Base):
    __tablename__ = "AutoProcScaling"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcId"],
            ["AutoProc.autoProcId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="AutoProcScalingFk1",
        ),
        Index("AutoProcScalingFk1", "autoProcId"),
        Index("AutoProcScalingIdx1", "autoProcScalingId", "autoProcId"),
    )

    autoProcScalingId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Related autoProc item (used by foreign key)"
    )
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Creation or last update date/time"
    )

    AutoProc_: Mapped["AutoProc"] = relationship(
        "AutoProc", back_populates="AutoProcScaling"
    )
    AutoProcScalingStatistics: Mapped[List["AutoProcScalingStatistics"]] = relationship(
        "AutoProcScalingStatistics", back_populates="AutoProcScaling_"
    )
    AutoProcScaling_has_Int: Mapped[List["AutoProcScalingHasInt"]] = relationship(
        "AutoProcScalingHasInt", back_populates="AutoProcScaling_"
    )
    MXMRRun: Mapped[List["MXMRRun"]] = relationship(
        "MXMRRun", back_populates="AutoProcScaling_"
    )
    PhasingStep: Mapped[List["PhasingStep"]] = relationship(
        "PhasingStep", back_populates="AutoProcScaling_"
    )
    Phasing_has_Scaling: Mapped[List["PhasingHasScaling"]] = relationship(
        "PhasingHasScaling", back_populates="AutoProcScaling_"
    )


class BFComponent(Base):
    __tablename__ = "BF_component"
    __table_args__ = (
        ForeignKeyConstraint(
            ["systemId"], ["BF_system.systemId"], name="bf_component_FK1"
        ),
        Index("bf_component_FK1", "systemId"),
    )

    componentId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    systemId: Mapped[Optional[int]] = mapped_column(INTEGER)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(200))

    BF_system: Mapped["BFSystem"] = relationship(
        "BFSystem", back_populates="BF_component"
    )
    BF_component_beamline: Mapped[List["BFComponentBeamline"]] = relationship(
        "BFComponentBeamline", back_populates="BF_component"
    )
    BF_subcomponent: Mapped[List["BFSubcomponent"]] = relationship(
        "BFSubcomponent", back_populates="BF_component"
    )


class BFSystemBeamline(Base):
    __tablename__ = "BF_system_beamline"
    __table_args__ = (
        ForeignKeyConstraint(
            ["systemId"], ["BF_system.systemId"], name="bf_system_beamline_FK1"
        ),
        Index("bf_system_beamline_FK1", "systemId"),
    )

    system_beamlineId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    systemId: Mapped[Optional[int]] = mapped_column(INTEGER)
    beamlineName: Mapped[Optional[str]] = mapped_column(String(20))

    BF_system: Mapped["BFSystem"] = relationship(
        "BFSystem", back_populates="BF_system_beamline"
    )


class BLSampleImageAnalysis(Base):
    __tablename__ = "BLSampleImageAnalysis"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleImageId"],
            ["BLSampleImage.blSampleImageId"],
            name="BLSampleImageAnalysis_ibfk1",
        ),
        Index("BLSampleImageAnalysis_ibfk1", "blSampleImageId"),
    )

    blSampleImageAnalysisId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    blSampleImageId: Mapped[Optional[int]] = mapped_column(INTEGER)
    oavSnapshotBefore: Mapped[Optional[str]] = mapped_column(String(255))
    oavSnapshotAfter: Mapped[Optional[str]] = mapped_column(String(255))
    deltaX: Mapped[Optional[int]] = mapped_column(Integer)
    deltaY: Mapped[Optional[int]] = mapped_column(Integer)
    goodnessOfFit: Mapped[Optional[float]] = mapped_column(Float)
    scaleFactor: Mapped[Optional[float]] = mapped_column(Float)
    resultCode: Mapped[Optional[str]] = mapped_column(String(15))
    matchStartTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    matchEndTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)

    BLSampleImage_: Mapped["BLSampleImage"] = relationship(
        "BLSampleImage", back_populates="BLSampleImageAnalysis"
    )


class BLSampleImageAutoScoreClass(Base):
    __tablename__ = "BLSampleImageAutoScoreClass"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleImageAutoScoreSchemaId"],
            ["BLSampleImageAutoScoreSchema.blSampleImageAutoScoreSchemaId"],
            onupdate="CASCADE",
            name="BLSampleImageAutoScoreClass_fk1",
        ),
        Index("BLSampleImageAutoScoreClass_fk1", "blSampleImageAutoScoreSchemaId"),
        {"comment": "The automated scoring classes - the thing being scored"},
    )

    blSampleImageAutoScoreClassId: Mapped[int] = mapped_column(
        TINYINT, primary_key=True
    )
    scoreClass: Mapped[str] = mapped_column(
        String(15), comment="Thing being scored e.g. crystal, precipitant"
    )
    blSampleImageAutoScoreSchemaId: Mapped[Optional[int]] = mapped_column(TINYINT)

    BLSampleImageAutoScoreSchema_: Mapped[
        "BLSampleImageAutoScoreSchema"
    ] = relationship(
        "BLSampleImageAutoScoreSchema", back_populates="BLSampleImageAutoScoreClass"
    )
    BLSampleImage_has_AutoScoreClass: Mapped[
        List["BLSampleImageHasAutoScoreClass"]
    ] = relationship(
        "BLSampleImageHasAutoScoreClass",
        back_populates="BLSampleImageAutoScoreClass_",
    )


class BLSampleImageMeasurement(Base):
    __tablename__ = "BLSampleImageMeasurement"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleImageId"],
            ["BLSampleImage.blSampleImageId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSampleImageMeasurement_ibfk_1",
        ),
        ForeignKeyConstraint(
            ["blSubSampleId"],
            ["BLSubSample.blSubSampleId"],
            name="BLSampleImageMeasurement_ibfk_2",
        ),
        Index("BLSampleImageMeasurement_ibfk_1", "blSampleImageId"),
        Index("BLSampleImageMeasurement_ibfk_2", "blSubSampleId"),
        {"comment": "For measuring crystal growth over time"},
    )

    blSampleImageMeasurementId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    blSampleImageId: Mapped[int] = mapped_column(INTEGER)
    blSubSampleId: Mapped[Optional[int]] = mapped_column(INTEGER)
    startPosX: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    startPosY: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    endPosX: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    endPosY: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    blTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    BLSampleImage_: Mapped["BLSampleImage"] = relationship(
        "BLSampleImage", back_populates="BLSampleImageMeasurement"
    )
    BLSubSample_: Mapped["BLSubSample"] = relationship(
        "BLSubSample", back_populates="BLSampleImageMeasurement"
    )


class BLSampleImageHasPositioner(Base):
    __tablename__ = "BLSampleImage_has_Positioner"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleImageId"],
            ["BLSampleImage.blSampleImageId"],
            name="BLSampleImageHasPositioner_ibfk1",
        ),
        ForeignKeyConstraint(
            ["positionerId"],
            ["Positioner.positionerId"],
            name="BLSampleImageHasPositioner_ibfk2",
        ),
        Index("BLSampleImageHasPositioner_ibfk1", "blSampleImageId"),
        Index("BLSampleImageHasPositioner_ibfk2", "positionerId"),
        {
            "comment": "Allows a BLSampleImage to store motor positions along with the "
            "image"
        },
    )

    blSampleImageHasPositionerId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    blSampleImageId: Mapped[int] = mapped_column(INTEGER)
    positionerId: Mapped[int] = mapped_column(INTEGER)
    value: Mapped[Optional[float]] = mapped_column(
        Float, comment="The position of this positioner for this blsampleimage"
    )

    BLSampleImage_: Mapped["BLSampleImage"] = relationship(
        "BLSampleImage", back_populates="BLSampleImage_has_Positioner"
    )
    Positioner_: Mapped["Positioner"] = relationship(
        "Positioner", back_populates="BLSampleImage_has_Positioner"
    )


class BLSampleHasPositioner(Base):
    __tablename__ = "BLSample_has_Positioner"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleId"], ["BLSample.blSampleId"], name="BLSampleHasPositioner_ibfk1"
        ),
        ForeignKeyConstraint(
            ["positionerId"],
            ["Positioner.positionerId"],
            name="BLSampleHasPositioner_ibfk2",
        ),
        Index("BLSampleHasPositioner_ibfk1", "blSampleId"),
        Index("BLSampleHasPositioner_ibfk2", "positionerId"),
    )

    blSampleHasPositioner: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    blSampleId: Mapped[int] = mapped_column(INTEGER)
    positionerId: Mapped[int] = mapped_column(INTEGER)

    BLSample_: Mapped["BLSample"] = relationship(
        "BLSample", back_populates="BLSample_has_Positioner"
    )
    Positioner_: Mapped["Positioner"] = relationship(
        "Positioner", back_populates="BLSample_has_Positioner"
    )


class BLSubSampleHasPositioner(Base):
    __tablename__ = "BLSubSample_has_Positioner"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSubSampleId"],
            ["BLSubSample.blSubSampleId"],
            name="BLSubSampleHasPositioner_ibfk1",
        ),
        ForeignKeyConstraint(
            ["positionerId"],
            ["Positioner.positionerId"],
            name="BLSubSampleHasPositioner_ibfk2",
        ),
        Index("BLSubSampleHasPositioner_ibfk1", "blSubSampleId"),
        Index("BLSubSampleHasPositioner_ibfk2", "positionerId"),
    )

    blSubSampleHasPositioner: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    blSubSampleId: Mapped[int] = mapped_column(INTEGER)
    positionerId: Mapped[int] = mapped_column(INTEGER)

    BLSubSample_: Mapped["BLSubSample"] = relationship(
        "BLSubSample", back_populates="BLSubSample_has_Positioner"
    )
    Positioner_: Mapped["Positioner"] = relationship(
        "Positioner", back_populates="BLSubSample_has_Positioner"
    )


class BeamApertures(Base):
    __tablename__ = "BeamApertures"
    __table_args__ = (
        ForeignKeyConstraint(
            ["beamlineStatsId"],
            ["BeamlineStats.beamlineStatsId"],
            ondelete="CASCADE",
            name="beamapertures_FK1",
        ),
        Index("beamapertures_FK1", "beamlineStatsId"),
    )

    beamAperturesid: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    beamlineStatsId: Mapped[Optional[int]] = mapped_column(INTEGER)
    flux: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    x: Mapped[Optional[float]] = mapped_column(Float)
    y: Mapped[Optional[float]] = mapped_column(Float)
    apertureSize: Mapped[Optional[int]] = mapped_column(SMALLINT)

    BeamlineStats_: Mapped["BeamlineStats"] = relationship(
        "BeamlineStats", back_populates="BeamApertures"
    )


class BeamCentres(Base):
    __tablename__ = "BeamCentres"
    __table_args__ = (
        ForeignKeyConstraint(
            ["beamlineStatsId"],
            ["BeamlineStats.beamlineStatsId"],
            ondelete="CASCADE",
            name="beamCentres_FK1",
        ),
        Index("beamCentres_FK1", "beamlineStatsId"),
    )

    beamCentresid: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    beamlineStatsId: Mapped[Optional[int]] = mapped_column(INTEGER)
    x: Mapped[Optional[float]] = mapped_column(Float)
    y: Mapped[Optional[float]] = mapped_column(Float)
    zoom: Mapped[Optional[int]] = mapped_column(TINYINT)

    BeamlineStats_: Mapped["BeamlineStats"] = relationship(
        "BeamlineStats", back_populates="BeamCentres"
    )


class BeamLineSetup(Base):
    __tablename__ = "BeamLineSetup"
    __table_args__ = (
        ForeignKeyConstraint(
            ["detectorId"], ["Detector.detectorId"], name="BeamLineSetup_ibfk_1"
        ),
        Index("BeamLineSetup_ibfk_1", "detectorId"),
    )

    beamLineSetupId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Creation or last update date/time",
    )
    active: Mapped[int] = mapped_column(TINYINT(1), server_default=text("'0'"))
    detectorId: Mapped[Optional[int]] = mapped_column(Integer)
    synchrotronMode: Mapped[Optional[str]] = mapped_column(String(255))
    undulatorType1: Mapped[Optional[str]] = mapped_column(String(45))
    undulatorType2: Mapped[Optional[str]] = mapped_column(String(45))
    undulatorType3: Mapped[Optional[str]] = mapped_column(String(45))
    focalSpotSizeAtSample: Mapped[Optional[float]] = mapped_column(Float)
    focusingOptic: Mapped[Optional[str]] = mapped_column(String(255))
    beamDivergenceHorizontal: Mapped[Optional[float]] = mapped_column(Float)
    beamDivergenceVertical: Mapped[Optional[float]] = mapped_column(Float)
    polarisation: Mapped[Optional[float]] = mapped_column(Float)
    monochromatorType: Mapped[Optional[str]] = mapped_column(String(255))
    setupDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    synchrotronName: Mapped[Optional[str]] = mapped_column(String(255))
    maxExpTimePerDataCollection: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    maxExposureTimePerImage: Mapped[Optional[float]] = mapped_column(
        Float, comment="unit: seconds"
    )
    minExposureTimePerImage: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    goniostatMaxOscillationSpeed: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    goniostatMaxOscillationWidth: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="unit: degrees"
    )
    goniostatMinOscillationWidth: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    maxTransmission: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="unit: percentage"
    )
    minTransmission: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    CS: Mapped[Optional[float]] = mapped_column(
        Float, comment="Spherical Aberration, Units: mm?"
    )
    beamlineName: Mapped[Optional[str]] = mapped_column(
        String(50), comment="Beamline that this setup relates to"
    )
    beamSizeXMin: Mapped[Optional[float]] = mapped_column(Float, comment="unit: um")
    beamSizeXMax: Mapped[Optional[float]] = mapped_column(Float, comment="unit: um")
    beamSizeYMin: Mapped[Optional[float]] = mapped_column(Float, comment="unit: um")
    beamSizeYMax: Mapped[Optional[float]] = mapped_column(Float, comment="unit: um")
    energyMin: Mapped[Optional[float]] = mapped_column(Float, comment="unit: eV")
    energyMax: Mapped[Optional[float]] = mapped_column(Float, comment="unit: eV")
    omegaMin: Mapped[Optional[float]] = mapped_column(Float, comment="unit: degrees")
    omegaMax: Mapped[Optional[float]] = mapped_column(Float, comment="unit: degrees")
    kappaMin: Mapped[Optional[float]] = mapped_column(Float, comment="unit: degrees")
    kappaMax: Mapped[Optional[float]] = mapped_column(Float, comment="unit: degrees")
    phiMin: Mapped[Optional[float]] = mapped_column(Float, comment="unit: degrees")
    phiMax: Mapped[Optional[float]] = mapped_column(Float, comment="unit: degrees")
    numberOfImagesMax: Mapped[Optional[int]] = mapped_column(MEDIUMINT)
    numberOfImagesMin: Mapped[Optional[int]] = mapped_column(MEDIUMINT)
    boxSizeXMin: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="For gridscans, unit: um"
    )
    boxSizeXMax: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="For gridscans, unit: um"
    )
    boxSizeYMin: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="For gridscans, unit: um"
    )
    boxSizeYMax: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="For gridscans, unit: um"
    )
    monoBandwidthMin: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="unit: percentage"
    )
    monoBandwidthMax: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="unit: percentage"
    )
    preferredDataCentre: Mapped[Optional[str]] = mapped_column(
        String(30),
        comment="Relevant datacentre to use to process data from this beamline",
    )
    amplitudeContrast: Mapped[Optional[float]] = mapped_column(
        Float, comment="Needed for cryo-ET"
    )

    Detector_: Mapped["Detector"] = relationship(
        "Detector", back_populates="BeamLineSetup"
    )
    BLSession: Mapped[List["BLSession"]] = relationship(
        "BLSession", back_populates="BeamLineSetup_"
    )


class DataCollectionFileAttachment(Base):
    __tablename__ = "DataCollectionFileAttachment"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dataCollectionId"],
            ["DataCollection.dataCollectionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="_dataCollectionFileAttachmentId_fk1",
        ),
        Index("_dataCollectionFileAttachmentId_fk1", "dataCollectionId"),
    )

    dataCollectionFileAttachmentId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True
    )
    dataCollectionId: Mapped[int] = mapped_column(INTEGER)
    fileFullPath: Mapped[str] = mapped_column(String(255))
    createTime: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    fileType: Mapped[Optional[str]] = mapped_column(
        Enum("snapshot", "log", "xy", "recip", "pia", "warning", "params")
    )

    DataCollection_: Mapped["DataCollection"] = relationship(
        "DataCollection", back_populates="DataCollectionFileAttachment"
    )


class EventChain(Base):
    __tablename__ = "EventChain"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dataCollectionId"],
            ["DataCollection.dataCollectionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="EventChain_ibfk_1",
        ),
        Index("dataCollectionId", "dataCollectionId"),
        {"comment": "Groups events together in a data collection."},
    )

    eventChainId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    dataCollectionId: Mapped[int] = mapped_column(INTEGER)
    name: Mapped[Optional[str]] = mapped_column(String(255, "utf8mb4_general_ci"))

    DataCollection_: Mapped["DataCollection"] = relationship(
        "DataCollection", back_populates="EventChain"
    )
    Event: Mapped[List["Event"]] = relationship("Event", back_populates="EventChain_")


class GridImageMap(Base):
    __tablename__ = "GridImageMap"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dataCollectionId"],
            ["DataCollection.dataCollectionId"],
            name="_GridImageMap_ibfk1",
        ),
        Index("_GridImageMap_ibfk1", "dataCollectionId"),
    )

    gridImageMapId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    dataCollectionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    imageNumber: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Movie number, sequential 1-n in time order"
    )
    outputFileId: Mapped[Optional[str]] = mapped_column(
        String(80), comment="File number, file 1 may not be movie 1"
    )
    positionX: Mapped[Optional[float]] = mapped_column(
        Float, comment="X position of stage, Units: um"
    )
    positionY: Mapped[Optional[float]] = mapped_column(
        Float, comment="Y position of stage, Units: um"
    )

    DataCollection_: Mapped["DataCollection"] = relationship(
        "DataCollection", back_populates="GridImageMap"
    )


class Image(Base):
    __tablename__ = "Image"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dataCollectionId"],
            ["DataCollection.dataCollectionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Image_ibfk_1",
        ),
        ForeignKeyConstraint(
            ["motorPositionId"],
            ["MotorPosition.motorPositionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Image_ibfk_2",
        ),
        Index("Image_FKIndex1", "dataCollectionId"),
        Index("Image_FKIndex2", "imageNumber"),
        Index("Image_Index3", "fileLocation", "fileName"),
        Index("motorPositionId", "motorPositionId"),
    )

    imageId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    dataCollectionId: Mapped[int] = mapped_column(INTEGER, server_default=text("'0'"))
    BLTIMESTAMP: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Creation or last update date/time",
    )
    imageNumber: Mapped[Optional[int]] = mapped_column(INTEGER)
    fileName: Mapped[Optional[str]] = mapped_column(String(255))
    fileLocation: Mapped[Optional[str]] = mapped_column(String(255))
    measuredIntensity: Mapped[Optional[float]] = mapped_column(Float)
    jpegFileFullPath: Mapped[Optional[str]] = mapped_column(String(255))
    jpegThumbnailFileFullPath: Mapped[Optional[str]] = mapped_column(String(255))
    temperature: Mapped[Optional[float]] = mapped_column(Float)
    cumulativeIntensity: Mapped[Optional[float]] = mapped_column(Float)
    synchrotronCurrent: Mapped[Optional[float]] = mapped_column(Float)
    comments: Mapped[Optional[str]] = mapped_column(String(1024))
    machineMessage: Mapped[Optional[str]] = mapped_column(String(1024))
    motorPositionId: Mapped[Optional[int]] = mapped_column(INTEGER)

    DataCollection_: Mapped["DataCollection"] = relationship(
        "DataCollection", back_populates="Image"
    )
    MotorPosition_: Mapped["MotorPosition"] = relationship(
        "MotorPosition", back_populates="Image"
    )


class LDAPSearchBase(Base):
    __tablename__ = "LDAPSearchBase"
    __table_args__ = (
        ForeignKeyConstraint(
            ["ldapSearchParametersId"],
            ["LDAPSearchParameters.ldapSearchParametersId"],
            name="LDAPSearchBase_fk_ldapSearchParametersId",
        ),
        Index("LDAPSearchBase_fk_ldapSearchParametersId", "ldapSearchParametersId"),
        {
            "comment": "LDAP search base and the sequence number in which it should be "
            "attempted"
        },
    )

    ldapSearchBaseId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    ldapSearchParametersId: Mapped[int] = mapped_column(
        INTEGER,
        comment="The other LDAP search parameters to be used with this search base",
    )
    searchBase: Mapped[str] = mapped_column(
        String(200, "utf8mb4_general_ci"), comment="Name of the object we search for"
    )
    sequenceNumber: Mapped[int] = mapped_column(
        TINYINT,
        comment="The number in the sequence of searches where this search base should be attempted",
    )

    LDAPSearchParameters_: Mapped["LDAPSearchParameters"] = relationship(
        "LDAPSearchParameters", back_populates="LDAPSearchBase"
    )


class Movie(Base):
    __tablename__ = "Movie"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dataCollectionId"],
            ["DataCollection.dataCollectionId"],
            name="Movie_ibfk1",
        ),
        Index("Movie_ibfk1", "dataCollectionId"),
    )

    movieId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    createdTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    dataCollectionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    movieNumber: Mapped[Optional[int]] = mapped_column(MEDIUMINT)
    movieFullPath: Mapped[Optional[str]] = mapped_column(String(255))
    positionX: Mapped[Optional[float]] = mapped_column(Float)
    positionY: Mapped[Optional[float]] = mapped_column(Float)
    nominalDefocus: Mapped[Optional[float]] = mapped_column(
        Float, comment="Nominal defocus, Units: A"
    )
    angle: Mapped[Optional[float]] = mapped_column(
        Float, comment="unit: degrees relative to perpendicular to beam"
    )
    fluence: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="accumulated electron fluence from start to end of acquisition of this movie (commonly, but incorrectly, referred to as ‘dose’)",
    )
    numberOfFrames: Mapped[Optional[int]] = mapped_column(
        INTEGER,
        comment="number of frames per movie. This should be equivalent to the number of\xa0MotionCorrectionDrift\xa0entries, but the latter is a property of data analysis, whereas the number of frames is an intrinsic property of acquisition.",
    )

    DataCollection_: Mapped["DataCollection"] = relationship(
        "DataCollection", back_populates="Movie"
    )
    MotionCorrection: Mapped[List["MotionCorrection"]] = relationship(
        "MotionCorrection", back_populates="Movie_"
    )
    TiltImageAlignment: Mapped[List["TiltImageAlignment"]] = relationship(
        "TiltImageAlignment", back_populates="Movie_"
    )


class PDBEntry(Base):
    __tablename__ = "PDBEntry"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcProgramId"],
            ["AutoProcProgram.autoProcProgramId"],
            ondelete="CASCADE",
            name="pdbEntry_FK1",
        ),
        Index("pdbEntryIdx1", "autoProcProgramId"),
    )

    pdbEntryId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    autoProcProgramId: Mapped[int] = mapped_column(INTEGER)
    code: Mapped[Optional[str]] = mapped_column(String(4))
    cell_a: Mapped[Optional[float]] = mapped_column(Float)
    cell_b: Mapped[Optional[float]] = mapped_column(Float)
    cell_c: Mapped[Optional[float]] = mapped_column(Float)
    cell_alpha: Mapped[Optional[float]] = mapped_column(Float)
    cell_beta: Mapped[Optional[float]] = mapped_column(Float)
    cell_gamma: Mapped[Optional[float]] = mapped_column(Float)
    resolution: Mapped[Optional[float]] = mapped_column(Float)
    pdbTitle: Mapped[Optional[str]] = mapped_column(String(255))
    pdbAuthors: Mapped[Optional[str]] = mapped_column(String(600))
    pdbDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    pdbBeamlineName: Mapped[Optional[str]] = mapped_column(String(50))
    beamlines: Mapped[Optional[str]] = mapped_column(String(100))
    distance: Mapped[Optional[float]] = mapped_column(Float)
    autoProcCount: Mapped[Optional[int]] = mapped_column(SmallInteger)
    dataCollectionCount: Mapped[Optional[int]] = mapped_column(SmallInteger)
    beamlineMatch: Mapped[Optional[int]] = mapped_column(TINYINT(1))
    authorMatch: Mapped[Optional[int]] = mapped_column(TINYINT(1))

    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="PDBEntry"
    )
    PDBEntry_has_AutoProcProgram: Mapped[
        List["PDBEntryHasAutoProcProgram"]
    ] = relationship("PDBEntryHasAutoProcProgram", back_populates="PDBEntry_")


class Person(Base):
    __tablename__ = "Person"
    __table_args__ = (
        ForeignKeyConstraint(
            ["laboratoryId"], ["Laboratory.laboratoryId"], name="Person_ibfk_1"
        ),
        Index("Person_FKIndex1", "laboratoryId"),
        Index("Person_FKIndexFamilyName", "familyName"),
        Index("Person_FKIndex_Login", "login", unique=True),
        Index("siteId", "siteId"),
    )

    personId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Creation or last update date/time",
    )
    laboratoryId: Mapped[Optional[int]] = mapped_column(INTEGER)
    siteId: Mapped[Optional[int]] = mapped_column(Integer)
    personUUID: Mapped[Optional[str]] = mapped_column(String(45))
    familyName: Mapped[Optional[str]] = mapped_column(String(100))
    givenName: Mapped[Optional[str]] = mapped_column(String(45))
    title: Mapped[Optional[str]] = mapped_column(String(45))
    emailAddress: Mapped[Optional[str]] = mapped_column(String(60))
    phoneNumber: Mapped[Optional[str]] = mapped_column(String(45))
    login: Mapped[Optional[str]] = mapped_column(String(45))
    faxNumber: Mapped[Optional[str]] = mapped_column(String(45))
    cache: Mapped[Optional[str]] = mapped_column(Text)
    externalId: Mapped[Optional[bytes]] = mapped_column(BINARY(16))

    Laboratory_: Mapped["Laboratory"] = relationship(
        "Laboratory", back_populates="Person"
    )
    UserGroup_: Mapped[List["UserGroup"]] = relationship(
        "UserGroup", secondary="UserGroup_has_Person", back_populates="Person"
    )
    Project: Mapped[List["Project"]] = relationship(
        "Project", secondary="Project_has_Person", back_populates="Person_"
    )
    ContainerReport: Mapped[List["ContainerReport"]] = relationship(
        "ContainerReport", back_populates="Person_"
    )
    DataCollectionComment: Mapped[List["DataCollectionComment"]] = relationship(
        "DataCollectionComment", back_populates="Person_"
    )
    Project_: Mapped[List["Project"]] = relationship(
        "Project", back_populates="Person1"
    )
    Proposal: Mapped[List["Proposal"]] = relationship(
        "Proposal", back_populates="Person_"
    )
    ContainerRegistry_has_Proposal: Mapped[
        List["ContainerRegistryHasProposal"]
    ] = relationship("ContainerRegistryHasProposal", back_populates="Person_")
    LabContact: Mapped[List["LabContact"]] = relationship(
        "LabContact", back_populates="Person_"
    )
    ProposalHasPerson: Mapped[List["ProposalHasPerson"]] = relationship(
        "ProposalHasPerson", back_populates="Person_"
    )
    SW_onceToken: Mapped[List["SWOnceToken"]] = relationship(
        "SWOnceToken", back_populates="Person_"
    )
    BF_fault: Mapped[List["BFFault"]] = relationship(
        "BFFault", foreign_keys="[BFFault.assigneeId]", back_populates="Person_"
    )
    BF_fault_: Mapped[List["BFFault"]] = relationship(
        "BFFault", foreign_keys="[BFFault.personId]", back_populates="Person1"
    )
    Session_has_Person: Mapped[List["SessionHasPerson"]] = relationship(
        "SessionHasPerson", back_populates="Person_"
    )
    Shipping: Mapped[List["Shipping"]] = relationship(
        "Shipping", back_populates="Person_"
    )
    CourierTermsAccepted: Mapped[List["CourierTermsAccepted"]] = relationship(
        "CourierTermsAccepted", back_populates="Person_"
    )
    DewarRegistry_has_Proposal: Mapped[List["DewarRegistryHasProposal"]] = relationship(
        "DewarRegistryHasProposal", back_populates="Person_"
    )
    Container: Mapped[List["Container"]] = relationship(
        "Container", back_populates="Person_"
    )
    ContainerQueue: Mapped[List["ContainerQueue"]] = relationship(
        "ContainerQueue", back_populates="Person_"
    )


class PhasingProgramAttachment(Base):
    __tablename__ = "PhasingProgramAttachment"
    __table_args__ = (
        ForeignKeyConstraint(
            ["phasingProgramRunId"],
            ["PhasingProgramRun.phasingProgramRunId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Phasing_phasingProgramAttachmentfk_1",
        ),
        Index("PhasingProgramAttachment_FKIndex1", "phasingProgramRunId"),
    )

    phasingProgramAttachmentId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingProgramRunId: Mapped[int] = mapped_column(
        INTEGER, comment="Related program item"
    )
    fileType: Mapped[Optional[str]] = mapped_column(
        Enum("Map", "Logfile", "PDB", "CSV", "INS", "RES", "TXT"), comment="file type"
    )
    fileName: Mapped[Optional[str]] = mapped_column(String(45), comment="file name")
    filePath: Mapped[Optional[str]] = mapped_column(String(255), comment="file path")
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Creation or last update date/time"
    )

    PhasingProgramRun_: Mapped["PhasingProgramRun"] = relationship(
        "PhasingProgramRun", back_populates="PhasingProgramAttachment"
    )


class ProcessingJobImageSweep(Base):
    __tablename__ = "ProcessingJobImageSweep"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dataCollectionId"],
            ["DataCollection.dataCollectionId"],
            name="ProcessingJobImageSweep_ibfk2",
        ),
        ForeignKeyConstraint(
            ["processingJobId"],
            ["ProcessingJob.processingJobId"],
            name="ProcessingJobImageSweep_ibfk1",
        ),
        Index("ProcessingJobImageSweep_ibfk1", "processingJobId"),
        Index("ProcessingJobImageSweep_ibfk2", "dataCollectionId"),
        {"comment": "This allows multiple sweeps per processing job for multi-xia2"},
    )

    processingJobImageSweepId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    processingJobId: Mapped[Optional[int]] = mapped_column(INTEGER)
    dataCollectionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    startImage: Mapped[Optional[int]] = mapped_column(MEDIUMINT)
    endImage: Mapped[Optional[int]] = mapped_column(MEDIUMINT)

    DataCollection_: Mapped["DataCollection"] = relationship(
        "DataCollection", back_populates="ProcessingJobImageSweep"
    )
    ProcessingJob_: Mapped["ProcessingJob"] = relationship(
        "ProcessingJob", back_populates="ProcessingJobImageSweep"
    )


class ProcessingJobParameter(Base):
    __tablename__ = "ProcessingJobParameter"
    __table_args__ = (
        ForeignKeyConstraint(
            ["processingJobId"],
            ["ProcessingJob.processingJobId"],
            name="ProcessingJobParameter_ibfk1",
        ),
        Index("ProcessingJobParameter_ibfk1", "processingJobId"),
    )

    processingJobParameterId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    processingJobId: Mapped[Optional[int]] = mapped_column(INTEGER)
    parameterKey: Mapped[Optional[str]] = mapped_column(
        String(80), comment="E.g. resolution, spacegroup, pipeline"
    )
    parameterValue: Mapped[Optional[str]] = mapped_column(String(1024))

    ProcessingJob_: Mapped["ProcessingJob"] = relationship(
        "ProcessingJob", back_populates="ProcessingJobParameter"
    )


class ProcessingPipeline(Base):
    __tablename__ = "ProcessingPipeline"
    __table_args__ = (
        ForeignKeyConstraint(
            ["processingPipelineCategoryId"],
            ["ProcessingPipelineCategory.processingPipelineCategoryId"],
            name="ProcessingPipeline_fk1",
        ),
        Index("ProcessingPipeline_fk1", "processingPipelineCategoryId"),
        {
            "comment": "A lookup table for different processing pipelines and their "
            "categories"
        },
    )

    processingPipelineId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    discipline: Mapped[str] = mapped_column(String(10))
    processingPipelineCategoryId: Mapped[Optional[int]] = mapped_column(INTEGER)
    pipelineStatus: Mapped[Optional[str]] = mapped_column(
        Enum("automatic", "optional", "deprecated"),
        comment="Is the pipeline in operation or available",
    )
    reprocessing: Mapped[Optional[int]] = mapped_column(
        TINYINT(1),
        server_default=text("'1'"),
        comment="Pipeline is available for re-processing",
    )

    ProcessingPipelineCategory_: Mapped["ProcessingPipelineCategory"] = relationship(
        "ProcessingPipelineCategory", back_populates="ProcessingPipeline"
    )
    Container: Mapped[List["Container"]] = relationship(
        "Container", back_populates="ProcessingPipeline_"
    )


class SSXDataCollection(DataCollection):
    __tablename__ = "SSXDataCollection"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dataCollectionId"],
            ["DataCollection.dataCollectionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="SSXDataCollection_ibfk_1",
        ),
        {"comment": "Extends DataCollection with SSX-specific fields."},
    )

    dataCollectionId: Mapped[int] = mapped_column(
        INTEGER,
        primary_key=True,
        comment="Primary key is same as dataCollection (1 to 1).",
    )
    repetitionRate: Mapped[Optional[float]] = mapped_column(Float)
    energyBandwidth: Mapped[Optional[float]] = mapped_column(Float)
    monoStripe: Mapped[Optional[str]] = mapped_column(String(255, "utf8mb4_general_ci"))
    jetSpeed: Mapped[Optional[float]] = mapped_column(
        Float, comment="For jet experiments."
    )
    jetSize: Mapped[Optional[float]] = mapped_column(
        Float, comment="For jet experiments."
    )
    chipPattern: Mapped[Optional[str]] = mapped_column(
        String(255, "utf8mb4_general_ci"), comment="For chip experiments."
    )
    chipModel: Mapped[Optional[str]] = mapped_column(
        String(255, "utf8mb4_general_ci"), comment="For chip experiments."
    )
    reactionDuration: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="When images are taken at constant time relative to reaction start.",
    )
    laserEnergy: Mapped[Optional[float]] = mapped_column(Float)
    experimentName: Mapped[Optional[str]] = mapped_column(
        String(255, "utf8mb4_general_ci")
    )


class ScheduleComponent(Base):
    __tablename__ = "ScheduleComponent"
    __table_args__ = (
        ForeignKeyConstraint(
            ["inspectionTypeId"],
            ["InspectionType.inspectionTypeId"],
            ondelete="CASCADE",
            name="ScheduleComponent_fk2",
        ),
        ForeignKeyConstraint(
            ["scheduleId"],
            ["Schedule.scheduleId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ScheduleComponent_fk1",
        ),
        Index("ScheduleComponent_fk2", "inspectionTypeId"),
        Index("ScheduleComponent_idx1", "scheduleId"),
    )

    scheduleComponentId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    scheduleId: Mapped[int] = mapped_column(INTEGER)
    offset_hours: Mapped[Optional[int]] = mapped_column(Integer)
    inspectionTypeId: Mapped[Optional[int]] = mapped_column(INTEGER)

    InspectionType_: Mapped["InspectionType"] = relationship(
        "InspectionType", back_populates="ScheduleComponent"
    )
    Schedule_: Mapped["Schedule"] = relationship(
        "Schedule", back_populates="ScheduleComponent"
    )
    ContainerInspection: Mapped[List["ContainerInspection"]] = relationship(
        "ContainerInspection", back_populates="ScheduleComponent_"
    )


class ScreeningInput(Base):
    __tablename__ = "ScreeningInput"
    __table_args__ = (
        ForeignKeyConstraint(
            ["screeningId"],
            ["Screening.screeningId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ScreeningInput_ibfk_1",
        ),
        Index("ScreeningInput_FKIndex1", "screeningId"),
    )

    screeningInputId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    screeningId: Mapped[int] = mapped_column(INTEGER, server_default=text("'0'"))
    beamX: Mapped[Optional[float]] = mapped_column(Float)
    beamY: Mapped[Optional[float]] = mapped_column(Float)
    rmsErrorLimits: Mapped[Optional[float]] = mapped_column(Float)
    minimumFractionIndexed: Mapped[Optional[float]] = mapped_column(Float)
    maximumFractionRejected: Mapped[Optional[float]] = mapped_column(Float)
    minimumSignalToNoise: Mapped[Optional[float]] = mapped_column(Float)
    diffractionPlanId: Mapped[Optional[int]] = mapped_column(
        Integer, comment="references DiffractionPlan table"
    )
    xmlSampleInformation: Mapped[Optional[bytes]] = mapped_column(LONGBLOB)

    Screening_: Mapped["Screening"] = relationship(
        "Screening", back_populates="ScreeningInput"
    )


class ScreeningOutputLattice(Base):
    __tablename__ = "ScreeningOutputLattice"
    __table_args__ = (
        ForeignKeyConstraint(
            ["screeningOutputId"],
            ["ScreeningOutput.screeningOutputId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ScreeningOutputLattice_ibfk_1",
        ),
        Index("ScreeningOutputLattice_FKIndex1", "screeningOutputId"),
    )

    screeningOutputLatticeId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    screeningOutputId: Mapped[int] = mapped_column(INTEGER, server_default=text("'0'"))
    bltimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    spaceGroup: Mapped[Optional[str]] = mapped_column(String(45))
    pointGroup: Mapped[Optional[str]] = mapped_column(String(45))
    bravaisLattice: Mapped[Optional[str]] = mapped_column(String(45))
    rawOrientationMatrix_a_x: Mapped[Optional[float]] = mapped_column(Float)
    rawOrientationMatrix_a_y: Mapped[Optional[float]] = mapped_column(Float)
    rawOrientationMatrix_a_z: Mapped[Optional[float]] = mapped_column(Float)
    rawOrientationMatrix_b_x: Mapped[Optional[float]] = mapped_column(Float)
    rawOrientationMatrix_b_y: Mapped[Optional[float]] = mapped_column(Float)
    rawOrientationMatrix_b_z: Mapped[Optional[float]] = mapped_column(Float)
    rawOrientationMatrix_c_x: Mapped[Optional[float]] = mapped_column(Float)
    rawOrientationMatrix_c_y: Mapped[Optional[float]] = mapped_column(Float)
    rawOrientationMatrix_c_z: Mapped[Optional[float]] = mapped_column(Float)
    unitCell_a: Mapped[Optional[float]] = mapped_column(Float)
    unitCell_b: Mapped[Optional[float]] = mapped_column(Float)
    unitCell_c: Mapped[Optional[float]] = mapped_column(Float)
    unitCell_alpha: Mapped[Optional[float]] = mapped_column(Float)
    unitCell_beta: Mapped[Optional[float]] = mapped_column(Float)
    unitCell_gamma: Mapped[Optional[float]] = mapped_column(Float)
    labelitIndexing: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), server_default=text("'0'")
    )

    ScreeningOutput_: Mapped["ScreeningOutput"] = relationship(
        "ScreeningOutput", back_populates="ScreeningOutputLattice"
    )


class ScreeningRank(Base):
    __tablename__ = "ScreeningRank"
    __table_args__ = (
        ForeignKeyConstraint(
            ["screeningId"],
            ["Screening.screeningId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ScreeningRank_ibfk_1",
        ),
        ForeignKeyConstraint(
            ["screeningRankSetId"],
            ["ScreeningRankSet.screeningRankSetId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ScreeningRank_ibfk_2",
        ),
        Index("ScreeningRank_FKIndex1", "screeningId"),
        Index("ScreeningRank_FKIndex2", "screeningRankSetId"),
    )

    screeningRankId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    screeningRankSetId: Mapped[int] = mapped_column(INTEGER, server_default=text("'0'"))
    screeningId: Mapped[int] = mapped_column(INTEGER, server_default=text("'0'"))
    rankValue: Mapped[Optional[float]] = mapped_column(Float)
    rankInformation: Mapped[Optional[str]] = mapped_column(String(1024))

    Screening_: Mapped["Screening"] = relationship(
        "Screening", back_populates="ScreeningRank"
    )
    ScreeningRankSet_: Mapped["ScreeningRankSet"] = relationship(
        "ScreeningRankSet", back_populates="ScreeningRank"
    )


class SpaceGroup(Base):
    __tablename__ = "SpaceGroup"
    __table_args__ = (
        ForeignKeyConstraint(
            ["geometryClassnameId"],
            ["GeometryClassname.geometryClassnameId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="SpaceGroup_ibfk_1",
        ),
        Index("SpaceGroup_FKShortName", "spaceGroupShortName"),
        Index("geometryClassnameId", "geometryClassnameId"),
    )

    spaceGroupId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key"
    )
    MX_used: Mapped[int] = mapped_column(
        TINYINT(1), server_default=text("'0'"), comment="1 if used in the crystal form"
    )
    spaceGroupNumber: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="ccp4 number pr IUCR"
    )
    spaceGroupShortName: Mapped[Optional[str]] = mapped_column(
        String(45), comment="short name without blank"
    )
    spaceGroupName: Mapped[Optional[str]] = mapped_column(
        String(45), comment="verbose name"
    )
    bravaisLattice: Mapped[Optional[str]] = mapped_column(
        String(45), comment="short name"
    )
    bravaisLatticeName: Mapped[Optional[str]] = mapped_column(
        String(45), comment="verbose name"
    )
    pointGroup: Mapped[Optional[str]] = mapped_column(String(45), comment="point group")
    geometryClassnameId: Mapped[Optional[int]] = mapped_column(INTEGER)

    GeometryClassname_: Mapped["GeometryClassname"] = relationship(
        "GeometryClassname", back_populates="SpaceGroup"
    )
    ModelBuilding: Mapped[List["ModelBuilding"]] = relationship(
        "ModelBuilding", back_populates="SpaceGroup_"
    )
    Phasing: Mapped[List["Phasing"]] = relationship(
        "Phasing", back_populates="SpaceGroup_"
    )
    PhasingStep: Mapped[List["PhasingStep"]] = relationship(
        "PhasingStep", back_populates="SpaceGroup_"
    )
    PreparePhasingData: Mapped[List["PreparePhasingData"]] = relationship(
        "PreparePhasingData", back_populates="SpaceGroup_"
    )
    SubstructureDetermination: Mapped[List["SubstructureDetermination"]] = relationship(
        "SubstructureDetermination", back_populates="SpaceGroup_"
    )


class Tomogram(Base):
    __tablename__ = "Tomogram"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcProgramId"],
            ["AutoProcProgram.autoProcProgramId"],
            ondelete="SET NULL",
            onupdate="CASCADE",
            name="Tomogram_fk_autoProcProgramId",
        ),
        ForeignKeyConstraint(
            ["dataCollectionId"],
            ["DataCollection.dataCollectionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Tomogram_fk_dataCollectionId",
        ),
        Index("Tomogram_fk_autoProcProgramId", "autoProcProgramId"),
        Index("Tomogram_fk_dataCollectionId", "dataCollectionId"),
        {
            "comment": "For storing per-sample, per-position data analysis results "
            "(reconstruction)"
        },
    )

    tomogramId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    dataCollectionId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="FK to\xa0DataCollection\xa0table"
    )
    autoProcProgramId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="FK, gives processing times/status and software information"
    )
    volumeFile: Mapped[Optional[str]] = mapped_column(
        String(255),
        comment=".mrc\xa0file representing the reconstructed tomogram volume",
    )
    stackFile: Mapped[Optional[str]] = mapped_column(
        String(255),
        comment=".mrc\xa0file containing the motion corrected images ordered by angle used as input for the reconstruction",
    )
    sizeX: Mapped[Optional[int]] = mapped_column(INTEGER, comment="unit: pixels")
    sizeY: Mapped[Optional[int]] = mapped_column(INTEGER, comment="unit: pixels")
    sizeZ: Mapped[Optional[int]] = mapped_column(INTEGER, comment="unit: pixels")
    pixelSpacing: Mapped[Optional[float]] = mapped_column(
        Float, comment="Angstrom/pixel conversion factor"
    )
    residualErrorMean: Mapped[Optional[float]] = mapped_column(
        Float, comment="Alignment error, unit: nm"
    )
    residualErrorSD: Mapped[Optional[float]] = mapped_column(
        Float, comment="Standard deviation of the alignment error, unit: nm"
    )
    xAxisCorrection: Mapped[Optional[float]] = mapped_column(
        Float, comment="X axis angle (etomo), unit: degrees"
    )
    tiltAngleOffset: Mapped[Optional[float]] = mapped_column(
        Float, comment="tilt Axis offset (etomo), unit: degrees"
    )
    zShift: Mapped[Optional[float]] = mapped_column(
        Float, comment="shift to center volumen in Z (etomo)"
    )
    fileDirectory: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Directory path for files referenced by this table"
    )
    centralSliceImage: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Tomogram central slice file"
    )
    tomogramMovie: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Movie traversing the tomogram across an axis"
    )
    xyShiftPlot: Mapped[Optional[str]] = mapped_column(
        String(255), comment="XY shift plot file"
    )
    projXY: Mapped[Optional[str]] = mapped_column(
        String(255), comment="XY projection file"
    )
    projXZ: Mapped[Optional[str]] = mapped_column(
        String(255), comment="XZ projection file"
    )
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Creation or last update date/time",
    )
    globalAlignmentQuality: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="Quality of fit metric for the alignment of the tilt series corresponding to this tomogram",
    )

    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="Tomogram"
    )
    DataCollection_: Mapped["DataCollection"] = relationship(
        "DataCollection", back_populates="Tomogram"
    )
    TiltImageAlignment: Mapped[List["TiltImageAlignment"]] = relationship(
        "TiltImageAlignment", back_populates="Tomogram_"
    )


class UserGroupHasLDAPSearchParameters(Base):
    __tablename__ = "UserGroup_has_LDAPSearchParameters"
    __table_args__ = (
        ForeignKeyConstraint(
            ["ldapSearchParametersId"],
            ["LDAPSearchParameters.ldapSearchParametersId"],
            name="UserGroup_has_LDAPSearchParameters_fk2",
        ),
        ForeignKeyConstraint(
            ["userGroupId"],
            ["UserGroup.userGroupId"],
            name="UserGroup_has_LDAPSearchParameters_fk1",
        ),
        Index("UserGroup_has_LDAPSearchParameters_fk2", "ldapSearchParametersId"),
        {
            "comment": "Gives the LDAP search parameters needed to find a set of "
            "usergroup members"
        },
    )

    userGroupId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    ldapSearchParametersId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(200, "utf8mb4_general_ci"),
        primary_key=True,
        comment="Name of the object we search for",
    )

    LDAPSearchParameters_: Mapped["LDAPSearchParameters"] = relationship(
        "LDAPSearchParameters", back_populates="UserGroup_has_LDAPSearchParameters"
    )
    UserGroup_: Mapped["UserGroup"] = relationship(
        "UserGroup", back_populates="UserGroup_has_LDAPSearchParameters"
    )


t_UserGroup_has_Permission = Table(
    "UserGroup_has_Permission",
    Base.metadata,
    Column("userGroupId", INTEGER, primary_key=True, nullable=False),
    Column("permissionId", INTEGER, primary_key=True, nullable=False),
    ForeignKeyConstraint(
        ["permissionId"],
        ["Permission.permissionId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="UserGroup_has_Permission_fk2",
    ),
    ForeignKeyConstraint(
        ["userGroupId"],
        ["UserGroup.userGroupId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="UserGroup_has_Permission_fk1",
    ),
    Index("UserGroup_has_Permission_fk2", "permissionId"),
)


class XRFFluorescenceMappingROI(Base):
    __tablename__ = "XRFFluorescenceMappingROI"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleId"],
            ["BLSample.blSampleId"],
            name="XRFFluorescenceMappingROI_FKblSampleId",
        ),
        Index("XRFFluorescenceMappingROI_FKblSampleId", "blSampleId"),
    )

    xrfFluorescenceMappingROIId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    startEnergy: Mapped[float] = mapped_column(Float)
    endEnergy: Mapped[float] = mapped_column(Float)
    element: Mapped[Optional[str]] = mapped_column(String(2))
    edge: Mapped[Optional[str]] = mapped_column(
        String(15),
        comment="Edge type i.e. Ka1, could be a custom edge in case of overlap Ka1-noCa",
    )
    r: Mapped[Optional[int]] = mapped_column(TINYINT, comment="R colour component")
    g: Mapped[Optional[int]] = mapped_column(TINYINT, comment="G colour component")
    b: Mapped[Optional[int]] = mapped_column(TINYINT, comment="B colour component")
    blSampleId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="ROIs can be created within the context of a sample"
    )
    scalar: Mapped[Optional[str]] = mapped_column(
        String(50),
        comment="For ROIs that are not an element, i.e. could be a scan counter instead",
    )

    BLSample_: Mapped["BLSample"] = relationship(
        "BLSample", back_populates="XRFFluorescenceMappingROI"
    )
    XRFFluorescenceMapping: Mapped[List["XRFFluorescenceMapping"]] = relationship(
        "XRFFluorescenceMapping", back_populates="XRFFluorescenceMappingROI_"
    )


class ZcZocaloBuffer(Base):
    __tablename__ = "zc_ZocaloBuffer"
    __table_args__ = (
        ForeignKeyConstraint(
            ["AutoProcProgramID"],
            ["AutoProcProgram.autoProcProgramId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="AutoProcProgram_fk_AutoProcProgramId",
        ),
    )

    AutoProcProgramID: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Reference to an existing AutoProcProgram"
    )
    UUID: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="AutoProcProgram-specific unique identifier"
    )
    Reference: Mapped[Optional[int]] = mapped_column(
        INTEGER,
        comment="Context-dependent reference to primary key IDs in other ISPyB tables",
    )

    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="zc_ZocaloBuffer"
    )


class AutoProcScalingStatistics(Base):
    __tablename__ = "AutoProcScalingStatistics"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcScalingId"],
            ["AutoProcScaling.autoProcScalingId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="_AutoProcScalingStatisticsFk1",
        ),
        Index("AutoProcScalingStatistics_FKindexType", "scalingStatisticsType"),
        Index(
            "AutoProcScalingStatistics_scalingId_statisticsType",
            "autoProcScalingId",
            "scalingStatisticsType",
        ),
    )

    autoProcScalingStatisticsId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    scalingStatisticsType: Mapped[str] = mapped_column(
        Enum("overall", "innerShell", "outerShell"),
        server_default=text("'overall'"),
        comment="Scaling statistics type",
    )
    autoProcScalingId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Related autoProcScaling item (used by foreign key)"
    )
    comments: Mapped[Optional[str]] = mapped_column(String(255), comment="Comments...")
    resolutionLimitLow: Mapped[Optional[float]] = mapped_column(
        Float, comment="Low resolution limit"
    )
    resolutionLimitHigh: Mapped[Optional[float]] = mapped_column(
        Float, comment="High resolution limit"
    )
    rMerge: Mapped[Optional[float]] = mapped_column(Float, comment="Rmerge")
    rMeasWithinIPlusIMinus: Mapped[Optional[float]] = mapped_column(
        Float, comment="Rmeas (within I+/I-)"
    )
    rMeasAllIPlusIMinus: Mapped[Optional[float]] = mapped_column(
        Float, comment="Rmeas (all I+ & I-)"
    )
    rPimWithinIPlusIMinus: Mapped[Optional[float]] = mapped_column(
        Float, comment="Rpim (within I+/I-) "
    )
    rPimAllIPlusIMinus: Mapped[Optional[float]] = mapped_column(
        Float, comment="Rpim (all I+ & I-)"
    )
    fractionalPartialBias: Mapped[Optional[float]] = mapped_column(
        Float, comment="Fractional partial bias"
    )
    nTotalObservations: Mapped[Optional[int]] = mapped_column(
        Integer, comment="Total number of observations"
    )
    nTotalUniqueObservations: Mapped[Optional[int]] = mapped_column(
        Integer, comment="Total number unique"
    )
    meanIOverSigI: Mapped[Optional[float]] = mapped_column(
        Float, comment="Mean((I)/sd(I))"
    )
    completeness: Mapped[Optional[float]] = mapped_column(Float, comment="Completeness")
    multiplicity: Mapped[Optional[float]] = mapped_column(Float, comment="Multiplicity")
    anomalousCompleteness: Mapped[Optional[float]] = mapped_column(
        Float, comment="Anomalous completeness"
    )
    anomalousMultiplicity: Mapped[Optional[float]] = mapped_column(
        Float, comment="Anomalous multiplicity"
    )
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Creation or last update date/time"
    )
    anomalous: Mapped[Optional[int]] = mapped_column(
        TINYINT(1),
        server_default=text("'0'"),
        comment="boolean type:0 noanoum - 1 anoum",
    )
    ccHalf: Mapped[Optional[float]] = mapped_column(
        Float, comment="information from XDS"
    )
    ccAnomalous: Mapped[Optional[float]] = mapped_column(Float)
    resIOverSigI2: Mapped[Optional[float]] = mapped_column(
        Float, comment="Resolution where I/Sigma(I) equals 2"
    )

    AutoProcScaling_: Mapped["AutoProcScaling"] = relationship(
        "AutoProcScaling", back_populates="AutoProcScalingStatistics"
    )


class AutoProcScalingHasInt(Base):
    __tablename__ = "AutoProcScaling_has_Int"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcIntegrationId"],
            ["AutoProcIntegration.autoProcIntegrationId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="AutoProcScaling_has_IntFk2",
        ),
        ForeignKeyConstraint(
            ["autoProcScalingId"],
            ["AutoProcScaling.autoProcScalingId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="AutoProcScaling_has_IntFk1",
        ),
        Index("AutoProcScal_has_IntIdx2", "autoProcIntegrationId"),
        Index(
            "AutoProcScalingHasInt_FKIndex3",
            "autoProcScalingId",
            "autoProcIntegrationId",
        ),
    )

    autoProcScaling_has_IntId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcIntegrationId: Mapped[int] = mapped_column(
        INTEGER, comment="AutoProcIntegration item"
    )
    autoProcScalingId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="AutoProcScaling item"
    )
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Creation or last update date/time"
    )

    AutoProcIntegration_: Mapped["AutoProcIntegration"] = relationship(
        "AutoProcIntegration", back_populates="AutoProcScaling_has_Int"
    )
    AutoProcScaling_: Mapped["AutoProcScaling"] = relationship(
        "AutoProcScaling", back_populates="AutoProcScaling_has_Int"
    )


class AutoProcStatus(Base):
    __tablename__ = "AutoProcStatus"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcIntegrationId"],
            ["AutoProcIntegration.autoProcIntegrationId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="AutoProcStatus_ibfk_1",
        ),
        Index("AutoProcStatus_FKIndex1", "autoProcIntegrationId"),
        {"comment": "AutoProcStatus table is linked to AutoProcIntegration"},
    )

    autoProcStatusId: Mapped[int] = mapped_column(
        Integer, primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcIntegrationId: Mapped[int] = mapped_column(INTEGER)
    step: Mapped[str] = mapped_column(
        Enum("Indexing", "Integration", "Correction", "Scaling", "Importing"),
        comment="autoprocessing step",
    )
    status: Mapped[str] = mapped_column(
        Enum("Launched", "Successful", "Failed"), comment="autoprocessing status"
    )
    bltimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    comments: Mapped[Optional[str]] = mapped_column(String(1024), comment="comments")

    AutoProcIntegration_: Mapped["AutoProcIntegration"] = relationship(
        "AutoProcIntegration", back_populates="AutoProcStatus"
    )


class BFComponentBeamline(Base):
    __tablename__ = "BF_component_beamline"
    __table_args__ = (
        ForeignKeyConstraint(
            ["componentId"],
            ["BF_component.componentId"],
            name="bf_component_beamline_FK1",
        ),
        Index("bf_component_beamline_FK1", "componentId"),
    )

    component_beamlineId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    componentId: Mapped[Optional[int]] = mapped_column(INTEGER)
    beamlinename: Mapped[Optional[str]] = mapped_column(String(20))

    BF_component: Mapped["BFComponent"] = relationship(
        "BFComponent", back_populates="BF_component_beamline"
    )


class BFSubcomponent(Base):
    __tablename__ = "BF_subcomponent"
    __table_args__ = (
        ForeignKeyConstraint(
            ["componentId"], ["BF_component.componentId"], name="bf_subcomponent_FK1"
        ),
        Index("bf_subcomponent_FK1", "componentId"),
    )

    subcomponentId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    componentId: Mapped[Optional[int]] = mapped_column(INTEGER)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(200))

    BF_component: Mapped["BFComponent"] = relationship(
        "BFComponent", back_populates="BF_subcomponent"
    )
    BF_subcomponent_beamline: Mapped[List["BFSubcomponentBeamline"]] = relationship(
        "BFSubcomponentBeamline", back_populates="BF_subcomponent"
    )
    BF_fault: Mapped[List["BFFault"]] = relationship(
        "BFFault", back_populates="BF_subcomponent"
    )


class BLSampleImageHasAutoScoreClass(Base):
    __tablename__ = "BLSampleImage_has_AutoScoreClass"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleImageAutoScoreClassId"],
            ["BLSampleImageAutoScoreClass.blSampleImageAutoScoreClassId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSampleImage_has_AutoScoreClass_fk2",
        ),
        ForeignKeyConstraint(
            ["blSampleImageId"],
            ["BLSampleImage.blSampleImageId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSampleImage_has_AutoScoreClass_fk1",
        ),
        Index("BLSampleImage_has_AutoScoreClass_fk2", "blSampleImageAutoScoreClassId"),
        {
            "comment": "Many-to-many relationship between drop images and thing being "
            "scored, as well as the actual probability (score) that the drop "
            "image contains that thing"
        },
    )

    blSampleImageId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    blSampleImageAutoScoreClassId: Mapped[int] = mapped_column(
        TINYINT, primary_key=True
    )
    probability: Mapped[Optional[float]] = mapped_column(Float)

    BLSampleImageAutoScoreClass_: Mapped["BLSampleImageAutoScoreClass"] = relationship(
        "BLSampleImageAutoScoreClass", back_populates="BLSampleImage_has_AutoScoreClass"
    )
    BLSampleImage_: Mapped["BLSampleImage"] = relationship(
        "BLSampleImage", back_populates="BLSampleImage_has_AutoScoreClass"
    )


class ContainerReport(Base):
    __tablename__ = "ContainerReport"
    __table_args__ = (
        ForeignKeyConstraint(
            ["containerRegistryId"],
            ["ContainerRegistry.containerRegistryId"],
            name="ContainerReport_ibfk1",
        ),
        ForeignKeyConstraint(
            ["personId"], ["Person.personId"], name="ContainerReport_ibfk2"
        ),
        Index("ContainerReport_ibfk1", "containerRegistryId"),
        Index("ContainerReport_ibfk2", "personId"),
    )

    containerReportId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    containerRegistryId: Mapped[Optional[int]] = mapped_column(INTEGER)
    personId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Person making report"
    )
    report: Mapped[Optional[str]] = mapped_column(Text)
    attachmentFilePath: Mapped[Optional[str]] = mapped_column(String(255))
    recordTimestamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    ContainerRegistry_: Mapped["ContainerRegistry"] = relationship(
        "ContainerRegistry", back_populates="ContainerReport"
    )
    Person_: Mapped["Person"] = relationship("Person", back_populates="ContainerReport")


class DataCollectionComment(Base):
    __tablename__ = "DataCollectionComment"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dataCollectionId"],
            ["DataCollection.dataCollectionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="dataCollectionComment_fk1",
        ),
        ForeignKeyConstraint(
            ["personId"],
            ["Person.personId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="dataCollectionComment_fk2",
        ),
        Index("dataCollectionComment_fk1", "dataCollectionId"),
        Index("dataCollectionComment_fk2", "personId"),
    )

    dataCollectionCommentId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    dataCollectionId: Mapped[int] = mapped_column(INTEGER)
    personId: Mapped[int] = mapped_column(INTEGER)
    createTime: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    comments: Mapped[Optional[str]] = mapped_column(String(4000))
    modTime: Mapped[Optional[datetime.date]] = mapped_column(Date)

    DataCollection_: Mapped["DataCollection"] = relationship(
        "DataCollection", back_populates="DataCollectionComment"
    )
    Person_: Mapped["Person"] = relationship(
        "Person", back_populates="DataCollectionComment"
    )


class MXMRRun(Base):
    __tablename__ = "MXMRRun"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcProgramId"],
            ["AutoProcProgram.autoProcProgramId"],
            name="mxMRRun_FK2",
        ),
        ForeignKeyConstraint(
            ["autoProcScalingId"],
            ["AutoProcScaling.autoProcScalingId"],
            name="mxMRRun_FK1",
        ),
        Index("mxMRRun_FK1", "autoProcScalingId"),
        Index("mxMRRun_FK2", "autoProcProgramId"),
    )

    mxMRRunId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    autoProcScalingId: Mapped[int] = mapped_column(INTEGER)
    rValueStart: Mapped[Optional[float]] = mapped_column(Float)
    rValueEnd: Mapped[Optional[float]] = mapped_column(Float)
    rFreeValueStart: Mapped[Optional[float]] = mapped_column(Float)
    rFreeValueEnd: Mapped[Optional[float]] = mapped_column(Float)
    LLG: Mapped[Optional[float]] = mapped_column(Float, comment="Log Likelihood Gain")
    TFZ: Mapped[Optional[float]] = mapped_column(
        Float, comment="Translation Function Z-score"
    )
    spaceGroup: Mapped[Optional[str]] = mapped_column(
        String(45), comment="Space group of the MR solution"
    )
    autoProcProgramId: Mapped[Optional[int]] = mapped_column(INTEGER)

    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="MXMRRun"
    )
    AutoProcScaling_: Mapped["AutoProcScaling"] = relationship(
        "AutoProcScaling", back_populates="MXMRRun"
    )
    MXMRRunBlob: Mapped[List["MXMRRunBlob"]] = relationship(
        "MXMRRunBlob", back_populates="MXMRRun_"
    )


class ModelBuilding(Base):
    __tablename__ = "ModelBuilding"
    __table_args__ = (
        ForeignKeyConstraint(
            ["phasingAnalysisId"],
            ["PhasingAnalysis.phasingAnalysisId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ModelBuilding_phasingAnalysisfk_1",
        ),
        ForeignKeyConstraint(
            ["phasingProgramRunId"],
            ["PhasingProgramRun.phasingProgramRunId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ModelBuilding_phasingProgramRunfk_1",
        ),
        ForeignKeyConstraint(
            ["spaceGroupId"],
            ["SpaceGroup.spaceGroupId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ModelBuilding_spaceGroupfk_1",
        ),
        Index("ModelBuilding_FKIndex1", "phasingAnalysisId"),
        Index("ModelBuilding_FKIndex2", "phasingProgramRunId"),
        Index("ModelBuilding_FKIndex3", "spaceGroupId"),
    )

    modelBuildingId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId: Mapped[int] = mapped_column(
        INTEGER, comment="Related phasing analysis item"
    )
    phasingProgramRunId: Mapped[int] = mapped_column(
        INTEGER, comment="Related program item"
    )
    spaceGroupId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Related spaceGroup"
    )
    lowRes: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    highRes: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Creation or last update date/time"
    )

    PhasingAnalysis_: Mapped["PhasingAnalysis"] = relationship(
        "PhasingAnalysis", back_populates="ModelBuilding"
    )
    PhasingProgramRun_: Mapped["PhasingProgramRun"] = relationship(
        "PhasingProgramRun", back_populates="ModelBuilding"
    )
    SpaceGroup_: Mapped["SpaceGroup"] = relationship(
        "SpaceGroup", back_populates="ModelBuilding"
    )


class MotionCorrection(Base):
    __tablename__ = "MotionCorrection"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcProgramId"],
            ["AutoProcProgram.autoProcProgramId"],
            name="MotionCorrection_ibfk2",
        ),
        ForeignKeyConstraint(
            ["dataCollectionId"],
            ["DataCollection.dataCollectionId"],
            name="_MotionCorrection_ibfk1",
        ),
        ForeignKeyConstraint(
            ["movieId"], ["Movie.movieId"], name="MotionCorrection_ibfk3"
        ),
        Index("MotionCorrection_ibfk2", "autoProcProgramId"),
        Index("MotionCorrection_ibfk3", "movieId"),
        Index("_MotionCorrection_ibfk1", "dataCollectionId"),
    )

    motionCorrectionId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    dataCollectionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    autoProcProgramId: Mapped[Optional[int]] = mapped_column(INTEGER)
    imageNumber: Mapped[Optional[int]] = mapped_column(
        SMALLINT, comment="Movie number, sequential in time 1-n"
    )
    firstFrame: Mapped[Optional[int]] = mapped_column(
        SMALLINT, comment="First frame of movie used"
    )
    lastFrame: Mapped[Optional[int]] = mapped_column(
        SMALLINT, comment="Last frame of movie used"
    )
    dosePerFrame: Mapped[Optional[float]] = mapped_column(
        Float, comment="Dose per frame, Units: e-/A^2"
    )
    doseWeight: Mapped[Optional[float]] = mapped_column(
        Float, comment="Dose weight, Units: dimensionless"
    )
    totalMotion: Mapped[Optional[float]] = mapped_column(
        Float, comment="Total motion, Units: A"
    )
    averageMotionPerFrame: Mapped[Optional[float]] = mapped_column(
        Float, comment="Average motion per frame, Units: A"
    )
    driftPlotFullPath: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Full path to the drift plot"
    )
    micrographFullPath: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Full path to the micrograph"
    )
    micrographSnapshotFullPath: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Full path to a snapshot (jpg) of the micrograph"
    )
    patchesUsedX: Mapped[Optional[int]] = mapped_column(
        MEDIUMINT, comment="Number of patches used in x (for motioncor2)"
    )
    patchesUsedY: Mapped[Optional[int]] = mapped_column(
        MEDIUMINT, comment="Number of patches used in y (for motioncor2)"
    )
    fftFullPath: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Full path to the jpg image of the raw micrograph FFT"
    )
    fftCorrectedFullPath: Mapped[Optional[str]] = mapped_column(
        String(255),
        comment="Full path to the jpg image of the drift corrected micrograph FFT",
    )
    comments: Mapped[Optional[str]] = mapped_column(String(255))
    movieId: Mapped[Optional[int]] = mapped_column(INTEGER)

    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="MotionCorrection"
    )
    DataCollection_: Mapped["DataCollection"] = relationship(
        "DataCollection", back_populates="MotionCorrection"
    )
    Movie_: Mapped["Movie"] = relationship("Movie", back_populates="MotionCorrection")
    CTF: Mapped[List["CTF"]] = relationship("CTF", back_populates="MotionCorrection_")
    ParticlePicker: Mapped[List["ParticlePicker"]] = relationship(
        "ParticlePicker", back_populates="MotionCorrection_"
    )
    RelativeIceThickness: Mapped[List["RelativeIceThickness"]] = relationship(
        "RelativeIceThickness", back_populates="MotionCorrection_"
    )


class PDBEntryHasAutoProcProgram(Base):
    __tablename__ = "PDBEntry_has_AutoProcProgram"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcProgramId"],
            ["AutoProcProgram.autoProcProgramId"],
            ondelete="CASCADE",
            name="pdbEntry_AutoProcProgram_FK2",
        ),
        ForeignKeyConstraint(
            ["pdbEntryId"],
            ["PDBEntry.pdbEntryId"],
            ondelete="CASCADE",
            name="pdbEntry_AutoProcProgram_FK1",
        ),
        Index("pdbEntry_AutoProcProgramIdx1", "pdbEntryId"),
        Index("pdbEntry_AutoProcProgramIdx2", "autoProcProgramId"),
    )

    pdbEntryHasAutoProcId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    pdbEntryId: Mapped[int] = mapped_column(INTEGER)
    autoProcProgramId: Mapped[int] = mapped_column(INTEGER)
    distance: Mapped[Optional[float]] = mapped_column(Float)

    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="PDBEntry_has_AutoProcProgram"
    )
    PDBEntry_: Mapped["PDBEntry"] = relationship(
        "PDBEntry", back_populates="PDBEntry_has_AutoProcProgram"
    )


class Phasing(Base):
    __tablename__ = "Phasing"
    __table_args__ = (
        ForeignKeyConstraint(
            ["phasingAnalysisId"],
            ["PhasingAnalysis.phasingAnalysisId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Phasing_phasingAnalysisfk_1",
        ),
        ForeignKeyConstraint(
            ["phasingProgramRunId"],
            ["PhasingProgramRun.phasingProgramRunId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Phasing_phasingProgramRunfk_1",
        ),
        ForeignKeyConstraint(
            ["spaceGroupId"],
            ["SpaceGroup.spaceGroupId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Phasing_spaceGroupfk_1",
        ),
        Index("Phasing_FKIndex1", "phasingAnalysisId"),
        Index("Phasing_FKIndex2", "phasingProgramRunId"),
        Index("Phasing_FKIndex3", "spaceGroupId"),
    )

    phasingId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId: Mapped[int] = mapped_column(
        INTEGER, comment="Related phasing analysis item"
    )
    phasingProgramRunId: Mapped[int] = mapped_column(
        INTEGER, comment="Related program item"
    )
    spaceGroupId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Related spaceGroup"
    )
    method: Mapped[Optional[str]] = mapped_column(
        Enum("solvent flattening", "solvent flipping", "e", "SAD", "shelxe"),
        comment="phasing method",
    )
    solventContent: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    enantiomorph: Mapped[Optional[int]] = mapped_column(TINYINT(1), comment="0 or 1")
    lowRes: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    highRes: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    PhasingAnalysis_: Mapped["PhasingAnalysis"] = relationship(
        "PhasingAnalysis", back_populates="Phasing"
    )
    PhasingProgramRun_: Mapped["PhasingProgramRun"] = relationship(
        "PhasingProgramRun", back_populates="Phasing"
    )
    SpaceGroup_: Mapped["SpaceGroup"] = relationship(
        "SpaceGroup", back_populates="Phasing"
    )


class PhasingStep(Base):
    __tablename__ = "PhasingStep"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcScalingId"],
            ["AutoProcScaling.autoProcScalingId"],
            name="FK_autoprocScaling",
        ),
        ForeignKeyConstraint(
            ["programRunId"],
            ["PhasingProgramRun.phasingProgramRunId"],
            name="FK_program",
        ),
        ForeignKeyConstraint(
            ["spaceGroupId"], ["SpaceGroup.spaceGroupId"], name="FK_spacegroup"
        ),
        Index("FK_autoprocScaling_id", "autoProcScalingId"),
        Index("FK_phasingAnalysis_id", "phasingAnalysisId"),
        Index("FK_programRun_id", "programRunId"),
        Index("FK_spacegroup_id", "spaceGroupId"),
    )

    phasingStepId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    previousPhasingStepId: Mapped[Optional[int]] = mapped_column(INTEGER)
    programRunId: Mapped[Optional[int]] = mapped_column(INTEGER)
    spaceGroupId: Mapped[Optional[int]] = mapped_column(INTEGER)
    autoProcScalingId: Mapped[Optional[int]] = mapped_column(INTEGER)
    phasingAnalysisId: Mapped[Optional[int]] = mapped_column(INTEGER)
    phasingStepType: Mapped[Optional[str]] = mapped_column(
        Enum("PREPARE", "SUBSTRUCTUREDETERMINATION", "PHASING", "MODELBUILDING")
    )
    method: Mapped[Optional[str]] = mapped_column(String(45))
    solventContent: Mapped[Optional[str]] = mapped_column(String(45))
    enantiomorph: Mapped[Optional[str]] = mapped_column(String(45))
    lowRes: Mapped[Optional[str]] = mapped_column(String(45))
    highRes: Mapped[Optional[str]] = mapped_column(String(45))

    AutoProcScaling_: Mapped["AutoProcScaling"] = relationship(
        "AutoProcScaling", back_populates="PhasingStep"
    )
    PhasingProgramRun_: Mapped["PhasingProgramRun"] = relationship(
        "PhasingProgramRun", back_populates="PhasingStep"
    )
    SpaceGroup_: Mapped["SpaceGroup"] = relationship(
        "SpaceGroup", back_populates="PhasingStep"
    )
    PhasingStatistics: Mapped[List["PhasingStatistics"]] = relationship(
        "PhasingStatistics", back_populates="PhasingStep_"
    )


class PhasingHasScaling(Base):
    __tablename__ = "Phasing_has_Scaling"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcScalingId"],
            ["AutoProcScaling.autoProcScalingId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="PhasingHasScaling_autoProcScalingfk_1",
        ),
        ForeignKeyConstraint(
            ["phasingAnalysisId"],
            ["PhasingAnalysis.phasingAnalysisId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="PhasingHasScaling_phasingAnalysisfk_1",
        ),
        Index("PhasingHasScaling_FKIndex1", "phasingAnalysisId"),
        Index("PhasingHasScaling_FKIndex2", "autoProcScalingId"),
    )

    phasingHasScalingId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId: Mapped[int] = mapped_column(
        INTEGER, comment="Related phasing analysis item"
    )
    autoProcScalingId: Mapped[int] = mapped_column(
        INTEGER, comment="Related autoProcScaling item"
    )
    datasetNumber: Mapped[Optional[int]] = mapped_column(
        Integer,
        comment="serial number of the dataset and always reserve 0 for the reference",
    )
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    AutoProcScaling_: Mapped["AutoProcScaling"] = relationship(
        "AutoProcScaling", back_populates="Phasing_has_Scaling"
    )
    PhasingAnalysis_: Mapped["PhasingAnalysis"] = relationship(
        "PhasingAnalysis", back_populates="Phasing_has_Scaling"
    )
    PhasingStatistics: Mapped[List["PhasingStatistics"]] = relationship(
        "PhasingStatistics",
        foreign_keys="[PhasingStatistics.phasingHasScalingId1]",
        back_populates="Phasing_has_Scaling",
    )
    PhasingStatistics_: Mapped[List["PhasingStatistics"]] = relationship(
        "PhasingStatistics",
        foreign_keys="[PhasingStatistics.phasingHasScalingId2]",
        back_populates="Phasing_has_Scaling_",
    )


class PreparePhasingData(Base):
    __tablename__ = "PreparePhasingData"
    __table_args__ = (
        ForeignKeyConstraint(
            ["phasingAnalysisId"],
            ["PhasingAnalysis.phasingAnalysisId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="PreparePhasingData_phasingAnalysisfk_1",
        ),
        ForeignKeyConstraint(
            ["phasingProgramRunId"],
            ["PhasingProgramRun.phasingProgramRunId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="PreparePhasingData_phasingProgramRunfk_1",
        ),
        ForeignKeyConstraint(
            ["spaceGroupId"],
            ["SpaceGroup.spaceGroupId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="PreparePhasingData_spaceGroupfk_1",
        ),
        Index("PreparePhasingData_FKIndex1", "phasingAnalysisId"),
        Index("PreparePhasingData_FKIndex2", "phasingProgramRunId"),
        Index("PreparePhasingData_FKIndex3", "spaceGroupId"),
    )

    preparePhasingDataId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId: Mapped[int] = mapped_column(
        INTEGER, comment="Related phasing analysis item"
    )
    phasingProgramRunId: Mapped[int] = mapped_column(
        INTEGER, comment="Related program item"
    )
    spaceGroupId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Related spaceGroup"
    )
    lowRes: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    highRes: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Creation or last update date/time"
    )

    PhasingAnalysis_: Mapped["PhasingAnalysis"] = relationship(
        "PhasingAnalysis", back_populates="PreparePhasingData"
    )
    PhasingProgramRun_: Mapped["PhasingProgramRun"] = relationship(
        "PhasingProgramRun", back_populates="PreparePhasingData"
    )
    SpaceGroup_: Mapped["SpaceGroup"] = relationship(
        "SpaceGroup", back_populates="PreparePhasingData"
    )


class Project(Base):
    __tablename__ = "Project"
    __table_args__ = (
        ForeignKeyConstraint(["personId"], ["Person.personId"], name="Project_FK1"),
        Index("Project_FK1", "personId"),
    )

    projectId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    personId: Mapped[Optional[int]] = mapped_column(INTEGER)
    title: Mapped[Optional[str]] = mapped_column(String(200))
    acronym: Mapped[Optional[str]] = mapped_column(String(100))
    owner: Mapped[Optional[str]] = mapped_column(String(50))

    BLSample_: Mapped[List["BLSample"]] = relationship(
        "BLSample", secondary="Project_has_BLSample", back_populates="Project"
    )
    Person_: Mapped[List["Person"]] = relationship(
        "Person", secondary="Project_has_Person", back_populates="Project"
    )
    Person1: Mapped["Person"] = relationship("Person", back_populates="Project_")
    Protein: Mapped[List["Protein"]] = relationship(
        "Protein", secondary="Project_has_Protein", back_populates="Project_"
    )
    BLSession: Mapped[List["BLSession"]] = relationship(
        "BLSession", secondary="Project_has_Session", back_populates="Project_"
    )
    Shipping: Mapped[List["Shipping"]] = relationship(
        "Shipping", secondary="Project_has_Shipping", back_populates="Project_"
    )
    XFEFluorescenceSpectrum: Mapped[List["XFEFluorescenceSpectrum"]] = relationship(
        "XFEFluorescenceSpectrum",
        secondary="Project_has_XFEFSpectrum",
        back_populates="Project_",
    )
    Project_has_User: Mapped[List["ProjectHasUser"]] = relationship(
        "ProjectHasUser", back_populates="Project_"
    )
    DataCollectionGroup: Mapped[List["DataCollectionGroup"]] = relationship(
        "DataCollectionGroup",
        secondary="Project_has_DCGroup",
        back_populates="Project_",
    )
    EnergyScan: Mapped[List["EnergyScan"]] = relationship(
        "EnergyScan", secondary="Project_has_EnergyScan", back_populates="Project_"
    )


class Proposal(Base):
    __tablename__ = "Proposal"
    __table_args__ = (
        ForeignKeyConstraint(
            ["personId"],
            ["Person.personId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Proposal_ibfk_1",
        ),
        Index("Proposal_FKIndex1", "personId"),
        Index(
            "Proposal_FKIndexCodeNumber", "proposalCode", "proposalNumber", unique=True
        ),
    )

    proposalId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    personId: Mapped[int] = mapped_column(INTEGER, server_default=text("'0'"))
    bltimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    title: Mapped[Optional[str]] = mapped_column(String(200))
    proposalCode: Mapped[Optional[str]] = mapped_column(String(45))
    proposalNumber: Mapped[Optional[str]] = mapped_column(String(45))
    proposalType: Mapped[Optional[str]] = mapped_column(
        String(2), comment="Proposal type: MX, BX"
    )
    externalId: Mapped[Optional[bytes]] = mapped_column(BINARY(16))
    state: Mapped[Optional[str]] = mapped_column(
        Enum("Open", "Closed", "Cancelled"), server_default=text("'Open'")
    )

    Person_: Mapped["Person"] = relationship("Person", back_populates="Proposal")
    BLSampleGroup: Mapped[List["BLSampleGroup"]] = relationship(
        "BLSampleGroup", back_populates="Proposal_"
    )
    BLSession: Mapped[List["BLSession"]] = relationship(
        "BLSession", back_populates="Proposal_"
    )
    Component: Mapped[List["Component"]] = relationship(
        "Component", back_populates="Proposal_"
    )
    ContainerRegistry_has_Proposal: Mapped[
        List["ContainerRegistryHasProposal"]
    ] = relationship("ContainerRegistryHasProposal", back_populates="Proposal_")
    DiffractionPlan: Mapped[List["DiffractionPlan"]] = relationship(
        "DiffractionPlan", back_populates="Proposal_"
    )
    LabContact: Mapped[List["LabContact"]] = relationship(
        "LabContact", back_populates="Proposal_"
    )
    ProposalHasPerson: Mapped[List["ProposalHasPerson"]] = relationship(
        "ProposalHasPerson", back_populates="Proposal_"
    )
    Protein: Mapped[List["Protein"]] = relationship(
        "Protein", back_populates="Proposal_"
    )
    SW_onceToken: Mapped[List["SWOnceToken"]] = relationship(
        "SWOnceToken", back_populates="Proposal_"
    )
    Screen: Mapped[List["Screen"]] = relationship("Screen", back_populates="Proposal_")
    DewarRegistry: Mapped[List["DewarRegistry"]] = relationship(
        "DewarRegistry", back_populates="Proposal_"
    )
    Shipping: Mapped[List["Shipping"]] = relationship(
        "Shipping", back_populates="Proposal_"
    )
    CourierTermsAccepted: Mapped[List["CourierTermsAccepted"]] = relationship(
        "CourierTermsAccepted", back_populates="Proposal_"
    )
    DewarRegistry_has_Proposal: Mapped[List["DewarRegistryHasProposal"]] = relationship(
        "DewarRegistryHasProposal", back_populates="Proposal_"
    )


class SubstructureDetermination(Base):
    __tablename__ = "SubstructureDetermination"
    __table_args__ = (
        ForeignKeyConstraint(
            ["phasingAnalysisId"],
            ["PhasingAnalysis.phasingAnalysisId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="SubstructureDetermination_phasingAnalysisfk_1",
        ),
        ForeignKeyConstraint(
            ["phasingProgramRunId"],
            ["PhasingProgramRun.phasingProgramRunId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="SubstructureDetermination_phasingProgramRunfk_1",
        ),
        ForeignKeyConstraint(
            ["spaceGroupId"],
            ["SpaceGroup.spaceGroupId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="SubstructureDetermination_spaceGroupfk_1",
        ),
        Index("SubstructureDetermination_FKIndex1", "phasingAnalysisId"),
        Index("SubstructureDetermination_FKIndex2", "phasingProgramRunId"),
        Index("SubstructureDetermination_FKIndex3", "spaceGroupId"),
    )

    substructureDeterminationId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId: Mapped[int] = mapped_column(
        INTEGER, comment="Related phasing analysis item"
    )
    phasingProgramRunId: Mapped[int] = mapped_column(
        INTEGER, comment="Related program item"
    )
    spaceGroupId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Related spaceGroup"
    )
    method: Mapped[Optional[str]] = mapped_column(
        Enum("SAD", "MAD", "SIR", "SIRAS", "MR", "MIR", "MIRAS", "RIP", "RIPAS"),
        comment="phasing method",
    )
    lowRes: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    highRes: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Creation or last update date/time"
    )

    PhasingAnalysis_: Mapped["PhasingAnalysis"] = relationship(
        "PhasingAnalysis", back_populates="SubstructureDetermination"
    )
    PhasingProgramRun_: Mapped["PhasingProgramRun"] = relationship(
        "PhasingProgramRun", back_populates="SubstructureDetermination"
    )
    SpaceGroup_: Mapped["SpaceGroup"] = relationship(
        "SpaceGroup", back_populates="SubstructureDetermination"
    )


class TiltImageAlignment(Base):
    __tablename__ = "TiltImageAlignment"
    __table_args__ = (
        ForeignKeyConstraint(
            ["movieId"],
            ["Movie.movieId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="TiltImageAlignment_fk_movieId",
        ),
        ForeignKeyConstraint(
            ["tomogramId"],
            ["Tomogram.tomogramId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="TiltImageAlignment_fk_tomogramId",
        ),
        Index("TiltImageAlignment_fk_tomogramId", "tomogramId"),
        {"comment": "For storing per-movie analysis results (reconstruction)"},
    )

    movieId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="FK to\xa0Movie\xa0table"
    )
    tomogramId: Mapped[int] = mapped_column(
        INTEGER,
        primary_key=True,
        comment="FK to\xa0Tomogram\xa0table; tuple (movieID, tomogramID) is unique",
    )
    defocusU: Mapped[Optional[float]] = mapped_column(Float, comment="unit: Angstroms")
    defocusV: Mapped[Optional[float]] = mapped_column(Float, comment="unit: Angstroms")
    psdFile: Mapped[Optional[str]] = mapped_column(String(255))
    resolution: Mapped[Optional[float]] = mapped_column(
        Float, comment="unit: Angstroms"
    )
    fitQuality: Mapped[Optional[float]] = mapped_column(Float)
    refinedMagnification: Mapped[Optional[float]] = mapped_column(
        Float, comment="unitless"
    )
    refinedTiltAngle: Mapped[Optional[float]] = mapped_column(
        Float, comment="units: degrees"
    )
    refinedTiltAxis: Mapped[Optional[float]] = mapped_column(
        Float, comment="units: degrees"
    )
    residualError: Mapped[Optional[float]] = mapped_column(
        Float, comment="Residual error, unit: nm"
    )

    Movie_: Mapped["Movie"] = relationship("Movie", back_populates="TiltImageAlignment")
    Tomogram_: Mapped["Tomogram"] = relationship(
        "Tomogram", back_populates="TiltImageAlignment"
    )


t_UserGroup_has_Person = Table(
    "UserGroup_has_Person",
    Base.metadata,
    Column("userGroupId", INTEGER, primary_key=True, nullable=False),
    Column("personId", INTEGER, primary_key=True, nullable=False),
    ForeignKeyConstraint(
        ["personId"],
        ["Person.personId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="userGroup_has_Person_fk2",
    ),
    ForeignKeyConstraint(
        ["userGroupId"],
        ["UserGroup.userGroupId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="userGroup_has_Person_fk1",
    ),
    Index("userGroup_has_Person_fk2", "personId"),
)


class BFSubcomponentBeamline(Base):
    __tablename__ = "BF_subcomponent_beamline"
    __table_args__ = (
        ForeignKeyConstraint(
            ["subcomponentId"],
            ["BF_subcomponent.subcomponentId"],
            name="bf_subcomponent_beamline_FK1",
        ),
        Index("bf_subcomponent_beamline_FK1", "subcomponentId"),
    )

    subcomponent_beamlineId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    subcomponentId: Mapped[Optional[int]] = mapped_column(INTEGER)
    beamlinename: Mapped[Optional[str]] = mapped_column(String(20))

    BF_subcomponent: Mapped["BFSubcomponent"] = relationship(
        "BFSubcomponent", back_populates="BF_subcomponent_beamline"
    )


class BLSampleGroup(Base):
    __tablename__ = "BLSampleGroup"
    __table_args__ = (
        ForeignKeyConstraint(
            ["proposalId"],
            ["Proposal.proposalId"],
            ondelete="SET NULL",
            onupdate="CASCADE",
            name="BLSampleGroup_fk_proposalId",
        ),
        Index("BLSampleGroup_fk_proposalId", "proposalId"),
    )

    blSampleGroupId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(
        String(100), comment="Human-readable name"
    )
    proposalId: Mapped[Optional[int]] = mapped_column(INTEGER)

    Proposal_: Mapped["Proposal"] = relationship(
        "Proposal", back_populates="BLSampleGroup"
    )
    BLSampleGroup_has_BLSample: Mapped[List["BLSampleGroupHasBLSample"]] = relationship(
        "BLSampleGroupHasBLSample", back_populates="BLSampleGroup_"
    )


class BLSession(Base):
    __tablename__ = "BLSession"
    __table_args__ = (
        ForeignKeyConstraint(
            ["beamCalendarId"],
            ["BeamCalendar.beamCalendarId"],
            ondelete="SET NULL",
            onupdate="CASCADE",
            name="BLSession_fk_beamCalendarId",
        ),
        ForeignKeyConstraint(
            ["beamLineSetupId"],
            ["BeamLineSetup.beamLineSetupId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSession_ibfk_2",
        ),
        ForeignKeyConstraint(
            ["proposalId"],
            ["Proposal.proposalId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSession_ibfk_1",
        ),
        Index("BLSession_fk_beamCalendarId", "beamCalendarId"),
        Index("Session_FKIndex2", "beamLineSetupId"),
        Index("Session_FKIndexBeamLineName", "beamLineName"),
        Index("Session_FKIndexEndDate", "endDate"),
        Index("Session_FKIndexStartDate", "startDate"),
        Index("proposalId", "proposalId", "visit_number", unique=True),
    )

    sessionId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    proposalId: Mapped[int] = mapped_column(INTEGER, server_default=text("'0'"))
    bltimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    lastUpdate: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="last update timestamp: by default the end of the session, the last collect...",
    )
    beamLineSetupId: Mapped[Optional[int]] = mapped_column(INTEGER)
    beamCalendarId: Mapped[Optional[int]] = mapped_column(INTEGER)
    startDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    endDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    beamLineName: Mapped[Optional[str]] = mapped_column(String(45))
    scheduled: Mapped[Optional[int]] = mapped_column(TINYINT(1))
    nbShifts: Mapped[Optional[int]] = mapped_column(INTEGER)
    comments: Mapped[Optional[str]] = mapped_column(String(2000))
    beamLineOperator: Mapped[Optional[str]] = mapped_column(String(255))
    visit_number: Mapped[Optional[int]] = mapped_column(
        INTEGER, server_default=text("'0'")
    )
    usedFlag: Mapped[Optional[int]] = mapped_column(
        TINYINT(1),
        comment="indicates if session has Datacollections or XFE or EnergyScans attached",
    )
    externalId: Mapped[Optional[bytes]] = mapped_column(BINARY(16))
    archived: Mapped[Optional[int]] = mapped_column(
        TINYINT(1),
        server_default=text("'0'"),
        comment="The data for the session is archived and no longer available on disk",
    )
    riskRating: Mapped[Optional[str]] = mapped_column(
        Enum("Low", "Medium", "High", "Not Permitted"),
        comment="ERA in user admin system",
    )

    Project_: Mapped[List["Project"]] = relationship(
        "Project", secondary="Project_has_Session", back_populates="BLSession"
    )
    BeamCalendar_: Mapped["BeamCalendar"] = relationship(
        "BeamCalendar", back_populates="BLSession"
    )
    BeamLineSetup_: Mapped["BeamLineSetup"] = relationship(
        "BeamLineSetup", back_populates="BLSession"
    )
    Proposal_: Mapped["Proposal"] = relationship("Proposal", back_populates="BLSession")
    Shipping: Mapped[List["Shipping"]] = relationship(
        "Shipping", secondary="ShippingHasSession", back_populates="BLSession_"
    )
    BF_fault: Mapped[List["BFFault"]] = relationship(
        "BFFault", back_populates="BLSession_"
    )
    BLSession_has_SCPosition: Mapped[List["BLSessionHasSCPosition"]] = relationship(
        "BLSessionHasSCPosition", back_populates="BLSession_"
    )
    BeamlineAction: Mapped[List["BeamlineAction"]] = relationship(
        "BeamlineAction", back_populates="BLSession_"
    )
    DataCollectionGroup: Mapped[List["DataCollectionGroup"]] = relationship(
        "DataCollectionGroup", back_populates="BLSession_"
    )
    EnergyScan: Mapped[List["EnergyScan"]] = relationship(
        "EnergyScan", back_populates="BLSession_"
    )
    RobotAction: Mapped[List["RobotAction"]] = relationship(
        "RobotAction", back_populates="BLSession_"
    )
    SessionType: Mapped[List["SessionType"]] = relationship(
        "SessionType", back_populates="BLSession_"
    )
    Session_has_Person: Mapped[List["SessionHasPerson"]] = relationship(
        "SessionHasPerson", back_populates="BLSession_"
    )
    XFEFluorescenceSpectrum: Mapped[List["XFEFluorescenceSpectrum"]] = relationship(
        "XFEFluorescenceSpectrum", back_populates="BLSession_"
    )
    Dewar: Mapped[List["Dewar"]] = relationship("Dewar", back_populates="BLSession_")
    Container: Mapped[List["Container"]] = relationship(
        "Container", back_populates="BLSession_"
    )


class CTF(Base):
    __tablename__ = "CTF"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcProgramId"],
            ["AutoProcProgram.autoProcProgramId"],
            name="CTF_ibfk2",
        ),
        ForeignKeyConstraint(
            ["motionCorrectionId"],
            ["MotionCorrection.motionCorrectionId"],
            name="CTF_ibfk1",
        ),
        Index("CTF_ibfk1", "motionCorrectionId"),
        Index("CTF_ibfk2", "autoProcProgramId"),
    )

    ctfId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    motionCorrectionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    autoProcProgramId: Mapped[Optional[int]] = mapped_column(INTEGER)
    boxSizeX: Mapped[Optional[float]] = mapped_column(
        Float, comment="Box size in x, Units: pixels"
    )
    boxSizeY: Mapped[Optional[float]] = mapped_column(
        Float, comment="Box size in y, Units: pixels"
    )
    minResolution: Mapped[Optional[float]] = mapped_column(
        Float, comment="Minimum resolution for CTF, Units: A"
    )
    maxResolution: Mapped[Optional[float]] = mapped_column(Float, comment="Units: A")
    minDefocus: Mapped[Optional[float]] = mapped_column(Float, comment="Units: A")
    maxDefocus: Mapped[Optional[float]] = mapped_column(Float, comment="Units: A")
    defocusStepSize: Mapped[Optional[float]] = mapped_column(Float, comment="Units: A")
    astigmatism: Mapped[Optional[float]] = mapped_column(Float, comment="Units: A")
    astigmatismAngle: Mapped[Optional[float]] = mapped_column(
        Float, comment="Units: deg?"
    )
    estimatedResolution: Mapped[Optional[float]] = mapped_column(
        Float, comment="Units: A"
    )
    estimatedDefocus: Mapped[Optional[float]] = mapped_column(Float, comment="Units: A")
    amplitudeContrast: Mapped[Optional[float]] = mapped_column(
        Float, comment="Units: %?"
    )
    ccValue: Mapped[Optional[float]] = mapped_column(Float, comment="Correlation value")
    fftTheoreticalFullPath: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Full path to the jpg image of the simulated FFT"
    )
    comments: Mapped[Optional[str]] = mapped_column(String(255))

    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="CTF"
    )
    MotionCorrection_: Mapped["MotionCorrection"] = relationship(
        "MotionCorrection", back_populates="CTF"
    )


class Component(Base):
    __tablename__ = "Component"
    __table_args__ = (
        ForeignKeyConstraint(
            ["componentTypeId"],
            ["ComponentType.componentTypeId"],
            name="Component_ibfk_1",
        ),
        ForeignKeyConstraint(
            ["proposalId"],
            ["Proposal.proposalId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Component_ibfk_2",
        ),
        Index("componentTypeId", "componentTypeId"),
        Index("proposalId", "proposalId"),
        {
            "comment": "Description of a component that can be used inside a crystal or a "
            "sample."
        },
    )

    componentId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    componentTypeId: Mapped[int] = mapped_column(INTEGER)
    name: Mapped[str] = mapped_column(String(255, "utf8mb4_general_ci"))
    proposalId: Mapped[Optional[int]] = mapped_column(INTEGER)
    composition: Mapped[Optional[str]] = mapped_column(
        String(255, "utf8mb4_general_ci")
    )

    ComponentType_: Mapped["ComponentType"] = relationship(
        "ComponentType", back_populates="Component"
    )
    Proposal_: Mapped["Proposal"] = relationship("Proposal", back_populates="Component")
    Event: Mapped[List["Event"]] = relationship("Event", back_populates="Component_")
    SampleComposition: Mapped[List["SampleComposition"]] = relationship(
        "SampleComposition", back_populates="Component_"
    )
    CrystalComposition: Mapped[List["CrystalComposition"]] = relationship(
        "CrystalComposition", back_populates="Component_"
    )


class ContainerRegistryHasProposal(Base):
    __tablename__ = "ContainerRegistry_has_Proposal"
    __table_args__ = (
        ForeignKeyConstraint(
            ["containerRegistryId"],
            ["ContainerRegistry.containerRegistryId"],
            name="ContainerRegistry_has_Proposal_ibfk1",
        ),
        ForeignKeyConstraint(
            ["personId"],
            ["Person.personId"],
            name="ContainerRegistry_has_Proposal_ibfk3",
        ),
        ForeignKeyConstraint(
            ["proposalId"],
            ["Proposal.proposalId"],
            name="ContainerRegistry_has_Proposal_ibfk2",
        ),
        Index("ContainerRegistry_has_Proposal_ibfk2", "proposalId"),
        Index("ContainerRegistry_has_Proposal_ibfk3", "personId"),
        Index("containerRegistryId", "containerRegistryId", "proposalId", unique=True),
    )

    containerRegistryHasProposalId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True
    )
    containerRegistryId: Mapped[Optional[int]] = mapped_column(INTEGER)
    proposalId: Mapped[Optional[int]] = mapped_column(INTEGER)
    personId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Person registering the container"
    )
    recordTimestamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    ContainerRegistry_: Mapped["ContainerRegistry"] = relationship(
        "ContainerRegistry", back_populates="ContainerRegistry_has_Proposal"
    )
    Person_: Mapped["Person"] = relationship(
        "Person", back_populates="ContainerRegistry_has_Proposal"
    )
    Proposal_: Mapped["Proposal"] = relationship(
        "Proposal", back_populates="ContainerRegistry_has_Proposal"
    )


class DiffractionPlan(Base):
    __tablename__ = "DiffractionPlan"
    __table_args__ = (
        CheckConstraint("json_valid(`scanParameters`)", name="DiffractionPlan_chk_2"),
        CheckConstraint("json_valid(`strategyOption`)", name="DiffractionPlan_chk_1"),
        ForeignKeyConstraint(
            ["detectorId"],
            ["Detector.detectorId"],
            onupdate="CASCADE",
            name="DataCollectionPlan_ibfk3",
        ),
        ForeignKeyConstraint(
            ["experimentTypeId"],
            ["ExperimentType.experimentTypeId"],
            name="DiffractionPlan_ibfk3",
        ),
        ForeignKeyConstraint(
            ["presetForProposalId"],
            ["Proposal.proposalId"],
            name="DiffractionPlan_ibfk1",
        ),
        ForeignKeyConstraint(
            ["purificationColumnId"],
            ["PurificationColumn.purificationColumnId"],
            name="DiffractionPlan_ibfk2",
        ),
        Index("DataCollectionPlan_ibfk3", "detectorId"),
        Index("DiffractionPlan_ibfk1", "presetForProposalId"),
        Index("DiffractionPlan_ibfk2", "purificationColumnId"),
        Index("DiffractionPlan_ibfk3", "experimentTypeId"),
    )

    diffractionPlanId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Creation or last update date/time",
    )
    name: Mapped[Optional[str]] = mapped_column(String(20))
    experimentKind: Mapped[Optional[str]] = mapped_column(
        Enum(
            "Default",
            "MXPressE",
            "MXPressO",
            "MXPressE_SAD",
            "MXScore",
            "MXPressM",
            "MAD",
            "SAD",
            "Fixed",
            "Ligand binding",
            "Refinement",
            "OSC",
            "MAD - Inverse Beam",
            "SAD - Inverse Beam",
            "MESH",
            "XFE",
            "Stepped transmission",
            "XChem High Symmetry",
            "XChem Low Symmetry",
            "Commissioning",
        )
    )
    observedResolution: Mapped[Optional[float]] = mapped_column(Float)
    minimalResolution: Mapped[Optional[float]] = mapped_column(Float)
    exposureTime: Mapped[Optional[float]] = mapped_column(Float)
    oscillationRange: Mapped[Optional[float]] = mapped_column(Float)
    maximalResolution: Mapped[Optional[float]] = mapped_column(Float)
    screeningResolution: Mapped[Optional[float]] = mapped_column(Float)
    radiationSensitivity: Mapped[Optional[float]] = mapped_column(Float)
    anomalousScatterer: Mapped[Optional[str]] = mapped_column(String(255))
    preferredBeamSizeX: Mapped[Optional[float]] = mapped_column(Float)
    preferredBeamSizeY: Mapped[Optional[float]] = mapped_column(Float)
    preferredBeamDiameter: Mapped[Optional[float]] = mapped_column(Float)
    comments: Mapped[Optional[str]] = mapped_column(String(1024))
    DIFFRACTIONPLANUUID: Mapped[Optional[str]] = mapped_column(String(1000))
    aimedCompleteness: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    aimedIOverSigmaAtHighestRes: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    aimedMultiplicity: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    aimedResolution: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    anomalousData: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), server_default=text("'0'")
    )
    complexity: Mapped[Optional[str]] = mapped_column(String(45))
    estimateRadiationDamage: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), server_default=text("'0'")
    )
    forcedSpaceGroup: Mapped[Optional[str]] = mapped_column(String(45))
    requiredCompleteness: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    requiredMultiplicity: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    requiredResolution: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    strategyOption: Mapped[Optional[str]] = mapped_column(VARCHAR(200))
    kappaStrategyOption: Mapped[Optional[str]] = mapped_column(String(45))
    numberOfPositions: Mapped[Optional[int]] = mapped_column(Integer)
    minDimAccrossSpindleAxis: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="minimum dimension accross the spindle axis"
    )
    maxDimAccrossSpindleAxis: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="maximum dimension accross the spindle axis"
    )
    radiationSensitivityBeta: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    radiationSensitivityGamma: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    minOscWidth: Mapped[Optional[float]] = mapped_column(Float)
    monochromator: Mapped[Optional[str]] = mapped_column(
        String(8), comment="DMM or DCM"
    )
    energy: Mapped[Optional[float]] = mapped_column(Float, comment="eV")
    transmission: Mapped[Optional[float]] = mapped_column(
        Float, comment="Decimal fraction in range [0,1]"
    )
    boxSizeX: Mapped[Optional[float]] = mapped_column(Float, comment="microns")
    boxSizeY: Mapped[Optional[float]] = mapped_column(Float, comment="microns")
    kappaStart: Mapped[Optional[float]] = mapped_column(Float, comment="degrees")
    axisStart: Mapped[Optional[float]] = mapped_column(Float, comment="degrees")
    axisRange: Mapped[Optional[float]] = mapped_column(Float, comment="degrees")
    numberOfImages: Mapped[Optional[int]] = mapped_column(
        MEDIUMINT, comment="The number of images requested"
    )
    presetForProposalId: Mapped[Optional[int]] = mapped_column(
        INTEGER,
        comment="Indicates this plan is available to all sessions on given proposal",
    )
    beamLineName: Mapped[Optional[str]] = mapped_column(
        String(45),
        comment="Indicates this plan is available to all sessions on given beamline",
    )
    detectorId: Mapped[Optional[int]] = mapped_column(Integer)
    distance: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    orientation: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    monoBandwidth: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    centringMethod: Mapped[Optional[str]] = mapped_column(
        Enum("xray", "loop", "diffraction", "optical")
    )
    userPath: Mapped[Optional[str]] = mapped_column(
        String(100),
        comment='User-specified relative "root" path inside the session directory to be used for holding collected data',
    )
    robotPlateTemperature: Mapped[Optional[float]] = mapped_column(
        Float, comment="units: kelvin"
    )
    exposureTemperature: Mapped[Optional[float]] = mapped_column(
        Float, comment="units: kelvin"
    )
    experimentTypeId: Mapped[Optional[int]] = mapped_column(INTEGER)
    purificationColumnId: Mapped[Optional[int]] = mapped_column(INTEGER)
    collectionMode: Mapped[Optional[str]] = mapped_column(
        Enum("auto", "manual"),
        comment="The requested collection mode, possible values are auto, manual",
    )
    priority: Mapped[Optional[int]] = mapped_column(
        Integer,
        comment="The priority of this sample relative to others in the shipment",
    )
    qMin: Mapped[Optional[float]] = mapped_column(
        Float, comment="minimum in qRange, unit: nm^-1, needed for SAXS"
    )
    qMax: Mapped[Optional[float]] = mapped_column(
        Float, comment="maximum in qRange, unit: nm^-1, needed for SAXS"
    )
    reductionParametersAveraging: Mapped[Optional[str]] = mapped_column(
        Enum("All", "Fastest Dimension", "1D"),
        comment="Post processing params for SAXS",
    )
    scanParameters: Mapped[Optional[str]] = mapped_column(
        LONGTEXT,
        comment="JSON serialised scan parameters, useful for parameters without designated columns",
    )

    BLSample_: Mapped[List["BLSample"]] = relationship(
        "BLSample", back_populates="DiffractionPlan"
    )
    BLSubSample_: Mapped[List["BLSubSample"]] = relationship(
        "BLSubSample", back_populates="DiffractionPlan"
    )
    DataCollection_: Mapped[List["DataCollection"]] = relationship(
        "DataCollection", back_populates="DiffractionPlan"
    )
    Detector_: Mapped["Detector"] = relationship(
        "Detector", back_populates="DiffractionPlan"
    )
    ExperimentType_: Mapped["ExperimentType"] = relationship(
        "ExperimentType", back_populates="DiffractionPlan"
    )
    Proposal_: Mapped["Proposal"] = relationship(
        "Proposal", back_populates="DiffractionPlan"
    )
    PurificationColumn_: Mapped["PurificationColumn"] = relationship(
        "PurificationColumn", back_populates="DiffractionPlan"
    )
    BLSample_has_DataCollectionPlan: Mapped[
        List["BLSampleHasDataCollectionPlan"]
    ] = relationship("BLSampleHasDataCollectionPlan", back_populates="DiffractionPlan_")
    Crystal: Mapped[List["Crystal"]] = relationship(
        "Crystal", back_populates="DiffractionPlan_"
    )
    DataCollectionPlan_has_Detector: Mapped[
        List["DataCollectionPlanHasDetector"]
    ] = relationship("DataCollectionPlanHasDetector", back_populates="DiffractionPlan_")
    ExperimentKindDetails: Mapped[List["ExperimentKindDetails"]] = relationship(
        "ExperimentKindDetails", back_populates="DiffractionPlan_"
    )
    ScanParametersModel: Mapped[List["ScanParametersModel"]] = relationship(
        "ScanParametersModel", back_populates="DiffractionPlan_"
    )
    ContainerQueueSample: Mapped[List["ContainerQueueSample"]] = relationship(
        "ContainerQueueSample", back_populates="DiffractionPlan_"
    )


class LabContact(Base):
    __tablename__ = "LabContact"
    __table_args__ = (
        ForeignKeyConstraint(
            ["personId"],
            ["Person.personId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="LabContact_ibfk_1",
        ),
        ForeignKeyConstraint(
            ["proposalId"],
            ["Proposal.proposalId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="LabContact_ibfk_2",
        ),
        Index("LabContact_FKIndex1", "proposalId"),
        Index("cardNameAndProposal", "cardName", "proposalId", unique=True),
        Index("personAndProposal", "personId", "proposalId", unique=True),
    )

    labContactId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    personId: Mapped[int] = mapped_column(INTEGER)
    cardName: Mapped[str] = mapped_column(String(40))
    proposalId: Mapped[int] = mapped_column(INTEGER)
    dewarAvgCustomsValue: Mapped[int] = mapped_column(
        INTEGER, server_default=text("'0'")
    )
    dewarAvgTransportValue: Mapped[int] = mapped_column(
        INTEGER, server_default=text("'0'")
    )
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Creation or last update date/time",
    )
    defaultCourrierCompany: Mapped[Optional[str]] = mapped_column(String(45))
    courierAccount: Mapped[Optional[str]] = mapped_column(String(45))
    billingReference: Mapped[Optional[str]] = mapped_column(String(45))

    Person_: Mapped["Person"] = relationship("Person", back_populates="LabContact")
    Proposal_: Mapped["Proposal"] = relationship(
        "Proposal", back_populates="LabContact"
    )
    DewarRegistry: Mapped[List["DewarRegistry"]] = relationship(
        "DewarRegistry", back_populates="LabContact_"
    )
    Shipping: Mapped[List["Shipping"]] = relationship(
        "Shipping",
        foreign_keys="[Shipping.returnLabContactId]",
        back_populates="LabContact_",
    )
    Shipping_: Mapped[List["Shipping"]] = relationship(
        "Shipping",
        foreign_keys="[Shipping.sendingLabContactId]",
        back_populates="LabContact1",
    )
    DewarRegistry_has_Proposal: Mapped[List["DewarRegistryHasProposal"]] = relationship(
        "DewarRegistryHasProposal", back_populates="LabContact_"
    )


class MXMRRunBlob(Base):
    __tablename__ = "MXMRRunBlob"
    __table_args__ = (
        ForeignKeyConstraint(
            ["mxMRRunId"], ["MXMRRun.mxMRRunId"], name="mxMRRunBlob_FK1"
        ),
        Index("mxMRRunBlob_FK1", "mxMRRunId"),
    )

    mxMRRunBlobId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    mxMRRunId: Mapped[int] = mapped_column(INTEGER)
    view1: Mapped[Optional[str]] = mapped_column(String(255))
    view2: Mapped[Optional[str]] = mapped_column(String(255))
    view3: Mapped[Optional[str]] = mapped_column(String(255))
    filePath: Mapped[Optional[str]] = mapped_column(
        String(255),
        comment="File path corresponding to the filenames in the view* columns",
    )
    x: Mapped[Optional[float]] = mapped_column(
        Float, comment="Fractional x coordinate of blob in range [-1, 1]"
    )
    y: Mapped[Optional[float]] = mapped_column(
        Float, comment="Fractional y coordinate of blob in range [-1, 1]"
    )
    z: Mapped[Optional[float]] = mapped_column(
        Float, comment="Fractional z coordinate of blob in range [-1, 1]"
    )
    height: Mapped[Optional[float]] = mapped_column(
        Float, comment="Blob height (sigmas)"
    )
    occupancy: Mapped[Optional[float]] = mapped_column(
        Float, comment="Site occupancy factor in range [0, 1]"
    )
    nearestAtomName: Mapped[Optional[str]] = mapped_column(
        String(4), comment="Name of nearest atom"
    )
    nearestAtomChainId: Mapped[Optional[str]] = mapped_column(
        String(2), comment="Chain identifier of nearest atom"
    )
    nearestAtomResName: Mapped[Optional[str]] = mapped_column(
        String(4), comment="Residue name of nearest atom"
    )
    nearestAtomResSeq: Mapped[Optional[int]] = mapped_column(
        MEDIUMINT, comment="Residue sequence number of nearest atom"
    )
    nearestAtomDistance: Mapped[Optional[float]] = mapped_column(
        Float, comment="Distance in Angstrom to nearest atom"
    )
    mapType: Mapped[Optional[str]] = mapped_column(
        Enum("anomalous", "difference"),
        comment="Type of electron density map corresponding to this blob",
    )

    MXMRRun_: Mapped["MXMRRun"] = relationship("MXMRRun", back_populates="MXMRRunBlob")


class ParticlePicker(Base):
    __tablename__ = "ParticlePicker"
    __table_args__ = (
        ForeignKeyConstraint(
            ["firstMotionCorrectionId"],
            ["MotionCorrection.motionCorrectionId"],
            onupdate="CASCADE",
            name="ParticlePicker_fk_motionCorrectionId",
        ),
        ForeignKeyConstraint(
            ["programId"],
            ["AutoProcProgram.autoProcProgramId"],
            onupdate="CASCADE",
            name="ParticlePicker_fk_programId",
        ),
        Index("ParticlePicker_fk_motionCorrectionId", "firstMotionCorrectionId"),
        Index("ParticlePicker_fk_particlePickerProgramId", "programId"),
        {"comment": "An instance of a particle picker program that was run"},
    )

    particlePickerId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    programId: Mapped[Optional[int]] = mapped_column(INTEGER)
    firstMotionCorrectionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    particlePickingTemplate: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Cryolo model"
    )
    particleDiameter: Mapped[Optional[float]] = mapped_column(Float, comment="Unit: nm")
    numberOfParticles: Mapped[Optional[int]] = mapped_column(INTEGER)
    summaryImageFullPath: Mapped[Optional[str]] = mapped_column(
        String(255),
        comment="Generated summary micrograph image with highlighted particles",
    )

    MotionCorrection_: Mapped["MotionCorrection"] = relationship(
        "MotionCorrection", back_populates="ParticlePicker"
    )
    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="ParticlePicker"
    )
    ParticleClassificationGroup: Mapped[
        List["ParticleClassificationGroup"]
    ] = relationship("ParticleClassificationGroup", back_populates="ParticlePicker_")


class PhasingStatistics(Base):
    __tablename__ = "PhasingStatistics"
    __table_args__ = (
        ForeignKeyConstraint(
            ["phasingHasScalingId1"],
            ["Phasing_has_Scaling.phasingHasScalingId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="PhasingStatistics_phasingHasScalingfk_1",
        ),
        ForeignKeyConstraint(
            ["phasingHasScalingId2"],
            ["Phasing_has_Scaling.phasingHasScalingId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="PhasingStatistics_phasingHasScalingfk_2",
        ),
        ForeignKeyConstraint(
            ["phasingStepId"],
            ["PhasingStep.phasingStepId"],
            name="fk_PhasingStatistics_phasingStep",
        ),
        Index("PhasingStatistics_FKIndex1", "phasingHasScalingId1"),
        Index("PhasingStatistics_FKIndex2", "phasingHasScalingId2"),
        Index("fk_PhasingStatistics_phasingStep_idx", "phasingStepId"),
    )

    phasingStatisticsId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingHasScalingId1: Mapped[int] = mapped_column(
        INTEGER, comment="the dataset in question"
    )
    phasingHasScalingId2: Mapped[Optional[int]] = mapped_column(
        INTEGER,
        comment="if this is MIT or MAD, which scaling are being compared, null otherwise",
    )
    phasingStepId: Mapped[Optional[int]] = mapped_column(INTEGER)
    numberOfBins: Mapped[Optional[int]] = mapped_column(
        Integer, comment="the total number of bins"
    )
    binNumber: Mapped[Optional[int]] = mapped_column(
        Integer, comment="binNumber, 999 for overall"
    )
    lowRes: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="low resolution cutoff of this binfloat"
    )
    highRes: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="high resolution cutoff of this binfloat"
    )
    metric: Mapped[Optional[str]] = mapped_column(
        Enum(
            "Rcullis",
            "Average Fragment Length",
            "Chain Count",
            "Residues Count",
            "CC",
            "PhasingPower",
            "FOM",
            '<d"/sig>',
            "Best CC",
            "CC(1/2)",
            "Weak CC",
            "CFOM",
            "Pseudo_free_CC",
            "CC of partial model",
        ),
        comment="metric",
    )
    statisticsValue: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="the statistics value"
    )
    nReflections: Mapped[Optional[int]] = mapped_column(Integer)
    recordTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    Phasing_has_Scaling: Mapped["PhasingHasScaling"] = relationship(
        "PhasingHasScaling",
        foreign_keys=[phasingHasScalingId1],
        back_populates="PhasingStatistics",
    )
    Phasing_has_Scaling_: Mapped["PhasingHasScaling"] = relationship(
        "PhasingHasScaling",
        foreign_keys=[phasingHasScalingId2],
        back_populates="PhasingStatistics_",
    )
    PhasingStep_: Mapped["PhasingStep"] = relationship(
        "PhasingStep", back_populates="PhasingStatistics"
    )


t_Project_has_BLSample = Table(
    "Project_has_BLSample",
    Base.metadata,
    Column("projectId", INTEGER, primary_key=True, nullable=False),
    Column("blSampleId", INTEGER, primary_key=True, nullable=False),
    ForeignKeyConstraint(
        ["blSampleId"],
        ["BLSample.blSampleId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="Project_has_BLSample_FK2",
    ),
    ForeignKeyConstraint(
        ["projectId"],
        ["Project.projectId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="Project_has_BLSample_FK1",
    ),
    Index("Project_has_BLSample_FK2", "blSampleId"),
)


t_Project_has_Person = Table(
    "Project_has_Person",
    Base.metadata,
    Column("projectId", INTEGER, primary_key=True, nullable=False),
    Column("personId", INTEGER, primary_key=True, nullable=False),
    ForeignKeyConstraint(
        ["personId"],
        ["Person.personId"],
        ondelete="CASCADE",
        name="project_has_person_FK2",
    ),
    ForeignKeyConstraint(
        ["projectId"],
        ["Project.projectId"],
        ondelete="CASCADE",
        name="project_has_person_FK1",
    ),
    Index("project_has_person_FK2", "personId"),
)


class ProjectHasUser(Base):
    __tablename__ = "Project_has_User"
    __table_args__ = (
        ForeignKeyConstraint(
            ["projectid"], ["Project.projectId"], name="Project_Has_user_FK1"
        ),
        Index("Project_Has_user_FK1", "projectid"),
    )

    projecthasuserid: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    projectid: Mapped[int] = mapped_column(INTEGER)
    username: Mapped[Optional[str]] = mapped_column(String(15))

    Project_: Mapped["Project"] = relationship(
        "Project", back_populates="Project_has_User"
    )


class ProposalHasPerson(Base):
    __tablename__ = "ProposalHasPerson"
    __table_args__ = (
        ForeignKeyConstraint(
            ["personId"], ["Person.personId"], name="fk_ProposalHasPerson_Personal"
        ),
        ForeignKeyConstraint(
            ["proposalId"],
            ["Proposal.proposalId"],
            name="fk_ProposalHasPerson_Proposal",
        ),
        Index("fk_ProposalHasPerson_Personal", "personId"),
        Index("fk_ProposalHasPerson_Proposal", "proposalId"),
    )

    proposalHasPersonId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    proposalId: Mapped[int] = mapped_column(INTEGER)
    personId: Mapped[int] = mapped_column(INTEGER)
    role: Mapped[Optional[str]] = mapped_column(
        Enum(
            "Co-Investigator",
            "Principal Investigator",
            "Alternate Contact",
            "ERA Admin",
            "Associate",
        )
    )

    Person_: Mapped["Person"] = relationship(
        "Person", back_populates="ProposalHasPerson"
    )
    Proposal_: Mapped["Proposal"] = relationship(
        "Proposal", back_populates="ProposalHasPerson"
    )


class Protein(Base):
    __tablename__ = "Protein"
    __table_args__ = (
        ForeignKeyConstraint(
            ["componentTypeId"],
            ["ComponentType.componentTypeId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="protein_fk3",
        ),
        ForeignKeyConstraint(
            ["concentrationTypeId"],
            ["ConcentrationType.concentrationTypeId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="protein_fk4",
        ),
        ForeignKeyConstraint(
            ["proposalId"],
            ["Proposal.proposalId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Protein_ibfk_1",
        ),
        Index("ProteinAcronym_Index", "proposalId", "acronym"),
        Index("Protein_FKIndex2", "personId"),
        Index("Protein_Index2", "acronym"),
        Index("protein_fk3", "componentTypeId"),
        Index("protein_fk4", "concentrationTypeId"),
    )

    proteinId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    proposalId: Mapped[int] = mapped_column(INTEGER, server_default=text("'0'"))
    hazardGroup: Mapped[int] = mapped_column(
        TINYINT, server_default=text("'1'"), comment="A.k.a. risk group"
    )
    containmentLevel: Mapped[int] = mapped_column(
        TINYINT,
        server_default=text("'1'"),
        comment="A.k.a. biosafety level, which indicates the level of containment required",
    )
    bltimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    name: Mapped[Optional[str]] = mapped_column(String(255))
    acronym: Mapped[Optional[str]] = mapped_column(String(45))
    description: Mapped[Optional[str]] = mapped_column(
        Text, comment="A description/summary using words and sentences"
    )
    safetyLevel: Mapped[Optional[str]] = mapped_column(Enum("GREEN", "YELLOW", "RED"))
    molecularMass: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    proteinType: Mapped[Optional[str]] = mapped_column(String(45))
    personId: Mapped[Optional[int]] = mapped_column(INTEGER)
    isCreatedBySampleSheet: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), server_default=text("'0'")
    )
    sequence: Mapped[Optional[str]] = mapped_column(Text)
    MOD_ID: Mapped[Optional[str]] = mapped_column(String(20))
    componentTypeId: Mapped[Optional[int]] = mapped_column(INTEGER)
    concentrationTypeId: Mapped[Optional[int]] = mapped_column(INTEGER)
    global_: Mapped[Optional[int]] = mapped_column(
        "global", TINYINT(1), server_default=text("'0'")
    )
    externalId: Mapped[Optional[bytes]] = mapped_column(BINARY(16))
    density: Mapped[Optional[float]] = mapped_column(Float)
    abundance: Mapped[Optional[float]] = mapped_column(Float, comment="Deprecated")
    isotropy: Mapped[Optional[str]] = mapped_column(Enum("isotropic", "anisotropic"))

    Project_: Mapped[List["Project"]] = relationship(
        "Project", secondary="Project_has_Protein", back_populates="Protein"
    )
    ComponentType_: Mapped["ComponentType"] = relationship(
        "ComponentType", back_populates="Protein"
    )
    ConcentrationType_: Mapped["ConcentrationType"] = relationship(
        "ConcentrationType", back_populates="Protein"
    )
    Proposal_: Mapped["Proposal"] = relationship("Proposal", back_populates="Protein")
    ComponentSubType_: Mapped[List["ComponentSubType"]] = relationship(
        "ComponentSubType", secondary="Component_has_SubType", back_populates="Protein"
    )
    ComponentLattice: Mapped[List["ComponentLattice"]] = relationship(
        "ComponentLattice", back_populates="Protein_"
    )
    Crystal: Mapped[List["Crystal"]] = relationship(
        "Crystal", back_populates="Protein_"
    )
    Protein_has_PDB: Mapped[List["ProteinHasPDB"]] = relationship(
        "ProteinHasPDB", back_populates="Protein_"
    )
    BLSampleType_has_Component: Mapped[List["BLSampleTypeHasComponent"]] = relationship(
        "BLSampleTypeHasComponent", back_populates="Protein_"
    )
    ScreenComponent: Mapped[List["ScreenComponent"]] = relationship(
        "ScreenComponent", back_populates="Protein_"
    )


class RelativeIceThickness(Base):
    __tablename__ = "RelativeIceThickness"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcProgramId"],
            ["AutoProcProgram.autoProcProgramId"],
            onupdate="CASCADE",
            name="RelativeIceThickness_fk_programId",
        ),
        ForeignKeyConstraint(
            ["motionCorrectionId"],
            ["MotionCorrection.motionCorrectionId"],
            onupdate="CASCADE",
            name="RelativeIceThickness_fk_motionCorrectionId",
        ),
        Index("RelativeIceThickness_fk_motionCorrectionId", "motionCorrectionId"),
        Index("RelativeIceThickness_fk_programId", "autoProcProgramId"),
    )

    relativeIceThicknessId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    motionCorrectionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    autoProcProgramId: Mapped[Optional[int]] = mapped_column(INTEGER)
    minimum: Mapped[Optional[float]] = mapped_column(
        Float, comment="Minimum relative ice thickness, Unitless"
    )
    q1: Mapped[Optional[float]] = mapped_column(Float, comment="Quartile 1, unitless")
    median: Mapped[Optional[float]] = mapped_column(
        Float, comment="Median relative ice thickness, Unitless"
    )
    q3: Mapped[Optional[float]] = mapped_column(Float, comment="Quartile 3, unitless")
    maximum: Mapped[Optional[float]] = mapped_column(
        Float, comment="Minimum relative ice thickness, Unitless"
    )

    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="RelativeIceThickness"
    )
    MotionCorrection_: Mapped["MotionCorrection"] = relationship(
        "MotionCorrection", back_populates="RelativeIceThickness"
    )


class SWOnceToken(Base):
    __tablename__ = "SW_onceToken"
    __table_args__ = (
        ForeignKeyConstraint(
            ["personId"], ["Person.personId"], name="SW_onceToken_fk1"
        ),
        ForeignKeyConstraint(
            ["proposalId"], ["Proposal.proposalId"], name="SW_onceToken_fk2"
        ),
        Index("SW_onceToken_fk1", "personId"),
        Index("SW_onceToken_fk2", "proposalId"),
        Index("SW_onceToken_recordTimeStamp_idx", "recordTimeStamp"),
        {
            "comment": "One-time use tokens needed for token auth in order to grant "
            "access to file downloads and webcams (and some images)"
        },
    )

    onceTokenId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    token: Mapped[Optional[str]] = mapped_column(String(128))
    personId: Mapped[Optional[int]] = mapped_column(INTEGER)
    proposalId: Mapped[Optional[int]] = mapped_column(INTEGER)
    validity: Mapped[Optional[str]] = mapped_column(String(200))

    Person_: Mapped["Person"] = relationship("Person", back_populates="SW_onceToken")
    Proposal_: Mapped["Proposal"] = relationship(
        "Proposal", back_populates="SW_onceToken"
    )


class Screen(Base):
    __tablename__ = "Screen"
    __table_args__ = (
        ForeignKeyConstraint(
            ["containerTypeId"],
            ["ContainerType.containerTypeId"],
            onupdate="CASCADE",
            name="Screen_fk_containerTypeId",
        ),
        ForeignKeyConstraint(
            ["proposalId"], ["Proposal.proposalId"], name="Screen_fk1"
        ),
        Index("Screen_fk1", "proposalId"),
        Index("Screen_fk_containerTypeId", "containerTypeId"),
    )

    screenId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(45))
    proposalId: Mapped[Optional[int]] = mapped_column(INTEGER)
    global_: Mapped[Optional[int]] = mapped_column("global", TINYINT(1))
    containerTypeId: Mapped[Optional[int]] = mapped_column(INTEGER)

    ContainerType_: Mapped["ContainerType"] = relationship(
        "ContainerType", back_populates="Screen"
    )
    Proposal_: Mapped["Proposal"] = relationship("Proposal", back_populates="Screen")
    ScreenComponentGroup: Mapped[List["ScreenComponentGroup"]] = relationship(
        "ScreenComponentGroup", back_populates="Screen_"
    )
    Container: Mapped[List["Container"]] = relationship(
        "Container", back_populates="Screen_"
    )


class BFFault(Base):
    __tablename__ = "BF_fault"
    __table_args__ = (
        ForeignKeyConstraint(["assigneeId"], ["Person.personId"], name="bf_fault_FK4"),
        ForeignKeyConstraint(["personId"], ["Person.personId"], name="bf_fault_FK3"),
        ForeignKeyConstraint(
            ["sessionId"], ["BLSession.sessionId"], name="bf_fault_FK1"
        ),
        ForeignKeyConstraint(
            ["subcomponentId"], ["BF_subcomponent.subcomponentId"], name="bf_fault_FK2"
        ),
        Index("bf_fault_FK1", "sessionId"),
        Index("bf_fault_FK2", "subcomponentId"),
        Index("bf_fault_FK3", "personId"),
        Index("bf_fault_FK4", "assigneeId"),
    )

    faultId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    sessionId: Mapped[int] = mapped_column(INTEGER)
    owner: Mapped[Optional[str]] = mapped_column(String(50))
    subcomponentId: Mapped[Optional[int]] = mapped_column(INTEGER)
    starttime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    endtime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    beamtimelost: Mapped[Optional[int]] = mapped_column(TINYINT(1))
    beamtimelost_starttime: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime
    )
    beamtimelost_endtime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    title: Mapped[Optional[str]] = mapped_column(String(200))
    description: Mapped[Optional[str]] = mapped_column(Text)
    resolved: Mapped[Optional[int]] = mapped_column(TINYINT(1))
    resolution: Mapped[Optional[str]] = mapped_column(Text)
    attachment: Mapped[Optional[str]] = mapped_column(String(200))
    eLogId: Mapped[Optional[int]] = mapped_column(Integer)
    assignee: Mapped[Optional[str]] = mapped_column(String(50))
    personId: Mapped[Optional[int]] = mapped_column(INTEGER)
    assigneeId: Mapped[Optional[int]] = mapped_column(INTEGER)

    Person_: Mapped["Person"] = relationship(
        "Person", foreign_keys=[assigneeId], back_populates="BF_fault"
    )
    Person1: Mapped["Person"] = relationship(
        "Person", foreign_keys=[personId], back_populates="BF_fault_"
    )
    BLSession_: Mapped["BLSession"] = relationship(
        "BLSession", back_populates="BF_fault"
    )
    BF_subcomponent: Mapped["BFSubcomponent"] = relationship(
        "BFSubcomponent", back_populates="BF_fault"
    )


class BLSampleGroupHasBLSample(Base):
    __tablename__ = "BLSampleGroup_has_BLSample"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleGroupId"],
            ["BLSampleGroup.blSampleGroupId"],
            name="BLSampleGroup_has_BLSample_ibfk1",
        ),
        ForeignKeyConstraint(
            ["blSampleId"],
            ["BLSample.blSampleId"],
            name="BLSampleGroup_has_BLSample_ibfk2",
        ),
        ForeignKeyConstraint(
            ["blSampleTypeId"],
            ["BLSampleType.blSampleTypeId"],
            name="BLSampleGroup_has_BLSample_ibfk3",
        ),
        Index("BLSampleGroup_has_BLSample_ibfk2", "blSampleId"),
        Index("BLSampleGroup_has_BLSample_ibfk3", "blSampleTypeId"),
    )

    blSampleGroupId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    blSampleId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    groupOrder: Mapped[Optional[int]] = mapped_column(MEDIUMINT)
    type: Mapped[Optional[str]] = mapped_column(
        Enum("background", "container", "sample", "calibrant", "capillary")
    )
    blSampleTypeId: Mapped[Optional[int]] = mapped_column(INTEGER)

    BLSampleGroup_: Mapped["BLSampleGroup"] = relationship(
        "BLSampleGroup", back_populates="BLSampleGroup_has_BLSample"
    )
    BLSample_: Mapped["BLSample"] = relationship(
        "BLSample", back_populates="BLSampleGroup_has_BLSample"
    )
    BLSampleType_: Mapped["BLSampleType"] = relationship(
        "BLSampleType", back_populates="BLSampleGroup_has_BLSample"
    )


class BLSampleHasDataCollectionPlan(Base):
    __tablename__ = "BLSample_has_DataCollectionPlan"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleId"],
            ["BLSample.blSampleId"],
            name="BLSample_has_DataCollectionPlan_ibfk1",
        ),
        ForeignKeyConstraint(
            ["dataCollectionPlanId"],
            ["DiffractionPlan.diffractionPlanId"],
            name="BLSample_has_DataCollectionPlan_ibfk2",
        ),
        Index("BLSample_has_DataCollectionPlan_ibfk2", "dataCollectionPlanId"),
    )

    blSampleId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    dataCollectionPlanId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    planOrder: Mapped[Optional[int]] = mapped_column(SMALLINT)

    BLSample_: Mapped["BLSample"] = relationship(
        "BLSample", back_populates="BLSample_has_DataCollectionPlan"
    )
    DiffractionPlan_: Mapped["DiffractionPlan"] = relationship(
        "DiffractionPlan", back_populates="BLSample_has_DataCollectionPlan"
    )


class BLSessionHasSCPosition(Base):
    __tablename__ = "BLSession_has_SCPosition"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blsessionid"],
            ["BLSession.sessionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="blsession_has_scposition_FK1",
        ),
        Index("blsession_has_scposition_FK1", "blsessionid"),
    )

    blsessionhasscpositionid: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    blsessionid: Mapped[int] = mapped_column(INTEGER)
    scContainer: Mapped[Optional[int]] = mapped_column(
        SMALLINT, comment="Position of container within sample changer"
    )
    containerPosition: Mapped[Optional[int]] = mapped_column(
        SMALLINT, comment="Position of sample within container"
    )

    BLSession_: Mapped["BLSession"] = relationship(
        "BLSession", back_populates="BLSession_has_SCPosition"
    )


class BeamlineAction(Base):
    __tablename__ = "BeamlineAction"
    __table_args__ = (
        ForeignKeyConstraint(
            ["sessionId"], ["BLSession.sessionId"], name="BeamlineAction_ibfk1"
        ),
        Index("BeamlineAction_ibfk1", "sessionId"),
    )

    beamlineActionId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    startTimestamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    endTimestamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("'0000-00-00 00:00:00'")
    )
    sessionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    message: Mapped[Optional[str]] = mapped_column(String(255))
    parameter: Mapped[Optional[str]] = mapped_column(String(50))
    value: Mapped[Optional[str]] = mapped_column(String(30))
    loglevel: Mapped[Optional[str]] = mapped_column(Enum("DEBUG", "CRITICAL", "INFO"))
    status: Mapped[Optional[str]] = mapped_column(
        Enum("PAUSED", "RUNNING", "TERMINATED", "COMPLETE", "ERROR", "EPICSFAIL")
    )

    BLSession_: Mapped["BLSession"] = relationship(
        "BLSession", back_populates="BeamlineAction"
    )


class ComponentLattice(Base):
    __tablename__ = "ComponentLattice"
    __table_args__ = (
        ForeignKeyConstraint(
            ["componentId"], ["Protein.proteinId"], name="ComponentLattice_ibfk1"
        ),
        Index("ComponentLattice_ibfk1", "componentId"),
    )

    componentLatticeId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    componentId: Mapped[Optional[int]] = mapped_column(INTEGER)
    spaceGroup: Mapped[Optional[str]] = mapped_column(String(20))
    cell_a: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    cell_b: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    cell_c: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    cell_alpha: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    cell_beta: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    cell_gamma: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )

    Protein_: Mapped["Protein"] = relationship(
        "Protein", back_populates="ComponentLattice"
    )


t_Component_has_SubType = Table(
    "Component_has_SubType",
    Base.metadata,
    Column("componentId", INTEGER, primary_key=True, nullable=False),
    Column("componentSubTypeId", INTEGER, primary_key=True, nullable=False),
    ForeignKeyConstraint(
        ["componentId"],
        ["Protein.proteinId"],
        ondelete="CASCADE",
        name="component_has_SubType_fk1",
    ),
    ForeignKeyConstraint(
        ["componentSubTypeId"],
        ["ComponentSubType.componentSubTypeId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="component_has_SubType_fk2",
    ),
    Index("component_has_SubType_fk2", "componentSubTypeId"),
)


class Crystal(Base):
    __tablename__ = "Crystal"
    __table_args__ = (
        ForeignKeyConstraint(
            ["diffractionPlanId"],
            ["DiffractionPlan.diffractionPlanId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Crystal_ibfk_2",
        ),
        ForeignKeyConstraint(
            ["proteinId"],
            ["Protein.proteinId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Crystal_ibfk_1",
        ),
        Index("Crystal_FKIndex1", "proteinId"),
        Index("Crystal_FKIndex2", "diffractionPlanId"),
    )

    crystalId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    proteinId: Mapped[int] = mapped_column(INTEGER, server_default=text("'0'"))
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Creation or last update date/time",
    )
    diffractionPlanId: Mapped[Optional[int]] = mapped_column(INTEGER)
    crystalUUID: Mapped[Optional[str]] = mapped_column(String(45))
    name: Mapped[Optional[str]] = mapped_column(String(255))
    spaceGroup: Mapped[Optional[str]] = mapped_column(String(20))
    morphology: Mapped[Optional[str]] = mapped_column(String(255))
    color: Mapped[Optional[str]] = mapped_column(String(45))
    size_X: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    size_Y: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    size_Z: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    cell_a: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    cell_b: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    cell_c: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    cell_alpha: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    cell_beta: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    cell_gamma: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    comments: Mapped[Optional[str]] = mapped_column(String(255))
    pdbFileName: Mapped[Optional[str]] = mapped_column(
        String(255), comment="pdb file name"
    )
    pdbFilePath: Mapped[Optional[str]] = mapped_column(
        String(1024), comment="pdb file path"
    )
    abundance: Mapped[Optional[float]] = mapped_column(Float)
    theoreticalDensity: Mapped[Optional[float]] = mapped_column(Float)

    BLSample_: Mapped[List["BLSample"]] = relationship(
        "BLSample", back_populates="Crystal"
    )
    DiffractionPlan_: Mapped["DiffractionPlan"] = relationship(
        "DiffractionPlan", back_populates="Crystal"
    )
    Protein_: Mapped["Protein"] = relationship("Protein", back_populates="Crystal")
    BLSampleType_has_Component: Mapped[List["BLSampleTypeHasComponent"]] = relationship(
        "BLSampleTypeHasComponent", back_populates="Crystal_"
    )
    CrystalComposition: Mapped[List["CrystalComposition"]] = relationship(
        "CrystalComposition", back_populates="Crystal_"
    )
    Crystal_has_UUID: Mapped[List["CrystalHasUUID"]] = relationship(
        "CrystalHasUUID", back_populates="Crystal_"
    )


class DataCollectionGroup(Base):
    __tablename__ = "DataCollectionGroup"
    __table_args__ = (
        CheckConstraint(
            "json_valid(`scanParameters`)", name="DataCollectionGroup_chk_1"
        ),
        ForeignKeyConstraint(
            ["blSampleId"],
            ["BLSample.blSampleId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="DataCollectionGroup_ibfk_1",
        ),
        ForeignKeyConstraint(
            ["experimentTypeId"],
            ["ExperimentType.experimentTypeId"],
            name="DataCollectionGroup_ibfk_4",
        ),
        ForeignKeyConstraint(
            ["sessionId"],
            ["BLSession.sessionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="DataCollectionGroup_ibfk_2",
        ),
        Index("DataCollectionGroup_FKIndex1", "blSampleId"),
        Index("DataCollectionGroup_FKIndex2", "sessionId"),
        Index("DataCollectionGroup_ibfk_4", "experimentTypeId"),
        {"comment": "a dataCollectionGroup is a group of dataCollection for a spe"},
    )

    dataCollectionGroupId: Mapped[int] = mapped_column(
        Integer, primary_key=True, comment="Primary key (auto-incremented)"
    )
    sessionId: Mapped[int] = mapped_column(INTEGER, comment="references Session table")
    comments: Mapped[Optional[str]] = mapped_column(String(1024), comment="comments")
    blSampleId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="references BLSample table"
    )
    experimentType: Mapped[Optional[str]] = mapped_column(
        Enum(
            "SAD",
            "SAD - Inverse Beam",
            "OSC",
            "Collect - Multiwedge",
            "MAD",
            "Helical",
            "Multi-positional",
            "Mesh",
            "Burn",
            "MAD - Inverse Beam",
            "Characterization",
            "Dehydration",
            "tomo",
            "experiment",
            "EM",
            "PDF",
            "PDF+Bragg",
            "Bragg",
            "single particle",
            "Serial Fixed",
            "Serial Jet",
            "Standard",
            "Time Resolved",
            "Diamond Anvil High Pressure",
            "Custom",
            "XRF map",
            "Energy scan",
            "XRF spectrum",
            "XRF map xas",
            "Mesh3D",
            "Screening",
            "Still",
            "SSX-Chip",
            "SSX-Jet",
        ),
        comment="Standard: Routine structure determination experiment. Time Resolved: Investigate the change of a system over time. Custom: Special or non-standard data collection.",
    )
    startTime: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Start time of the dataCollectionGroup"
    )
    endTime: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="end time of the dataCollectionGroup"
    )
    crystalClass: Mapped[Optional[str]] = mapped_column(
        String(20), comment="Crystal Class for industrials users"
    )
    detectorMode: Mapped[Optional[str]] = mapped_column(
        String(255), comment="Detector mode"
    )
    actualSampleBarcode: Mapped[Optional[str]] = mapped_column(
        String(45), comment="Actual sample barcode"
    )
    actualSampleSlotInContainer: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Actual sample slot number in container"
    )
    actualContainerBarcode: Mapped[Optional[str]] = mapped_column(
        String(45), comment="Actual container barcode"
    )
    actualContainerSlotInSC: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Actual container slot number in sample changer"
    )
    xtalSnapshotFullPath: Mapped[Optional[str]] = mapped_column(String(255))
    scanParameters: Mapped[Optional[str]] = mapped_column(LONGTEXT)
    experimentTypeId: Mapped[Optional[int]] = mapped_column(INTEGER)

    DataCollection_: Mapped[List["DataCollection"]] = relationship(
        "DataCollection", back_populates="DataCollectionGroup"
    )
    Screening_: Mapped[List["Screening"]] = relationship(
        "Screening", back_populates="DataCollectionGroup"
    )
    BLSample_: Mapped["BLSample"] = relationship(
        "BLSample", back_populates="DataCollectionGroup"
    )
    ExperimentType_: Mapped["ExperimentType"] = relationship(
        "ExperimentType", back_populates="DataCollectionGroup"
    )
    BLSession_: Mapped["BLSession"] = relationship(
        "BLSession", back_populates="DataCollectionGroup"
    )
    Project_: Mapped[List["Project"]] = relationship(
        "Project", secondary="Project_has_DCGroup", back_populates="DataCollectionGroup"
    )
    GridInfo: Mapped[List["GridInfo"]] = relationship(
        "GridInfo", back_populates="DataCollectionGroup_"
    )
    XrayCentring: Mapped[List["XrayCentring"]] = relationship(
        "XrayCentring", back_populates="DataCollectionGroup_"
    )


class DataCollectionPlanHasDetector(Base):
    __tablename__ = "DataCollectionPlan_has_Detector"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dataCollectionPlanId"],
            ["DiffractionPlan.diffractionPlanId"],
            name="DataCollectionPlan_has_Detector_ibfk1",
        ),
        ForeignKeyConstraint(
            ["detectorId"],
            ["Detector.detectorId"],
            name="DataCollectionPlan_has_Detector_ibfk2",
        ),
        Index("DataCollectionPlan_has_Detector_ibfk2", "detectorId"),
        Index(
            "dataCollectionPlanId", "dataCollectionPlanId", "detectorId", unique=True
        ),
    )

    dataCollectionPlanHasDetectorId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True
    )
    dataCollectionPlanId: Mapped[int] = mapped_column(INTEGER)
    detectorId: Mapped[int] = mapped_column(Integer)
    exposureTime: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True)
    )
    distance: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    roll: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))

    DiffractionPlan_: Mapped["DiffractionPlan"] = relationship(
        "DiffractionPlan", back_populates="DataCollectionPlan_has_Detector"
    )
    Detector_: Mapped["Detector"] = relationship(
        "Detector", back_populates="DataCollectionPlan_has_Detector"
    )


class DewarRegistry(Base):
    __tablename__ = "DewarRegistry"
    __table_args__ = (
        ForeignKeyConstraint(
            ["labContactId"],
            ["LabContact.labContactId"],
            ondelete="SET NULL",
            onupdate="CASCADE",
            name="DewarRegistry_ibfk_2",
        ),
        ForeignKeyConstraint(
            ["proposalId"],
            ["Proposal.proposalId"],
            onupdate="CASCADE",
            name="DewarRegistry_ibfk_1",
        ),
        Index("DewarRegistry_ibfk_1", "proposalId"),
        Index("DewarRegistry_ibfk_2", "labContactId"),
        Index("facilityCode", "facilityCode", unique=True),
    )

    dewarRegistryId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    facilityCode: Mapped[str] = mapped_column(String(20))
    bltimestamp: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    proposalId: Mapped[Optional[int]] = mapped_column(INTEGER)
    labContactId: Mapped[Optional[int]] = mapped_column(INTEGER)
    purchaseDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    manufacturerSerialNumber: Mapped[Optional[str]] = mapped_column(
        String(15),
        comment="Dewar serial number as given by manufacturer. Used to be typically 5 or 6 digits, more likely to be 11 alphanumeric chars in future",
    )

    LabContact_: Mapped["LabContact"] = relationship(
        "LabContact", back_populates="DewarRegistry"
    )
    Proposal_: Mapped["Proposal"] = relationship(
        "Proposal", back_populates="DewarRegistry"
    )
    DewarRegistry_has_Proposal: Mapped[List["DewarRegistryHasProposal"]] = relationship(
        "DewarRegistryHasProposal", back_populates="DewarRegistry_"
    )
    DewarReport: Mapped[List["DewarReport"]] = relationship(
        "DewarReport", back_populates="DewarRegistry_"
    )


class EnergyScan(Base):
    __tablename__ = "EnergyScan"
    __table_args__ = (
        ForeignKeyConstraint(["blSampleId"], ["BLSample.blSampleId"], name="ES_ibfk_2"),
        ForeignKeyConstraint(
            ["blSubSampleId"], ["BLSubSample.blSubSampleId"], name="ES_ibfk_3"
        ),
        ForeignKeyConstraint(
            ["sessionId"],
            ["BLSession.sessionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ES_ibfk_1",
        ),
        Index("ES_ibfk_2", "blSampleId"),
        Index("ES_ibfk_3", "blSubSampleId"),
        Index("EnergyScan_FKIndex2", "sessionId"),
    )

    energyScanId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    sessionId: Mapped[int] = mapped_column(INTEGER)
    blSampleId: Mapped[Optional[int]] = mapped_column(INTEGER)
    fluorescenceDetector: Mapped[Optional[str]] = mapped_column(String(255))
    scanFileFullPath: Mapped[Optional[str]] = mapped_column(String(255))
    jpegChoochFileFullPath: Mapped[Optional[str]] = mapped_column(String(255))
    element: Mapped[Optional[str]] = mapped_column(String(45))
    startEnergy: Mapped[Optional[float]] = mapped_column(Float)
    endEnergy: Mapped[Optional[float]] = mapped_column(Float)
    transmissionFactor: Mapped[Optional[float]] = mapped_column(Float)
    exposureTime: Mapped[Optional[float]] = mapped_column(Float)
    axisPosition: Mapped[Optional[float]] = mapped_column(Float)
    synchrotronCurrent: Mapped[Optional[float]] = mapped_column(Float)
    temperature: Mapped[Optional[float]] = mapped_column(Float)
    peakEnergy: Mapped[Optional[float]] = mapped_column(Float)
    peakFPrime: Mapped[Optional[float]] = mapped_column(Float)
    peakFDoublePrime: Mapped[Optional[float]] = mapped_column(Float)
    inflectionEnergy: Mapped[Optional[float]] = mapped_column(Float)
    inflectionFPrime: Mapped[Optional[float]] = mapped_column(Float)
    inflectionFDoublePrime: Mapped[Optional[float]] = mapped_column(Float)
    xrayDose: Mapped[Optional[float]] = mapped_column(Float)
    startTime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    endTime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    edgeEnergy: Mapped[Optional[str]] = mapped_column(String(255))
    filename: Mapped[Optional[str]] = mapped_column(String(255))
    beamSizeVertical: Mapped[Optional[float]] = mapped_column(Float)
    beamSizeHorizontal: Mapped[Optional[float]] = mapped_column(Float)
    choochFileFullPath: Mapped[Optional[str]] = mapped_column(String(255))
    crystalClass: Mapped[Optional[str]] = mapped_column(String(20))
    comments: Mapped[Optional[str]] = mapped_column(String(1024))
    flux: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="flux measured before the energyScan"
    )
    flux_end: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="flux measured after the energyScan"
    )
    workingDirectory: Mapped[Optional[str]] = mapped_column(String(45))
    blSubSampleId: Mapped[Optional[int]] = mapped_column(INTEGER)

    BLSample_: Mapped["BLSample"] = relationship(
        "BLSample", back_populates="EnergyScan"
    )
    BLSubSample_: Mapped["BLSubSample"] = relationship(
        "BLSubSample", back_populates="EnergyScan"
    )
    BLSession_: Mapped["BLSession"] = relationship(
        "BLSession", back_populates="EnergyScan"
    )
    Project_: Mapped[List["Project"]] = relationship(
        "Project", secondary="Project_has_EnergyScan", back_populates="EnergyScan"
    )
    BLSample_has_EnergyScan: Mapped[List["BLSampleHasEnergyScan"]] = relationship(
        "BLSampleHasEnergyScan", back_populates="EnergyScan_"
    )


class Event(Base):
    __tablename__ = "Event"
    __table_args__ = (
        ForeignKeyConstraint(
            ["componentId"], ["Component.componentId"], name="Event_ibfk_2"
        ),
        ForeignKeyConstraint(
            ["eventChainId"],
            ["EventChain.eventChainId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Event_ibfk_1",
        ),
        ForeignKeyConstraint(
            ["eventTypeId"], ["EventType.eventTypeId"], name="Event_ibfk_3"
        ),
        Index("componentId", "componentId"),
        Index("eventChainId", "eventChainId"),
        Index("eventTypeId", "eventTypeId"),
        {
            "comment": "Describes an event that occurred during a data collection and "
            "should be taken into account for data analysis. Can optionally be "
            "repeated at a specified frequency."
        },
    )

    eventId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    eventChainId: Mapped[int] = mapped_column(INTEGER)
    eventTypeId: Mapped[int] = mapped_column(INTEGER)
    offset: Mapped[float] = mapped_column(
        Float,
        comment="Start of the event relative to data collection start time in seconds.",
    )
    componentId: Mapped[Optional[int]] = mapped_column(INTEGER)
    name: Mapped[Optional[str]] = mapped_column(String(255, "utf8mb4_general_ci"))
    duration: Mapped[Optional[float]] = mapped_column(
        Float, comment="Duration of the event if applicable."
    )
    period: Mapped[Optional[float]] = mapped_column(
        Float, comment="Repetition period if applicable in seconds."
    )
    repetition: Mapped[Optional[float]] = mapped_column(
        Float, comment="Number of repetitions if applicable."
    )

    Component_: Mapped["Component"] = relationship("Component", back_populates="Event")
    EventChain_: Mapped["EventChain"] = relationship(
        "EventChain", back_populates="Event"
    )
    EventType_: Mapped["EventType"] = relationship("EventType", back_populates="Event")


class ExperimentKindDetails(Base):
    __tablename__ = "ExperimentKindDetails"
    __table_args__ = (
        ForeignKeyConstraint(
            ["diffractionPlanId"],
            ["DiffractionPlan.diffractionPlanId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="EKD_ibfk_1",
        ),
        Index("ExperimentKindDetails_FKIndex1", "diffractionPlanId"),
    )

    experimentKindId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    diffractionPlanId: Mapped[int] = mapped_column(INTEGER)
    exposureIndex: Mapped[Optional[int]] = mapped_column(INTEGER)
    dataCollectionType: Mapped[Optional[str]] = mapped_column(String(45))
    dataCollectionKind: Mapped[Optional[str]] = mapped_column(String(45))
    wedgeValue: Mapped[Optional[float]] = mapped_column(Float)

    DiffractionPlan_: Mapped["DiffractionPlan"] = relationship(
        "DiffractionPlan", back_populates="ExperimentKindDetails"
    )


class ParticleClassificationGroup(Base):
    __tablename__ = "ParticleClassificationGroup"
    __table_args__ = (
        ForeignKeyConstraint(
            ["particlePickerId"],
            ["ParticlePicker.particlePickerId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ParticleClassificationGroup_fk_particlePickerId",
        ),
        ForeignKeyConstraint(
            ["programId"],
            ["AutoProcProgram.autoProcProgramId"],
            onupdate="CASCADE",
            name="ParticleClassificationGroup_fk_programId",
        ),
        Index("ParticleClassificationGroup_fk_particlePickerId", "particlePickerId"),
        Index("ParticleClassificationGroup_fk_programId", "programId"),
    )

    particleClassificationGroupId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True
    )
    particlePickerId: Mapped[Optional[int]] = mapped_column(INTEGER)
    programId: Mapped[Optional[int]] = mapped_column(INTEGER)
    type: Mapped[Optional[str]] = mapped_column(
        Enum("2D", "3D"), comment="Indicates the type of particle classification"
    )
    batchNumber: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Corresponding to batch number"
    )
    numberOfParticlesPerBatch: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="total number of particles per batch (a large integer)"
    )
    numberOfClassesPerBatch: Mapped[Optional[int]] = mapped_column(INTEGER)
    symmetry: Mapped[Optional[str]] = mapped_column(String(20))

    ParticlePicker_: Mapped["ParticlePicker"] = relationship(
        "ParticlePicker", back_populates="ParticleClassificationGroup"
    )
    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="ParticleClassificationGroup"
    )
    ParticleClassification: Mapped[List["ParticleClassification"]] = relationship(
        "ParticleClassification", back_populates="ParticleClassificationGroup_"
    )


t_Project_has_Protein = Table(
    "Project_has_Protein",
    Base.metadata,
    Column("projectId", INTEGER, primary_key=True, nullable=False),
    Column("proteinId", INTEGER, primary_key=True, nullable=False),
    ForeignKeyConstraint(
        ["projectId"],
        ["Project.projectId"],
        ondelete="CASCADE",
        name="project_has_protein_FK1",
    ),
    ForeignKeyConstraint(
        ["proteinId"],
        ["Protein.proteinId"],
        ondelete="CASCADE",
        name="project_has_protein_FK2",
    ),
    Index("project_has_protein_FK2", "proteinId"),
)


t_Project_has_Session = Table(
    "Project_has_Session",
    Base.metadata,
    Column("projectId", INTEGER, primary_key=True, nullable=False),
    Column("sessionId", INTEGER, primary_key=True, nullable=False),
    ForeignKeyConstraint(
        ["projectId"],
        ["Project.projectId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="project_has_session_FK1",
    ),
    ForeignKeyConstraint(
        ["sessionId"],
        ["BLSession.sessionId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="project_has_session_FK2",
    ),
    Index("project_has_session_FK2", "sessionId"),
)


class ProteinHasPDB(Base):
    __tablename__ = "Protein_has_PDB"
    __table_args__ = (
        ForeignKeyConstraint(["pdbid"], ["PDB.pdbId"], name="Protein_Has_PDB_fk2"),
        ForeignKeyConstraint(
            ["proteinid"], ["Protein.proteinId"], name="Protein_Has_PDB_fk1"
        ),
        Index("Protein_Has_PDB_fk1", "proteinid"),
        Index("Protein_Has_PDB_fk2", "pdbid"),
    )

    proteinhaspdbid: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    proteinid: Mapped[int] = mapped_column(INTEGER)
    pdbid: Mapped[int] = mapped_column(INTEGER)

    PDB_: Mapped["PDB"] = relationship("PDB", back_populates="Protein_has_PDB")
    Protein_: Mapped["Protein"] = relationship(
        "Protein", back_populates="Protein_has_PDB"
    )


class RobotAction(Base):
    __tablename__ = "RobotAction"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blsampleId"], ["BLSample.blSampleId"], name="RobotAction_FK2"
        ),
        ForeignKeyConstraint(
            ["blsessionId"], ["BLSession.sessionId"], name="RobotAction_FK1"
        ),
        Index("RobotAction_FK1", "blsessionId"),
        Index("RobotAction_FK2", "blsampleId"),
        {"comment": "Robot actions as reported by GDA"},
    )

    robotActionId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    blsessionId: Mapped[int] = mapped_column(INTEGER)
    startTimestamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    endTimestamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("'0000-00-00 00:00:00'")
    )
    blsampleId: Mapped[Optional[int]] = mapped_column(INTEGER)
    actionType: Mapped[Optional[str]] = mapped_column(
        Enum("LOAD", "UNLOAD", "DISPOSE", "STORE", "WASH", "ANNEAL", "MOSAIC")
    )
    status: Mapped[Optional[str]] = mapped_column(
        Enum("SUCCESS", "ERROR", "CRITICAL", "WARNING", "EPICSFAIL", "COMMANDNOTSENT")
    )
    message: Mapped[Optional[str]] = mapped_column(String(255))
    containerLocation: Mapped[Optional[int]] = mapped_column(SmallInteger)
    dewarLocation: Mapped[Optional[int]] = mapped_column(SmallInteger)
    sampleBarcode: Mapped[Optional[str]] = mapped_column(String(45))
    xtalSnapshotBefore: Mapped[Optional[str]] = mapped_column(String(255))
    xtalSnapshotAfter: Mapped[Optional[str]] = mapped_column(String(255))

    BLSample_: Mapped["BLSample"] = relationship(
        "BLSample", back_populates="RobotAction"
    )
    BLSession_: Mapped["BLSession"] = relationship(
        "BLSession", back_populates="RobotAction"
    )


class SampleComposition(Base):
    __tablename__ = "SampleComposition"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleId"], ["BLSample.blSampleId"], name="SampleComposition_ibfk_2"
        ),
        ForeignKeyConstraint(
            ["componentId"], ["Component.componentId"], name="SampleComposition_ibfk_1"
        ),
        ForeignKeyConstraint(
            ["concentrationTypeId"],
            ["ConcentrationType.concentrationTypeId"],
            name="SampleComposition_ibfk_3",
        ),
        Index("blSampleId", "blSampleId"),
        Index("componentId", "componentId"),
        Index("concentrationTypeId", "concentrationTypeId"),
        {
            "comment": "Links a sample to its components with a specified abundance or "
            "ratio."
        },
    )

    sampleCompositionId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    componentId: Mapped[int] = mapped_column(INTEGER)
    blSampleId: Mapped[int] = mapped_column(INTEGER)
    concentrationTypeId: Mapped[Optional[int]] = mapped_column(INTEGER)
    abundance: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="Abundance or concentration in the unit defined by concentrationTypeId.",
    )
    ratio: Mapped[Optional[float]] = mapped_column(Float)
    pH: Mapped[Optional[float]] = mapped_column(Float)

    BLSample_: Mapped["BLSample"] = relationship(
        "BLSample", back_populates="SampleComposition"
    )
    Component_: Mapped["Component"] = relationship(
        "Component", back_populates="SampleComposition"
    )
    ConcentrationType_: Mapped["ConcentrationType"] = relationship(
        "ConcentrationType", back_populates="SampleComposition"
    )


class ScanParametersModel(Base):
    __tablename__ = "ScanParametersModel"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dataCollectionPlanId"],
            ["DiffractionPlan.diffractionPlanId"],
            onupdate="CASCADE",
            name="PDF_Model_ibfk2",
        ),
        ForeignKeyConstraint(
            ["scanParametersServiceId"],
            ["ScanParametersService.scanParametersServiceId"],
            onupdate="CASCADE",
            name="PDF_Model_ibfk1",
        ),
        Index("PDF_Model_ibfk1", "scanParametersServiceId"),
        Index("PDF_Model_ibfk2", "dataCollectionPlanId"),
    )

    scanParametersModelId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    scanParametersServiceId: Mapped[Optional[int]] = mapped_column(INTEGER)
    dataCollectionPlanId: Mapped[Optional[int]] = mapped_column(INTEGER)
    sequenceNumber: Mapped[Optional[int]] = mapped_column(TINYINT)
    start: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    stop: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    step: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    array: Mapped[Optional[str]] = mapped_column(Text)
    duration: Mapped[Optional[int]] = mapped_column(
        MEDIUMINT, comment="Duration for parameter change in seconds"
    )

    DiffractionPlan_: Mapped["DiffractionPlan"] = relationship(
        "DiffractionPlan", back_populates="ScanParametersModel"
    )
    ScanParametersService_: Mapped["ScanParametersService"] = relationship(
        "ScanParametersService", back_populates="ScanParametersModel"
    )


class ScreenComponentGroup(Base):
    __tablename__ = "ScreenComponentGroup"
    __table_args__ = (
        ForeignKeyConstraint(
            ["screenId"], ["Screen.screenId"], name="ScreenComponentGroup_fk1"
        ),
        Index("ScreenComponentGroup_fk1", "screenId"),
    )

    screenComponentGroupId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    screenId: Mapped[int] = mapped_column(INTEGER)
    position: Mapped[Optional[int]] = mapped_column(SmallInteger)

    BLSample_: Mapped[List["BLSample"]] = relationship(
        "BLSample", back_populates="ScreenComponentGroup"
    )
    Screen_: Mapped["Screen"] = relationship(
        "Screen", back_populates="ScreenComponentGroup"
    )
    ScreenComponent: Mapped[List["ScreenComponent"]] = relationship(
        "ScreenComponent", back_populates="ScreenComponentGroup_"
    )


class SessionType(Base):
    __tablename__ = "SessionType"
    __table_args__ = (
        ForeignKeyConstraint(
            ["sessionId"],
            ["BLSession.sessionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="SessionType_ibfk_1",
        ),
        Index("SessionType_FKIndex1", "sessionId"),
    )

    sessionTypeId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    sessionId: Mapped[int] = mapped_column(INTEGER)
    typeName: Mapped[str] = mapped_column(String(31))

    BLSession_: Mapped["BLSession"] = relationship(
        "BLSession", back_populates="SessionType"
    )


class SessionHasPerson(Base):
    __tablename__ = "Session_has_Person"
    __table_args__ = (
        ForeignKeyConstraint(
            ["personId"],
            ["Person.personId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Session_has_Person_ibfk_2",
        ),
        ForeignKeyConstraint(
            ["sessionId"],
            ["BLSession.sessionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Session_has_Person_ibfk_1",
        ),
        Index("Session_has_Person_FKIndex2", "personId"),
    )

    sessionId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, server_default=text("'0'")
    )
    personId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, server_default=text("'0'")
    )
    role: Mapped[Optional[str]] = mapped_column(
        Enum(
            "Local Contact",
            "Local Contact 2",
            "Staff",
            "Team Leader",
            "Co-Investigator",
            "Principal Investigator",
            "Alternate Contact",
            "Data Access",
            "Team Member",
            "ERA Admin",
            "Associate",
        )
    )
    remote: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), server_default=text("'0'")
    )

    Person_: Mapped["Person"] = relationship(
        "Person", back_populates="Session_has_Person"
    )
    BLSession_: Mapped["BLSession"] = relationship(
        "BLSession", back_populates="Session_has_Person"
    )


class Shipping(Base):
    __tablename__ = "Shipping"
    __table_args__ = (
        CheckConstraint("json_valid(`extra`)", name="Shipping_chk_1"),
        ForeignKeyConstraint(
            ["deliveryAgent_flightCodePersonId"],
            ["Person.personId"],
            name="Shipping_ibfk_4",
        ),
        ForeignKeyConstraint(
            ["proposalId"],
            ["Proposal.proposalId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Shipping_ibfk_1",
        ),
        ForeignKeyConstraint(
            ["returnLabContactId"],
            ["LabContact.labContactId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Shipping_ibfk_3",
        ),
        ForeignKeyConstraint(
            ["sendingLabContactId"],
            ["LabContact.labContactId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Shipping_ibfk_2",
        ),
        Index("Shipping_FKIndex1", "proposalId"),
        Index("Shipping_FKIndex2", "sendingLabContactId"),
        Index("Shipping_FKIndex3", "returnLabContactId"),
        Index("Shipping_FKIndexCreationDate", "creationDate"),
        Index("Shipping_FKIndexName", "shippingName"),
        Index("Shipping_FKIndexStatus", "shippingStatus"),
        Index("Shipping_ibfk_4", "deliveryAgent_flightCodePersonId"),
        Index("laboratoryId", "laboratoryId"),
    )

    shippingId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    proposalId: Mapped[int] = mapped_column(INTEGER, server_default=text("'0'"))
    shippingName: Mapped[Optional[str]] = mapped_column(String(45))
    deliveryAgent_agentName: Mapped[Optional[str]] = mapped_column(String(45))
    deliveryAgent_shippingDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    deliveryAgent_deliveryDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    deliveryAgent_agentCode: Mapped[Optional[str]] = mapped_column(String(45))
    deliveryAgent_flightCode: Mapped[Optional[str]] = mapped_column(String(45))
    shippingStatus: Mapped[Optional[str]] = mapped_column(String(45))
    bltimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    laboratoryId: Mapped[Optional[int]] = mapped_column(INTEGER)
    isStorageShipping: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), server_default=text("'0'")
    )
    creationDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    comments: Mapped[Optional[str]] = mapped_column(String(1000))
    sendingLabContactId: Mapped[Optional[int]] = mapped_column(INTEGER)
    returnLabContactId: Mapped[Optional[int]] = mapped_column(INTEGER)
    returnCourier: Mapped[Optional[str]] = mapped_column(String(45))
    dateOfShippingToUser: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    shippingType: Mapped[Optional[str]] = mapped_column(String(45))
    SAFETYLEVEL: Mapped[Optional[str]] = mapped_column(String(8))
    deliveryAgent_flightCodeTimestamp: Mapped[
        Optional[datetime.datetime]
    ] = mapped_column(TIMESTAMP, comment="Date flight code created, if automatic")
    deliveryAgent_label: Mapped[Optional[str]] = mapped_column(
        Text, comment="Base64 encoded pdf of airway label"
    )
    readyByTime: Mapped[Optional[datetime.time]] = mapped_column(
        Time, comment="Time shipment will be ready"
    )
    closeTime: Mapped[Optional[datetime.time]] = mapped_column(
        Time, comment="Time after which shipment cannot be picked up"
    )
    physicalLocation: Mapped[Optional[str]] = mapped_column(
        String(50), comment="Where shipment can be picked up from: i.e. Stores"
    )
    deliveryAgent_pickupConfirmationTimestamp: Mapped[
        Optional[datetime.datetime]
    ] = mapped_column(TIMESTAMP, comment="Date picked confirmed")
    deliveryAgent_pickupConfirmation: Mapped[Optional[str]] = mapped_column(
        String(10), comment="Confirmation number of requested pickup"
    )
    deliveryAgent_readyByTime: Mapped[Optional[datetime.time]] = mapped_column(
        Time, comment="Confirmed ready-by time"
    )
    deliveryAgent_callinTime: Mapped[Optional[datetime.time]] = mapped_column(
        Time, comment="Confirmed courier call-in time"
    )
    deliveryAgent_productcode: Mapped[Optional[str]] = mapped_column(
        String(10), comment="A code that identifies which shipment service was used"
    )
    deliveryAgent_flightCodePersonId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="The person who created the AWB (for auditing)"
    )
    extra: Mapped[Optional[str]] = mapped_column(
        LONGTEXT,
        comment="JSON column for facility-specific or hard-to-define attributes",
    )

    Project_: Mapped[List["Project"]] = relationship(
        "Project", secondary="Project_has_Shipping", back_populates="Shipping"
    )
    BLSession_: Mapped[List["BLSession"]] = relationship(
        "BLSession", secondary="ShippingHasSession", back_populates="Shipping"
    )
    Person_: Mapped["Person"] = relationship("Person", back_populates="Shipping")
    Proposal_: Mapped["Proposal"] = relationship("Proposal", back_populates="Shipping")
    LabContact_: Mapped["LabContact"] = relationship(
        "LabContact", foreign_keys=[returnLabContactId], back_populates="Shipping"
    )
    LabContact1: Mapped["LabContact"] = relationship(
        "LabContact", foreign_keys=[sendingLabContactId], back_populates="Shipping_"
    )
    CourierTermsAccepted: Mapped[List["CourierTermsAccepted"]] = relationship(
        "CourierTermsAccepted", back_populates="Shipping_"
    )
    Dewar: Mapped[List["Dewar"]] = relationship("Dewar", back_populates="Shipping_")


class XFEFluorescenceSpectrum(Base):
    __tablename__ = "XFEFluorescenceSpectrum"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleId"],
            ["BLSample.blSampleId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="XFE_ibfk_2",
        ),
        ForeignKeyConstraint(
            ["blSubSampleId"], ["BLSubSample.blSubSampleId"], name="XFE_ibfk_3"
        ),
        ForeignKeyConstraint(
            ["sessionId"],
            ["BLSession.sessionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="XFE_ibfk_1",
        ),
        Index("XFEFluorescnceSpectrum_FKIndex1", "blSampleId"),
        Index("XFEFluorescnceSpectrum_FKIndex2", "sessionId"),
        Index("XFE_ibfk_3", "blSubSampleId"),
    )

    xfeFluorescenceSpectrumId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    sessionId: Mapped[int] = mapped_column(INTEGER)
    blSampleId: Mapped[Optional[int]] = mapped_column(INTEGER)
    jpegScanFileFullPath: Mapped[Optional[str]] = mapped_column(String(255))
    startTime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    endTime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    filename: Mapped[Optional[str]] = mapped_column(String(255))
    exposureTime: Mapped[Optional[float]] = mapped_column(Float)
    axisPosition: Mapped[Optional[float]] = mapped_column(Float)
    beamTransmission: Mapped[Optional[float]] = mapped_column(Float)
    annotatedPymcaXfeSpectrum: Mapped[Optional[str]] = mapped_column(String(255))
    fittedDataFileFullPath: Mapped[Optional[str]] = mapped_column(String(255))
    scanFileFullPath: Mapped[Optional[str]] = mapped_column(String(255))
    energy: Mapped[Optional[float]] = mapped_column(Float)
    beamSizeVertical: Mapped[Optional[float]] = mapped_column(Float)
    beamSizeHorizontal: Mapped[Optional[float]] = mapped_column(Float)
    crystalClass: Mapped[Optional[str]] = mapped_column(String(20))
    comments: Mapped[Optional[str]] = mapped_column(String(1024))
    blSubSampleId: Mapped[Optional[int]] = mapped_column(INTEGER)
    flux: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="flux measured before the xrfSpectra"
    )
    flux_end: Mapped[Optional[decimal.Decimal]] = mapped_column(
        Double(asdecimal=True), comment="flux measured after the xrfSpectra"
    )
    workingDirectory: Mapped[Optional[str]] = mapped_column(String(512))

    Project_: Mapped[List["Project"]] = relationship(
        "Project",
        secondary="Project_has_XFEFSpectrum",
        back_populates="XFEFluorescenceSpectrum",
    )
    BLSample_: Mapped["BLSample"] = relationship(
        "BLSample", back_populates="XFEFluorescenceSpectrum"
    )
    BLSubSample_: Mapped["BLSubSample"] = relationship(
        "BLSubSample", back_populates="XFEFluorescenceSpectrum"
    )
    BLSession_: Mapped["BLSession"] = relationship(
        "BLSession", back_populates="XFEFluorescenceSpectrum"
    )


class BLSampleTypeHasComponent(Base):
    __tablename__ = "BLSampleType_has_Component"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleTypeId"],
            ["Crystal.crystalId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="blSampleType_has_Component_fk1",
        ),
        ForeignKeyConstraint(
            ["componentId"],
            ["Protein.proteinId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="blSampleType_has_Component_fk2",
        ),
        Index("blSampleType_has_Component_fk2", "componentId"),
    )

    blSampleTypeId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    componentId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    abundance: Mapped[Optional[float]] = mapped_column(Float)

    Crystal_: Mapped["Crystal"] = relationship(
        "Crystal", back_populates="BLSampleType_has_Component"
    )
    Protein_: Mapped["Protein"] = relationship(
        "Protein", back_populates="BLSampleType_has_Component"
    )


class BLSampleHasEnergyScan(Base):
    __tablename__ = "BLSample_has_EnergyScan"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleId"],
            ["BLSample.blSampleId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSample_has_EnergyScan_ibfk_1",
        ),
        ForeignKeyConstraint(
            ["energyScanId"],
            ["EnergyScan.energyScanId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="BLSample_has_EnergyScan_ibfk_2",
        ),
        Index("BLSample_has_EnergyScan_FKIndex1", "blSampleId"),
        Index("BLSample_has_EnergyScan_FKIndex2", "energyScanId"),
    )

    blSampleId: Mapped[int] = mapped_column(INTEGER, server_default=text("'0'"))
    energyScanId: Mapped[int] = mapped_column(INTEGER, server_default=text("'0'"))
    blSampleHasEnergyScanId: Mapped[int] = mapped_column(Integer, primary_key=True)

    BLSample_: Mapped["BLSample"] = relationship(
        "BLSample", back_populates="BLSample_has_EnergyScan"
    )
    EnergyScan_: Mapped["EnergyScan"] = relationship(
        "EnergyScan", back_populates="BLSample_has_EnergyScan"
    )


class CourierTermsAccepted(Base):
    __tablename__ = "CourierTermsAccepted"
    __table_args__ = (
        ForeignKeyConstraint(
            ["personId"], ["Person.personId"], name="CourierTermsAccepted_ibfk_2"
        ),
        ForeignKeyConstraint(
            ["proposalId"], ["Proposal.proposalId"], name="CourierTermsAccepted_ibfk_1"
        ),
        ForeignKeyConstraint(
            ["shippingId"],
            ["Shipping.shippingId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="CourierTermsAccepted_ibfk_3",
        ),
        Index("CourierTermsAccepted_ibfk_1", "proposalId"),
        Index("CourierTermsAccepted_ibfk_2", "personId"),
        Index("CourierTermsAccepted_ibfk_3", "shippingId"),
        {"comment": "Records acceptances of the courier T and C"},
    )

    courierTermsAcceptedId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    proposalId: Mapped[int] = mapped_column(INTEGER)
    personId: Mapped[int] = mapped_column(INTEGER)
    shippingName: Mapped[Optional[str]] = mapped_column(String(100))
    timestamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    shippingId: Mapped[Optional[int]] = mapped_column(INTEGER)

    Person_: Mapped["Person"] = relationship(
        "Person", back_populates="CourierTermsAccepted"
    )
    Proposal_: Mapped["Proposal"] = relationship(
        "Proposal", back_populates="CourierTermsAccepted"
    )
    Shipping_: Mapped["Shipping"] = relationship(
        "Shipping", back_populates="CourierTermsAccepted"
    )


class CrystalComposition(Base):
    __tablename__ = "CrystalComposition"
    __table_args__ = (
        ForeignKeyConstraint(
            ["componentId"], ["Component.componentId"], name="CrystalComposition_ibfk_1"
        ),
        ForeignKeyConstraint(
            ["concentrationTypeId"],
            ["ConcentrationType.concentrationTypeId"],
            name="CrystalComposition_ibfk_3",
        ),
        ForeignKeyConstraint(
            ["crystalId"], ["Crystal.crystalId"], name="CrystalComposition_ibfk_2"
        ),
        Index("componentId", "componentId"),
        Index("concentrationTypeId", "concentrationTypeId"),
        Index("crystalId", "crystalId"),
        {
            "comment": "Links a crystal to its components with a specified abundance or "
            "ratio."
        },
    )

    crystalCompositionId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    componentId: Mapped[int] = mapped_column(INTEGER)
    crystalId: Mapped[int] = mapped_column(INTEGER)
    concentrationTypeId: Mapped[Optional[int]] = mapped_column(INTEGER)
    abundance: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="Abundance or concentration in the unit defined by concentrationTypeId.",
    )
    ratio: Mapped[Optional[float]] = mapped_column(Float)
    pH: Mapped[Optional[float]] = mapped_column(Float)

    Component_: Mapped["Component"] = relationship(
        "Component", back_populates="CrystalComposition"
    )
    ConcentrationType_: Mapped["ConcentrationType"] = relationship(
        "ConcentrationType", back_populates="CrystalComposition"
    )
    Crystal_: Mapped["Crystal"] = relationship(
        "Crystal", back_populates="CrystalComposition"
    )


class CrystalHasUUID(Base):
    __tablename__ = "Crystal_has_UUID"
    __table_args__ = (
        ForeignKeyConstraint(
            ["crystalId"],
            ["Crystal.crystalId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ibfk_1",
        ),
        Index("Crystal_has_UUID_FKIndex1", "crystalId"),
        Index("Crystal_has_UUID_FKIndex2", "UUID"),
    )

    crystal_has_UUID_Id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    crystalId: Mapped[int] = mapped_column(INTEGER)
    UUID: Mapped[Optional[str]] = mapped_column(String(45))
    imageURL: Mapped[Optional[str]] = mapped_column(String(255))

    Crystal_: Mapped["Crystal"] = relationship(
        "Crystal", back_populates="Crystal_has_UUID"
    )


class Dewar(Base):
    __tablename__ = "Dewar"
    __table_args__ = (
        CheckConstraint("json_valid(`extra`)", name="Dewar_chk_1"),
        ForeignKeyConstraint(
            ["firstExperimentId"],
            ["BLSession.sessionId"],
            ondelete="SET NULL",
            onupdate="CASCADE",
            name="Dewar_fk_firstExperimentId",
        ),
        ForeignKeyConstraint(
            ["shippingId"],
            ["Shipping.shippingId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Dewar_ibfk_1",
        ),
        Index("Dewar_FKIndex1", "shippingId"),
        Index("Dewar_FKIndex2", "firstExperimentId"),
        Index("Dewar_FKIndexCode", "code"),
        Index("Dewar_FKIndexStatus", "dewarStatus"),
        Index("barCode", "barCode", unique=True),
    )

    dewarId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    shippingId: Mapped[int] = mapped_column(INTEGER)
    type: Mapped[str] = mapped_column(
        Enum("Dewar", "Toolbox", "Parcel"), server_default=text("'Dewar'")
    )
    code: Mapped[Optional[str]] = mapped_column(String(45))
    comments: Mapped[Optional[str]] = mapped_column(String(1024))
    storageLocation: Mapped[Optional[str]] = mapped_column(String(45))
    dewarStatus: Mapped[Optional[str]] = mapped_column(String(45))
    bltimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    isStorageDewar: Mapped[Optional[int]] = mapped_column(
        TINYINT(1), server_default=text("'0'")
    )
    barCode: Mapped[Optional[str]] = mapped_column(String(45))
    firstExperimentId: Mapped[Optional[int]] = mapped_column(INTEGER)
    customsValue: Mapped[Optional[int]] = mapped_column(INTEGER)
    transportValue: Mapped[Optional[int]] = mapped_column(INTEGER)
    trackingNumberToSynchrotron: Mapped[Optional[str]] = mapped_column(String(30))
    trackingNumberFromSynchrotron: Mapped[Optional[str]] = mapped_column(String(30))
    facilityCode: Mapped[Optional[str]] = mapped_column(String(20))
    weight: Mapped[Optional[float]] = mapped_column(Float, comment="dewar weight in kg")
    deliveryAgent_barcode: Mapped[Optional[str]] = mapped_column(
        String(30), comment="Courier piece barcode (not the airway bill)"
    )
    extra: Mapped[Optional[str]] = mapped_column(
        LONGTEXT,
        comment="JSON column for facility-specific or hard-to-define attributes, e.g. LN2 top-ups and contents checks",
    )

    BLSession_: Mapped["BLSession"] = relationship("BLSession", back_populates="Dewar")
    Shipping_: Mapped["Shipping"] = relationship("Shipping", back_populates="Dewar")
    Container: Mapped[List["Container"]] = relationship(
        "Container", foreign_keys="[Container.currentDewarId]", back_populates="Dewar_"
    )
    Container_: Mapped[List["Container"]] = relationship(
        "Container", foreign_keys="[Container.dewarId]", back_populates="Dewar1"
    )
    DewarTransportHistory: Mapped[List["DewarTransportHistory"]] = relationship(
        "DewarTransportHistory", back_populates="Dewar_"
    )
    ContainerHistory: Mapped[List["ContainerHistory"]] = relationship(
        "ContainerHistory", back_populates="Dewar_"
    )


class DewarRegistryHasProposal(Base):
    __tablename__ = "DewarRegistry_has_Proposal"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dewarRegistryId"],
            ["DewarRegistry.dewarRegistryId"],
            name="DewarRegistry_has_Proposal_ibfk1",
        ),
        ForeignKeyConstraint(
            ["labContactId"],
            ["LabContact.labContactId"],
            onupdate="CASCADE",
            name="DewarRegistry_has_Proposal_ibfk4",
        ),
        ForeignKeyConstraint(
            ["personId"], ["Person.personId"], name="DewarRegistry_has_Proposal_ibfk3"
        ),
        ForeignKeyConstraint(
            ["proposalId"],
            ["Proposal.proposalId"],
            name="DewarRegistry_has_Proposal_ibfk2",
        ),
        Index("DewarRegistry_has_Proposal_ibfk2", "proposalId"),
        Index("DewarRegistry_has_Proposal_ibfk3", "personId"),
        Index("DewarRegistry_has_Proposal_ibfk4", "labContactId"),
        Index("dewarRegistryId", "dewarRegistryId", "proposalId", unique=True),
    )

    dewarRegistryHasProposalId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    dewarRegistryId: Mapped[Optional[int]] = mapped_column(INTEGER)
    proposalId: Mapped[Optional[int]] = mapped_column(INTEGER)
    personId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Person registering the dewar"
    )
    recordTimestamp: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    labContactId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Owner of the dewar"
    )

    DewarRegistry_: Mapped["DewarRegistry"] = relationship(
        "DewarRegistry", back_populates="DewarRegistry_has_Proposal"
    )
    LabContact_: Mapped["LabContact"] = relationship(
        "LabContact", back_populates="DewarRegistry_has_Proposal"
    )
    Person_: Mapped["Person"] = relationship(
        "Person", back_populates="DewarRegistry_has_Proposal"
    )
    Proposal_: Mapped["Proposal"] = relationship(
        "Proposal", back_populates="DewarRegistry_has_Proposal"
    )


class DewarReport(Base):
    __tablename__ = "DewarReport"
    __table_args__ = (
        ForeignKeyConstraint(
            ["facilityCode"],
            ["DewarRegistry.facilityCode"],
            ondelete="CASCADE",
            name="DewarReport_ibfk_1",
        ),
        Index("DewarReportIdx1", "facilityCode"),
    )

    dewarReportId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    facilityCode: Mapped[str] = mapped_column(String(20))
    bltimestamp: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    report: Mapped[Optional[str]] = mapped_column(Text)
    attachment: Mapped[Optional[str]] = mapped_column(String(255))

    DewarRegistry_: Mapped["DewarRegistry"] = relationship(
        "DewarRegistry", back_populates="DewarReport"
    )


class GridInfo(Base):
    __tablename__ = "GridInfo"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dataCollectionGroupId"],
            ["DataCollectionGroup.dataCollectionGroupId"],
            name="GridInfo_ibfk_2",
        ),
        ForeignKeyConstraint(
            ["dataCollectionId"],
            ["DataCollection.dataCollectionId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="GridInfo_fk_dataCollectionId",
        ),
        Index("GridInfo_fk_dataCollectionId", "dataCollectionId"),
        Index("GridInfo_ibfk_2", "dataCollectionGroupId"),
        Index("workflowMeshId", "workflowMeshId"),
    )

    gridInfoId: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, comment="Primary key (auto-incremented)"
    )
    recordTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        comment="Creation or last update date/time",
    )
    xOffset: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    yOffset: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    dx_mm: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    dy_mm: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    steps_x: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    steps_y: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    meshAngle: Mapped[Optional[decimal.Decimal]] = mapped_column(Double(asdecimal=True))
    workflowMeshId: Mapped[Optional[int]] = mapped_column(INTEGER)
    orientation: Mapped[Optional[str]] = mapped_column(
        Enum("vertical", "horizontal"), server_default=text("'horizontal'")
    )
    dataCollectionGroupId: Mapped[Optional[int]] = mapped_column(Integer)
    pixelsPerMicronX: Mapped[Optional[float]] = mapped_column(Float)
    pixelsPerMicronY: Mapped[Optional[float]] = mapped_column(Float)
    snapshot_offsetXPixel: Mapped[Optional[float]] = mapped_column(Float)
    snapshot_offsetYPixel: Mapped[Optional[float]] = mapped_column(Float)
    snaked: Mapped[Optional[int]] = mapped_column(
        TINYINT(1),
        server_default=text("'0'"),
        comment="True: The images associated with the DCG were collected in a snaked pattern",
    )
    dataCollectionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    patchesX: Mapped[Optional[int]] = mapped_column(
        Integer,
        server_default=text("'1'"),
        comment="Number of patches the grid is made up of in the X direction",
    )
    patchesY: Mapped[Optional[int]] = mapped_column(
        Integer,
        server_default=text("'1'"),
        comment="Number of patches the grid is made up of in the Y direction",
    )
    micronsPerPixelX: Mapped[Optional[float]] = mapped_column(Float)
    micronsPerPixelY: Mapped[Optional[float]] = mapped_column(Float)

    DataCollectionGroup_: Mapped["DataCollectionGroup"] = relationship(
        "DataCollectionGroup", back_populates="GridInfo"
    )
    DataCollection_: Mapped["DataCollection"] = relationship(
        "DataCollection", back_populates="GridInfo"
    )
    XRFFluorescenceMapping: Mapped[List["XRFFluorescenceMapping"]] = relationship(
        "XRFFluorescenceMapping", back_populates="GridInfo_"
    )


class ParticleClassification(Base):
    __tablename__ = "ParticleClassification"
    __table_args__ = (
        ForeignKeyConstraint(
            ["particleClassificationGroupId"],
            ["ParticleClassificationGroup.particleClassificationGroupId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ParticleClassification_fk_particleClassificationGroupId",
        ),
        Index(
            "ParticleClassification_fk_particleClassificationGroupId",
            "particleClassificationGroupId",
        ),
        {"comment": "Results of 2D or 2D classification"},
    )

    particleClassificationId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    classNumber: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Identified of the class. A unique ID given by Relion"
    )
    classImageFullPath: Mapped[Optional[str]] = mapped_column(
        String(255), comment="The PNG of the class"
    )
    particlesPerClass: Mapped[Optional[int]] = mapped_column(
        INTEGER,
        comment="Number of particles within the selected class, can then be used together with the total number above to calculate the percentage",
    )
    rotationAccuracy: Mapped[Optional[float]] = mapped_column(Float, comment="???")
    translationAccuracy: Mapped[Optional[float]] = mapped_column(
        Float, comment="Unit: Angstroms"
    )
    estimatedResolution: Mapped[Optional[float]] = mapped_column(
        Float, comment="???, Unit: Angstroms"
    )
    overallFourierCompleteness: Mapped[Optional[float]] = mapped_column(Float)
    particleClassificationGroupId: Mapped[Optional[int]] = mapped_column(INTEGER)
    classDistribution: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="Provides a figure of merit for the class, higher number is better",
    )
    selected: Mapped[Optional[int]] = mapped_column(
        TINYINT(1),
        server_default=text("'0'"),
        comment="Indicates whether the class is selected for further processing or not",
    )
    bFactorFitIntercept: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="Intercept of quadratic fit to refinement resolution against the logarithm of the number of particles",
    )
    bFactorFitLinear: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="Linear coefficient of quadratic fit to refinement resolution against the logarithm of the number of particles, equal to half of the B factor",
    )
    bFactorFitQuadratic: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="Quadratic coefficient of quadratic fit to refinement resolution against the logarithm of the number of particles",
    )

    CryoemInitialModel_: Mapped[List["CryoemInitialModel"]] = relationship(
        "CryoemInitialModel",
        secondary="ParticleClassification_has_CryoemInitialModel",
        back_populates="ParticleClassification",
    )
    ParticleClassificationGroup_: Mapped["ParticleClassificationGroup"] = relationship(
        "ParticleClassificationGroup", back_populates="ParticleClassification"
    )
    BFactorFit: Mapped[List["BFactorFit"]] = relationship(
        "BFactorFit", back_populates="ParticleClassification_"
    )


t_Project_has_DCGroup = Table(
    "Project_has_DCGroup",
    Base.metadata,
    Column("projectId", INTEGER, primary_key=True, nullable=False),
    Column("dataCollectionGroupId", Integer, primary_key=True, nullable=False),
    ForeignKeyConstraint(
        ["dataCollectionGroupId"],
        ["DataCollectionGroup.dataCollectionGroupId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="Project_has_DCGroup_FK2",
    ),
    ForeignKeyConstraint(
        ["projectId"],
        ["Project.projectId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="Project_has_DCGroup_FK1",
    ),
    Index("Project_has_DCGroup_FK2", "dataCollectionGroupId"),
)


t_Project_has_EnergyScan = Table(
    "Project_has_EnergyScan",
    Base.metadata,
    Column("projectId", INTEGER, primary_key=True, nullable=False),
    Column("energyScanId", INTEGER, primary_key=True, nullable=False),
    ForeignKeyConstraint(
        ["energyScanId"],
        ["EnergyScan.energyScanId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="project_has_energyscan_FK2",
    ),
    ForeignKeyConstraint(
        ["projectId"],
        ["Project.projectId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="project_has_energyscan_FK1",
    ),
    Index("project_has_energyscan_FK2", "energyScanId"),
)


t_Project_has_Shipping = Table(
    "Project_has_Shipping",
    Base.metadata,
    Column("projectId", INTEGER, primary_key=True, nullable=False),
    Column("shippingId", INTEGER, primary_key=True, nullable=False),
    ForeignKeyConstraint(
        ["projectId"],
        ["Project.projectId"],
        ondelete="CASCADE",
        name="project_has_shipping_FK1",
    ),
    ForeignKeyConstraint(
        ["shippingId"],
        ["Shipping.shippingId"],
        ondelete="CASCADE",
        name="project_has_shipping_FK2",
    ),
    Index("project_has_shipping_FK2", "shippingId"),
)


t_Project_has_XFEFSpectrum = Table(
    "Project_has_XFEFSpectrum",
    Base.metadata,
    Column("projectId", INTEGER, primary_key=True, nullable=False),
    Column("xfeFluorescenceSpectrumId", INTEGER, primary_key=True, nullable=False),
    ForeignKeyConstraint(
        ["projectId"],
        ["Project.projectId"],
        ondelete="CASCADE",
        name="project_has_xfefspectrum_FK1",
    ),
    ForeignKeyConstraint(
        ["xfeFluorescenceSpectrumId"],
        ["XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId"],
        ondelete="CASCADE",
        name="project_has_xfefspectrum_FK2",
    ),
    Index("project_has_xfefspectrum_FK2", "xfeFluorescenceSpectrumId"),
)


class ScreenComponent(Base):
    __tablename__ = "ScreenComponent"
    __table_args__ = (
        ForeignKeyConstraint(
            ["componentId"], ["Protein.proteinId"], name="ScreenComponent_fk2"
        ),
        ForeignKeyConstraint(
            ["screenComponentGroupId"],
            ["ScreenComponentGroup.screenComponentGroupId"],
            name="ScreenComponent_fk1",
        ),
        Index("ScreenComponent_fk1", "screenComponentGroupId"),
        Index("ScreenComponent_fk2", "componentId"),
    )

    screenComponentId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    screenComponentGroupId: Mapped[int] = mapped_column(INTEGER)
    componentId: Mapped[Optional[int]] = mapped_column(INTEGER)
    concentration: Mapped[Optional[float]] = mapped_column(Float)
    pH: Mapped[Optional[float]] = mapped_column(Float)

    Protein_: Mapped["Protein"] = relationship(
        "Protein", back_populates="ScreenComponent"
    )
    ScreenComponentGroup_: Mapped["ScreenComponentGroup"] = relationship(
        "ScreenComponentGroup", back_populates="ScreenComponent"
    )


t_ShippingHasSession = Table(
    "ShippingHasSession",
    Base.metadata,
    Column("shippingId", INTEGER, primary_key=True, nullable=False),
    Column("sessionId", INTEGER, primary_key=True, nullable=False),
    ForeignKeyConstraint(
        ["sessionId"],
        ["BLSession.sessionId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="ShippingHasSession_ibfk_2",
    ),
    ForeignKeyConstraint(
        ["shippingId"],
        ["Shipping.shippingId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="ShippingHasSession_ibfk_1",
    ),
    Index("ShippingHasSession_FKIndex2", "sessionId"),
)


class XrayCentring(Base):
    __tablename__ = "XrayCentring"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dataCollectionGroupId"],
            ["DataCollectionGroup.dataCollectionGroupId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="XrayCentring_ibfk_1",
        ),
        Index("dataCollectionGroupId", "dataCollectionGroupId"),
        {"comment": "Xray Centring analysis associated with one or more grid scans."},
    )

    xrayCentringId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    dataCollectionGroupId: Mapped[int] = mapped_column(
        Integer, comment="references DataCollectionGroup table"
    )
    status: Mapped[Optional[str]] = mapped_column(ENUM("success", "failed", "pending"))
    xrayCentringType: Mapped[Optional[str]] = mapped_column(ENUM("2d", "3d"))

    DataCollectionGroup_: Mapped["DataCollectionGroup"] = relationship(
        "DataCollectionGroup", back_populates="XrayCentring"
    )
    XrayCentringResult: Mapped[List["XrayCentringResult"]] = relationship(
        "XrayCentringResult", back_populates="XrayCentring_"
    )


class BFactorFit(Base):
    __tablename__ = "BFactorFit"
    __table_args__ = (
        ForeignKeyConstraint(
            ["particleClassificationId"],
            ["ParticleClassification.particleClassificationId"],
            name="BFactorFit_fk_particleClassificationId",
        ),
        Index("BFactorFit_fk_particleClassificationId", "particleClassificationId"),
        {
            "comment": "CryoEM reconstruction resolution as a function of the number of "
            "particles for the creation of a Rosenthal-Henderson plot and the "
            "calculation of B-factors"
        },
    )

    bFactorFitId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    particleClassificationId: Mapped[int] = mapped_column(INTEGER)
    resolution: Mapped[Optional[float]] = mapped_column(
        Float, comment="Resolution of a refined map using a given number of particles"
    )
    numberOfParticles: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Number of particles used in refinement"
    )
    particleBatchSize: Mapped[Optional[int]] = mapped_column(
        INTEGER,
        comment="Number of particles in the batch that the B-factor analysis was performed on",
    )

    ParticleClassification_: Mapped["ParticleClassification"] = relationship(
        "ParticleClassification", back_populates="BFactorFit"
    )


class Container(Base):
    __tablename__ = "Container"
    __table_args__ = (
        ForeignKeyConstraint(
            ["containerRegistryId"],
            ["ContainerRegistry.containerRegistryId"],
            name="Container_ibfk8",
        ),
        ForeignKeyConstraint(
            ["containerTypeId"],
            ["ContainerType.containerTypeId"],
            name="Container_ibfk10",
        ),
        ForeignKeyConstraint(
            ["currentDewarId"], ["Dewar.dewarId"], name="Container_fk_currentDewarId"
        ),
        ForeignKeyConstraint(
            ["dewarId"],
            ["Dewar.dewarId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="Container_ibfk_1",
        ),
        ForeignKeyConstraint(
            ["experimentTypeId"],
            ["ExperimentType.experimentTypeId"],
            name="Container_fk_experimentTypeId",
        ),
        ForeignKeyConstraint(["imagerId"], ["Imager.imagerId"], name="Container_ibfk4"),
        ForeignKeyConstraint(["ownerId"], ["Person.personId"], name="Container_ibfk5"),
        ForeignKeyConstraint(
            ["parentContainerId"],
            ["Container.containerId"],
            name="Container_fk_parentContainerId",
        ),
        ForeignKeyConstraint(
            ["priorityPipelineId"],
            ["ProcessingPipeline.processingPipelineId"],
            name="Container_ibfk9",
        ),
        ForeignKeyConstraint(
            ["requestedImagerId"], ["Imager.imagerId"], name="Container_ibfk7"
        ),
        ForeignKeyConstraint(
            ["scheduleId"], ["Schedule.scheduleId"], name="Container_ibfk3"
        ),
        ForeignKeyConstraint(["screenId"], ["Screen.screenId"], name="Container_ibfk2"),
        ForeignKeyConstraint(
            ["sessionId"],
            ["BLSession.sessionId"],
            ondelete="SET NULL",
            onupdate="CASCADE",
            name="Container_ibfk6",
        ),
        Index("Container_FKIndex", "beamlineLocation"),
        Index("Container_FKIndex1", "dewarId"),
        Index("Container_FKIndexStatus", "containerStatus"),
        Index("Container_UNIndex1", "barcode", unique=True),
        Index("Container_fk_currentDewarId", "currentDewarId"),
        Index("Container_fk_experimentTypeId", "experimentTypeId"),
        Index("Container_fk_parentContainerId", "parentContainerId"),
        Index("Container_ibfk10", "containerTypeId"),
        Index("Container_ibfk2", "screenId"),
        Index("Container_ibfk3", "scheduleId"),
        Index("Container_ibfk4", "imagerId"),
        Index("Container_ibfk5", "ownerId"),
        Index("Container_ibfk6", "sessionId"),
        Index("Container_ibfk7", "requestedImagerId"),
        Index("Container_ibfk8", "containerRegistryId"),
        Index("Container_ibfk9", "priorityPipelineId"),
    )

    containerId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    dewarId: Mapped[Optional[int]] = mapped_column(INTEGER)
    code: Mapped[Optional[str]] = mapped_column(String(45))
    containerType: Mapped[Optional[str]] = mapped_column(String(20))
    capacity: Mapped[Optional[int]] = mapped_column(INTEGER)
    sampleChangerLocation: Mapped[Optional[str]] = mapped_column(String(20))
    containerStatus: Mapped[Optional[str]] = mapped_column(String(45))
    bltimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    beamlineLocation: Mapped[Optional[str]] = mapped_column(String(20))
    screenId: Mapped[Optional[int]] = mapped_column(INTEGER)
    scheduleId: Mapped[Optional[int]] = mapped_column(INTEGER)
    barcode: Mapped[Optional[str]] = mapped_column(String(45))
    imagerId: Mapped[Optional[int]] = mapped_column(INTEGER)
    sessionId: Mapped[Optional[int]] = mapped_column(INTEGER)
    ownerId: Mapped[Optional[int]] = mapped_column(INTEGER)
    requestedImagerId: Mapped[Optional[int]] = mapped_column(INTEGER)
    requestedReturn: Mapped[Optional[int]] = mapped_column(
        TINYINT(1),
        server_default=text("'0'"),
        comment="True for requesting return, False means container will be disposed",
    )
    comments: Mapped[Optional[str]] = mapped_column(String(255))
    experimentType: Mapped[Optional[str]] = mapped_column(String(20))
    storageTemperature: Mapped[Optional[float]] = mapped_column(
        Float, comment="NULL=ambient"
    )
    containerRegistryId: Mapped[Optional[int]] = mapped_column(INTEGER)
    scLocationUpdated: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    priorityPipelineId: Mapped[Optional[int]] = mapped_column(
        INTEGER,
        server_default=text("'6'"),
        comment="Processing pipeline to prioritise, defaults to 6 which is xia2/DIALS",
    )
    experimentTypeId: Mapped[Optional[int]] = mapped_column(INTEGER)
    containerTypeId: Mapped[Optional[int]] = mapped_column(INTEGER)
    currentDewarId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="The dewar with which the container is currently associated"
    )
    parentContainerId: Mapped[Optional[int]] = mapped_column(INTEGER)

    BLSample_: Mapped[List["BLSample"]] = relationship(
        "BLSample", back_populates="Container"
    )
    ContainerRegistry_: Mapped["ContainerRegistry"] = relationship(
        "ContainerRegistry", back_populates="Container"
    )
    ContainerType_: Mapped["ContainerType"] = relationship(
        "ContainerType", back_populates="Container"
    )
    Dewar_: Mapped["Dewar"] = relationship(
        "Dewar", foreign_keys=[currentDewarId], back_populates="Container"
    )
    Dewar1: Mapped["Dewar"] = relationship(
        "Dewar", foreign_keys=[dewarId], back_populates="Container_"
    )
    ExperimentType_: Mapped["ExperimentType"] = relationship(
        "ExperimentType", back_populates="Container"
    )
    Imager_: Mapped["Imager"] = relationship(
        "Imager", foreign_keys=[imagerId], back_populates="Container"
    )
    Person_: Mapped["Person"] = relationship("Person", back_populates="Container")
    Container: Mapped["Container"] = relationship(
        "Container", remote_side=[containerId], back_populates="Container_reverse"
    )
    Container_reverse: Mapped[List["Container"]] = relationship(
        "Container", remote_side=[parentContainerId], back_populates="Container"
    )
    ProcessingPipeline_: Mapped["ProcessingPipeline"] = relationship(
        "ProcessingPipeline", back_populates="Container"
    )
    Imager1: Mapped["Imager"] = relationship(
        "Imager", foreign_keys=[requestedImagerId], back_populates="Container_"
    )
    Schedule_: Mapped["Schedule"] = relationship("Schedule", back_populates="Container")
    Screen_: Mapped["Screen"] = relationship("Screen", back_populates="Container")
    BLSession_: Mapped["BLSession"] = relationship(
        "BLSession", back_populates="Container"
    )
    BF_automationFault: Mapped[List["BFAutomationFault"]] = relationship(
        "BFAutomationFault", back_populates="Container_"
    )
    ContainerHistory: Mapped[List["ContainerHistory"]] = relationship(
        "ContainerHistory", back_populates="Container_"
    )
    ContainerInspection: Mapped[List["ContainerInspection"]] = relationship(
        "ContainerInspection", back_populates="Container_"
    )
    ContainerQueue: Mapped[List["ContainerQueue"]] = relationship(
        "ContainerQueue", back_populates="Container_"
    )


class DewarTransportHistory(Base):
    __tablename__ = "DewarTransportHistory"
    __table_args__ = (
        ForeignKeyConstraint(
            ["dewarId"],
            ["Dewar.dewarId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="DewarTransportHistory_ibfk_1",
        ),
        Index("DewarTransportHistory_FKIndex1", "dewarId"),
    )

    DewarTransportHistoryId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    dewarStatus: Mapped[str] = mapped_column(String(45))
    storageLocation: Mapped[str] = mapped_column(String(45))
    arrivalDate: Mapped[datetime.datetime] = mapped_column(DateTime)
    dewarId: Mapped[Optional[int]] = mapped_column(INTEGER)

    Dewar_: Mapped["Dewar"] = relationship(
        "Dewar", back_populates="DewarTransportHistory"
    )


t_ParticleClassification_has_CryoemInitialModel = Table(
    "ParticleClassification_has_CryoemInitialModel",
    Base.metadata,
    Column("particleClassificationId", INTEGER, primary_key=True, nullable=False),
    Column("cryoemInitialModelId", INTEGER, primary_key=True, nullable=False),
    ForeignKeyConstraint(
        ["cryoemInitialModelId"],
        ["CryoemInitialModel.cryoemInitialModelId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="ParticleClassification_has_InitialModel_fk2",
    ),
    ForeignKeyConstraint(
        ["particleClassificationId"],
        ["ParticleClassification.particleClassificationId"],
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="ParticleClassification_has_CryoemInitialModel_fk1",
    ),
    Index("ParticleClassification_has_InitialModel_fk2", "cryoemInitialModelId"),
)


class XRFFluorescenceMapping(Base):
    __tablename__ = "XRFFluorescenceMapping"
    __table_args__ = (
        ForeignKeyConstraint(
            ["autoProcProgramId"],
            ["AutoProcProgram.autoProcProgramId"],
            name="XRFFluorescenceMapping_ibfk3",
        ),
        ForeignKeyConstraint(
            ["gridInfoId"], ["GridInfo.gridInfoId"], name="XRFFluorescenceMapping_ibfk2"
        ),
        ForeignKeyConstraint(
            ["xrfFluorescenceMappingROIId"],
            ["XRFFluorescenceMappingROI.xrfFluorescenceMappingROIId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="XRFFluorescenceMapping_ibfk1",
        ),
        Index("XRFFluorescenceMapping_ibfk1", "xrfFluorescenceMappingROIId"),
        Index("XRFFluorescenceMapping_ibfk2", "gridInfoId"),
        Index("XRFFluorescenceMapping_ibfk3", "autoProcProgramId"),
        {
            "comment": "An XRF map generated from an XRF Mapping ROI based on data from a "
            "gridscan of a sample"
        },
    )

    xrfFluorescenceMappingId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    xrfFluorescenceMappingROIId: Mapped[int] = mapped_column(INTEGER)
    gridInfoId: Mapped[int] = mapped_column(INTEGER)
    dataFormat: Mapped[str] = mapped_column(
        String(15),
        comment="Description of format and any compression, i.e. json+gzip for gzipped json",
    )
    data: Mapped[bytes] = mapped_column(LONGBLOB, comment="The actual data")
    opacity: Mapped[float] = mapped_column(
        Float, server_default=text("'1'"), comment="Display opacity"
    )
    points: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="The number of points available, for realtime feedback"
    )
    colourMap: Mapped[Optional[str]] = mapped_column(
        String(20), comment="Colour map for displaying the data"
    )
    min: Mapped[Optional[int]] = mapped_column(
        Integer, comment="Min value in the data for histogramming"
    )
    max: Mapped[Optional[int]] = mapped_column(
        Integer, comment="Max value in the data for histogramming"
    )
    autoProcProgramId: Mapped[Optional[int]] = mapped_column(
        INTEGER, comment="Related autoproc programid"
    )

    AutoProcProgram_: Mapped["AutoProcProgram"] = relationship(
        "AutoProcProgram", back_populates="XRFFluorescenceMapping"
    )
    GridInfo_: Mapped["GridInfo"] = relationship(
        "GridInfo", back_populates="XRFFluorescenceMapping"
    )
    XRFFluorescenceMappingROI_: Mapped["XRFFluorescenceMappingROI"] = relationship(
        "XRFFluorescenceMappingROI", back_populates="XRFFluorescenceMapping"
    )
    XFEFluorescenceComposite: Mapped[List["XFEFluorescenceComposite"]] = relationship(
        "XFEFluorescenceComposite",
        foreign_keys="[XFEFluorescenceComposite.b]",
        back_populates="XRFFluorescenceMapping_",
    )
    XFEFluorescenceComposite_: Mapped[List["XFEFluorescenceComposite"]] = relationship(
        "XFEFluorescenceComposite",
        foreign_keys="[XFEFluorescenceComposite.g]",
        back_populates="XRFFluorescenceMapping1",
    )
    XFEFluorescenceComposite1: Mapped[List["XFEFluorescenceComposite"]] = relationship(
        "XFEFluorescenceComposite",
        foreign_keys="[XFEFluorescenceComposite.r]",
        back_populates="XRFFluorescenceMapping2",
    )


class XrayCentringResult(Base):
    __tablename__ = "XrayCentringResult"
    __table_args__ = (
        ForeignKeyConstraint(
            ["xrayCentringId"],
            ["XrayCentring.xrayCentringId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="XrayCentringResult_ibfk_1",
        ),
        Index("xrayCentringId", "xrayCentringId"),
        {"comment": "Xray Centring result."},
    )

    xrayCentringResultId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    xrayCentringId: Mapped[int] = mapped_column(
        INTEGER, comment="references XrayCentring table"
    )
    centreOfMassX: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="x-coordinate corresponding to the centre of mass of the crystal (in voxels)",
    )
    centreOfMassY: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="y-coordinate corresponding to the centre of mass of the crystal (in voxels)",
    )
    centreOfMassZ: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="z-coordinate corresponding to the centre of mass of the crystal (in voxels)",
    )
    maxVoxelX: Mapped[Optional[int]] = mapped_column(
        Integer,
        comment="x-coordinate of the voxel with the maximum value within this crystal volume",
    )
    maxVoxelY: Mapped[Optional[int]] = mapped_column(
        Integer,
        comment="y-coordinate of the voxel with the maximum value within this crystal volume",
    )
    maxVoxelZ: Mapped[Optional[int]] = mapped_column(
        Integer,
        comment="z-coordinate of the voxel with the maximum value within this crystal volume",
    )
    numberOfVoxels: Mapped[Optional[int]] = mapped_column(
        Integer, comment="Number of voxels within the specified bounding box"
    )
    totalCount: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="The sum of the values of all the voxels within the specified bounding box",
    )
    boundingBoxMinX: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="Minimum x-coordinate of the bounding box containing the crystal (in voxels)",
    )
    boundingBoxMaxX: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="Maximum x-coordinate of the bounding box containing the crystal (in voxels)",
    )
    boundingBoxMinY: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="Minimum y-coordinate of the bounding box containing the crystal (in voxels)",
    )
    boundingBoxMaxY: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="Maximum y-coordinate of the bounding box containing the crystal (in voxels)",
    )
    boundingBoxMinZ: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="Minimum z-coordinate of the bounding box containing the crystal (in voxels)",
    )
    boundingBoxMaxZ: Mapped[Optional[float]] = mapped_column(
        Float,
        comment="Maximum z-coordinate of the bounding box containing the crystal (in voxels)",
    )
    status: Mapped[Optional[str]] = mapped_column(
        ENUM("success", "failure", "pending"), comment="to be removed"
    )
    gridInfoId: Mapped[Optional[int]] = mapped_column(INTEGER, comment="to be removed")

    XrayCentring_: Mapped["XrayCentring"] = relationship(
        "XrayCentring", back_populates="XrayCentringResult"
    )


class BFAutomationFault(Base):
    __tablename__ = "BF_automationFault"
    __table_args__ = (
        ForeignKeyConstraint(
            ["automationErrorId"],
            ["BF_automationError.automationErrorId"],
            name="BF_automationFault_ibfk1",
        ),
        ForeignKeyConstraint(
            ["containerId"], ["Container.containerId"], name="BF_automationFault_ibfk2"
        ),
        Index("BF_automationFault_ibfk1", "automationErrorId"),
        Index("BF_automationFault_ibfk2", "containerId"),
    )

    automationFaultId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    faultTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    automationErrorId: Mapped[Optional[int]] = mapped_column(INTEGER)
    containerId: Mapped[Optional[int]] = mapped_column(INTEGER)
    severity: Mapped[Optional[str]] = mapped_column(Enum("1", "2", "3"))
    stacktrace: Mapped[Optional[str]] = mapped_column(Text)
    resolved: Mapped[Optional[int]] = mapped_column(TINYINT(1))

    BF_automationError: Mapped["BFAutomationError"] = relationship(
        "BFAutomationError", back_populates="BF_automationFault"
    )
    Container_: Mapped["Container"] = relationship(
        "Container", back_populates="BF_automationFault"
    )


class ContainerHistory(Base):
    __tablename__ = "ContainerHistory"
    __table_args__ = (
        ForeignKeyConstraint(
            ["containerId"],
            ["Container.containerId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ContainerHistory_ibfk1",
        ),
        ForeignKeyConstraint(
            ["currentDewarId"], ["Dewar.dewarId"], name="ContainerHistory_fk_dewarId"
        ),
        Index("ContainerHistory_fk_dewarId", "currentDewarId"),
        Index("ContainerHistory_ibfk1", "containerId"),
    )

    containerHistoryId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    blTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    containerId: Mapped[Optional[int]] = mapped_column(INTEGER)
    location: Mapped[Optional[str]] = mapped_column(String(45))
    status: Mapped[Optional[str]] = mapped_column(String(45))
    beamlineName: Mapped[Optional[str]] = mapped_column(String(20))
    currentDewarId: Mapped[Optional[int]] = mapped_column(
        INTEGER,
        comment="The dewar with which the container was associated at the creation of this row",
    )

    Container_: Mapped["Container"] = relationship(
        "Container", back_populates="ContainerHistory"
    )
    Dewar_: Mapped["Dewar"] = relationship("Dewar", back_populates="ContainerHistory")


class ContainerInspection(Base):
    __tablename__ = "ContainerInspection"
    __table_args__ = (
        ForeignKeyConstraint(
            ["containerId"],
            ["Container.containerId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ContainerInspection_fk1",
        ),
        ForeignKeyConstraint(
            ["imagerId"], ["Imager.imagerId"], name="ContainerInspection_fk3"
        ),
        ForeignKeyConstraint(
            ["inspectionTypeId"],
            ["InspectionType.inspectionTypeId"],
            name="ContainerInspection_fk2",
        ),
        ForeignKeyConstraint(
            ["scheduleComponentid"],
            ["ScheduleComponent.scheduleComponentId"],
            name="ContainerInspection_fk4",
        ),
        Index("ContainerInspection_fk4", "scheduleComponentid"),
        Index("ContainerInspection_idx2", "inspectionTypeId"),
        Index("ContainerInspection_idx3", "imagerId"),
        Index(
            "ContainerInspection_idx4",
            "containerId",
            "scheduleComponentid",
            "state",
            "manual",
        ),
    )

    containerInspectionId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    containerId: Mapped[int] = mapped_column(INTEGER)
    inspectionTypeId: Mapped[int] = mapped_column(INTEGER)
    imagerId: Mapped[Optional[int]] = mapped_column(INTEGER)
    temperature: Mapped[Optional[float]] = mapped_column(Float)
    blTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    scheduleComponentid: Mapped[Optional[int]] = mapped_column(INTEGER)
    state: Mapped[Optional[str]] = mapped_column(String(20))
    priority: Mapped[Optional[int]] = mapped_column(SmallInteger)
    manual: Mapped[Optional[int]] = mapped_column(TINYINT(1))
    scheduledTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    completedTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    BLSampleImage_: Mapped[List["BLSampleImage"]] = relationship(
        "BLSampleImage", back_populates="ContainerInspection"
    )
    Container_: Mapped["Container"] = relationship(
        "Container", back_populates="ContainerInspection"
    )
    Imager_: Mapped["Imager"] = relationship(
        "Imager", back_populates="ContainerInspection"
    )
    InspectionType_: Mapped["InspectionType"] = relationship(
        "InspectionType", back_populates="ContainerInspection"
    )
    ScheduleComponent_: Mapped["ScheduleComponent"] = relationship(
        "ScheduleComponent", back_populates="ContainerInspection"
    )


class ContainerQueue(Base):
    __tablename__ = "ContainerQueue"
    __table_args__ = (
        ForeignKeyConstraint(
            ["containerId"],
            ["Container.containerId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ContainerQueue_ibfk1",
        ),
        ForeignKeyConstraint(
            ["personId"],
            ["Person.personId"],
            onupdate="CASCADE",
            name="ContainerQueue_ibfk2",
        ),
        Index("ContainerQueue_ibfk1", "containerId"),
        Index("ContainerQueue_ibfk2", "personId"),
    )

    containerQueueId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    createdTimeStamp: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    containerId: Mapped[Optional[int]] = mapped_column(INTEGER)
    personId: Mapped[Optional[int]] = mapped_column(INTEGER)
    completedTimeStamp: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)

    Container_: Mapped["Container"] = relationship(
        "Container", back_populates="ContainerQueue"
    )
    Person_: Mapped["Person"] = relationship("Person", back_populates="ContainerQueue")
    ContainerQueueSample: Mapped[List["ContainerQueueSample"]] = relationship(
        "ContainerQueueSample", back_populates="ContainerQueue_"
    )


class XFEFluorescenceComposite(Base):
    __tablename__ = "XFEFluorescenceComposite"
    __table_args__ = (
        ForeignKeyConstraint(
            ["b"],
            ["XRFFluorescenceMapping.xrfFluorescenceMappingId"],
            name="XFEFluorescenceComposite_ibfk3",
        ),
        ForeignKeyConstraint(
            ["g"],
            ["XRFFluorescenceMapping.xrfFluorescenceMappingId"],
            name="XFEFluorescenceComposite_ibfk2",
        ),
        ForeignKeyConstraint(
            ["r"],
            ["XRFFluorescenceMapping.xrfFluorescenceMappingId"],
            name="XFEFluorescenceComposite_ibfk1",
        ),
        Index("XFEFluorescenceComposite_ibfk1", "r"),
        Index("XFEFluorescenceComposite_ibfk2", "g"),
        Index("XFEFluorescenceComposite_ibfk3", "b"),
        {
            "comment": "A composite XRF map composed of three XRFFluorescenceMapping "
            "entries creating r, g, b layers"
        },
    )

    xfeFluorescenceCompositeId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    r: Mapped[int] = mapped_column(INTEGER, comment="Red layer")
    g: Mapped[int] = mapped_column(INTEGER, comment="Green layer")
    b: Mapped[int] = mapped_column(INTEGER, comment="Blue layer")
    rOpacity: Mapped[float] = mapped_column(
        Float, server_default=text("'1'"), comment="Red layer opacity"
    )
    bOpacity: Mapped[float] = mapped_column(
        Float, server_default=text("'1'"), comment="Red layer opacity"
    )
    gOpacity: Mapped[float] = mapped_column(
        Float, server_default=text("'1'"), comment="Red layer opacity"
    )
    opacity: Mapped[float] = mapped_column(
        Float, server_default=text("'1'"), comment="Total map opacity"
    )

    XRFFluorescenceMapping_: Mapped["XRFFluorescenceMapping"] = relationship(
        "XRFFluorescenceMapping",
        foreign_keys=[b],
        back_populates="XFEFluorescenceComposite",
    )
    XRFFluorescenceMapping1: Mapped["XRFFluorescenceMapping"] = relationship(
        "XRFFluorescenceMapping",
        foreign_keys=[g],
        back_populates="XFEFluorescenceComposite_",
    )
    XRFFluorescenceMapping2: Mapped["XRFFluorescenceMapping"] = relationship(
        "XRFFluorescenceMapping",
        foreign_keys=[r],
        back_populates="XFEFluorescenceComposite1",
    )


class ContainerQueueSample(Base):
    __tablename__ = "ContainerQueueSample"
    __table_args__ = (
        ForeignKeyConstraint(
            ["blSampleId"],
            ["BLSample.blSampleId"],
            name="ContainerQueueSample_blSampleId",
        ),
        ForeignKeyConstraint(
            ["blSubSampleId"],
            ["BLSubSample.blSubSampleId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ContainerQueueSample_ibfk2",
        ),
        ForeignKeyConstraint(
            ["containerQueueId"],
            ["ContainerQueue.containerQueueId"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="ContainerQueueSample_ibfk1",
        ),
        ForeignKeyConstraint(
            ["dataCollectionPlanId"],
            ["DiffractionPlan.diffractionPlanId"],
            name="ContainerQueueSample_dataCollectionPlanId",
        ),
        Index("ContainerQueueSample_blSampleId", "blSampleId"),
        Index("ContainerQueueSample_dataCollectionPlanId", "dataCollectionPlanId"),
        Index("ContainerQueueSample_ibfk1", "containerQueueId"),
        Index("ContainerQueueSample_ibfk2", "blSubSampleId"),
    )

    containerQueueSampleId: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    containerQueueId: Mapped[Optional[int]] = mapped_column(INTEGER)
    blSubSampleId: Mapped[Optional[int]] = mapped_column(INTEGER)
    status: Mapped[Optional[str]] = mapped_column(
        String(20),
        comment="The status of the queued item, i.e. skipped, reinspect. Completed / failed should be inferred from related DataCollection",
    )
    startTime: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="Start time of processing the queue item"
    )
    endTime: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, comment="End time of processing the queue item"
    )
    dataCollectionPlanId: Mapped[Optional[int]] = mapped_column(INTEGER)
    blSampleId: Mapped[Optional[int]] = mapped_column(INTEGER)

    BLSample_: Mapped["BLSample"] = relationship(
        "BLSample", back_populates="ContainerQueueSample"
    )
    BLSubSample_: Mapped["BLSubSample"] = relationship(
        "BLSubSample", back_populates="ContainerQueueSample"
    )
    ContainerQueue_: Mapped["ContainerQueue"] = relationship(
        "ContainerQueue", back_populates="ContainerQueueSample"
    )
    DiffractionPlan_: Mapped["DiffractionPlan"] = relationship(
        "DiffractionPlan", back_populates="ContainerQueueSample"
    )
