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
build(dict(slug="easttexas", name="East Texas", checked=C,
  title="East Texas Watch",
  desc="Old mill sites, gas hubs and data centers across the Piney Woods, from the Angelina and Neches rivers to the Sabine. What's coming to East Texas.",
  intro="Developers have discovered East Texas for the same reasons families love it: water, land and room. From Lufkin's old paper mill to the old plywood mill at Bon Wier, from Cedar Creek Lake to the Neches River, these projects share the same rivers and the same aquifer.",
  counts=[("2","old mill sites targeted: Lufkin and Bon Wier"),("$150M+","incentives granted for a Bon Wier biorefinery that was never built"),("$16B","NextEra's planned gas hub in Anderson County"),("1","project already withdrawn: Cedar Creek Lake")],
  projects=[
    (["Proposed","Records"],"Amp Z / Project Lufkin, Angelina County","Former Southland Paper Mill on State Highway 103 East. About 1,041 acres, expandable to 4,000, targeting 245 MW and scaling to 2.1 GW. Asked the City of Lufkin for about 20 million gallons a day. See Angelina County Watch."),
    (["Proposed","Records"],"HyperDataGrid and Longleaf, Angelina County","A data center on Ben Dunn Road with five on-site wells, and WattBridge's 600 MW gas plant near Kurth Lake. ERCOT also lists a second 600 MW Longleaf plant and a 202 MW battery project."),
    (["Disputed","Reporting"],"Bon Wier Innovation Park, Newton County","About 1,400 to 1,600 acres at the former L-P Plywood mill on the Sabine River, now marketed to data centers. A July 2026 release announced a deal with a data center developer; the owner then said no sale or deal was made. See Newton County Watch."),
    (["Announced","Reporting"],"NextEra gas hub, Anderson County","A $16 billion natural gas generation hub with a data center to follow. Residents fear for Lake Palestine and the Neches River."),
    (["Withdrawn","Reporting"],"Diode Ventures, Henderson County","Would have drawn up to 5 million gallons a day from Cedar Creek Lake. Withdrawn July 2026. See Henderson County Watch."),
    (["Denied","Reporting"],"Bitcoin mine near downtown Tyler, Smith County","The City of Tyler denied the rezoning in July 2026."),
    (["Proposed","Reporting, verify"],"Two projects near Texarkana, Bowie County","An AI data center at the I-30 megasite in Hooks, and Project Big Pine at the TexAmericas Center.")],
  timeline=[
    ("Feb 2026","Amp Z eyes the Lufkin mill","Residents begin organizing."),
    ("May 2026","Cedar Creek water district pauses big commitments","Data center development in Henderson County halts."),
    ("July 2026","Diode withdraws; Tyler denies a bitcoin mine; Angelina asks Austin for authority","A data center deal is announced for the Bon Wier mill site, then denied by the owner."),
    ("Aug to Sept 2026","The state freezes data center approvals","The Governor orders a grid audit and a TCEQ permit pause."),
    ("Nov 9, 2026","Pineywoods Groundwater Conservation District rules hearing","1:30 p.m., Kurth Lake Lodge.")],
  lessons=[
    ("Old mill sites are targets","They come with power lines, water rights, rail and industrial history. Watch every closed mill in your county."),
    ("Our rivers connect us","The Angelina feeds the Neches. What happens upstream reaches everyone downstream, so neighboring counties should work together."),
    ("Water providers hold power","Cedar Creek Lake was saved when the water district paused new commitments."),
    ("Use the Deep East Texas Standard","Contract terms any county can ask for. See /standards.")],
  sources="Angelina County records and ERCOT data (via Angelina County Watch); KJAS (July 31, 2026); The Center Square; Tyler Morning Telegraph (July 24, 2026); Texas Tribune; More Than Just Parks tracker."))

