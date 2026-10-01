"""Hosted tool worker: serves QaConvertTemperature on the queue agent-deploy assigns.

agent-deploy injects TEMPORAL_HOST, TEMPORAL_NAMESPACE, TEMPORAL_TASK_QUEUE,
TRASE_WORKFLOW_SERVICE_URL and TRASE_INTERNAL_TOKEN into the pod.
"""

import asyncio
import logging
import os

from trase_os_sdk.activities import ActivityWorker, HttpActivityPayloadStore
from trase_os_sdk.clients.workflow_service.factory import WorkflowClientOptions, get_client
from trase_os_sdk.tools.tool_activity import LocalToolActivity

from tools.convert_temperature import QaConvertTemperature


async def main() -> None:
    client = get_client(
        token=lambda: os.environ["TRASE_INTERNAL_TOKEN"],
        options=WorkflowClientOptions(base_url=os.environ["TRASE_WORKFLOW_SERVICE_URL"]),
    )
    store = HttpActivityPayloadStore(client)
    await ActivityWorker.start(
        [LocalToolActivity(store, QaConvertTemperature(), client=client)]
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
