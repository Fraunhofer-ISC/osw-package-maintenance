from pathlib import Path

from reusable import IscCreat, IscMeta

# Provide information on the page package to be created
package_meta_data = IscMeta(
    # Package name
    name="ISC Base",
    # Package repository name - usually the GitHub repository name
    repo="de.fraunhofer.isc.osl.base",
    # Package ID - usually the same as repo
    id="de.fraunhofer.isc.osl.base",
    # Package subdirectory - usually resembling parts of the package name
    subdir="base",
    # Package branch - usually "main"
    branch="main",
    # Provide a package description
    description=(
        "Extends the OpenSemanticWorld Package 'world.opensemantic.base' with "
        "concepts and pages that are specific to the Fraunhofer ISC."
    ),
    # Specify the package version - use semantic versioning
    version="0.2.0",
    # Author(s)
    author=["Simon Stier", "Lukas Gold"],
    # List the full page titles of the pages to be included in the package
    # You can include a comment in the same line, stating the page label
    page_titles=[
        "Category:OSW52a4518aa6a6479885a13afc078d191e",  # FhgUser
        "Category:OSWf4f9c18f28594bc4923e61863ba5ddde",  # IscUser
        "Category:OSW385b58cfdd8347cf9693526411611476",  # IscLocation
        "Category:OSWfafdfdadffe140ebb129d7df7675d189",  # IscSite
        "Category:OSWf77099f7f36240b6a9fa421647535375",  # IscBuilding
        "Category:OSW0cc1cdac0822496f9d9cd7f11d8cd02b",  # IscFloor
        "Category:OSW60930f31843f4602a56a5223308ae23e",  # IscRoom
        "Category:OSW52a4518aa6a6479885a13afc078d191e",  # FhgUser
        "Category:OSWf4f9c18f28594bc4923e61863ba5ddde",  # IscUser
        "Category:OSWa13c672ad63e48378e4e0080697e977d",  # FhgGroup
        "Category:OSWa2b790323e94405caf35d87cbca7502d",  # FhgOrganizationalSubUnit
        "Category:OSW31de2378749041e7b3443cc5afb3d0fe",  # FhgDepartment
        "Category:OSW25aad9e7985140c6bbda075833d93425",  # FraunhoferInstitute
    ],
)
# Provide the information needed (only) to create the page package
package_creation_config = IscCreat(
    # Specify the path to the working directory - where the package is stored on disk
    working_dir=Path(__file__).parents[1]
    / "packages"
    / package_meta_data.repo,
)
# Create the page package
package_meta_data.create(
    creation_config=package_creation_config,
)
