import stardate as sd
import pandas as pd
import numpy as np
from multiprocessing import Pool

def measure_koi_ages(row):
    df = row[1]

    iso_params = {"G": (df.phot_g_mean_mag,
                        df.phot_g_mean_mag*.05),
                  "bp": (df.phot_bp_mean_mag,
                         df.phot_bp_mean_mag*.05),
                  "rp": (df.phot_rp_mean_mag,
                         df.phot_rp_mean_mag*.05),
                  "J": (df.kic_jmag,
                        df.kic_jmag*.05),
                  "H": (df.kic_hmag,
                        df.kic_hmag*.05),
                  "K": (df.kic_kmag,
                        df.kic_kmag*.05),
                  "teff": (df.iso_steff,
                           df.iso_steff_err2),
                  "logg": (df.iso_slogg,
                           df.iso_slogg_err2),
                  "feh": (df.iso_smet,
                          df.iso_smet_err2),
                  "parallax": (df.parallax,
                               df.parallax_error)}

    starname = str(int(df.id_kic)).zfill(9)
    filename = "planet_results/{}".format(starname)

    star = sd.Star(
        iso_params, df.period, .5*(df.period_errp + df.period_errm),
        filename=filename)

    sampler = star.fit(max_n=200000)


if __name__ == "__main__":
    full_df = pd.read_csv("kane_cks_tdmra_dr2.csv")
    p = Pool(4)
    list(p.map(measure_koi_ages, full_df.iterrows()))
    # for row in full_df.iterrows():
    #     measure_koi_ages(row)