build(dict(slug="newton", name="Newton", checked=C,
  title="Newton County Watch",
  desc="The old plywood mill at Bon Wier won $150M+ in incentives for a biorefinery that was never built. Now it is being marketed to data centers.",
  intro="On the Sabine River at Bon Wier, the old L-P Plywood mill site was supposed to become a $1.7 billion biorefinery, backed by more than $150 million in state and local incentives. It was never built. Now the owner is marketing the same land to data centers, with talk of on-site nuclear and gas power.",
  counts=[("$150M+","state and local incentives granted in 2022"),("Late 2025","when the biorefinery was supposed to be finished"),("1,400-1,600","acres at the site"),("2","conflicting statements about a data center deal")],
  projects=[
    (["Disputed","Reporting"],"Bon Wier Innovation Park","Owned by USA BioEnergy of Scottsdale, Arizona, which calls the rail-served site, in a federal opportunity zone, Innovation Park. It advertises behind-the-meter power options including nuclear and gas. A July 31, 2026 release said the owner had entered a purchase agreement with Clean Holding Company for an East Texas Energy Campus; a tracker lists it at 1.8 GW. CEO Nick Andrews then told KJAS that no sale or deal had been made, only a letter of support. Judge Ronnie Cochran says he wrote a letter of recommendation and nothing more.")],
  timeline=[
    ("2022","Biorefinery announced","USA BioEnergy picked Bon Wier for a $1.7B plant to turn wood waste into fuels, citing more than $150M in state and local incentives. The Governor welcomed it."),
    ("2023","Southwest Airlines deal","A 20-year agreement for up to 680 million gallons of sustainable aviation fuel."),
    ("Oct 2025","Nuclear partner named","Applied Atomics was announced to supply small nuclear power, and the chairman said data centers were interested in the site."),
    ("Late 2025","Target completion passes","The biorefinery has not been built."),
    ("July 31, 2026","Data center deal announced","A release said the owner entered a purchase agreement with Clean Holding Company."),
    ("Aug 2026","Deal denied","The CEO told KJAS no sale or deal was made. The county judge said he only wrote a letter of recommendation.")],
  lessons=[
    ("Follow the incentives","When a project changes from one industry to another, ask what happens to the incentives granted for the first one, and whether clawbacks apply."),
    ("Old mill sites are targets","Bon Wier, like Lufkin's old paper mill, has rail, power lines and industrial history. Developers see that as a head start."),
    ("Letters of support matter","A judge's letter can be quoted in a press release as an endorsement. Ask officials what they have signed, and post it publicly."),
    ("Watch the river","The site sits on the Sabine River. Ask where any water would come from, and where wastewater would go.")],
  sources="KJAS (two articles, Aug 2026); East Texas Banner; KFDM (Oct 2025 and 2023); Newswire (2022); Texas Forest Country Partnership; More Than Just Parks tracker."))
build(dict(slug="anderson", name="Anderson", checked=C,
  title="Anderson County Watch",
  desc="Project Anderson: a 5.2 GW, $16 billion gas plant built to power data centers, between the Trinity and Neches rivers. What residents need to know.",
  intro="Between the Trinity and Neches rivers, NextEra plans one of the largest gas plants in the country: 5.2 gigawatts on about 1,700 acres, built to serve data centers. It is part of a U.S.-Japan trade deal, which puts it under federal control and leaves the county with little say.",
  counts=[("5.2 GW","of gas generation planned"),("$16B","estimated cost"),("1,700","acres near Tennessee Colony"),("100 vs 3,000","permanent jobs: the city's number vs a lawmaker's")],
  projects=[
    (["Announced","Reporting"],"Project Anderson","NextEra Energy Resources will build and operate the plant, jointly owned by Japan and the U.S. government under a $550B trade deal, with gas from Comstock Resources. It can serve up to 5 GW of large loads such as data centers, and the U.S. Commerce Department says a data center will follow. NextEra says the plant will be air-cooled and it is exploring recycled water instead of fresh groundwater. Groundbreaking is expected in 2027, with the first phase running in 2028 and construction through 2032.")],
  timeline=[
    ("March 2026","Federal approval announced","Part of 10 GW of NextEra gas plants in Texas and Pennsylvania tied to the U.S.-Japan deal."),
    ("April 7, 2026","First public meeting","Residents asked about water, noise and fire protection. A volunteer fire chief who lives three miles away said it would ruin a quiet county."),
    ("May 2026","City of Palestine posts details","At least 100 full-time jobs after construction, plus hundreds of construction jobs."),
    ("2027","Groundbreaking expected","")],
  lessons=[
    ("Power plants come first","A gas hub built for large loads is an invitation to data centers. Watch for the data center that follows."),
    ("Compare the jobs numbers","A state representative claimed 3,000 long-term jobs; the city's own page says at least 100. Ask for the number in writing."),
    ("Federal projects still need local services","Counties keep some tools, such as noise rules and road agreements, and volunteer fire departments must be ready for a plant this size."),
    ("Get the water plan in writing","Air cooling and recycled water are promises today. Ask the Trinity River Authority and the groundwater district what has been requested.")],
  sources="Utility Dive (Mar 24, 2026); Data Center Dynamics; Texas Scorecard (Mar 26, 2026); KETK (Apr 2026); City of Palestine (May 2026); The Center Square."))
