"""Document constants for testing."""

from typing import ClassVar, List


class PDFTestCases:
    """PDF document test constants."""

    # Directory paths
    TEST_DOCUMENT_DIRECTORY = "tests/data/documents"

    # Local file paths
    DOCUMENT_FILE_PATHS: ClassVar[List[str]] = [
        f"{TEST_DOCUMENT_DIRECTORY}/solar_system.pdf",
        f"{TEST_DOCUMENT_DIRECTORY}/illustrated_train_article.pdf",
    ]

    # Remote URLs
    DOCUMENT_URLS: ClassVar[List[str]] = ["https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"]
