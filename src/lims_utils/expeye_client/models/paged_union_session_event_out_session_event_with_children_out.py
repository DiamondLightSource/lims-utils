from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.session_event_out import SessionEventOut
    from ..models.session_event_with_children_out import SessionEventWithChildrenOut


T = TypeVar("T", bound="PagedUnionSessionEventOutSessionEventWithChildrenOut")


@_attrs_define
class PagedUnionSessionEventOutSessionEventWithChildrenOut:
    """
    Attributes:
        items (list[SessionEventOut | SessionEventWithChildrenOut]):
        total (int):
        page (int):
        limit (int):
    """

    items: list[SessionEventOut | SessionEventWithChildrenOut]
    total: int
    page: int
    limit: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_event_out import SessionEventOut

        items = []
        for items_item_data in self.items:
            items_item: dict[str, Any]
            if isinstance(items_item_data, SessionEventOut):
                items_item = items_item_data.to_dict()
            else:
                items_item = items_item_data.to_dict()

            items.append(items_item)

        total = self.total

        page = self.page

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "total": total,
                "page": page,
                "limit": limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_event_out import SessionEventOut
        from ..models.session_event_with_children_out import SessionEventWithChildrenOut

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:

            def _parse_items_item(data: object) -> SessionEventOut | SessionEventWithChildrenOut:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    items_item_type_0 = SessionEventOut.from_dict(data)

                    return items_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                items_item_type_1 = SessionEventWithChildrenOut.from_dict(data)

                return items_item_type_1

            items_item = _parse_items_item(items_item_data)

            items.append(items_item)

        total = d.pop("total")

        page = d.pop("page")

        limit = d.pop("limit")

        paged_union_session_event_out_session_event_with_children_out = cls(
            items=items,
            total=total,
            page=page,
            limit=limit,
        )

        paged_union_session_event_out_session_event_with_children_out.additional_properties = d
        return paged_union_session_event_out_session_event_with_children_out

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
