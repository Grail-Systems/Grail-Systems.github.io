import sys; sys.path.insert(0, "tools")
from build_county import build
C = "Oct 31, 2026"
build(dict(slug="ellis", name="Ellis", checked=C,
  title="Ellis County Watch",
  desc="Red Oak and Midlothian have become one of Texas's biggest data center clusters. Who is building, how much, and what to watch.",
  intro="South of Dallas, Red Oak and Midlothian have become one of the densest data center clusters in Texas, with Google, DataBank and Compass all building, and thousands more acres bought for future campuses.",
  counts=[("4+","major campuses built or underway"),("480 MW","DataBank's Red Oak campus at full build"),("$325M","one DataBank building filed with the state, starting Dec 2026"),("$15M","animal shelter grant Compass offered amid opposition")],
  projects=[
    (["Under construction","Records (TDLR)"],"DataBank Red Oak campus","292 acres off Stainback and Batchler roads, up to eight buildings and 480 MW. Each building is filed under its own LLC, such as DB Data Center Red Oak 12, LLC. State TDLR filings list building DFW14 at 3600 Batchler Rd at $325M, starting Dec 1, 2026."),
    (["Under construction","Records (TDLR)"],"Compass Red Oak campus","375 acres around Austin Blvd, about 360 MW. TDLR lists Building 6 at 500 Austin Blvd at $100M. Proposed a $15M grant for a county animal shelter in June 2026 amid opposition."),
    (["Operating","Reporting"],"Google Midlothian campus","On Railport Parkway, built starting in 2019 through a shell company, Alamo Mission LLC, under the project name Sharka. 375 acres plus 165 more; Phase 4 under construction."),
    (["Operating","Reporting"],"Google Red Oak campus","About 165 acres. First building operating. Part of Google's $40B Texas plan through 2027."),
    (["Land acquired","Reporting, verify"],"Cawley Partners data center park","About 5,200 acres south of Dallas, acquired in 2025.")],
  timeline=[
    ("2019","Google arrives under another name","Google's first Midlothian building was filed under Alamo Mission LLC."),
    ("2023","Compass buys 375 acres in Red Oak",""),
    ("Sept 2024","DataBank announces a 480 MW campus",""),
    ("April 2026","DataBank raises $2B","To build the first three Red Oak buildings."),
    ("May 2026","Red Oak approves a major new campus","After hours of public debate over growth, water and infrastructure."),
    ("June 2026","Compass offers a $15M shelter grant","Proposed to Ellis County amid opposition to its plans."),
    ("Dec 1, 2026","Next DataBank building due to start","Per its state TDLR filing.")],
  lessons=[
    ("State filings show buildings before they rise","TDLR's TABS database listed DataBank's $325M building with an exact address and start date. Anyone can search it by county."),
    ("Shell names hide the owner","Google built here as Alamo Mission LLC. Watch land and permit records for unfamiliar LLCs."),
    ("Get gifts in writing","A $15M grant offer is not a contract. Benefits belong in a binding agreement."),
    ("Count the whole cluster","One city can host many campuses. Ask for a study of their combined water and power use.")],
  sources="Texas Department of Licensing and Regulation TABS filings; Data Center Dynamics; Dallas Morning News; KERA (May 12, 2026); Baxtel; Cleanview; Energy Capital HTX."))
build(dict(slug="young", name="Young", checked=C,
  title="Young County Watch",
  desc="Project Saltworks: a proposed 15-building data center campus near Graham, and the residents asking where the water will come from.",
  intro="Near Graham, a developer has proposed one of the largest private investments in Young County's history: a 15-building data center campus called Project Saltworks. Residents want to know where the water will come from.",
  counts=[("~870-890","acres proposed"),("15","data center buildings"),("~$10B","reported investment"),("0","votes taken so far")],
  projects=[
    (["Proposed","Reporting"],"Project Saltworks","Stream Data Centers. About 867 to 890 acres in unincorporated Young County, south of FM 61 and north of FM 209, near Graham. Up to 15 buildings and about $10B reported.")],
  timeline=[
    ("June 22, 2026","Residents confront the developer","A crowd told commissioners and the developer the campus would take the county's water and change its way of life. Commissioners took no vote."),
    ("July 2026","Plans reported by industry press","15 buildings and about $10B in investment."),
    ("Sept 2026","State freezes data center permits","The Governor told TCEQ to pause data center permits until state grid and water audits are done.")],
  lessons=[
    ("Ask for the water source in writing","No numbers have been made public. Ask the developer, the county and any water supplier."),
    ("Raise chemicals early","Residents asked about PFAS. Ask which chemicals a cooling system will use and where its wastewater goes."),
    ("Use the state pause","With state permits paused, there is no reason for local officials to rush.")],
  sources="Graham Leader (June 22, 2026 meeting coverage); Baxtel (July 2026); Texas Tribune and KBTX on the state permit pause."))
build(dict(slug="somervell", name="Somervell", checked=C,
  title="Somervell County Watch",
  desc="Home of Comanche Peak nuclear plant and Dinosaur Valley State Park. Somervell County voted unanimously to oppose new data centers until the Legislature acts.",
  intro="Somervell County is home to the Comanche Peak nuclear plant and Dinosaur Valley State Park. After approving incentives for an Amazon project, its commissioners changed course and voted unanimously to oppose new data centers until the Legislature acts.",
  counts=[("1","unanimous resolution opposing new data centers"),("2","projects tracked"),("1","nuclear plant drawing developers")],
  projects=[
    (["Proposed","Reporting"],"Amazon near Comanche Peak","Amazon Web Services sought to build near the Comanche Peak nuclear plant. The county approved incentives tied to the project earlier in 2026."),
    (["Opposed by county","Reporting"],"Glen Rose AI data center","North of Dinosaur Valley State Park. Black Mountain Power holds an air permit near the park, which may be this project (verify).")],
  timeline=[
    ("Early 2026","Incentives approved for Amazon",""),
    ("May 11, 2026","Unanimous resolution","Commissioners opposed new data centers until the Legislature addresses water and energy concerns.")],
  lessons=[
    ("A county can change course","Somervell approved incentives, then took a public stand once residents spoke up."),
    ("Watch for power-plant magnets","Nuclear and gas plants draw data centers looking for direct power. Neighbors of any big plant should watch for co-location deals."),
    ("Protect public lands","A state park nearby gives the whole state a stake. Park users can be allies.")],
  sources="KERA (May 12, 2026); Fort Worth Weekly; Baxtel; More Than Just Parks data center tracker."))
