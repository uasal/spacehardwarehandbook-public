Document Management
====================

Document management has long been recognized as key to success of high reliability systems, e.g.: `Johnson, S. B. (2006). The Secret of Apollo. Baltimore, Maryland, USA: Johns Hopkins University Press. <https://doi.org/10.1353/book.3214>`__

Word documents are stored in binary format and thus limit the utility of text based automation tools such as git. Word (docx) an however be a convenient document drafting tool and many legacy documents exist in docx or similar formats. To convert an existing docx file to markdown or restructured text, `pandoc <https://pandoc.org/MANUAL.html>`_ is a commonly used command line tool. One downside of pandoc, when media files are extracted, the filenames are the same. this can be mitigated by extracting the images to a unique folder as, shown in the example below:

.. code-block:: shell

    pandoc my_document.docx -o my_document.rst --extract-media=my_doc_images

Pandoc does not support markdown, but there is a less well supported pptx2md tool that shows promise: `<https://github.com/ssine/pptx2md>`__

Additional references on documentation and git documentation version control practices:

- `Adam, F., Lösch, C., & Müntinaga, H. (2023). An Open and Customizable Software Suite for Systems Engineering and Data Management. In 2023 IEEE Aerospace Conference (pp. 1-16). <https://doi.org/10.1109/AERO55745.2023.10115910>`
- `Waits, T., & Yankel, J. (2014). Continuous system and user documentation integration. In 2014 IEEE International Professional Communication Conference (IPCC) (pp. 1-5). <https://doi.org/10.1109/IPCC.2014.7020385>`
- `Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. PLOS Computational Biology, 13(6), e1005510. <https://doi.org/10.1371/journal.pcbi.1005510>`
