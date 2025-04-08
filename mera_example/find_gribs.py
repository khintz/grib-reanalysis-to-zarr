from datetime import datetime, timedelta
from isodate import parse_duration
from pathlib import Path
import yaml

def find_files_for_time_interval(t_start: datetime, t_end: datetime) -> list[str]:

    root_path = Path("/scratch/duuw/reanalysis/mera/")

    # Example: MERA_PRODYEAR_2017_12_11_105_2_0_ANALYSIS
    path_format = "{indicatorofparameter}/{leveltype}/{level}/{timerangeindicator}"
    filename_format = "MERA_PRODYEAR_{start:%Y_%m}_{indicatorofparameter}_{leveltype}_{level}_{timerangeindicator}_{suffix}"
    suffixes = ["ANALYSIS"]

    # list of tuples for each parameter in format indicatorofparameter, leveltype, level, timerangeindicator
    parameters = [
        (1, 100, 500, 0),
        (1, 103, 0, 0),
        (1, 105, 0, 0),
        (6, 100, 1000, 0),
        (6, 100, 500, 0),
        (11, 100, 500, 0),
        (11, 100, 850, 0),
        (11, 105, 2, 0),
        (11, 105, 30, 0),
        (33, 100, 850, 0),
        (33, 105, 30, 0),
        (34, 100, 850, 0),
        (34, 105, 30, 0),
        (52, 105, 2, 0),
        (52, 105, 30, 0),
        (54, 200, 0, 0),
        (61, 105, 0, 4),
        (113, 8, 0, 4),
        (115, 105, 0, 4),
        (116, 105, 0, 4)
    ]


    paths = []
    t = t_start

    for suffix in suffixes:

        for parameter in parameters:

            indicatorofparameter, leveltype, level, timerangeindicator = parameter

            path_file = path_format.format(indicatorofparameter=indicatorofparameter,
                                            leveltype=leveltype,
                                            level=level,
                                            timerangeindicator=timerangeindicator)

            filename = filename_format.format(start=t,
                                            indicatorofparameter=indicatorofparameter,
                                            leveltype=leveltype,
                                            level=level,
                                            timerangeindicator=timerangeindicator,
                                            suffix=suffix)

            paths.append(root_path / path_file / filename)

    print(paths)
    print(len(paths))
    return paths