build(dict(slug="elpaso", name="El Paso", checked=C,
  title="El Paso County Watch",
  desc="Meta's data center in Northeast El Paso: the water cap, the tax break, the jobs promise and the push for a community benefits agreement.",
  intro="Meta is building a data center campus in Northeast El Paso, near the state line, now described as a $10B, 3.1-million-square-foot buildout. It is one of the few Texas projects with a public water cap, and residents are now pushing for a community benefits agreement.",
  counts=[("2.5M","gallons a day: the water cap"),("~480,000","gallons a day expected on average"),("80%","city tax cut, for 25 years"),("50","permanent jobs required")],
  projects=[
    (["Under construction","Reporting"],"Meta El Paso","Closed-loop cooling. El Paso Water caps use at 2.5 million gallons a day and expects an average of about 480,000, rising on hot days. Earlier reporting described a 1.5 million gallon maximum. The city's incentive gives an 80% tax cut for 25 years tied to at least 50 permanent jobs; Meta has said it will employ about 300. Land was bought through Wurldwide LLC.")],
  timeline=[
    ("Late 2023","Incentives and water agreement","Meta negotiated an incentive package for an $800M initial investment and a water supply agreement with El Paso Water. The city sold the land to Wurldwide LLC for about $8.5M."),
    ("Oct 2025","Construction announced",""),
    ("2026","Council orders a community benefits agreement","Staff were directed to draft one after heavy public comment."),
    ("May 26, 2026","No more incentives for hyperscale data centers","Council voted unanimously to stop recruiting or incentivizing future hyperscale data centers."),
    ("July 2026","El Paso Water explains the numbers","The utility said it will hold Meta to the 2.5 million gallon cap."),
    ("July 20, 2026","First Data Center Policy Framework","Adopted unanimously for future projects. It does not apply to Meta, and the council separately voted to keep Meta's incentive deal.")],
  lessons=[
    ("A water cap belongs in the contract","El Paso has one. But a cap five times the expected average leaves a lot of room. Ask for caps close to real need."),
    ("Ask who pays for power","A state utility commissioner raised concern that household customers could subsidize the cost of serving the data center."),
    ("It's not too late for benefits","El Paso is negotiating a community benefits agreement after incentives were granted.")],
  sources="El Paso Matters / Texas Standard (Oct 2025); KFOX14 (2026); KVIA (July 7, 2026); El Paso Inc.; Blockspace; GovTech Insider."))
build(dict(slug="hays", name="Hays", checked=C,
  title="Hays County Watch",
  desc="San Marcos became the first Texas city to ban data centers. How Hays County residents fought back over the Edwards Aquifer and a historic drought.",
  intro="Between Austin and San Antonio, in a multiyear drought over the Edwards Aquifer, Hays County residents turned out by the hundreds against data centers. In June 2026, San Marcos became the first city in Texas to ban them.",
  counts=[("1st","Texas city to ban data centers: San Marcos"),("~5","potential data centers counted by local water advocates"),("2011","the last full county water study, until this year"),("4-3","the San Marcos council vote")],
  projects=[
    (["Denied","Reporting"],"San Marcos data center, Francis Harris Lane","About 200 acres at 904 Francis Harris Lane. The City Council denied the rezoning 5-2 in February 2026 after hundreds protested inside and outside city hall."),
    (["Watch list","Reporting"],"Other proposals near San Marcos","At least two data centers have been proposed in unincorporated Hays County near the city's borders, and local water advocates count about five potential projects in the area.")],
  timeline=[
    ("Jan 20, 2026","County orders a water study","Its first comprehensive water study since 2011."),
    ("Feb 17-18, 2026","San Marcos denies a 200-acre data center","The vote was 5-2 after an overflow crowd."),
    ("Feb 2026","County tables a 30-day pause","County attorneys warned it would almost certainly bring a lawsuit."),
    ("June 12, 2026","County refuses an aquifer-zone deal","Denied an agreement with a 340-acre development over the Edwards Aquifer recharge zone."),
    ("June 2026","San Marcos bans data centers","Voted 4-3 to prohibit them in every zoning district, the first Texas city to do so. A state senator vowed a legal challenge."),
    ("June 23, 2026","County passes a symbolic pause","A non-binding resolution pausing consideration of high-water-use developments, including data centers.")],
  lessons=[
    ("Cities can do what counties can't","Zoning power let San Marcos ban data centers outright. Find out whether a site is inside a city or its extraterritorial jurisdiction."),
    ("A ban is not a moratorium","San Marcos changed its zoning rules rather than pausing permits, which it argues puts it on firmer legal ground."),
    ("Study your water","A county without zoning power can still commission a water study, and the facts it finds shape every decision after."),
    ("Show up","Hundreds of residents at city hall turned a rezoning vote.")],
  sources="Texas Tribune (June 30, 2026); KSAT; Community Impact; KUT; The Real Deal; Hoodline."))
