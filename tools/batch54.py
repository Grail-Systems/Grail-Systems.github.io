"""Bring company profiles and the El Paso page in line with tonight's map corrections."""
import os
EDITS = {
 "companies.html": [
  ('know:"Its Fort Spunky project in Hood County is reported canceled and its Bastrop campus listed as blocked by a moratorium; it also has a gas-powered campus planned in the Big Bend region."',
   'know:"Its Fort Spunky project in Hood County is reported canceled. Its Cedar Creek campus in Bastrop County is moving: a gas plant site permit was issued in July 2026, the developers withdrew their county tax break requests, and the first $366M building is filed to start construction November 30, 2026 (a moratorium a tracker cited was at its alternate site in Ohio). It also has a gas-powered campus planned in the Big Bend region."'),
  ('know:"A 750 MW campus in Childress and a 1.4 GW site in Sweetwater. Its Childress site is registered for the state data center tax exemption."',
   'know:"A 750 MW campus in Childress, now adding AI halls with capacity for Microsoft, and a 1.4 GW site in Sweetwater whose substation was connected in May 2026 but is not yet operating; a mid-2026 analysis said no customer had signed for it. A second Sweetwater site is in Fisher County. Its Childress site is registered for the state data center tax exemption."'),
  ('know:"The most active builder in Texas by site count. Places data centers right next to Calpine gas plants at Freestone and Thad Hill."',
   'know:"The most active builder in Texas by site count, and it pairs data centers with gas plants: next to Calpine plants at Freestone and Thad Hill, beside Vistra\'s plant in Jack County, and now considering the Sulphur Springs site with an on-site gas plant."'),
  ('know:"Builder of Stargate Abilene, with projects across West Texas plus a 1.5 GW Kahla project in Leon County and a 1.5 GW campus at the Port of Victoria."',
   'know:"Builder of Stargate Abilene, with a West Texas corridor of projects: a $7B Nolan County campus with a 10-year tax break, a 1 GW Childress campus for Meta under construction, and a $4.8B Jayton campus filed in Kent County. Also a 1.5 GW Kahla project in Leon County and a Port of Victoria campus whose gas and nuclear power dates have already slipped."'),
 ],
 "elpaso/index.html": [
  ('data-companies="Meta, Wurldwide LLC, EdgeCore"', 'data-companies="Meta, Wurldwide LLC, BlackRock"'),
 ],
}
for path, pairs in EDITS.items():
    s = open(path).read()
    for old, new in pairs:
        if new in s: continue
        assert s.count(old) == 1, path + " not found: " + old[:60]
        s = s.replace(old, new)
    open(path, "w").write(s)
print("Batch 54: Pacifico, IREN, CyrusOne, Crusoe profiles updated; El Paso request list fixed")
