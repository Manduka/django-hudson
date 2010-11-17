from django.test import TestCase

class XMLRunnerTest(TestCase):

    def test_logging_failure(self):
        print '<![CDATA[ I are evil!  & <> ]]>'
