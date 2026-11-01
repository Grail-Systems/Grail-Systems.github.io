"""Source batch 7, part A: link every card that cites the More Than Just Parks tracker to its tracker entry."""
B = "https://morethanjustparks.com/data-center-tracker/"
M = {
 "Fort Bliss data center": "fort-bliss-data-center-carlyle-group-u-s-army-tx--50d8e6ef-f359-48e5-9769-d4843f62d7b4",
 "JMG data center, Conroe": "jmg-data-center-100-plantation-drive-conroe-tx--a2e7bac6-2a05-4353-a876-408c4c9059df",
 "Project Raptor (Google)": "project-raptor-google-archer-county-tx--53f5cff2-660f-4417-b89f-e6fe4cb8c5ee",
 "Energy Ranch": "energy-ranch-hc-capital-partners-herrmann-family-companies-tx--4c77ecab-ee09-4b5c-910a-e06c3d8b5977",
 "Applewhite Technology Park": "applewhite-technology-park-tract-tx--2a3e21a5-4740-41cf-89d8-14cbdd8484a7",
 "CloudHQ SAT Campus": "cloudhq-sat-campus-tx--6c841707-3500-4ccf-a3b0-a1814ccf9239",
 "Microsoft South Central Campus": "microsoft-south-central-campus-tx--24a32659-3068-4031-b4cb-95e7010450d4",
 "Applied Digital Belton Campus": "applied-digital-belton-campus-tx--00eca0f6-9f94-4420-8256-3484baf80ebe",
 "Williamson County AI Campus": "williamson-county-ai-campus-tx--ddee8daf-cf64-4d45-b7ff-dfa48aa18807",
 "Project Mustang (Taylor)": "project-mustang-big-watt-digital-powerhouse-data-centers-taylor-tx--3899d8e3-fb78-474a-9680-aae6dcc5c40a",
 "KDC Project Comal": "kdc-project-comal-tx--0d8ced9d-7d96-4c16-8ec5-4fa57a4894f2",
 "Mesone data center (Jarrell)": "mesone-data-center-jarrell-tx--334b3b03-a0ad-4c87-8d28-1a0e0138d513",
 "Ellis County Data Ranch": "ellis-county-data-ranch-tx--0678a219-d5e0-487c-87e2-539d002b54a8",
 "Lincoln Rackhouse Dallas Wholesale II": "lincoln-rackhouse-dallas-wholesale-ii-tx--765b7397-aaf5-4e79-88cd-cc84d558fdb3",
 "EdgeCore El Paso": "edgecore-el-paso-tx--44852f88-9ac1-4cb3-96b3-6d9142dc8825",
 "Guadalupe County Technology Center": "guadalupe-county-technology-center-tx--14e371fc-b5d5-42b7-8047-6659c888a65c",
 "McLennan County Data Campus": "mclennan-county-data-campus-tx--a9be931c-5608-42bf-bcf9-2eb66a5fbd77",
 "Project Merlin (McGregor)": "project-merlin-galaxy-digital-mcgregor-tx--3d578ec2-926b-443f-98bc-76b767896432",
 "Tract Medina Technology Park": "tract-medina-technology-park-tx--723ea193-0435-4776-9f3c-adb85192158b",
 "Cinco data center": "cinco-data-center-tx--9fc3e0fd-5479-422b-a23f-92f97a62f79c",
 "Beacon Point": "beacon-point-hut-8-tx--4c4f5123-bd82-48f5-82c4-c326035eae6b",
 "Project Horizon (Longfellow Ranch)": "project-horizon-poolside-coreweave-longfellow-ranch-tx--c3529d48-788a-4669-8742-3ee1cc15d760",
 "Project Kilby": "chevron-microsoft-project-kilby-reeves-county-tx--996b55b1-c096-403f-a759-8ed4ea5f049b",
 "Reeves County Solar Data Ranch": "reeves-county-solar-data-ranch-tx--3a711b9e-cf27-47e7-a241-be63ec1c676d",
 "Cipher Colchis Project": "cipher-digital-colchis-project-tom-green-county-tx--0ca280c0-79c7-48d3-85ab-7aab3902578c",
 "Greater Abilene gas-powered data center": "powerplay-ai-sharon-ai-greater-abilene-gas-powered-data-center-tx--9991e300-6b0a-4efc-b2ab-d678846670e9",
 "IREN Sweetwater 1": "iren-sweetwater-1-tx--6ea0b85e-de0a-4301-9f78-43aefc0950e5",
 "CloudBurst AI data center (Sweetwater)": "cloudburst-ai-data-center-sweetwater-tx--e61171be-7a67-451d-bb39-06d76a71163c",
 "Crusoe Nolan County data center": "crusoe-energy-nolan-county-data-center-tx--aac97fd9-2cc1-4588-8ee4-264ca0a3a076",
 "CleanSpark Valley Gamma": "cleanspark-valley-gamma-tx--7dc182d1-8a44-4dc1-b0f0-3cacda1f3562",
 "InfraTech Capital campus": "infratech-capital-data-center-campus-carson-county-tx--dc5da265-93a3-4c69-8ed7-25ee18d0c248",
 "Crusoe / Lancium Childress campus": "crusoe-lancium-childress-data-center-campus-tx--62a7f764-202b-4224-aaed-cb35f4ee6392",
 "IREN Childress AI and mining campus": "iren-childress-ai-and-mining-campus-tx--ff540993-11fa-4c9d-b959-6baa0acebc02",
 "Geronimo Power AI data center": "ai-data-center-geronimo-power-ammannsville-dubina-area-tx--907a65a1-cb94-4f0e-8b3d-04ee9af07dd7",
 "PlaceMKR AI data center (Winchester)": "ai-data-center-placemkr-la-grange-winchester-llc-winchester-tx--08654c1d-98af-4e0c-af8c-19d4b001452d",
 "Project Caprock (Abernathy)": "project-caprock-aligned-data-centers-abernathy-tx--2844c1ae-6ed3-48da-b67e-40808658cf57",
 "TeraWulf / Fluidstack Abernathy": "terawulf-fluidstack-abernathy-data-center-tx--8c064095-6b27-4716-a13a-1aa26484e108",
 "CloudBurst San Marcos Gigacenter": "cloudburst-san-marcos-gigacenter-tx--c387151f-37d4-4196-b39e-8628bb5a7743",
 "Sabey / Carson Select San Marcos campus": "sabey-carson-select-san-marcos-data-center-campus-tx--4ed87767-70bd-4287-9af6-bff25ef45241",
}
M.update({
 "Telios Quinlan Campus": "telios-quinlan-campus-core-scientific-tx--58b7da98-9e8b-497b-a7f8-e09d5f659adf",
 "Port Arthur AI data center": "port-arthur-ai-data-center-tx--576be522-cd99-48ff-9145-b086867ea973",
 "FluidStack Cameron County campus": "fluidstack-data-center-campus-fluidstack-cameron-county-tx--86089d2e-927c-40eb-afa0-e6ef5571fd8d",
 "Wichita Falls Business Park data center": "wichita-falls-business-park-data-center-texas-data-center-campus-llc-tx--df191d5a-e10c-455b-9b07-105f912c57d8",
 "Bells AI data center": "bells-ai-data-center-black-mountain-tx--b9a73968-2680-4773-bbe5-33c1495a9982",
 "Delta County data center": "proposed-delta-county-data-center-ls-power-tx--00fd0f10-4c40-4655-9dd7-03dfc6ddf3b8",
 "CyrusOne Jack County campus": "cyrusone-jack-county-data-center-campus-c1-jack-i-tx--fd5559ed-a5b0-4ccf-b6b5-ccf1dd222d98",
 "Prometheus Hyperscale Kaufman campus": "prometheus-hyperscale-kaufman-county-campus-tx--391e6d30-8c49-4627-9061-1e18c29b731f",
 "Crusoe Jayton campus": "crusoe-jayton-data-center-campus-project-kent-project-hyper-spur-tx--ca0197bb-2fe8-4b86-9f8c-7e949c3627d6",
 "Kahla Project (Marquez)": "kahla-project-crusoe-technologies-marquez-tx--bec6bd3f-31a7-4a64-b900-5b9982aacd62",
 "LAMP power and innovation hub": "liberty-american-multi-sourced-power-and-innovation-hub-lamp-tx--75422881-0333-4f8e-83da-4efe5b0cf21b",
 "Cipher Mikeska HPC data center": "cipher-mikeska-hpc-data-center-tx--fad01621-efc2-4e4f-9273-e30309405ca7",
 "Cipher Milsing HPC data center": "cipher-milsing-hpc-data-center-cipher-digital-tx--bdf94e5c-6980-4dcc-8549-ba3583a97910",
 "Crusoe Victoria AI Factory": "crusoe-victoria-ai-factory-blue-energy-port-of-victoria-campus-tx--053e4e72-53d2-4f92-bf9f-f1b000309d58",
 "Data City Texas": "data-city-texas-energy-abundance-tx--7ea6a5d6-c201-4608-9658-3f361a911ce5",
 "Desert Haven data center": "desert-haven-data-center-kaufman-and-company-serverdomes-hudspeth-county-tx--bbae55e3-2165-4218-9850-07ae7ccfed29",
 "Project Eagle (AWS)": "project-eagle-aws-wharton-county-campus-tx--dd6ff1a7-bac7-41fd-b16a-37f4404a3692",
 "Project Roman (Hereford)": "project-roman-google-data-center-hereford-tx--4144a447-ecbe-4bbd-a168-ea221b6ea529",
 "Google Wilbarger County data center": "google-wilbarger-county-data-center-tx--b855a91f-893e-4c51-9c1b-fe14f20c87c9",
 "Project North (Shackelford)": "project-north-bolt-data-and-energy-shackelford-county-tx--1ed530ba-8fd2-4bc4-b473-77f92cb3e53d",
 "BlockchAIn Wise County mining site": "blockchain-wise-county-data-mining-site-blockchain-digital-infrastructure-tx--24eada77-eeb0-46ac-9c7c-f3d8eb1dd637",
 "Ziastra (Marfa)": "ziastra-open-origin-marfa-campus-tx--cda99336-e25e-472f-83c6-1f3a9761c119",
 "Matrix Data Center Campus (Sulphur Springs)": "matrix-data-center-campus-msb-global-sulphur-springs-tx--36a8e10f-045d-47b7-8e64-0319d509ce45",
 "Project Aggie": "project-aggie-data-center-priority-power-midtown-business-park-tx--ee35ac96-05c3-43ef-9618-5e536b3297de",
 "Zydeco Hutto data center": "zydeco-hutto-data-center-tx--52b6a680-5444-40fb-96de-886471697c9f",
 "Data Factory Athens": "data-factory-athens-data-center-tx--53035780-aaef-4edb-b279-eb8e2b5cc470",
 "NFN8 Crystal City bitcoin mine": "nfn8-crystal-city-bitcoin-mining-facility-nfn8-group-tx--de5aa2f5-e2c2-4fc5-9344-917a7025d1fb",
 "Airport Drive data center": "airport-drive-data-center-tx--113665c7-a75f-49e3-ae78-e7ddd2123d9f",
 "Highlander SM One (San Marcos)": "highlander-sm-one-llc-san-marcos-tx--1c23acb7-4ec3-459b-aa99-1bd3104a4fb9",
 "Harlingen data center": "rgv-data-center-eneus-energy-harlingen-tx--9bd1f4db-9d0c-47b4-964b-bb8c297578ca",
 "Pacifico Cedar Creek Campus": "cedar-creek-campus-pacifico-energy-tx--a6c6c249-830c-422a-87e4-64c96b0c144b",
 "Datahub Developers AI data center": "datahub-developers-ai-data-center-east-texas-logistics-center-i-30-megasite-hook-tx--10f03b88-c06d-4457-9381-7bc6f68d2a8c",
 "Project Big Pine": "texamericas-center-project-big-pine-tx--6e133d1d-f922-4252-b06a-7e783f110cd3",
 "Old Ocean data center": "old-ocean-data-center-nightpeak-energy-tx--904d2057-1dc9-4540-8010-16474f7fbfaa",
 "Alpha Digital Campus": "alpha-digital-campus-landbridge-and-powerbridge-reeves-county-tx--dfb4f9f2-bf7d-42c3-99b6-2b5d1e94a5e3",
 "FO Permian Partners data center": "fo-permian-partners-data-center-hivolt-energy-midland-county-tx--79e400aa-8e72-413f-aa09-ab2e929ea2d2",
 "MARA Matagorda County campus": "mara-matagorda-county-campus-former-hif-site-tx--49acb7a6-ab9a-4117-8b4e-848a1cc83187",
 "Google, Gray County": "google-meitner-energy-center-gray-county-tx--456df088-1541-42c6-b144-93b6bc50b27b",
 "Pace Glasscock County": "lone-star-project-pace-glasscock-county-tx--044675ea-0492-4c79-9f30-48f40c1ce91e",
 "Texas Critical Data Centers": "texas-critical-data-centers-tcdc-campus-tx--1dd16d9f-c22a-4f43-b23a-8eaa8c3151a1",
 "Fermi America campus": "fermi-america-hypergrid-campus-tx--9b3ab8f8-b605-49c0-856c-0f59e3eb3c9e",
 "QTS at Lancium, Hall County": "qts-lancium-hall-county-campus-turkey-tx--0a79b1b8-3a79-4c13-a67a-79c14b6a1973",
})
import json
p = "data/details.json"; d = json.load(open(p)); n = 0
for k, slug in M.items():
    e = d.setdefault(k, {}); L = e.setdefault("links", [])
    if not any(B + slug == u for _, u in L):
        L.append(["More Than Just Parks tracker entry (names its original source)", B + slug]); n += 1
g = d["Google, Gray County"]
g["comp"] = "Meitner Data Center (owner IP Meitner DTC, LLC; occupant Google LLC), certified Apr 27, 2026. The tracker places Meitner in Gray County."
g.setdefault("links", [])
if not any("comptroller" in u for _, u in g["links"]): g["links"].append(["Texas Comptroller data center list", "https://comptroller.texas.gov/taxes/data-centers/data-center-lists.php"])
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [('dev:"Highlander SM One LLC", power:"Size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Listed as canceled. Listed by the More Than Just Parks tracker; needs verification."',
      'dev:"Highlander SM One LLC", power:"Size not disclosed", water:"Not disclosed", conf:"Reporting", note:"This is the same project as the San Marcos data center on Francis Harris Lane, which the City Council denied in Feb 2026. See that card for the full record."')]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:70]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>San Marcos: one project, two cards</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>The map listed Highlander SM One (San Marcos) and the San Marcos data center on Francis Harris Lane as separate projects. They are the same proposal. Both cards now say so.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print(f"Batch 7: {n} cards now link to their tracker entries; Gray County gets its Comptroller record; San Marcos duplicate flagged")
