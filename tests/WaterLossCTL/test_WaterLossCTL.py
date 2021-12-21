from benchmark import Benchmark, benchmark
import astropy.units as u
import pytest


@benchmark(
    {
        "log.final.b.MeanMotion": {"value": 1.592839e-05, "unit": 1 / u.sec},
        "log.final.b.Eccentricity": {"value": 0.099920},
        "log.final.b.SurfWaterMass": {"value": 8.973863, "unit": u.TO},
        "log.final.b.OxygenMass": {"value": 5.192387, "unit": u.bars},
        "log.final.b.XO": {"value": 0.333876},
        "log.final.b.EtaO": {"value": 0.161293},
    }
)
class TestWaterLossCTL(Benchmark):
    pass
