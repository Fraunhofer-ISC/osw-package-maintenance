from pathlib import Path
from typing import Optional

from osw.controller.page_package import PagePackageController as Package
from pydantic import FilePath


class IscMeta(Package):
    """Metadata for the isc.fraunhofer page packages"""

    # name: is required but not provided here -> needs to be set in each script
    # repo: is required but not provided here -> needs to be set in each script
    # id: is required but not provided here -> needs to be set in each script
    # subdir: is required but not provided here -> needs to be set in each script
    # branch: is required but not provided here -> needs to be set in each script
    repo_org = "Fraunhofer-ISC"
    # description: is required but not provided here -> needs to be set in each script
    language = "en"
    # version: is required but not provided here -> needs to be set in each script
    # author: is required but not provided here -> needs to be set in each script
    publisher = "Fraunhofer-ISC"
    # page_titles: is required but not provided here -> needs to be set in each script


class IscCreat(Package.CreationConfig):
    """Creation config for the isc.fraunhofer page packages"""

    domain = "wiki-dev.open-semantic-lab.org"
    credentials_file_path: Optional[FilePath] = (
        Path(__file__).parent / "accounts.pwd.yaml"
    )
    # working_dir: is required but not provided here -> needs to be set in each script
