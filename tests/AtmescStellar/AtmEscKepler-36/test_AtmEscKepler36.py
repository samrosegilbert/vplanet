import astropy.units as u
import pytest
from benchmark import Benchmark, benchmark


@benchmark(
    {
        "log.initial.system.Age": {"value": 3.155760e14, "unit": u.sec},
        "log.initial.system.Time": {"value": 0.000000, "unit": u.sec},
        "log.initial.system.TotAngMom": {
            "value": 8.090294e47,
            "unit": (u.kg * u.m**2) / u.sec,
        },
        "log.initial.system.TotEnergy": {"value": 2.941607e43, "unit": u.Joule},
        "log.initial.system.PotEnergy": {"value": -1.058388e39, "unit": u.Joule},
        "log.initial.system.KinEnergy": {"value": 2.941713e43, "unit": u.Joule},
        "log.initial.system.DeltaTime": {"value": 0.000000, "unit": u.sec},
        "log.initial.star.Mass": {"value": 1.988416e30, "unit": u.kg},
        "log.initial.star.Radius": {"value": 1.495979e11, "unit": u.m},
        "log.initial.star.RadGyra": {"value": 0.500000},
        "log.initial.star.RotAngMom": {
            "value": 8.090292e47,
            "unit": (u.kg * u.m**2) / u.sec,
        },
        "log.initial.star.RotVel": {"value": 1.087906e07, "unit": u.m / u.sec},
        "log.initial.star.BodyType": {"value": 0.000000},
        "log.initial.star.RotRate": {"value": 7.272205e-05, "unit": 1 / u.sec},
        "log.initial.star.RotPer": {"value": 8.640000e04, "unit": u.sec},
        "log.initial.star.Density": {"value": 0.000142, "unit": u.kg / u.m**3},
        "log.initial.star.HZLimitDryRunaway": {"value": 1.357831e11, "unit": u.m},
        "log.initial.star.HZLimRecVenus": {"value": 1.118929e11, "unit": u.m},
        "log.initial.star.HZLimRunaway": {"value": 1.461108e11, "unit": u.m},
        "log.initial.star.HZLimMoistGreenhouse": {"value": 1.480517e11, "unit": u.m},
        "log.initial.star.HZLimMaxGreenhouse": {"value": 2.509538e11, "unit": u.m},
        "log.initial.star.HZLimEarlyMars": {"value": 2.738109e11, "unit": u.m},
        "log.initial.star.Instellation": {
            "value": -1.000000,
            "unit": u.kg / u.sec**3,
        },
        "log.initial.star.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.initial.star.LXUVTot": {"value": 3.846000e23, "unit": u.kg / u.sec**3},
        "log.initial.star.LostEnergy": {"value": 5.562685e-309, "unit": u.Joule},
        "log.initial.star.LostAngMom": {
            "value": 5.562685e-309,
            "unit": (u.kg * u.m**2) / u.sec,
        },
        "log.initial.star.Luminosity": {"value": 3.846000e26, "unit": u.W},
        "log.initial.star.LXUVStellar": {"value": 3.846000e23, "unit": u.W},
        "log.initial.star.Temperature": {"value": 5778.000000, "unit": u.K},
        "log.initial.star.LXUVFrac": {"value": 0.001000},
        "log.initial.star.RossbyNumber": {"value": 0.078260},
        "log.initial.star.DRotPerDtStellar": {"value": 0.002412},
        "log.initial.b.Mass": {"value": 1.818180, "unit": u.Mearth},
        "log.initial.b.Radius": {"value": 1.922653e08, "unit": u.m},
        "log.initial.b.RadGyra": {"value": 0.500000},
        "log.initial.b.BodyType": {"value": 0.000000},
        "log.initial.b.Density": {"value": 0.364736, "unit": u.kg / u.m**3},
        "log.initial.b.HZLimitDryRunaway": {"value": 1.357831e11, "unit": u.m},
        "log.initial.b.HZLimRecVenus": {"value": 1.118929e11, "unit": u.m},
        "log.initial.b.HZLimRunaway": {"value": 1.461108e11, "unit": u.m},
        "log.initial.b.HZLimMoistGreenhouse": {"value": 1.480517e11, "unit": u.m},
        "log.initial.b.HZLimMaxGreenhouse": {"value": 2.509538e11, "unit": u.m},
        "log.initial.b.HZLimEarlyMars": {"value": 2.738109e11, "unit": u.m},
        "log.initial.b.Instellation": {"value": 1.367567e05, "unit": u.kg / u.sec**3},
        "log.initial.b.MeanMotion": {"value": 6.296061e-06, "unit": 1 / u.sec},
        "log.initial.b.OrbPeriod": {"value": 9.979550e05, "unit": u.sec},
        "log.initial.b.SemiMajorAxis": {"value": 1.495979e10, "unit": u.m},
        "log.initial.b.LXUVTot": {"value": -1.000000, "unit": u.kg / u.sec**3},
        "log.initial.b.SurfWaterMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.b.EnvelopeMass": {"value": 0.818180, "unit": u.Mearth},
        "log.initial.b.OxygenMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.b.RGLimit": {"value": 1.403151e11, "unit": u.m},
        "log.initial.b.XO": {"value": 0.000000},
        "log.initial.b.EtaO": {"value": 0.000000},
        "log.initial.b.PlanetRadius": {"value": 1.922653e08, "unit": u.m},
        "log.initial.b.OxygenMantleMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.b.RadXUV": {"value": -1.000000, "unit": u.m},
        "log.initial.b.RadSolid": {"value": -1.000000, "unit": u.m},
        "log.initial.b.PresXUV": {"value": 5.000000},
        "log.initial.b.ScaleHeight": {"value": -1.000000, "unit": u.m},
        "log.initial.b.ThermTemp": {"value": 400.000000, "unit": u.K},
        "log.initial.b.AtmGasConst": {"value": 4124.000000},
        "log.initial.b.PresSurf": {"value": -1.000000, "unit": u.Pa},
        "log.initial.b.DEnvMassDt": {"value": -4.213344e11, "unit": u.kg / u.sec},
        "log.initial.b.FXUV": {"value": 136.756693, "unit": u.W / u.m**2},
        "log.initial.b.AtmXAbsEffH2O": {"value": 0.300000},
        "log.initial.b.RocheRadius": {"value": 1.826583e08, "unit": u.m},
        "log.initial.b.BondiRadius": {"value": 4.689081e06, "unit": u.m},
        "log.initial.b.HEscapeRegime": {"value": 3.000000},
        "log.initial.b.RRCriticalFlux": {"value": 0.014584, "unit": u.W / u.m**2},
        "log.initial.b.KTide": {"value": 1.000000},
        "log.initial.b.RGDuration": {"value": 0.00000e00, "unit": u.yr},
        "log.initial.c.Mass": {"value": 8.510699e25, "unit": u.kg},
        "log.initial.c.Radius": {"value": 1.009224e08, "unit": u.m},
        "log.initial.c.RadGyra": {"value": 0.500000},
        "log.initial.c.BodyType": {"value": 0.000000},
        "log.initial.c.Density": {"value": 19.765777, "unit": u.kg / u.m**3},
        "log.initial.c.HZLimitDryRunaway": {"value": 1.357831e11, "unit": u.m},
        "log.initial.c.HZLimRecVenus": {"value": 1.118929e11, "unit": u.m},
        "log.initial.c.HZLimRunaway": {"value": 1.461108e11, "unit": u.m},
        "log.initial.c.HZLimMoistGreenhouse": {"value": 1.480517e11, "unit": u.m},
        "log.initial.c.HZLimMaxGreenhouse": {"value": 2.509538e11, "unit": u.m},
        "log.initial.c.HZLimEarlyMars": {"value": 2.738109e11, "unit": u.m},
        "log.initial.c.Instellation": {"value": 1.367567e05, "unit": u.kg / u.sec**3},
        "log.initial.c.MeanMotion": {"value": 6.296178e-06, "unit": 1 / u.sec},
        "log.initial.c.OrbPeriod": {"value": 9.979364e05, "unit": u.sec},
        "log.initial.c.SemiMajorAxis": {"value": 1.495979e10, "unit": u.m},
        "log.initial.c.LXUVTot": {"value": -1.000000, "unit": u.kg / u.sec**3},
        "log.initial.c.SurfWaterMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.c.EnvelopeMass": {"value": 6.412750, "unit": u.Mearth},
        "log.initial.c.OxygenMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.c.RGLimit": {"value": 1.342939e11, "unit": u.m},
        "log.initial.c.XO": {"value": 0.000000},
        "log.initial.c.EtaO": {"value": 0.000000},
        "log.initial.c.PlanetRadius": {"value": 1.009224e08, "unit": u.m},
        "log.initial.c.OxygenMantleMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.c.RadXUV": {"value": -1.000000, "unit": u.m},
        "log.initial.c.RadSolid": {"value": -1.000000, "unit": u.m},
        "log.initial.c.PresXUV": {"value": 5.000000},
        "log.initial.c.ScaleHeight": {"value": -1.000000, "unit": u.m},
        "log.initial.c.ThermTemp": {"value": 400.000000, "unit": u.K},
        "log.initial.c.AtmGasConst": {"value": 4124.000000},
        "log.initial.c.PresSurf": {"value": -1.000000, "unit": u.Pa},
        "log.initial.c.DEnvMassDt": {"value": -1.309930e10, "unit": u.kg / u.sec},
        "log.initial.c.FXUV": {"value": 136.756693, "unit": u.W / u.m**2},
        "log.initial.c.AtmXAbsEffH2O": {"value": 0.300000},
        "log.initial.c.RocheRadius": {"value": 3.628310e08, "unit": u.m},
        "log.initial.c.BondiRadius": {"value": 3.675215e07, "unit": u.m},
        "log.initial.c.HEscapeRegime": {"value": 3.000000},
        "log.initial.c.RRCriticalFlux": {"value": 2.182140, "unit": u.W / u.m**2},
        "log.initial.c.KTide": {"value": 0.593531},
        "log.initial.c.RGDuration": {"value": 0.00000e00, "unit": u.yr},
        "log.final.system.Age": {"value": 1.581036e17, "unit": u.sec, "rtol": 1e-4},
        "log.final.system.Time": {"value": 1.577880e17, "unit": u.sec, "rtol": 1e-4},
        "log.final.system.TotAngMom": {
            "value": 8.090293e47,
            "unit": (u.kg * u.m**2) / u.sec,
            "rtol": 1e-4,
        },
        "log.final.system.TotEnergy": {
            "value": 2.941607e43,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.system.PotEnergy": {
            "value": -1.058388e39,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.system.KinEnergy": {
            "value": 3.070608e36,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.system.DeltaTime": {
            "value": 2.705648e12,
            "unit": u.sec,
            "rtol": 1e-4,
        },
        "log.final.star.Mass": {"value": 1.988416e30, "unit": u.kg, "rtol": 1e-4},
        "log.final.star.Radius": {"value": 1.495979e11, "unit": u.m, "rtol": 1e-4},
        "log.final.star.RadGyra": {"value": 0.500000, "rtol": 1e-4},
        "log.final.star.RotAngMom": {
            "value": 2.613823e44,
            "unit": (u.kg * u.m**2) / u.sec,
            "rtol": 1e-4,
        },
        "log.final.star.RotVel": {
            "value": 3514.823556,
            "unit": u.m / u.sec,
            "rtol": 1e-4,
        },
        "log.final.star.BodyType": {"value": 0.000000, "rtol": 1e-4},
        "log.final.star.RotRate": {
            "value": 2.349514e-08,
            "unit": 1 / u.sec,
            "rtol": 1e-4,
        },
        "log.final.star.RotPer": {"value": 2.674248e08, "unit": u.sec, "rtol": 1e-4},
        "log.final.star.Density": {
            "value": 0.000142,
            "unit": u.kg / u.m**3,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimitDryRunaway": {
            "value": 1.357831e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimRecVenus": {
            "value": 1.118929e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimRunaway": {
            "value": 1.461108e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimMoistGreenhouse": {
            "value": 1.480517e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimMaxGreenhouse": {
            "value": 2.509538e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.HZLimEarlyMars": {
            "value": 2.738109e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.Instellation": {
            "value": -1.000000,
            "unit": u.kg / u.sec**3,
            "rtol": 1e-4,
        },
        "log.final.star.CriticalSemiMajorAxis": {
            "value": -1.000000,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.star.LXUVTot": {
            "value": 3.120390e21,
            "unit": u.kg / u.sec**3,
            "rtol": 1e-4,
        },
        "log.final.star.LostEnergy": {
            "value": 2.941713e43,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.star.LostAngMom": {
            "value": 8.087678e47,
            "unit": (u.kg * u.m**2) / u.sec,
            "rtol": 1e-4,
        },
        "log.final.star.Luminosity": {"value": 3.846000e26, "unit": u.W, "rtol": 1e-4},
        "log.final.star.LXUVStellar": {"value": 3.120390e21, "unit": u.W, "rtol": 1e-4},
        "log.final.star.Temperature": {"value": 5778.000000, "unit": u.K, "rtol": 1e-4},
        "log.final.star.LXUVFrac": {"value": 8.113339e-06, "rtol": 1e-4},
        "log.final.star.RossbyNumber": {"value": 242.228868, "rtol": 1e-4},
        "log.final.star.DRotPerDtStellar": {"value": 4.237091e-10, "rtol": 1e-4},
        "log.final.b.Mass": {"value": 1.000000, "unit": u.Mearth, "rtol": 1e-4},
        "log.final.b.Radius": {"value": 6.378100e06, "unit": u.m, "rtol": 1e-4},
        "log.final.b.RadGyra": {"value": 0.500000, "rtol": 1e-4},
        "log.final.b.BodyType": {"value": 0.000000, "rtol": 1e-4},
        "log.final.b.Density": {
            "value": 5495.038549,
            "unit": u.kg / u.m**3,
            "rtol": 1e-4,
        },
        "log.final.b.HZLimitDryRunaway": {
            "value": 1.357831e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.b.HZLimRecVenus": {"value": 1.118929e11, "unit": u.m, "rtol": 1e-4},
        "log.final.b.HZLimRunaway": {"value": 1.461108e11, "unit": u.m, "rtol": 1e-4},
        "log.final.b.HZLimMoistGreenhouse": {
            "value": 1.480517e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.b.HZLimMaxGreenhouse": {
            "value": 2.509538e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.b.HZLimEarlyMars": {"value": 2.738109e11, "unit": u.m, "rtol": 1e-4},
        "log.final.b.Instellation": {
            "value": 1.367567e05,
            "unit": u.kg / u.sec**3,
            "rtol": 1e-4,
        },
        "log.final.b.MeanMotion": {
            "value": 6.296053e-06,
            "unit": 1 / u.sec,
            "rtol": 1e-4,
        },
        "log.final.b.OrbPeriod": {"value": 9.979562e05, "unit": u.sec, "rtol": 1e-4},
        "log.final.b.SemiMajorAxis": {"value": 1.495979e10, "unit": u.m, "rtol": 1e-4},
        "log.final.b.LXUVTot": {
            "value": -1.000000,
            "unit": u.kg / u.sec**3,
            "rtol": 1e-4,
        },
        "log.final.b.SurfWaterMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.b.EnvelopeMass": {"value": 0.000000, "unit": u.Mearth, "rtol": 1e-4},
        "log.final.b.OxygenMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.b.RGLimit": {"value": 1.422209e11, "unit": u.m, "rtol": 1e-4},
        "log.final.b.XO": {"value": 0.000000, "rtol": 1e-4},
        "log.final.b.EtaO": {"value": 0.000000, "rtol": 1e-4},
        "log.final.b.PlanetRadius": {"value": 6.378100e06, "unit": u.m, "rtol": 1e-4},
        "log.final.b.OxygenMantleMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.b.RadXUV": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.b.RadSolid": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.b.PresXUV": {"value": 5.000000, "rtol": 1e-4},
        "log.final.b.ScaleHeight": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.b.ThermTemp": {"value": 400.000000, "unit": u.K, "rtol": 1e-4},
        "log.final.b.AtmGasConst": {"value": 4124.000000, "rtol": 1e-4},
        "log.final.b.PresSurf": {"value": -1.000000, "unit": u.Pa, "rtol": 1e-4},
        "log.final.b.DEnvMassDt": {
            "value": 5.562685e-309,
            "unit": u.kg / u.sec,
            "rtol": 1e-4,
        },
        "log.final.b.FXUV": {"value": 1.109553, "unit": u.W / u.m**2, "rtol": 1e-4},
        "log.final.b.AtmXAbsEffH2O": {"value": 0.300000, "rtol": 1e-4},
        "log.final.b.RocheRadius": {"value": 1.496558e08, "unit": u.m, "rtol": 1e-4},
        "log.final.b.BondiRadius": {"value": 2.578997e06, "unit": u.m, "rtol": 1e-4},
        "log.final.b.HEscapeRegime": {"value": 8.000000, "rtol": 1e-4},
        "log.final.b.RRCriticalFlux": {
            "value": 105.894924,
            "unit": u.W / u.m**2,
            "rtol": 1e-4,
        },
        "log.final.b.KTide": {"value": 0.936111, "rtol": 1e-4},
        "log.final.b.RGDuration": {"value": 0.00000e00, "unit": u.yr, "rtol": 1e-4},
        "log.final.c.Mass": {"value": 6.650983e25, "unit": u.kg, "rtol": 1e-4},
        "log.final.c.Radius": {"value": 3.372667e07, "unit": u.m, "rtol": 1e-4},
        "log.final.c.RadGyra": {"value": 0.500000, "rtol": 1e-4},
        "log.final.c.BodyType": {"value": 0.000000, "rtol": 1e-4},
        "log.final.c.Density": {
            "value": 413.882226,
            "unit": u.kg / u.m**3,
            "rtol": 1e-4,
        },
        "log.final.c.HZLimitDryRunaway": {
            "value": 1.357831e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.c.HZLimRecVenus": {"value": 1.118929e11, "unit": u.m, "rtol": 1e-4},
        "log.final.c.HZLimRunaway": {"value": 1.461108e11, "unit": u.m, "rtol": 1e-4},
        "log.final.c.HZLimMoistGreenhouse": {
            "value": 1.480517e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.c.HZLimMaxGreenhouse": {
            "value": 2.509538e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.c.HZLimEarlyMars": {"value": 2.738109e11, "unit": u.m, "rtol": 1e-4},
        "log.final.c.Instellation": {
            "value": 1.367567e05,
            "unit": u.kg / u.sec**3,
            "rtol": 1e-4,
        },
        "log.final.c.MeanMotion": {
            "value": 6.296149e-06,
            "unit": 1 / u.sec,
            "rtol": 1e-4,
        },
        "log.final.c.OrbPeriod": {"value": 9.979411e05, "unit": u.sec, "rtol": 1e-4},
        "log.final.c.SemiMajorAxis": {"value": 1.495979e10, "unit": u.m, "rtol": 1e-4},
        "log.final.c.LXUVTot": {
            "value": -1.000000,
            "unit": u.kg / u.sec**3,
            "rtol": 1e-4,
        },
        "log.final.c.SurfWaterMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.c.EnvelopeMass": {"value": 3.298788, "unit": u.Mearth, "rtol": 1e-4},
        "log.final.c.OxygenMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.c.RGLimit": {"value": 1.349743e11, "unit": u.m, "rtol": 1e-4},
        "log.final.c.XO": {"value": 0.000000, "rtol": 1e-4},
        "log.final.c.EtaO": {"value": 0.000000, "rtol": 1e-4},
        "log.final.c.PlanetRadius": {"value": 3.372667e07, "unit": u.m, "rtol": 1e-4},
        "log.final.c.OxygenMantleMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.c.RadXUV": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.c.RadSolid": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.c.PresXUV": {"value": 5.000000, "rtol": 1e-4},
        "log.final.c.ScaleHeight": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.c.ThermTemp": {"value": 400.000000, "unit": u.K, "rtol": 1e-4},
        "log.final.c.AtmGasConst": {"value": 4124.000000, "rtol": 1e-4},
        "log.final.c.PresSurf": {"value": -1.000000, "unit": u.Pa, "rtol": 1e-4},
        "log.final.c.DEnvMassDt": {
            "value": 5.562685e-309,
            "unit": u.kg / u.sec,
            "rtol": 1e-4,
        },
        "log.final.c.FXUV": {"value": 1.109553, "unit": u.W / u.m**2, "rtol": 1e-4},
        "log.final.c.AtmXAbsEffH2O": {"value": 0.300000, "rtol": 1e-4},
        "log.final.c.RocheRadius": {"value": 3.342037e08, "unit": u.m, "rtol": 1e-4},
        "log.final.c.BondiRadius": {"value": 2.872125e07, "unit": u.m, "rtol": 1e-4},
        "log.final.c.HEscapeRegime": {"value": 7.000000, "rtol": 1e-4},
        "log.final.c.RRCriticalFlux": {
            "value": 73.086412,
            "unit": u.W / u.m**2,
            "rtol": 1e-4,
        },
        "log.final.c.KTide": {"value": 0.849139, "rtol": 1e-4},
        "log.final.c.RGDuration": {"value": 0.00000e00, "unit": u.yr, "rtol": 1e-4},
    }
)
class TestAtmEscKepler36(Benchmark):
    pass
