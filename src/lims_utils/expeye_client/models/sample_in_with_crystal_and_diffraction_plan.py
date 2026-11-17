from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crystal_with_protein import CrystalWithProtein
    from ..models.diffraction_plan_in import DiffractionPlanIn
    from ..models.sample_image_in import SampleImageIn


T = TypeVar("T", bound="SampleInWithCrystalAndDiffractionPlan")


@_attrs_define
class SampleInWithCrystalAndDiffractionPlan:
    """
    Attributes:
        diffraction_plan_id (int | None | Unset):
        name (None | str | Unset):
        code (None | str | Unset):
        location (int | None | Unset):
        comments (None | str | Unset):
        sub_location (int | None | Unset):
        bl_sample_status (None | str | Unset):
        holder_length (float | None | Unset):
        loop_length (float | None | Unset):
        loop_type (None | str | Unset):
        wire_width (float | None | Unset):
        source (None | str | Unset):  Default: 'Expeye'.
        is_in_sample_changer (int | None | Unset):
        crystal_id (int | None | Unset):
        sample_images (list[SampleImageIn] | None | Unset):
        diffraction_plan (DiffractionPlanIn | None | Unset):
        crystal (CrystalWithProtein | None | Unset):
    """

    diffraction_plan_id: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    code: None | str | Unset = UNSET
    location: int | None | Unset = UNSET
    comments: None | str | Unset = UNSET
    sub_location: int | None | Unset = UNSET
    bl_sample_status: None | str | Unset = UNSET
    holder_length: float | None | Unset = UNSET
    loop_length: float | None | Unset = UNSET
    loop_type: None | str | Unset = UNSET
    wire_width: float | None | Unset = UNSET
    source: None | str | Unset = "Expeye"
    is_in_sample_changer: int | None | Unset = UNSET
    crystal_id: int | None | Unset = UNSET
    sample_images: list[SampleImageIn] | None | Unset = UNSET
    diffraction_plan: DiffractionPlanIn | None | Unset = UNSET
    crystal: CrystalWithProtein | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.crystal_with_protein import CrystalWithProtein  # noqa: PLC0415
        from ..models.diffraction_plan_in import DiffractionPlanIn  # noqa: PLC0415

        diffraction_plan_id: int | None | Unset
        if isinstance(self.diffraction_plan_id, Unset):
            diffraction_plan_id = UNSET
        else:
            diffraction_plan_id = self.diffraction_plan_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        location: int | None | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        sub_location: int | None | Unset
        if isinstance(self.sub_location, Unset):
            sub_location = UNSET
        else:
            sub_location = self.sub_location

        bl_sample_status: None | str | Unset
        if isinstance(self.bl_sample_status, Unset):
            bl_sample_status = UNSET
        else:
            bl_sample_status = self.bl_sample_status

        holder_length: float | None | Unset
        if isinstance(self.holder_length, Unset):
            holder_length = UNSET
        else:
            holder_length = self.holder_length

        loop_length: float | None | Unset
        if isinstance(self.loop_length, Unset):
            loop_length = UNSET
        else:
            loop_length = self.loop_length

        loop_type: None | str | Unset
        if isinstance(self.loop_type, Unset):
            loop_type = UNSET
        else:
            loop_type = self.loop_type

        wire_width: float | None | Unset
        if isinstance(self.wire_width, Unset):
            wire_width = UNSET
        else:
            wire_width = self.wire_width

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        is_in_sample_changer: int | None | Unset
        if isinstance(self.is_in_sample_changer, Unset):
            is_in_sample_changer = UNSET
        else:
            is_in_sample_changer = self.is_in_sample_changer

        crystal_id: int | None | Unset
        if isinstance(self.crystal_id, Unset):
            crystal_id = UNSET
        else:
            crystal_id = self.crystal_id

        sample_images: list[dict[str, Any]] | None | Unset
        if isinstance(self.sample_images, Unset):
            sample_images = UNSET
        elif isinstance(self.sample_images, list):
            sample_images = []
            for sample_images_type_0_item_data in self.sample_images:
                sample_images_type_0_item = sample_images_type_0_item_data.to_dict()
                sample_images.append(sample_images_type_0_item)

        else:
            sample_images = self.sample_images

        diffraction_plan: dict[str, Any] | None | Unset
        if isinstance(self.diffraction_plan, Unset):
            diffraction_plan = UNSET
        elif isinstance(self.diffraction_plan, DiffractionPlanIn):
            diffraction_plan = self.diffraction_plan.to_dict()
        else:
            diffraction_plan = self.diffraction_plan

        crystal: dict[str, Any] | None | Unset
        if isinstance(self.crystal, Unset):
            crystal = UNSET
        elif isinstance(self.crystal, CrystalWithProtein):
            crystal = self.crystal.to_dict()
        else:
            crystal = self.crystal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if diffraction_plan_id is not UNSET:
            field_dict["diffractionPlanId"] = diffraction_plan_id
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if location is not UNSET:
            field_dict["location"] = location
        if comments is not UNSET:
            field_dict["comments"] = comments
        if sub_location is not UNSET:
            field_dict["subLocation"] = sub_location
        if bl_sample_status is not UNSET:
            field_dict["blSampleStatus"] = bl_sample_status
        if holder_length is not UNSET:
            field_dict["holderLength"] = holder_length
        if loop_length is not UNSET:
            field_dict["loopLength"] = loop_length
        if loop_type is not UNSET:
            field_dict["loopType"] = loop_type
        if wire_width is not UNSET:
            field_dict["wireWidth"] = wire_width
        if source is not UNSET:
            field_dict["source"] = source
        if is_in_sample_changer is not UNSET:
            field_dict["isInSampleChanger"] = is_in_sample_changer
        if crystal_id is not UNSET:
            field_dict["crystalId"] = crystal_id
        if sample_images is not UNSET:
            field_dict["sampleImages"] = sample_images
        if diffraction_plan is not UNSET:
            field_dict["diffractionPlan"] = diffraction_plan
        if crystal is not UNSET:
            field_dict["crystal"] = crystal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crystal_with_protein import CrystalWithProtein  # noqa: PLC0415
        from ..models.diffraction_plan_in import DiffractionPlanIn  # noqa: PLC0415
        from ..models.sample_image_in import SampleImageIn  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_diffraction_plan_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        diffraction_plan_id = _parse_diffraction_plan_id(d.pop("diffractionPlanId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_location(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_sub_location(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sub_location = _parse_sub_location(d.pop("subLocation", UNSET))

        def _parse_bl_sample_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bl_sample_status = _parse_bl_sample_status(d.pop("blSampleStatus", UNSET))

        def _parse_holder_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        holder_length = _parse_holder_length(d.pop("holderLength", UNSET))

        def _parse_loop_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        loop_length = _parse_loop_length(d.pop("loopLength", UNSET))

        def _parse_loop_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        loop_type = _parse_loop_type(d.pop("loopType", UNSET))

        def _parse_wire_width(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wire_width = _parse_wire_width(d.pop("wireWidth", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_is_in_sample_changer(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        is_in_sample_changer = _parse_is_in_sample_changer(d.pop("isInSampleChanger", UNSET))

        def _parse_crystal_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        crystal_id = _parse_crystal_id(d.pop("crystalId", UNSET))

        def _parse_sample_images(data: object) -> list[SampleImageIn] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sample_images_type_0 = []
                _sample_images_type_0 = data
                for sample_images_type_0_item_data in _sample_images_type_0:
                    sample_images_type_0_item = SampleImageIn.from_dict(sample_images_type_0_item_data)

                    sample_images_type_0.append(sample_images_type_0_item)

                return sample_images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SampleImageIn] | None | Unset, data)

        sample_images = _parse_sample_images(d.pop("sampleImages", UNSET))

        def _parse_diffraction_plan(data: object) -> DiffractionPlanIn | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                diffraction_plan_type_0 = DiffractionPlanIn.from_dict(data)

                return diffraction_plan_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DiffractionPlanIn | None | Unset, data)

        diffraction_plan = _parse_diffraction_plan(d.pop("diffractionPlan", UNSET))

        def _parse_crystal(data: object) -> CrystalWithProtein | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                crystal_type_0 = CrystalWithProtein.from_dict(data)

                return crystal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CrystalWithProtein | None | Unset, data)

        crystal = _parse_crystal(d.pop("crystal", UNSET))

        sample_in_with_crystal_and_diffraction_plan = cls(
            diffraction_plan_id=diffraction_plan_id,
            name=name,
            code=code,
            location=location,
            comments=comments,
            sub_location=sub_location,
            bl_sample_status=bl_sample_status,
            holder_length=holder_length,
            loop_length=loop_length,
            loop_type=loop_type,
            wire_width=wire_width,
            source=source,
            is_in_sample_changer=is_in_sample_changer,
            crystal_id=crystal_id,
            sample_images=sample_images,
            diffraction_plan=diffraction_plan,
            crystal=crystal,
        )

        sample_in_with_crystal_and_diffraction_plan.additional_properties = d
        return sample_in_with_crystal_and_diffraction_plan

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
