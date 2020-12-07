## Migrate http://stigmaj.org/ to OSF
1. Copy `config.template.py` to `config.py`, make sure you have an OSF API token and the
guid of your OSF project.  

2. In OJS export issue metadata in crossref and doaj xml formats and store to the paths
 in `config.py` (`DOAJ_FILE` and `CROSSREF_FILE`)
 
3. Download the article pdf files from the OJS server.

4. Start `rename_pdf.py`. This will download the pdf-files to `<PDF_PATH>` and uses the Crossref XML to 
copy to `<PDF_PATH>/renamed/<doi suffix>.pdf`

5. Upload the renamed pdf files to OSF storage (drag and drop).

6. Run `osf_guid_list.py` (twice if needed) to get the OSF file guids. Will be stored in `output/name_guid.json` (`NAME_GUID_FILE`)

7. Run `create_pages_and_toc.py`. This will create wiki pages on OSF with article 
metadata and a link to the pdf and a table of contents in `TOC.md` which can be pasted to
  the wiki home page.
  
8. Run `modify_crossref.py`. This will create `output/crossref_osf.xml`, a copy
 of `xml/crossref.xml` with the URLs changed to the new OSF locations.
  
9. Upload xml-file to Crossref.
