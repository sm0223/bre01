from dateutil.zoneinfo.rebuild import rebuild
from xsdata.cli import generate
schema = "mpp.xsd"
generate(
    sources=schema,
    output="generated",
    package="icici",
    rebuild=True
)