from benchmark import Benchmark, benchmark 
import astropy.units as u 
 
@benchmark( 
   { 
       "log.initial.system.Age": {"value": 0.000000, "unit": u.sec}, 
       "log.initial.system.Time": {"value": 0.000000, "unit": u.sec}, 
       "log.initial.system.TotAngMom": {"value": 1.474456e+42, "unit": (u.kg * u.m ** 2) / u.sec}, 
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
       "log.initial.earth.Mass": {"value": 5.972186e+24, "unit": u.kg}, 
       "log.initial.earth.Radius": {"value": 6.378100e+06, "unit": u.m}, 
       "log.initial.earth.RadGyra": {"value": 0.500000}, 
       "log.initial.earth.BodyType": {"value": 0.000000}, 
       "log.initial.earth.Density": {"value": 5495.038549, "unit": u.kg / u.m ** 3}, 
       "log.initial.earth.SurfEnFluxTotal": {"value": 196.308833, "unit": u.kg / u.sec ** 3}, 
       "log.initial.earth.TidalQ": {"value": -1.000000}, 
       "log.initial.earth.ImK2": {"value": -1.000000}, 
       "log.initial.earth.K2": {"value": 1.500000}, 
       "log.initial.earth.K2Man": {"value": -1.000000}, 
       "log.initial.earth.Imk2Man": {"value": -1.000000}, 
       "log.initial.earth.TidalQMantle": {"value": -1.000000}, 
       "log.initial.earth.ViscUMan": {"value": 9.025442e+07, "unit": u.m ** 2 / u.sec}, 
       "log.initial.earth.HZLimitDryRunaway": {"value": 1.358020e+11, "unit": u.m}, 
       "log.initial.earth.HZLimRecVenus": {"value": 1.118929e+11, "unit": u.m}, 
       "log.initial.earth.HZLimRunaway": {"value": 1.461108e+11, "unit": u.m}, 
       "log.initial.earth.HZLimMoistGreenhouse": {"value": 1.480517e+11, "unit": u.m}, 
       "log.initial.earth.HZLimMaxGreenhouse": {"value": 2.509538e+11, "unit": u.m}, 
       "log.initial.earth.HZLimEarlyMars": {"value": 2.738109e+11, "unit": u.m}, 
       "log.initial.earth.Instellation": {"value": 1367.757675, "unit": u.kg / u.sec ** 3}, 
       "log.initial.earth.D26AlPowerDt": {"value": -1.000000}, 
       "log.initial.earth.D26AlNumManDt": {"value": 0.000000, "unit": 1 / u.sec}, 
       "log.initial.earth.D40KPowerDt": {"value": -1.000000}, 
       "log.initial.earth.D40KNumManDt": {"value": -1.694596e+26, "unit": 1 / u.sec}, 
       "log.initial.earth.D232ThNumManDt": {"value": -9.534863e+23, "unit": 1 / u.sec}, 
       "log.initial.earth.D238UNumManDt": {"value": -1.408812e+24, "unit": 1 / u.sec}, 
       "log.initial.earth.D235UNumManDt": {"value": -3.089017e+24, "unit": 1 / u.sec}, 
       "log.initial.earth.RadPowerMan": {"value": 74.591650, "unit": u.TW}, 
       "log.initial.earth.RadPowerCore": {"value": 34.624677, "unit": u.TW}, 
       "log.initial.earth.RadPowerCrust": {"value": 33.267780, "unit": u.TW}, 
       "log.initial.earth.RadPowerTotal": {"value": 142.484107, "unit": u.TW}, 
       "log.initial.earth.SurfEnFluxRadTotal": {"value": 0.278724, "unit": u.kg / u.sec ** 3}, 
       "log.initial.earth.TMan": {"value": 3000.000000, "unit": u.K}, 
       "log.initial.earth.TUMan": {"value": 2100.000000, "unit": u.K}, 
       "log.initial.earth.TLMan": {"value": 3900.000000, "unit": u.K}, 
       "log.initial.earth.TCore": {"value": 6000.000000, "unit": u.K}, 
       "log.initial.earth.TCMB": {"value": 4800.000000, "unit": u.K}, 
       "log.initial.earth.BLUMan": {"value": 0.042882, "unit": u.km}, 
       "log.initial.earth.BLLMan": {"value": 19.389573, "unit": u.km}, 
       "log.initial.earth.TJumpUMan": {"value": 1800.000000, "unit": u.K}, 
       "log.initial.earth.TJumpLMan": {"value": 900.000000, "unit": u.K}, 
       "log.initial.earth.SignTJumpUMan": {"value": 1.000000}, 
       "log.initial.earth.SignTJumpLMan": {"value": 1.000000}, 
       "log.initial.earth.ViscLMan": {"value": 4.171658e+15, "unit": u.m ** 2 / u.sec}, 
       "log.initial.earth.ShmodUMan": {"value": 4897.808734}, 
       "log.initial.earth.FMeltUMan": {"value": 1.000000, "unit": u.nd}, 
       "log.initial.earth.FMeltLMan": {"value": 0.000000}, 
       "log.initial.earth.MeltfactorUMan": {"value": 1.925879e+07}, 
       "log.initial.earth.MeltfactorLMan": {"value": 1.000000}, 
       "log.initial.earth.DepthMeltMan": {"value": 1.503842e+06}, 
       "log.initial.earth.TDepthMeltMan": {"value": 2851.899507}, 
       "log.initial.earth.TJumpMeltMan": {"value": 1799.978559}, 
       "log.initial.earth.MeltMassFluxMan": {"value": 4.581035e+10, "unit": u.kg / u.sec}, 
       "log.initial.earth.ViscUManArr": {"value": 1.738191e+15, "unit": u.m ** 2 / u.sec}, 
       "log.initial.earth.RayleighMan": {"value": 3.030360e+16, "unit": u.nd}, 
       "log.initial.earth.ViscMMan": {"value": 9.025442e+08, "unit": u.m ** 2 / u.sec}, 
       "log.initial.earth.TDotMan": {"value": -1.534504e-11, "unit": u.K / u.sec}, 
       "log.initial.earth.TDotCore": {"value": -2.210642e-14, "unit": u.K / u.sec}, 
       "log.initial.earth.HfluxUMan": {"value": 176.296472}, 
       "log.initial.earth.HflowUMan": {"value": 8.992257e+04, "unit": u.TW}, 
       "log.initial.earth.HfluxLMan": {"value": 0.464167}, 
       "log.initial.earth.HflowLMan": {"value": 7.067929e+13}, 
       "log.initial.earth.HfluxCMB": {"value": 0.464167}, 
       "log.initial.earth.HflowCMB": {"value": 70.679290, "unit": u.TW}, 
       "log.initial.earth.HflowLatentMan": {"value": 2.237044e+16}, 
       "log.initial.earth.HflowMeltMan": {"value": 1.043089e+04, "unit": u.TW}, 
       "log.initial.earth.HflowLatentIC": {"value": 0.000000}, 
       "log.initial.earth.PowerGravIC": {"value": 0.000000}, 
       "log.initial.earth.HflowSurf": {"value": 1.003535e+17}, 
       "log.initial.earth.HflowSecMan": {"value": 7.783775e+04, "unit": u.TW}, 
       "log.initial.earth.HfluxCMBAd": {"value": 0.049882}, 
       "log.initial.earth.HfluxCMBConv": {"value": 0.414285}, 
       "log.initial.earth.RIC": {"value": 0.000000, "unit": u.km}, 
       "log.initial.earth.DRICDTCMB": {"value": 0.000000}, 
       "log.initial.earth.RICDot": {"value": 0.000000}, 
       "log.initial.earth.ChiOC": {"value": 0.094946}, 
       "log.initial.earth.ChiIC": {"value": 0.000000}, 
       "log.initial.earth.ThermConductOC": {"value": 120.000000}, 
       "log.initial.earth.MassOC": {"value": 1.941615e+24}, 
       "log.initial.earth.MassIC": {"value": 0.000000}, 
       "log.initial.earth.MassChiOC": {"value": 1.843482e+23}, 
       "log.initial.earth.MassChiIC": {"value": 0.000000}, 
       "log.initial.earth.DTChi": {"value": 0.000000}, 
       "log.initial.earth.CoreBuoyTherm": {"value": 4.757325e-12, "unit": u.m ** 2 / u.sec ** 3}, 
       "log.initial.earth.CoreBuoyCompo": {"value": 0.000000, "unit": u.m ** 2 / u.sec ** 3}, 
       "log.initial.earth.CoreBuoyTotal": {"value": 4.757325e-12, "unit": u.m ** 2 / u.sec ** 3}, 
       "log.initial.earth.GravICB": {"value": 0.000000}, 
       "log.initial.earth.MagMom": {"value": 1.730934}, 
       "log.initial.earth.PresSWind": {"value": 2.676100e-09}, 
       "log.initial.earth.MagPauseRad": {"value": 1.200746}, 
       "log.initial.earth.ViscJumpMan": {"value": 2.400000}, 
       "log.initial.earth.EruptEff": {"value": 0.100000}, 
       "log.initial.earth.TrefLind": {"value": 5451.600000}, 
       "log.initial.earth.DynViscUMan": {"value": 2.256360e+09, "unit": u.Joule}, 
       "log.final.system.Age": {"value": 1.420092e+17, "unit": u.sec, "rtol": 1e-4}, 
       "log.final.system.Time": {"value": 1.420092e+17, "unit": u.sec, "rtol": 1e-4}, 
       "log.final.system.TotAngMom": {"value": 1.474456e+42, "unit": (u.kg * u.m ** 2) / u.sec, "rtol": 1e-4}, 
       "log.final.system.TotEnergy": {"value": -7.839372e+41, "unit": u.Joule, "rtol": 1e-4}, 
       "log.final.system.PotEnergy": {"value": -7.839908e+41, "unit": u.Joule, "rtol": 1e-4}, 
       "log.final.system.KinEnergy": {"value": 6.207914e+36, "unit": u.Joule, "rtol": 1e-4}, 
       "log.final.sun.Mass": {"value": 1.988416e+30, "unit": u.kg, "rtol": 1e-4}, 
       "log.final.sun.Radius": {"value": 2.019571e+08, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.RadGyra": {"value": 0.500000, "rtol": 1e-4}, 
       "log.final.sun.RotAngMom": {"value": 5.017307e+41, "unit": (u.kg * u.m ** 2) / u.sec, "rtol": 1e-4}, 
       "log.final.sun.RotVel": {"value": 4997.631307, "unit": u.m / u.sec, "rtol": 1e-4}, 
       "log.final.sun.BodyType": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.sun.RotRate": {"value": 2.474600e-05, "unit": 1 / u.sec, "rtol": 1e-4}, 
       "log.final.sun.RotPer": {"value": 2.539071e+05, "unit": u.sec, "rtol": 1e-4}, 
       "log.final.sun.Density": {"value": 5.762900e+04, "unit": u.kg / u.m ** 3, "rtol": 1e-4}, 
       "log.final.sun.HZLimitDryRunaway": {"value": 1.357831e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.HZLimRecVenus": {"value": 1.118929e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.HZLimRunaway": {"value": 1.461108e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.HZLimMoistGreenhouse": {"value": 1.480517e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.HZLimMaxGreenhouse": {"value": 2.509538e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.HZLimEarlyMars": {"value": 2.738109e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.Instellation": {"value": -1.000000, "unit": u.kg / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.sun.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m, "rtol": 1e-4}, 
       "log.final.sun.LXUVTot": {"value": 3.560885e+21, "unit": u.kg / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.sun.LostEnergy": {"value": 4.740481e+37, "unit": u.Joule, "rtol": 1e-4}, 
       "log.final.sun.LostAngMom": {"value": 9.727251e+41, "unit": (u.kg * u.m ** 2) / u.sec, "rtol": 1e-4}, 
       "log.final.sun.Luminosity": {"value": 3.846000e+26, "unit": u.W, "rtol": 1e-4}, 
       "log.final.sun.LXUVStellar": {"value": 3.560885e+21, "unit": u.W, "rtol": 1e-4}, 
       "log.final.sun.Temperature": {"value": 5778.000000, "unit": u.K, "rtol": 1e-4}, 
       "log.final.sun.LXUVFrac": {"value": 9.258670e-06, "rtol": 1e-4}, 
       "log.final.sun.RossbyNumber": {"value": 0.229985, "rtol": 1e-4}, 
       "log.final.sun.DRotPerDtStellar": {"value": 1.927389e-12, "rtol": 1e-4}, 
       "log.final.earth.Mass": {"value": 5.972186e+24, "unit": u.kg, "rtol": 1e-4}, 
       "log.final.earth.Radius": {"value": 6.378100e+06, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.RadGyra": {"value": 0.500000, "rtol": 1e-4}, 
       "log.final.earth.BodyType": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.Density": {"value": 5495.038549, "unit": u.kg / u.m ** 3, "rtol": 1e-4}, 
       "log.final.earth.SurfEnFluxTotal": {"value": 0.065450, "unit": u.kg / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.earth.TidalQ": {"value": -1.000000, "rtol": 1e-4}, 
       "log.final.earth.ImK2": {"value": -1.000000, "rtol": 1e-4}, 
       "log.final.earth.K2": {"value": 0.486732, "rtol": 1e-4}, 
       "log.final.earth.K2Man": {"value": -1.000000, "rtol": 1e-4}, 
       "log.final.earth.Imk2Man": {"value": -1.000000, "rtol": 1e-4}, 
       "log.final.earth.TidalQMantle": {"value": -1.000000, "rtol": 1e-4}, 
       "log.final.earth.ViscUMan": {"value": 4.536769e+17, "unit": u.m ** 2 / u.sec, "rtol": 1e-4}, 
       "log.final.earth.HZLimitDryRunaway": {"value": 1.358020e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.HZLimRecVenus": {"value": 1.118929e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.HZLimRunaway": {"value": 1.461108e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.HZLimMoistGreenhouse": {"value": 1.480517e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.HZLimMaxGreenhouse": {"value": 2.509538e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.HZLimEarlyMars": {"value": 2.738109e+11, "unit": u.m, "rtol": 1e-4}, 
       "log.final.earth.Instellation": {"value": 1367.757675, "unit": u.kg / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.earth.D26AlPowerDt": {"value": -1.000000, "rtol": 1e-4}, 
       "log.final.earth.D26AlNumManDt": {"value": 0.000000, "unit": 1 / u.sec, "rtol": 1e-4}, 
       "log.final.earth.D40KPowerDt": {"value": -1.000000, "rtol": 1e-4}, 
       "log.final.earth.D40KNumManDt": {"value": -1.425473e+25, "unit": 1 / u.sec, "rtol": 1e-4}, 
       "log.final.earth.D232ThNumManDt": {"value": -7.630893e+23, "unit": 1 / u.sec, "rtol": 1e-4}, 
       "log.final.earth.D238UNumManDt": {"value": -7.013465e+23, "unit": 1 / u.sec, "rtol": 1e-4}, 
       "log.final.earth.D235UNumManDt": {"value": -3.671217e+22, "unit": 1 / u.sec, "rtol": 1e-4}, 
       "log.final.earth.RadPowerMan": {"value": 14.306064, "unit": u.TW, "rtol": 1e-4}, 
       "log.final.earth.RadPowerCore": {"value": 3.030298, "unit": u.TW, "rtol": 1e-4}, 
       "log.final.earth.RadPowerCrust": {"value": 6.926650, "unit": u.TW, "rtol": 1e-4}, 
       "log.final.earth.RadPowerTotal": {"value": 24.322856, "unit": u.TW, "rtol": 1e-4}, 
       "log.final.earth.SurfEnFluxRadTotal": {"value": 0.047580, "unit": u.kg / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.earth.TMan": {"value": 2257.850930, "unit": u.K, "rtol": 1e-4}, 
       "log.final.earth.TUMan": {"value": 1580.495651, "unit": u.K, "rtol": 1e-4}, 
       "log.final.earth.TLMan": {"value": 2935.206210, "unit": u.K, "rtol": 1e-4}, 
       "log.final.earth.TCore": {"value": 4999.131849, "unit": u.K, "rtol": 1e-4}, 
       "log.final.earth.TCMB": {"value": 3999.305479, "unit": u.K, "rtol": 1e-4}, 
       "log.final.earth.BLUMan": {"value": 82.287509, "unit": u.km, "rtol": 1e-4}, 
       "log.final.earth.BLLMan": {"value": 120.474484, "unit": u.km, "rtol": 1e-4}, 
       "log.final.earth.TJumpUMan": {"value": 1280.495651, "unit": u.K, "rtol": 1e-4}, 
       "log.final.earth.TJumpLMan": {"value": 1064.099270, "unit": u.K, "rtol": 1e-4}, 
       "log.final.earth.SignTJumpUMan": {"value": 1.000000, "rtol": 1e-4}, 
       "log.final.earth.SignTJumpLMan": {"value": 1.000000, "rtol": 1e-4}, 
       "log.final.earth.ViscLMan": {"value": 1.183120e+18, "unit": u.m ** 2 / u.sec, "rtol": 1e-4}, 
       "log.final.earth.ShmodUMan": {"value": 3.747198e+12, "rtol": 1e-4}, 
       "log.final.earth.FMeltUMan": {"value": 0.032556, "unit": u.nd, "rtol": 1e-4}, 
       "log.final.earth.FMeltLMan": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.MeltfactorUMan": {"value": 1.086603, "rtol": 1e-4}, 
       "log.final.earth.MeltfactorLMan": {"value": 1.000000, "rtol": 1e-4}, 
       "log.final.earth.DepthMeltMan": {"value": 1.015466e+05, "rtol": 1e-4}, 
       "log.final.earth.TDepthMeltMan": {"value": 1590.125195, "rtol": 1e-4}, 
       "log.final.earth.TJumpMeltMan": {"value": 1239.351897, "rtol": 1e-4}, 
       "log.final.earth.MeltMassFluxMan": {"value": 7.772176e+05, "unit": u.kg / u.sec, "rtol": 1e-4}, 
       "log.final.earth.ViscUManArr": {"value": 4.929667e+17, "unit": u.m ** 2 / u.sec, "rtol": 1e-4}, 
       "log.final.earth.RayleighMan": {"value": 5.235041e+06, "unit": u.nd, "rtol": 1e-4}, 
       "log.final.earth.ViscMMan": {"value": 4.536769e+18, "unit": u.m ** 2 / u.sec, "rtol": 1e-4}, 
       "log.final.earth.TDotMan": {"value": -9.133773e-16, "unit": u.K / u.sec, "rtol": 1e-4}, 
       "log.final.earth.TDotCore": {"value": -1.891962e-15, "unit": u.K / u.sec, "rtol": 1e-4}, 
       "log.final.earth.HfluxUMan": {"value": 0.065357, "rtol": 1e-4}, 
       "log.final.earth.HflowUMan": {"value": 33.336389, "unit": u.TW, "rtol": 1e-4}, 
       "log.final.earth.HfluxLMan": {"value": 0.088326, "rtol": 1e-4}, 
       "log.final.earth.HflowLMan": {"value": 1.344946e+13, "rtol": 1e-4}, 
       "log.final.earth.HfluxCMB": {"value": 0.088326, "rtol": 1e-4}, 
       "log.final.earth.HflowCMB": {"value": 13.449464, "unit": u.TW, "rtol": 1e-4}, 
       "log.final.earth.HflowLatentMan": {"value": 1.038850e+12, "rtol": 1e-4}, 
       "log.final.earth.HflowMeltMan": {"value": 0.121851, "unit": u.TW, "rtol": 1e-4}, 
       "log.final.earth.HflowLatentIC": {"value": 8.208257e+12, "rtol": 1e-4}, 
       "log.final.earth.PowerGravIC": {"value": 3.283303e+12, "rtol": 1e-4}, 
       "log.final.earth.HflowSurf": {"value": 3.345824e+13, "rtol": 1e-4}, 
       "log.final.earth.HflowSecMan": {"value": 4.633108, "unit": u.TW, "rtol": 1e-4}, 
       "log.final.earth.HfluxCMBAd": {"value": 0.034629, "rtol": 1e-4}, 
       "log.final.earth.HfluxCMBConv": {"value": 0.053697, "rtol": 1e-4}, 
       "log.final.earth.RIC": {"value": 1233.676354, "unit": u.km, "rtol": 1e-4}, 
       "log.final.earth.DRICDTCMB": {"value": -1.851901e+04, "rtol": 1e-4}, 
       "log.final.earth.RICDot": {"value": 2.817177e-11, "rtol": 1e-4}, 
       "log.final.earth.ChiOC": {"value": 0.015281, "rtol": 1e-4}, 
       "log.final.earth.ChiIC": {"value": 1.528121, "rtol": 1e-4}, 
       "log.final.earth.ThermConductOC": {"value": 99.982637, "rtol": 1e-4}, 
       "log.final.earth.MassOC": {"value": 1.839372e+24, "rtol": 1e-4}, 
       "log.final.earth.MassIC": {"value": 1.022435e+23, "rtol": 1e-4}, 
       "log.final.earth.MassChiOC": {"value": 2.810783e+22, "rtol": 1e-4}, 
       "log.final.earth.MassChiIC": {"value": 1.562404e+23, "rtol": 1e-4}, 
       "log.final.earth.DTChi": {"value": 0.000000, "rtol": 1e-4}, 
       "log.final.earth.CoreBuoyTherm": {"value": 6.166165e-13, "unit": u.m ** 2 / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.earth.CoreBuoyCompo": {"value": 8.467345e-13, "unit": u.m ** 2 / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.earth.CoreBuoyTotal": {"value": 1.463351e-12, "unit": u.m ** 2 / u.sec ** 3, "rtol": 1e-4}, 
       "log.final.earth.GravICB": {"value": 3.756670, "rtol": 1e-4}, 
       "log.final.earth.MagMom": {"value": 1.009864, "rtol": 1e-4}, 
       "log.final.earth.PresSWind": {"value": 2.676100e-09, "rtol": 1e-4}, 
       "log.final.earth.MagPauseRad": {"value": 1.003333, "rtol": 1e-4}, 
       "log.final.earth.ViscJumpMan": {"value": 2.400000, "rtol": 1e-4}, 
       "log.final.earth.EruptEff": {"value": 0.100000, "rtol": 1e-4}, 
       "log.final.earth.TrefLind": {"value": 5451.600000, "rtol": 1e-4}, 
       "log.final.earth.DynViscUMan": {"value": 1.134192e+19, "unit": u.Joule, "rtol": 1e-4}, 
   } 
)
class Test_EarthInterior(Benchmark): 
   pass 
