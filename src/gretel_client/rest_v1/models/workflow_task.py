# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations

import json
import pprint
import re  # noqa: F401

from datetime import datetime
from inspect import getfullargspec
from typing import Optional

from pydantic import BaseModel, StrictInt, StrictStr, validator

from gretel_client.rest_v1.models.user_profile import UserProfile


class WorkflowTask(BaseModel):
    """
    WorkflowTask
    """

    id: StrictStr = ...
    workflow_run_id: StrictStr = ...
    log_location: StrictStr = ...
    status: StrictStr = ...
    action_name: StrictStr = ...
    action_type: StrictStr = ...
    error_msg: Optional[StrictStr] = None
    error_code: Optional[StrictInt] = None
    stack_trace: Optional[StrictStr] = None
    created_by: StrictStr = ...
    created_at: datetime = ...
    updated_at: Optional[datetime] = None
    pending_at: Optional[datetime] = None
    active_at: Optional[datetime] = None
    error_at: Optional[datetime] = None
    lost_at: Optional[datetime] = None
    created_by_profile: Optional[UserProfile] = None
    __properties = [
        "id",
        "workflow_run_id",
        "log_location",
        "status",
        "action_name",
        "action_type",
        "error_msg",
        "error_code",
        "stack_trace",
        "created_by",
        "created_at",
        "updated_at",
        "pending_at",
        "active_at",
        "error_at",
        "lost_at",
        "created_by_profile",
    ]

    @validator("status")
    def status_validate_enum(cls, v):
        if v not in (
            "RUN_STATUS_UNKNOWN",
            "RUN_STATUS_CREATED",
            "RUN_STATUS_PENDING",
            "RUN_STATUS_ACTIVE",
            "RUN_STATUS_ERROR",
            "RUN_STATUS_LOST",
            "RUN_STATUS_COMPLETED",
            "RUN_STATUS_CANCELLING",
            "RUN_STATUS_CANCELLED",
        ):
            raise ValueError(
                "must be one of enum values ('RUN_STATUS_UNKNOWN', 'RUN_STATUS_CREATED', 'RUN_STATUS_PENDING', 'RUN_STATUS_ACTIVE', 'RUN_STATUS_ERROR', 'RUN_STATUS_LOST', 'RUN_STATUS_COMPLETED', 'RUN_STATUS_CANCELLING', 'RUN_STATUS_CANCELLED')"
            )
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> WorkflowTask:
        """Create an instance of WorkflowTask from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of created_by_profile
        if self.created_by_profile:
            _dict["created_by_profile"] = self.created_by_profile.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WorkflowTask:
        """Create an instance of WorkflowTask from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return WorkflowTask.parse_obj(obj)

        _obj = WorkflowTask.parse_obj(
            {
                "id": obj.get("id"),
                "workflow_run_id": obj.get("workflow_run_id"),
                "log_location": obj.get("log_location"),
                "status": obj.get("status"),
                "action_name": obj.get("action_name"),
                "action_type": obj.get("action_type"),
                "error_msg": obj.get("error_msg"),
                "error_code": obj.get("error_code"),
                "stack_trace": obj.get("stack_trace"),
                "created_by": obj.get("created_by"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "pending_at": obj.get("pending_at"),
                "active_at": obj.get("active_at"),
                "error_at": obj.get("error_at"),
                "lost_at": obj.get("lost_at"),
                "created_by_profile": UserProfile.from_dict(
                    obj.get("created_by_profile")
                )
                if obj.get("created_by_profile") is not None
                else None,
            }
        )
        return _obj