build(dict(slug="navarro", name="Navarro", checked=C,
  title="Navarro County Watch",
  desc="Riot's 1 GW Corsicana campus, a 600 MW powered-land campus, and the lake that supplies them. What's happening in Navarro County.",
  intro="South of Dallas, Corsicana hosts one of the largest bitcoin mining campuses in the world, now shifting to AI, and more developers are lining up behind it. The water comes from Navarro Mills Lake.",
  counts=[("1 GW","approved by ERCOT for Riot Corsicana"),("858","acres in Riot's campus"),("600 MW","listed for a second powered-land campus"),("0","public numbers on Riot's water use")],
  projects=[
    (["Operating and expanding","Reporting"],"Riot Corsicana","Riot Platforms' campus, which ERCOT approved for 1 GW, the first 1 GW load it approved. About 400 MW is built on 858 acres. AMD leases 50 MW for AI computing. The City of Corsicana said in 2022 that Riot's water would come from Navarro Mills Lake; Riot has never published how much."),
    (["Proposed","Reporting, verify"],"Hedgehog USA powered land campus","Listed at 600 MW by a public tracker."),
    (["Proposed","Reporting, verify"],"EG AI Rice data center","A small 3 MW edge site near Rice.")],
  timeline=[
    ("2022","Riot breaks ground","Residents formed a Facebook group of more than 500 members and started a petition against the mine."),
    ("2025","Riot buys more land","The campus grows to 858 acres."),
    ("2026","AI moves in","AMD doubles its lease at Corsicana to 50 MW.")],
  lessons=[
    ("Crypto mines become AI campuses","The same site, power and water can switch uses. Agreements should require a new hearing for any change in use."),
    ("Ask the lake's owner","Navarro Mills Lake water is contracted through the Trinity River Authority. Drought restrictions have been triggered before."),
    ("Watch what follows","Once one big load arrives, powered-land developers follow.")],
  sources="Data Center Dynamics; Riot Platforms releases; Greenpeace USA research; Tech Xplore / Dallas Morning News (2022); Baxtel; Trinity River Authority; More Than Just Parks tracker."))
build(dict(slug="milam", name="Milam", checked=C,
  title="Milam County Watch",
  desc="Rockdale's old Alcoa smelter became one of the biggest bitcoin mines in the country. Now AI is moving in, and Stargate has a site here too.",
  intro="In Rockdale, the land where Alcoa once smelted aluminum now hosts two of the largest bitcoin mines in the country, side by side. AI tenants are moving in, and OpenAI's Stargate has named Milam County as a site.",
  counts=[("700 MW","Riot's Rockdale capacity"),("$2.1M","a year Riot pays for a lake water reservation, per Greenpeace research"),("2","giant crypto mines side by side"),("1","Stargate site announced")],
  projects=[
    (["Operating","Reporting"],"Riot Rockdale","Riot Platforms, 700 MW, on former Alcoa land. Riot bought about 200 acres it had leased for $96M and signed AMD as an AI tenant. Uses a mix of air and immersion cooling, with a lake water reservation reported at about $2.1M a year."),
    (["Operating","Reporting"],"Bitdeer Rockdale","Spun off from China's Bitmain, less than half a mile from Riot on former Alcoa land."),
    (["Announced","Reporting"],"Stargate Milam County","Named as an OpenAI Stargate site in late 2025. Details are still not public.")],
  timeline=[
    ("2021","Riot buys the Whinstone site",""),
    ("2023","Rockdale becomes one of the largest bitcoin mines in North America",""),
    ("Late 2025","Stargate names Milam County",""),
    ("2026","AMD signs on at Rockdale","Riot begins shifting to AI hosting.")],
  lessons=[
    ("Old industrial land draws new loads","The Alcoa site had the power lines; the miners followed. Compare Lufkin's paper mill and Bon Wier's plywood mill."),
    ("Ask who owns the water rights","A private lake water reservation can bypass the debates residents expect."),
    ("Track every announced site","Stargate named Milam County with no public details. Watch TDLR filings and the appraisal district.")],
  sources="The Block; Greenpeace USA research; Baxtel; Data Center Dynamics; TechRadar."))

import subprocess; subprocess.run(["python3", "tools/add_live.py"])
subprocess.run(["python3", "tools/add_builder.py"])
