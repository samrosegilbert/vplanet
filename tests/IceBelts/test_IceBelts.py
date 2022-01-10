from benchmark import Benchmark, benchmark 
import astropy.units as u 
import pytest 
 
@benchmark( 
   { 
       "log.initial.system.Age": {"value": 0.000000, "unit": u.sec}, 
       "log.initial.system.Time": {"value": 0.000000, "unit": u.sec}, 
       "log.initial.system.TotAngMom": {"value": 1.501328e+42, "unit": (u.kg * u.m ** 2) / u.sec}, 
       "log.initial.system.TotEnergy": {"value": -7.839372e+41, "unit": u.Joule}, 
       "log.initial.system.PotEnergy": {"value": -7.839908e+41, "unit": u.Joule}, 
       "log.initial.system.KinEnergy": {"value": 5.361272e+37, "unit": u.Joule}, 
       "log.initial.system.DeltaTime": {"value": 0.000000, "unit": u.sec}, 
       "log.initial.sun.Mass": {"value": 1.988416e+30, "unit": u.kg}, 
       "log.initial.sun.Radius": {"value": 2.019571e+08, "unit": u.m}, 
       "log.initial.sun.RadGyra": {"value": 0.500000}, 
       "log.initial.sun.RotAngMom": {"value": 1.474456e+42, "unit": (u.kg * u.m ** 2) / u.sec}, 
       "log.initial.sun.RotVel": {"value": 1.468674e+04, "unit": u.m / u.sec}, 
       "log.initial.sun.BodyType": {"value": 0.000000}, 
       "log.initial.sun.RotRate": {"value": 7.272205e-05, "unit": 1 / u.sec}, 
       "log.initial.sun.RotPer": {"value": 8.640000e+04, "unit": u.sec}, 
       "log.initial.sun.Density": {"value": 5.762900e+04, "unit": u.kg / u.m ** 3}, 
       "log.initial.sun.HZLimitDryRunaway": {"value": 1.357831e+11, "unit": u.m}, 
       "log.initial.sun.HZLimRecVenus": {"value": 1.118929e+11, "unit": u.m}, 
       "log.initial.sun.HZLimRunaway": {"value": 1.461108e+11, "unit": u.m}, 
       "log.initial.sun.HZLimMoistGreenhouse": {"value": 1.480517e+11, "unit": u.m}, 
       "log.initial.sun.HZLimMaxGreenhouse": {"value": 2.509538e+11, "unit": u.m}, 
       "log.initial.sun.HZLimEarlyMars": {"value": 2.738109e+11, "unit": u.m}, 
       "log.initial.sun.Instellation": {"value": -1.000000, "unit": u.kg / u.sec ** 3}, 
       "log.initial.sun.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m}, 
       "log.initial.sun.LXUVTot": {"value": 3.846000e+23, "unit": u.kg / u.sec ** 3}, 
       "log.initial.sun.LostEnergy": {"value": 5.562685e-309, "unit": u.Joule}, 
       "log.initial.sun.LostAngMom": {"value": 5.562685e-309, "unit": (u.kg * u.m ** 2) / u.sec}, 
       "log.initial.sun.Luminosity": {"value": 3.846000e+26, "unit": u.W}, 
       "log.initial.sun.LXUVStellar": {"value": 3.846000e+23, "unit": u.W}, 
       "log.initial.sun.Temperature": {"value": 5778.000000, "unit": u.K}, 
       "log.initial.sun.LXUVFrac": {"value": 0.001000}, 
       "log.initial.sun.RossbyNumber": {"value": 0.078260}, 
       "log.initial.sun.DRotPerDtStellar": {"value": 6.558557e-13}, 
       "log.initial.earth.Mass": {"value": 5.971546e+24, "unit": u.kg}, 
       "log.initial.earth.Obliquity": {"value": 0.959931, "unit": u.rad}, 
       "log.initial.earth.PrecA": {"value": 0.000000, "unit": u.rad}, 
       "log.initial.earth.Radius": {"value": 6.378100e+06, "unit": u.m}, 
       "log.initial.earth.RadGyra": {"value": 0.500000}, 
       "log.initial.earth.BodyType": {"value": 0.000000}, 
       "log.initial.earth.Density": {"value": 5494.449526, "unit": u.kg / u.m ** 3}, 
       "log.initial.earth.HZLimitDryRunaway": {"value": 1.081774e+11, "unit": u.m}, 
       "log.initial.earth.HZLimRecVenus": {"value": 1.118929e+11, "unit": u.m}, 
       "log.initial.earth.HZLimRunaway": {"value": 1.461108e+11, "unit": u.m}, 
       "log.initial.earth.HZLimMoistGreenhouse": {"value": 1.480517e+11, "unit": u.m}, 
       "log.initial.earth.HZLimMaxGreenhouse": {"value": 2.509538e+11, "unit": u.m}, 
       "log.initial.earth.HZLimEarlyMars": {"value": 2.738109e+11, "unit": u.m}, 
       "log.initial.earth.Instellation": {"value": 1314.462644, "unit": u.kg / u.sec ** 3}, 
       "log.initial.earth.Eccentricity": {"value": 0.000000}, 
       "log.initial.earth.MeanMotion": {"value": 1.932716e-07, "unit": 1 / u.sec}, 
       "log.initial.earth.OrbPeriod": {"value": 3.250961e+07, "unit": u.sec}, 
       "log.initial.earth.SemiMajorAxis": {"value": 1.525898e+11, "unit": u.m}, 
       "log.initial.earth.COPP": {"value": 0.000000}, 
       "log.initial.earth.TGlobal": {"value": 7.129840, "unit": u.deg_C}, 
       "log.initial.earth.AlbedoGlobal": {"value": 0.365281}, 
       "log.initial.earth.FluxInGlobal": {"value": 217.198135, "unit": u.kg / u.sec ** 3}, 
       "log.initial.earth.FluxOutGlobal": {"value": 218.201366, "unit": u.W / u.m ** 2}, 
       "log.initial.earth.TotIceMass": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.earth.TotIceFlow": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.earth.TotIceBalance": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.earth.SkipSeas": {"value": 0.000000}, 
       "log.initial.earth.AreaIceCov": {"value": 0.000000}, 
       "log.initial.earth.Latitude": {"value": -83.402352, "unit": u.deg}, 
       "log.initial.earth.TempLat": {"value": 9.381310, "unit": u.deg_C}, 
       "log.initial.earth.AlbedoLat": {"value": 0.377296}, 
       "log.initial.earth.AnnInsol": {"value": 342.162291, "unit": u.W / u.m ** 2}, 
       "log.initial.earth.FluxMerid": {"value": 0.069957, "unit": u.PW}, 
       "log.initial.earth.FluxIn": {"value": 226.930428, "unit": u.W / u.m ** 2}, 
       "log.initial.earth.FluxOut": {"value": 222.906937, "unit": u.W / u.m ** 2}, 
       "log.initial.earth.DivFlux": {"value": 4.732700, "unit": u.W / u.m ** 2}, 
       "log.initial.earth.IceMass": {"value": 0.000000}, 
       "log.initial.earth.IceHeight": {"value": 0.000000, "unit": u.m}, 
       "log.initial.earth.DIceMassDt": {"value": 0.000000, "unit": u.m}, 
       "log.initial.earth.IceFlow": {"value": 0.000000, "unit": u.m / u.sec}, 
       "log.initial.earth.EnergyResL": {"value": 4.163780e-12, "unit": u.kg / u.sec ** 3}, 
       "log.initial.earth.EnergyResW": {"value": 4.362732e-12, "unit": u.kg / u.sec ** 3}, 
       "log.initial.earth.BedrockH": {"value": 0.000000, "unit": u.m}, 
       "log.initial.earth.TempLandLat": {"value": 274.617109, "unit": u.sec}, 
       "log.initial.earth.TempWaterLat": {"value": 286.381049, "unit": u.sec}, 
       "log.initial.earth.AlbedoLandLat": {"value": 0.523047}, 
       "log.initial.earth.AlbedoWaterLat": {"value": 0.302212}, 
       "log.initial.earth.TempMinLat": {"value": -7.099591, "unit": u.deg_C}, 
       "log.initial.earth.TempMaxLat": {"value": 34.794296, "unit": u.deg_C}, 
       "log.initial.earth.Snowball": {"value": 0.000000}, 
       "log.initial.earth.PlanckBAvg": {"value": 2.090000}, 
       "log.initial.earth.IceAccum": {"value": 0.458812}, 
       "log.initial.earth.IceAblate": {"value": -0.378888}, 
       "log.initial.earth.TempMaxLand": {"value": 337.865637, "unit": u.sec}, 
       "log.initial.earth.TempMaxWater": {"value": 294.302304, "unit": u.sec}, 
       "log.initial.earth.PeakInsol": {"value": 1069.614002, "unit": u.kg / u.sec ** 3}, 
       "log.initial.earth.IceCapNorthLand": {"value": 0.000000}, 
       "log.initial.earth.IceCapNorthSea": {"value": 0.000000}, 
       "log.initial.earth.IceCapSouthLand": {"value": 0.000000}, 
       "log.initial.earth.IceCapSouthSea": {"value": 0.000000}, 
       "log.initial.earth.IceBeltLand": {"value": 1.000000}, 
       "log.initial.earth.IceBeltSea": {"value": 0.000000}, 
       "log.initial.earth.SnowballLand": {"value": 0.000000}, 
       "log.initial.earth.SnowballSea": {"value": 0.000000}, 
       "log.initial.earth.IceFree": {"value": 0.000000}, 
       "log.initial.earth.IceCapNorthLatLand": {"value": 100.000000, "unit": u.rad}, 
       "log.initial.earth.IceCapNorthLatSea": {"value": 100.000000, "unit": u.rad}, 
       "log.initial.earth.IceCapSouthLatLand": {"value": 100.000000, "unit": u.rad}, 
       "log.initial.earth.IceCapSouthLatSea": {"value": 100.000000, "unit": u.rad}, 
       "log.initial.earth.IceBeltNorthLatLand": {"value": 0.013245, "unit": u.rad}, 
       "log.initial.earth.IceBeltNorthLatSea": {"value": 100.000000, "unit": u.rad}, 
       "log.initial.earth.IceBeltSouthLatLand": {"value": 0.000000, "unit": u.rad}, 
       "log.initial.earth.IceBeltSouthLatSea": {"value": 100.000000, "unit": u.rad}, 
       "log.final.system.Age": {"value": 3.155760e+07, "unit": u.sec, "rtol": 1e-4}, 
       "log.final.system.Time": {"value": 3.155760e+07, "unit": u.sec, "rtol": 1e-4}, 
       "log.final.system.TotAngMom": {"value": 1.501328e+42, "unit": (u.kg * u.m ** 2) / u.sec, "rtol": 1e-4}, 
       "log.final.system.TotEnergy": {"value": -7.839372e+41, "unit": u.Joule, "rtol": 1e-4}, 
       "log.final.system.PotEnergy": {"value": -7.839908e+41, "unit": u.Joule, "rtol": 1e-4}, 
       "log.final.system.KinEnergy": {"value": 5.361272e+37, "unit": u.Joule, "rtol": 1e-4}, 
       "log.final.system.DeltaTime": {"value": 3.155760e+07, "unit": u.sec, "rtol": 1e-4}, 
       "log.final.sun.Mass": {"value": 1.988416e+30, "unit": u.kg, "rtol": 1e-4}, 
       "log.final.sun.Radius": {"value": 2.019571e+08, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.RadGyra": {"value": 0.500000, "rtol": 1e-4}, 
       "log.final.sun.RotAngMom": {"value": 1.474456e+42, "unit": (u.kg * u.m ** 2) / u.sec, "rtol": 1e-4}, 
       "log.final.sun.RotVel": {"value": 1.468674e+04, "unit": u.m / u.sec, "rtol": 1e-4}, 
       "log.final.sun.BodyType": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.sun.RotRate": {"value": 7.272205e-05, "unit": 1 / u.sec, "rtol": 1e-4}, 
       "log.final.sun.RotPer": {"value": 8.640000e+04, "unit": u.sec, "rtol": 1e-4}, 
       "log.final.sun.Density": {"value": 5.762900e+04, "unit": u.kg / u.m ** 3, "rtol": 1e-4}, 
       "log.final.sun.HZLimitDryRunaway": {"value": 1.357831e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.HZLimRecVenus": {"value": 1.118929e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.HZLimRunaway": {"value": 1.461108e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.HZLimMoistGreenhouse": {"value": 1.480517e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.HZLimMaxGreenhouse": {"value": 2.509538e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.HZLimEarlyMars": {"value": 2.738109e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.Instellation": {"value": -1.000000, "unit": u.kg / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.sun.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.LXUVTot": {"value": 3.846000e+23, "unit": u.kg / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.sun.LostEnergy": {"value": 2.568599e+28, "unit": u.Joule, "rtol": 1e-4}, 
       "log.final.sun.LostAngMom": {"value": 3.532078e+32, "unit": (u.kg * u.m ** 2) / u.sec, "rtol": 1e-4}, 
       "log.final.sun.Luminosity": {"value": 3.846000e+26, "unit": u.W, "rtol": 1e-4}, 
       "log.final.sun.LXUVStellar": {"value": 3.846000e+23, "unit": u.W, "rtol": 1e-4}, 
       "log.final.sun.Temperature": {"value": 5778.000000, "unit": u.K, "rtol": 1e-4}, 
       "log.final.sun.LXUVFrac": {"value": 0.001000, "rtol": 1e-4}, 
       "log.final.sun.RossbyNumber": {"value": 0.078260, "rtol": 1e-4}, 
       "log.final.sun.DRotPerDtStellar": {"value": 6.558557e-13, "rtol": 1e-4}, 
       "log.final.earth.Mass": {"value": 5.971546e+24, "unit": u.kg, "rtol": 1e-4}, 
       "log.final.earth.Obliquity": {"value": 0.959931, "unit": u.rad, "rtol": 1e-4}, 
       "log.final.earth.PrecA": {"value": 0.000000, "unit": u.rad, "rtol": 1e-4}, 
       "log.final.earth.Radius": {"value": 6.378100e+06, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.RadGyra": {"value": 0.500000, "rtol": 1e-4}, 
       "log.final.earth.BodyType": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.Density": {"value": 5494.449526, "unit": u.kg / u.m ** 3, "rtol": 1e-4}, 
       "log.final.earth.HZLimitDryRunaway": {"value": 1.081713e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.HZLimRecVenus": {"value": 1.118929e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.HZLimRunaway": {"value": 1.461108e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.HZLimMoistGreenhouse": {"value": 1.480517e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.HZLimMaxGreenhouse": {"value": 2.509538e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.HZLimEarlyMars": {"value": 2.738109e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.Instellation": {"value": 1314.462644, "unit": u.kg / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.earth.Eccentricity": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.MeanMotion": {"value": 1.932716e-07, "unit": 1 / u.sec, "rtol": 1e-4}, 
       "log.final.earth.OrbPeriod": {"value": 3.250961e+07, "unit": u.sec, "rtol": 1e-4}, 
       "log.final.earth.SemiMajorAxis": {"value": 1.525898e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.COPP": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.TGlobal": {"value": 7.082835, "unit": u.deg_C, "rtol": 1e-4}, 
       "log.final.earth.AlbedoGlobal": {"value": 0.365352, "rtol": 1e-4}, 
       "log.final.earth.FluxInGlobal": {"value": 217.176511, "unit": u.kg / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.earth.FluxOutGlobal": {"value": 218.103125, "unit": u.W / u.m ** 2, "rtol": 1e-4}, 
       "log.final.earth.TotIceMass": {"value": 3.071389e+15, "unit": u.kg, "rtol": 1e-4}, 
       "log.final.earth.TotIceFlow": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4}, 
       "log.final.earth.TotIceBalance": {"value": 9.223785e-08, "unit": u.kg, "rtol": 1e-4}, 
       "log.final.earth.SkipSeas": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.AreaIceCov": {"value": 0.054040, "rtol": 1e-4}, 
       "log.final.earth.Latitude": {"value": 83.402352, "unit": u.deg, "rtol": 1e-4}, 
       "log.final.earth.TempLat": {"value": 9.357899, "unit": u.deg_C, "rtol": 1e-4}, 
       "log.final.earth.AlbedoLat": {"value": 0.377297, "rtol": 1e-4}, 
       "log.final.earth.AnnInsol": {"value": 342.162291, "unit": u.W / u.m ** 2, "rtol": 1e-4}, 
       "log.final.earth.FluxMerid": {"value": -0.070969, "unit": u.PW, "rtol": 1e-4}, 
       "log.final.earth.FluxIn": {"value": 226.923741, "unit": u.W / u.m ** 2, "rtol": 1e-4}, 
       "log.final.earth.FluxOut": {"value": 222.858010, "unit": u.W / u.m ** 2, "rtol": 1e-4}, 
       "log.final.earth.DivFlux": {"value": 4.801158, "unit": u.W / u.m ** 2, "rtol": 1e-4}, 
       "log.final.earth.IceMass": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.IceHeight": {"value": 0.000000, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.DIceMassDt": {"value": 0.000000, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.IceFlow": {"value": 0.000000, "unit": u.m / u.sec, "rtol": 1e-4}, 
       "log.final.earth.EnergyResL": {"value": -0.875366, "unit": u.kg / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.earth.EnergyResW": {"value": 0.238817, "unit": u.kg / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.earth.BedrockH": {"value": 0.000000, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.TempLandLat": {"value": 274.594095, "unit": u.sec, "rtol": 1e-4}, 
       "log.final.earth.TempWaterLat": {"value": 286.357435, "unit": u.sec, "rtol": 1e-4}, 
       "log.final.earth.AlbedoLandLat": {"value": 0.523054, "rtol": 1e-4}, 
       "log.final.earth.AlbedoWaterLat": {"value": 0.302211, "rtol": 1e-4}, 
       "log.final.earth.TempMinLat": {"value": -7.106305, "unit": u.deg_C, "rtol": 1e-4}, 
       "log.final.earth.TempMaxLat": {"value": 34.755235, "unit": u.deg_C, "rtol": 1e-4}, 
       "log.final.earth.Snowball": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.PlanckBAvg": {"value": 2.090000, "rtol": 1e-4}, 
       "log.final.earth.IceAccum": {"value": 0.458812, "rtol": 1e-4}, 
       "log.final.earth.IceAblate": {"value": -0.343222, "rtol": 1e-4}, 
       "log.final.earth.TempMaxLand": {"value": 337.829716, "unit": u.sec, "rtol": 1e-4}, 
       "log.final.earth.TempMaxWater": {"value": 294.261368, "unit": u.sec, "rtol": 1e-4}, 
       "log.final.earth.PeakInsol": {"value": 1069.614002, "unit": u.kg / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.earth.IceCapNorthLand": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.IceCapNorthSea": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.IceCapSouthLand": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.IceCapSouthSea": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.IceBeltLand": {"value": 1.000000, "rtol": 1e-4}, 
       "log.final.earth.IceBeltSea": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.SnowballLand": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.SnowballSea": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.IceFree": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.IceCapNorthLatLand": {"value": 100.000000, "unit": u.rad, "rtol": 1e-4}, 
       "log.final.earth.IceCapNorthLatSea": {"value": 100.000000, "unit": u.rad, "rtol": 1e-4}, 
       "log.final.earth.IceCapSouthLatLand": {"value": 100.000000, "unit": u.rad, "rtol": 1e-4}, 
       "log.final.earth.IceCapSouthLatSea": {"value": 100.000000, "unit": u.rad, "rtol": 1e-4}, 
       "log.final.earth.IceBeltNorthLatLand": {"value": 0.173048, "unit": u.rad, "rtol": 1e-4}, 
       "log.final.earth.IceBeltNorthLatSea": {"value": 100.000000, "unit": u.rad, "rtol": 1e-4}, 
       "log.final.earth.IceBeltSouthLatLand": {"value": -0.146216, "unit": u.rad, "rtol": 1e-4}, 
       "log.final.earth.IceBeltSouthLatSea": {"value": 100.000000, "unit": u.rad, "rtol": 1e-4}, 
   } 
)
class TestIceBelts(Benchmark): 
   pass 
