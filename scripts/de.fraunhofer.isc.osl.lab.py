from pathlib import Path

from reusable import IscCreat, IscMeta

# Provide information on the page package to be created
package_meta_data = IscMeta(
    # Package name
    name="ISC Base",
    # Package repository name - usually the GitHub repository name
    repo="de.fraunhofer.isc.osl.lab",
    # Package ID - usually the same as repo
    id="de.fraunhofer.isc.osl.lab",
    # Package subdirectory - usually resembling parts of the package name
    subdir="base",
    # Package branch - usually "main"
    branch="main",
    # Provide a package description
    description=(
        "Extends the OpenSemanticWorld Package 'world.opensemantic.lab' with "
        "concepts and pages that are specific to the Fraunhofer ISC."
    ),
    # Specify the required PagePackages
    requiredPackages=[
        "world.opensemantic.lab",
    ],
    # Specify the package version - use semantic versioning
    version="0.1.0",
    # Author(s)
    author=["Simon Stier"],
    # List the full page titles of the pages to be included in the package
    # You can include a comment in the same line, stating the page label
    page_titles=[
        "Category:OSWd29aa2537f434fbe87c74ded34ee34cb",  # ZaaKleinauftrag
        "Category:OSW3a86b2496454417296ad2cd784194da6",  # IscZaaKavTabs
        "Category:OSW89d01b6ec9e9412aa6fadf244f59cc78",  # ZaaKleinauftragZugewiesen
        "Category:OSW2b2649b89d1e4ae4866c8cd18e1652e2",  # AnalyticsTask
        "Category:OSWbd354f0cbc7c41d38ee301be9bb3ce8d",  # ObjectStatus
        "Item:OSWfaa3d40356f64db0ae0852935ec9ccb6",      # Store
        "Item:OSW60bd050bf7c5459182fe638351d9cea7",      # SendBack
        "Item:OSWe44f5c0404d8422dbd3fafbc66687264",      # Dispose
        "Category:OSWae1ec765ea47421695e9e8af5e212cb9",  # HazardClassification
        "Item:OSWc9ccfe2e330d4ddcb33f02454fff6fcc",      # Ghs01ExplosiveSubstance
        "Item:OSW052811fa2436493aa9ddc5f035542e21",      # Ghs02FlammableSubstance
        "Category:OSW9d4553ced7324cdc9088cdb786c339f8",  # SubstanceClassification
        "Item:OSW645887b914d74ea2aae860f572932c73",      # TemperatureSensitive
        "Item:OSW92db60f6a7e14865afc8ddb1394f5333",      # UnknownComposition
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
