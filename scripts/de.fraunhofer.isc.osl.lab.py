from pathlib import Path

from reusable import IscCreat, IscMeta

# Provide information on the page package to be created
package_meta_data = IscMeta(
    # Package name
    name="ISC Lab",
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
    version="0.2.0",
    # Author(s)
    author=["Simon Stier", "Lukas Scheuplein"],
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
        "Item:OSW339886c2284b4f7a8fa769ddea93ebc2",      # GHS03: Oxidizing substance
        "Item:OSW75506ab31f8b4e92b5be9d0ec04ee2f9",      # GHS04: Pressurized substance
        "Item:OSW7d0c0b54f1fe4598862c536da6c18d11",      # GHS05: Corrosive substance
        "Item:OSWf4551e8c9cb4461bb64eec3fc923dfe9",      # GHS06: Poisonous substance
        "Item:OSW9bec9fe8dc6841eeb1552e39704a660a",      # GHS07: Irritant substance
        "Item:OSWf9c34cccbe9c472193d0a82c78a2eecc",      # GHS08: Health hazardous substances
        "Item:OSWad455fb51036469796892aebb78de4b0",      # GHS09: Environmentally hazardous substances
        "Category:OSW9d4553ced7324cdc9088cdb786c339f8",  # SubstanceClassification
        "Item:OSWd0deaf3e4c5448c1a968b6992f3c756a",      # Harmful to genetic material
        "Item:OSWf9580469aa2047baa4ab11b07d92e6f5",      # Highly volatile
        "Item:OSW957ba9c439f54d268eaf23229fef5948",      # Hygroscopic
        "Item:OSW645887b914d74ea2aae860f572932c73",      # Temperature sensitive
        "Item:OSW92db60f6a7e14865afc8ddb1394f5333",      # Unknown composition
        "Item:OSWf44e85b0e41d4e52aca6acbe6e8f5f1e",      # Water sensitive
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

if __name__ == "XX__main__":
    # Create the page package
    package_meta_data.create(
        creation_config=package_creation_config,
    )
    # Check if all required pages are present
    package_meta_data.check_required_pages(
        params=IscMeta.CheckRequiredPagesParams(
            creation_config=package_creation_config,
            # Enable the following line to use the package creation script for the
            #  check of listed pages in the requiredPackages instead of the
            #  package.json (which is only up-to-date after the execution of the
            #  package creation script)
            #read_listed_pages_from_script=True,
            #script_dir=Path(__file__).parent.parent.parent + "osw-package-maintenance" + "scripts"
        )
    )
