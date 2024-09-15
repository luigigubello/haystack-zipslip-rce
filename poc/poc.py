from haystack.utils import fetch_archive_from_http


def zipSlip():
    doc_dir = "zip_folder"
    fetch_archive_from_http(
        url="https://github.com/luigigubello/haystack-zipslip-rce/raw/main/zipslip.tar.gz",
        output_dir=doc_dir,
    )
