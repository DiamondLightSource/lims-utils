from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_collection_group_out_experiment_type_type_0 import DataCollectionGroupOutExperimentTypeType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataCollectionGroupOut")


@_attrs_define
class DataCollectionGroupOut:
    """
    Attributes:
        data_collection_group_id (int): Data Collection Group ID
        session_id (int): Session ID
        experiment_type (DataCollectionGroupOutExperimentTypeType0 | None | Unset):
        experiment_type_id (int | None | Unset):
        experiment_type_name (None | str | Unset):
        comments (None | str | Unset):
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
        crystal_class (None | str | Unset):
        detector_mode (None | str | Unset):
        actual_sample_barcode (None | str | Unset):
        actual_sample_slot_in_container (int | None | Unset):
        actual_container_barcode (None | str | Unset):
        actual_sample_slot_in_sc (int | None | Unset):
        xtal_snapshot_full_path (None | str | Unset):
        scan_parameters (None | str | Unset):
        sample_id (int | None | Unset):
        collections (int | None | Unset):
        image_directory (None | str | Unset): The directory where files reside - should end with a slash
    """

    data_collection_group_id: int
    session_id: int
    experiment_type: DataCollectionGroupOutExperimentTypeType0 | None | Unset = UNSET
    experiment_type_id: int | None | Unset = UNSET
    experiment_type_name: None | str | Unset = UNSET
    comments: None | str | Unset = UNSET
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    crystal_class: None | str | Unset = UNSET
    detector_mode: None | str | Unset = UNSET
    actual_sample_barcode: None | str | Unset = UNSET
    actual_sample_slot_in_container: int | None | Unset = UNSET
    actual_container_barcode: None | str | Unset = UNSET
    actual_sample_slot_in_sc: int | None | Unset = UNSET
    xtal_snapshot_full_path: None | str | Unset = UNSET
    scan_parameters: None | str | Unset = UNSET
    sample_id: int | None | Unset = UNSET
    collections: int | None | Unset = UNSET
    image_directory: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_collection_group_id = self.data_collection_group_id

        session_id = self.session_id

        experiment_type: None | str | Unset
        if isinstance(self.experiment_type, Unset):
            experiment_type = UNSET
        elif isinstance(self.experiment_type, DataCollectionGroupOutExperimentTypeType0):
            experiment_type = self.experiment_type.value
        else:
            experiment_type = self.experiment_type

        experiment_type_id: int | None | Unset
        if isinstance(self.experiment_type_id, Unset):
            experiment_type_id = UNSET
        else:
            experiment_type_id = self.experiment_type_id

        experiment_type_name: None | str | Unset
        if isinstance(self.experiment_type_name, Unset):
            experiment_type_name = UNSET
        else:
            experiment_type_name = self.experiment_type_name

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        crystal_class: None | str | Unset
        if isinstance(self.crystal_class, Unset):
            crystal_class = UNSET
        else:
            crystal_class = self.crystal_class

        detector_mode: None | str | Unset
        if isinstance(self.detector_mode, Unset):
            detector_mode = UNSET
        else:
            detector_mode = self.detector_mode

        actual_sample_barcode: None | str | Unset
        if isinstance(self.actual_sample_barcode, Unset):
            actual_sample_barcode = UNSET
        else:
            actual_sample_barcode = self.actual_sample_barcode

        actual_sample_slot_in_container: int | None | Unset
        if isinstance(self.actual_sample_slot_in_container, Unset):
            actual_sample_slot_in_container = UNSET
        else:
            actual_sample_slot_in_container = self.actual_sample_slot_in_container

        actual_container_barcode: None | str | Unset
        if isinstance(self.actual_container_barcode, Unset):
            actual_container_barcode = UNSET
        else:
            actual_container_barcode = self.actual_container_barcode

        actual_sample_slot_in_sc: int | None | Unset
        if isinstance(self.actual_sample_slot_in_sc, Unset):
            actual_sample_slot_in_sc = UNSET
        else:
            actual_sample_slot_in_sc = self.actual_sample_slot_in_sc

        xtal_snapshot_full_path: None | str | Unset
        if isinstance(self.xtal_snapshot_full_path, Unset):
            xtal_snapshot_full_path = UNSET
        else:
            xtal_snapshot_full_path = self.xtal_snapshot_full_path

        scan_parameters: None | str | Unset
        if isinstance(self.scan_parameters, Unset):
            scan_parameters = UNSET
        else:
            scan_parameters = self.scan_parameters

        sample_id: int | None | Unset
        if isinstance(self.sample_id, Unset):
            sample_id = UNSET
        else:
            sample_id = self.sample_id

        collections: int | None | Unset
        if isinstance(self.collections, Unset):
            collections = UNSET
        else:
            collections = self.collections

        image_directory: None | str | Unset
        if isinstance(self.image_directory, Unset):
            image_directory = UNSET
        else:
            image_directory = self.image_directory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataCollectionGroupId": data_collection_group_id,
                "sessionId": session_id,
            }
        )
        if experiment_type is not UNSET:
            field_dict["experimentType"] = experiment_type
        if experiment_type_id is not UNSET:
            field_dict["experimentTypeId"] = experiment_type_id
        if experiment_type_name is not UNSET:
            field_dict["experimentTypeName"] = experiment_type_name
        if comments is not UNSET:
            field_dict["comments"] = comments
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if crystal_class is not UNSET:
            field_dict["crystalClass"] = crystal_class
        if detector_mode is not UNSET:
            field_dict["detectorMode"] = detector_mode
        if actual_sample_barcode is not UNSET:
            field_dict["actualSampleBarcode"] = actual_sample_barcode
        if actual_sample_slot_in_container is not UNSET:
            field_dict["actualSampleSlotInContainer"] = actual_sample_slot_in_container
        if actual_container_barcode is not UNSET:
            field_dict["actualContainerBarcode"] = actual_container_barcode
        if actual_sample_slot_in_sc is not UNSET:
            field_dict["actualSampleSlotInSC"] = actual_sample_slot_in_sc
        if xtal_snapshot_full_path is not UNSET:
            field_dict["xtalSnapshotFullPath"] = xtal_snapshot_full_path
        if scan_parameters is not UNSET:
            field_dict["scanParameters"] = scan_parameters
        if sample_id is not UNSET:
            field_dict["sampleId"] = sample_id
        if collections is not UNSET:
            field_dict["collections"] = collections
        if image_directory is not UNSET:
            field_dict["imageDirectory"] = image_directory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_collection_group_id = d.pop("dataCollectionGroupId")

        session_id = d.pop("sessionId")

        def _parse_experiment_type(data: object) -> DataCollectionGroupOutExperimentTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                experiment_type_type_0 = DataCollectionGroupOutExperimentTypeType0(data)

                return experiment_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DataCollectionGroupOutExperimentTypeType0 | None | Unset, data)

        experiment_type = _parse_experiment_type(d.pop("experimentType", UNSET))

        def _parse_experiment_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        experiment_type_id = _parse_experiment_type_id(d.pop("experimentTypeId", UNSET))

        def _parse_experiment_type_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        experiment_type_name = _parse_experiment_type_name(d.pop("experimentTypeName", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = datetime.datetime.fromisoformat(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = datetime.datetime.fromisoformat(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        def _parse_crystal_class(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crystal_class = _parse_crystal_class(d.pop("crystalClass", UNSET))

        def _parse_detector_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detector_mode = _parse_detector_mode(d.pop("detectorMode", UNSET))

        def _parse_actual_sample_barcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actual_sample_barcode = _parse_actual_sample_barcode(d.pop("actualSampleBarcode", UNSET))

        def _parse_actual_sample_slot_in_container(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        actual_sample_slot_in_container = _parse_actual_sample_slot_in_container(
            d.pop("actualSampleSlotInContainer", UNSET)
        )

        def _parse_actual_container_barcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actual_container_barcode = _parse_actual_container_barcode(d.pop("actualContainerBarcode", UNSET))

        def _parse_actual_sample_slot_in_sc(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        actual_sample_slot_in_sc = _parse_actual_sample_slot_in_sc(d.pop("actualSampleSlotInSC", UNSET))

        def _parse_xtal_snapshot_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        xtal_snapshot_full_path = _parse_xtal_snapshot_full_path(d.pop("xtalSnapshotFullPath", UNSET))

        def _parse_scan_parameters(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scan_parameters = _parse_scan_parameters(d.pop("scanParameters", UNSET))

        def _parse_sample_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sample_id = _parse_sample_id(d.pop("sampleId", UNSET))

        def _parse_collections(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        collections = _parse_collections(d.pop("collections", UNSET))

        def _parse_image_directory(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_directory = _parse_image_directory(d.pop("imageDirectory", UNSET))

        data_collection_group_out = cls(
            data_collection_group_id=data_collection_group_id,
            session_id=session_id,
            experiment_type=experiment_type,
            experiment_type_id=experiment_type_id,
            experiment_type_name=experiment_type_name,
            comments=comments,
            start_time=start_time,
            end_time=end_time,
            crystal_class=crystal_class,
            detector_mode=detector_mode,
            actual_sample_barcode=actual_sample_barcode,
            actual_sample_slot_in_container=actual_sample_slot_in_container,
            actual_container_barcode=actual_container_barcode,
            actual_sample_slot_in_sc=actual_sample_slot_in_sc,
            xtal_snapshot_full_path=xtal_snapshot_full_path,
            scan_parameters=scan_parameters,
            sample_id=sample_id,
            collections=collections,
            image_directory=image_directory,
        )

        data_collection_group_out.additional_properties = d
        return data_collection_group_out

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
