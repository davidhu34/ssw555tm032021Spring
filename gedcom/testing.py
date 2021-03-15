from unittest import TestCase
from typing import Callable
from os.path import abspath
from .repository import GedcomRepository, read_repository_file
from .exceptions import GedcomValidationException


class GedcomTestCase(TestCase):
    ''' GEDCOM feature test cases base class '''
    repo = None

    def parse_test_file(self, file_name: str) -> GedcomRepository:
        self.repo = read_repository_file(
            abspath(f'./test_files/{file_name}.ged'))
        return self.repo

    def prepare_validation_test(self, file_name: str, validator: Callable) -> None:
        self.parse_test_file(file_name)
        if not validator:
            raise 'No validator provided for test case'

    def assert_file_validation_passes(self, file_name: str, validator: Callable) -> None:
        self.prepare_validation_test(file_name, validator)
        self.assertEqual(True, validator(self.repo))

    def assert_file_validation_fails(self, file_name: str, validator: Callable) -> None:
        self.prepare_validation_test(file_name, validator)
        self.assertRaises(GedcomValidationException, validator, self.repo)