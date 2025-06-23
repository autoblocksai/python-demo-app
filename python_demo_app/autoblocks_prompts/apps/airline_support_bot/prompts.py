from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import pydantic

from autoblocks.prompts.v2.models import FrozenModel
from autoblocks.prompts.v2.context import PromptExecutionContext
from autoblocks.prompts.v2.manager import AutoblocksPromptManager
from autoblocks.prompts.v2.renderer import TemplateRenderer, ToolRenderer


class _AirlineSupportBotV1Params(FrozenModel):
    temperature: Union[float, int] = pydantic.Field(..., alias="temperature")
    model: str = pydantic.Field(..., alias="model")


class _AirlineSupportBotV1TemplateRenderer(TemplateRenderer):
    __name_mapper__ = {}
    def system(
        self,
    ) -> str:
        return self._render(
            "system",
        )


class _AirlineSupportBotV1ToolRenderer(ToolRenderer):
    __name_mapper__ = {}


class _AirlineSupportBotV1ExecutionContext(PromptExecutionContext[_AirlineSupportBotV1Params, _AirlineSupportBotV1TemplateRenderer, _AirlineSupportBotV1ToolRenderer]):
    __params_class__ = _AirlineSupportBotV1Params
    __template_renderer_class__ = _AirlineSupportBotV1TemplateRenderer
    __tool_renderer_class__ = _AirlineSupportBotV1ToolRenderer


class _AirlineSupportBotV1PromptManager(AutoblocksPromptManager[_AirlineSupportBotV1ExecutionContext]):
    __app_id__ = "nt1umq3cknbgqn7wnahefcb8"
    __prompt_id__ = "airline-support-bot"
    __prompt_major_version__ = "1"
    __execution_context_class__ = _AirlineSupportBotV1ExecutionContext


class AirlineSupportBotFactory:
    @staticmethod
    def create(
        major_version: Optional[str] = None,
        minor_version: str = "0",
        api_key: Optional[str] = None,
        init_timeout: Optional[float] = None,
        refresh_timeout: Optional[float] = None,
        refresh_interval: Optional[float] = None,
    ) -> _AirlineSupportBotV1PromptManager:
        kwargs: Dict[str, Any] = {}
        if api_key is not None:
            kwargs['api_key'] = api_key
        if init_timeout is not None:
            kwargs['init_timeout'] = init_timeout
        if refresh_timeout is not None:
            kwargs['refresh_timeout'] = refresh_timeout
        if refresh_interval is not None:
            kwargs['refresh_interval'] = refresh_interval

        if major_version is None:
            major_version = '1'  # Latest version

        if major_version == '1':
            return _AirlineSupportBotV1PromptManager(minor_version=minor_version, **kwargs)

        raise ValueError("Unsupported major version. Available versions: 1")
