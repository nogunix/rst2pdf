Glossary term identifiers
=========================

Sphinx makes the identifier for a glossary term out of the term as it is
written, so a term with a capital letter in it has one to match.  The
index that rst2pdf generates has to link to that identifier as Sphinx
gave it, not to a version of it that has been through make_id().

See :term:`Sign Extend`, and :term:`lowercase term` for comparison.

.. glossary::

   Sign Extend
      Filling the high bits of a widened value with copies of its sign
      bit.

   lowercase term
      A term whose identifier survives being lowercased, so it works
      either way.
