"""Unit tests for rst2pdf.flowables."""

import pytest

from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.tables import TableStyle

from rst2pdf.flowables import MySpacer, SplitTable


#
# The one-row, two-column table rst2pdf builds for a bullet, a definition
# term or an admonition: a fixed gutter, and a second column written as
# None to mean "the rest of the row".
#
GUTTER = 20.0
AVAILABLE = 515.24

STYLE = TableStyle(
    [
        ['VALIGN', [0, 0], [-1, -1], 'TOP'],
        ['RIGHTPADDING', [0, 0], [1, -1], 0],
        ['BOTTOMPADDING', [0, 0], [-1, -1], -3],
    ]
)


@pytest.mark.parametrize(
    'cell',
    (
        pytest.param([MySpacer(0, 6.0)], id='measurable'),
        pytest.param(
            [Paragraph('Some text whose width is not known in advance.')],
            id='not-measurable',
        ),
    ),
)
def test_undefined_column_takes_the_rest_of_the_row(cell):
    """A column of no declared width is as wide as the others leave it.

    ReportLab works that out for itself, but only by way of a fallback it
    runs when some cell holds a thing whose width cannot be known in
    advance.  Give it a cell it can measure -- a Spacer is zero wide and
    perfectly measurable -- and it sizes the column from the content
    instead, leaving it narrower than the padding the cell charges, which
    it then refuses.  The row should come out the same width either way.
    """
    table = SplitTable([['', cell]], colWidths=[GUTTER, None], style=STYLE)

    width, _height = table.wrap(AVAILABLE, 700)

    assert width == pytest.approx(AVAILABLE)
