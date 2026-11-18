from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sample_out import SampleOut


T = TypeVar("T", bound="ContainerWithChildrenOut")


@_attrs_define
class ContainerWithChildrenOut:
    """
    Attributes:
        container_id (int):
        code (None | str | Unset):
        container_type (None | str | Unset):
        capacity (int | None | Unset):
        container_status (None | str | Unset):
        beamline_location (None | str | Unset):
        barcode (None | str | Unset):
        current_dewar_id (int | None | Unset):
        storage_temperature (int | None | Unset):
        sample_changer_location (None | str | Unset):
        experiment_type_id (int | None | Unset):
        comments (None | str | Unset):
        container_registry_id (int | None | Unset):
        source (None | str | Unset):
        session_id (int | None | Unset):
        imager_id (int | None | Unset):
        dewar_id (int | None | Unset):
        parent_container_id (int | None | Unset):
        children (list[SampleOut] | Unset):
    """

    container_id: int
    code: None | str | Unset = UNSET
    container_type: None | str | Unset = UNSET
    capacity: int | None | Unset = UNSET
    container_status: None | str | Unset = UNSET
    beamline_location: None | str | Unset = UNSET
    barcode: None | str | Unset = UNSET
    current_dewar_id: int | None | Unset = UNSET
    storage_temperature: int | None | Unset = UNSET
    sample_changer_location: None | str | Unset = UNSET
    experiment_type_id: int | None | Unset = UNSET
    comments: None | str | Unset = UNSET
    container_registry_id: int | None | Unset = UNSET
    source: None | str | Unset = UNSET
    session_id: int | None | Unset = UNSET
    imager_id: int | None | Unset = UNSET
    dewar_id: int | None | Unset = UNSET
    parent_container_id: int | None | Unset = UNSET
    children: list[SampleOut] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_id = self.container_id

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        container_type: None | str | Unset
        if isinstance(self.container_type, Unset):
            container_type = UNSET
        else:
            container_type = self.container_type

        capacity: int | None | Unset
        if isinstance(self.capacity, Unset):
            capacity = UNSET
        else:
            capacity = self.capacity

        container_status: None | str | Unset
        if isinstance(self.container_status, Unset):
            container_status = UNSET
        else:
            container_status = self.container_status

        beamline_location: None | str | Unset
        if isinstance(self.beamline_location, Unset):
            beamline_location = UNSET
        else:
            beamline_location = self.beamline_location

        barcode: None | str | Unset
        if isinstance(self.barcode, Unset):
            barcode = UNSET
        else:
            barcode = self.barcode

        current_dewar_id: int | None | Unset
        if isinstance(self.current_dewar_id, Unset):
            current_dewar_id = UNSET
        else:
            current_dewar_id = self.current_dewar_id

        storage_temperature: int | None | Unset
        if isinstance(self.storage_temperature, Unset):
            storage_temperature = UNSET
        else:
            storage_temperature = self.storage_temperature

        sample_changer_location: None | str | Unset
        if isinstance(self.sample_changer_location, Unset):
            sample_changer_location = UNSET
        else:
            sample_changer_location = self.sample_changer_location

        experiment_type_id: int | None | Unset
        if isinstance(self.experiment_type_id, Unset):
            experiment_type_id = UNSET
        else:
            experiment_type_id = self.experiment_type_id

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        container_registry_id: int | None | Unset
        if isinstance(self.container_registry_id, Unset):
            container_registry_id = UNSET
        else:
            container_registry_id = self.container_registry_id

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        session_id: int | None | Unset
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        imager_id: int | None | Unset
        if isinstance(self.imager_id, Unset):
            imager_id = UNSET
        else:
            imager_id = self.imager_id

        dewar_id: int | None | Unset
        if isinstance(self.dewar_id, Unset):
            dewar_id = UNSET
        else:
            dewar_id = self.dewar_id

        parent_container_id: int | None | Unset
        if isinstance(self.parent_container_id, Unset):
            parent_container_id = UNSET
        else:
            parent_container_id = self.parent_container_id

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "containerId": container_id,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if container_type is not UNSET:
            field_dict["containerType"] = container_type
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if container_status is not UNSET:
            field_dict["containerStatus"] = container_status
        if beamline_location is not UNSET:
            field_dict["beamlineLocation"] = beamline_location
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if current_dewar_id is not UNSET:
            field_dict["currentDewarId"] = current_dewar_id
        if storage_temperature is not UNSET:
            field_dict["storageTemperature"] = storage_temperature
        if sample_changer_location is not UNSET:
            field_dict["sampleChangerLocation"] = sample_changer_location
        if experiment_type_id is not UNSET:
            field_dict["experimentTypeId"] = experiment_type_id
        if comments is not UNSET:
            field_dict["comments"] = comments
        if container_registry_id is not UNSET:
            field_dict["containerRegistryId"] = container_registry_id
        if source is not UNSET:
            field_dict["source"] = source
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if imager_id is not UNSET:
            field_dict["imagerId"] = imager_id
        if dewar_id is not UNSET:
            field_dict["dewarId"] = dewar_id
        if parent_container_id is not UNSET:
            field_dict["parentContainerId"] = parent_container_id
        if children is not UNSET:
            field_dict["children"] = children

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sample_out import SampleOut

        d = dict(src_dict)
        container_id = d.pop("containerId")

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_container_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        container_type = _parse_container_type(d.pop("containerType", UNSET))

        def _parse_capacity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity = _parse_capacity(d.pop("capacity", UNSET))

        def _parse_container_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        container_status = _parse_container_status(d.pop("containerStatus", UNSET))

        def _parse_beamline_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beamline_location = _parse_beamline_location(d.pop("beamlineLocation", UNSET))

        def _parse_barcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barcode = _parse_barcode(d.pop("barcode", UNSET))

        def _parse_current_dewar_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        current_dewar_id = _parse_current_dewar_id(d.pop("currentDewarId", UNSET))

        def _parse_storage_temperature(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_temperature = _parse_storage_temperature(d.pop("storageTemperature", UNSET))

        def _parse_sample_changer_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sample_changer_location = _parse_sample_changer_location(d.pop("sampleChangerLocation", UNSET))

        def _parse_experiment_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        experiment_type_id = _parse_experiment_type_id(d.pop("experimentTypeId", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_container_registry_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        container_registry_id = _parse_container_registry_id(d.pop("containerRegistryId", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_session_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        session_id = _parse_session_id(d.pop("sessionId", UNSET))

        def _parse_imager_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        imager_id = _parse_imager_id(d.pop("imagerId", UNSET))

        def _parse_dewar_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dewar_id = _parse_dewar_id(d.pop("dewarId", UNSET))

        def _parse_parent_container_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_container_id = _parse_parent_container_id(d.pop("parentContainerId", UNSET))

        _children = d.pop("children", UNSET)
        children: list[SampleOut] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = SampleOut.from_dict(children_item_data)

                children.append(children_item)

        container_with_children_out = cls(
            container_id=container_id,
            code=code,
            container_type=container_type,
            capacity=capacity,
            container_status=container_status,
            beamline_location=beamline_location,
            barcode=barcode,
            current_dewar_id=current_dewar_id,
            storage_temperature=storage_temperature,
            sample_changer_location=sample_changer_location,
            experiment_type_id=experiment_type_id,
            comments=comments,
            container_registry_id=container_registry_id,
            source=source,
            session_id=session_id,
            imager_id=imager_id,
            dewar_id=dewar_id,
            parent_container_id=parent_container_id,
            children=children,
        )

        container_with_children_out.additional_properties = d
        return container_with_children_out

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
