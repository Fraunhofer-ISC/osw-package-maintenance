from pathlib import Path

from reusable import IscCreat, IscMeta

# Provide information on the page package to be created
package_meta_data = IscMeta(
    # Package name
    name="ISC Lab Analytics",
    # Package repository name - usually the GitHub repository name
    repo="de.fraunhofer.isc.osl.lab.analytics",
    # Package ID - usually the same as repo
    id="de.fraunhofer.isc.osl.lab.analytics",
    # Package subdirectory - usually resembling parts of the package name
    subdir="base",
    # Package branch - usually "main"
    branch="main",
    # Provide a package description
    description=(
        "Extends the ISC Package 'de.fraunhofer.isc.osl.lab' with "
        "concepts and pages that are specific to the (chemical) analytics."
    ),
    # Specify the required PagePackages
    requiredPackages=[
        "de.fraunhofer.isc.osl.lab",
    ],
    # Specify the package version - use semantic versioning
    version="0.2.1",
    # Author(s)
    author=["Matthias Albert Popp", "Simon Stier"],
    # List the full page titles of the pages to be included in the package
    # You can include a comment in the same line, stating the page label
    page_titles=[
        #"Category:OSW11a53cdfbdc24524bf8ac435cbf65d9d",  # File
        #"Category:OSW11a53cdfbdc24524bf8ac435cbf65d9d",  # WikiFile
        #"Category:OSW3e3f5dd4f71842fbb8f270e511af8031",  # LocalFile
        #"Category:OSWfe72974590fd4e8ba94cd4e8366375e8",  # Dataset

        #"Category:OSW77e749fc598341ac8b6d2fff21574058",  # Software => part of world.opensemantic.base package
        #"Category:OSW8c56fd1e858f499da801691c5f2b7309",  # WebService => part of world.opensemantic.base package
       # "Category:OSW72eae3c8f41f4a22a94dbc01974ed404",  # PrefectFlow  => part of world.opensemantic.base package
       # "JsonSchema:PrefectWorkflowRuns", #  => part of world.opensemantic.base package
        #"JsonSchema:QuantityProperty", # part of world.opensemantic.core package; copy script does not work for this (main slot is missing)
        #"Property:HasTemperature",  # part of world.opensemantic.lab package
        #"Property:HasTime",  # part of world.opensemantic.lab package

        #"Category:OSW44deaa5b806d41a2a88594f562b110e9",  # Person
        #"Category:OSW3cb8cef2225e403092f098f99bc4c472",  # OrganizationalUnit
        #"Category:OSW807f1da5b42e42f296b213ab06ca873b",  # City

        #"Category:OSWd29aa2537f434fbe87c74ded34ee34cb",  # ZaaKleinauftrag
        #"Category:OSW89d01b6ec9e9412aa6fadf244f59cc78",  # ZaaLaborauftragZugewiesen
        #"Category:OSW88894b63a51d46b08b5b4b05a6b1b3c3",  # Sample => already in the package lab
        "Category:OSW5000c5d47b2f47648063e0354d9d1199",  # ZaaAcKleinauftrag 
        #"Category:OSWc11438cd6c814ed1a5a253555ee351b4",  # MetaProcessCategory => part of world.opensemantic.core package
        "Category:OSW417008476ca94a3ebe59846b4e87c3fa",  # MetaWorkflow
        "Category:OSW65f6adea07934d169b769105a4c25458",  # Workflow
        "Category:OSWba98920367be47fb8267d2e1d4bd41e5",  # IcpOes
        "Category:OSW93cdd2f874774ab3ade44427cb60f286",  # IcpOesAnGlaswolle
        "Category:OSW454ec98de37d461abe1b33add7b50f2d",  # IcpOesAnSteinwolle
        "Category:OSWe328f0e5968d474ea501ced69b001926",  # OxideFractionAnalysis
        "Category:OSWc4a5814ef07143b6879e86d6d9be9294",  # RoentgenfluoreszenzanalyseRfa

        "Category:OSWedb9c4ddc1774b11a70866f0ed8f4998",  # SamplePreparationProcess
        "Category:OSWbb4dcf3518204aacaf5b2e49d38289fb",  # ChemicalDigestion
        "Category:OSW7c7e07b4e6a44158a6243cffa397c86e",  # AcidicDigestion
        "Category:OSW883248f0a6424d90a5dd5f14a94ad7eb",  # AlkalineDigestion
        "Category:OSW5bcc582b12a440559eccbd75c6da00fd",  # LossOnIgnitionDetermination

        "Category:OSW8c89baeb38e6418184f6bdd582489b7a",  # GravimetricAndIcpDeterminationOfSilicon
        "Category:OSW65f58d16280a49ae87de52b706f65d4a",  # MassFraction
        "Category:OSWdfd2e06f0a614d9c897e5658e2433649",  # RemovalOfPartialAmount
        "Category:OSW37065ca362824d37b2d81dd8bbef1ca3",  # IcpAfterAcidicDigestion

        "Category:OSW4ef92ac53714494da09c377898bf275f",  # MeasurementProcess
        "Category:OSWb83e84ddc4cd4afd988391c98ee5eb48",  # ElementFractionAnalysis
        "Category:OSWf6fa3f8a74c848f1a5d9a5670283159a",  # Weighing
        "Category:OSW417f0e6df8bb4eb9bd6727fafdddc633",  # IcpDeterminationOfBoronContent

        "Category:OSWedb9c4ddc1774b11a70866f0ed8f4998",  # SamplePreparationProcess
        "Category:OSWa8f0708e996d4a66bc1d6e8c2e27b75c",  # MillingInAgateMill

        "Category:OSW69a417aee9f046a6819f9e95b865e0a6",  # EvaluationProcess
        "Category:OSWb6a227a110c54a4b95a9bfe0c41da102",  # CalculationOfSiliconContent
        "Category:OSW7e33cec6edee4bd2bb27c8f3bc6977b4",  # GravimetricAndIcpDeterminationOfSiliconContent

        # ToDo: add to world.opensemantic.lab package
        #"Category:OSWdd31b71b06915d0182e40d15953f3daa",  # MeasurementDevice
        #"Category:OSW7506cc847c8550bbbdba20e9c616cf85",  # Scale
    ],
)
# Provide the information needed (only) to create the page package
package_creation_config = IscCreat(
    # domain="test.kav.isc.fraunhofer.de",
    domain="wiki-dev.open-semantic-lab.org",
    # Specify the path to the working directory - where the package is stored on disk
    working_dir=Path(__file__).parents[1]
    / "packages"
    / package_meta_data.repo,
)

if __name__ == "__main__":
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
            #script_dir=Path(__file__).parent,
            #additional_script_dirs=[Path(__file__).parent.parent.parent / "osw-package-maintenance" / "scripts"],
            additional_package_dirs=[Path(__file__).parent.parent.parent / "osw-package-maintenance" / "packages"],
        )
    )
