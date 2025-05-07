from dataclasses import dataclass

from autoblocks.api.app_client import AutoblocksAppClient
from autoblocks.testing.models import BaseTestCase
from autoblocks.testing.util import md5
from autoblocks.testing.v2.run import run_test_suite
from dotenv import load_dotenv

from python_demo_app.app import run
from python_demo_app.models import Output

load_dotenv()

client = AutoblocksAppClient(
    app_slug="doctor-gpt",
)


@dataclass
class TestCase(BaseTestCase):
    question: str
    expected_router_output: str
    expected_answer: str

    def hash(self) -> str:
        return md5(self.question)


def run_tests():
    dataset_items = client.datasets.get_items(external_id="test-cases")
    test_cases: list[TestCase] = [
        TestCase(
            question=item.data["Question"],
            expected_router_output=item.data["Expected Router Output"],
            expected_answer=item.data["Expected Answer"],
        )
        for item in dataset_items
    ]

    async def test_fn(test_case: TestCase) -> Output:
        return await run(test_case.question)

    run_test_suite(id="doctor-gpt", app_slug="doctor-gpt", test_cases=test_cases, fn=test_fn, evaluators=[])
