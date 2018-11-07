import stardate as sd
import pandas as pd
import numpy as np

df = pd.read_csv("kane_cks_tdmra_dr2.csv")

savedir = "planet_results"

prot, prot_err = df.period, df.period_errm

N = len(df)

m = np.arange(len(df.id_kic.values)) > 22
df = df.iloc[m]

for i, id in enumerate(df.id_kic.values):
    print(i, "of", N)
    print("kepid = ", str(id).zfill(9))

    iso_params = {"G": (df.phot_g_mean_mag.values[i],
                        df.phot_g_mean_mag.values[i]*.05),
                  "bp": (df.phot_bp_mean_mag.values[i],
                         df.phot_bp_mean_mag.values[i]*.05),
                  "rp": (df.phot_rp_mean_mag.values[i],
                         df.phot_rp_mean_mag.values[i]*.05),
                  "J": (df.kic_jmag.values[i],
                        df.kic_jmag.values[i]*.05),
                  "H": (df.kic_hmag.values[i],
                        df.kic_hmag.values[i]*.05),
                  "K": (df.kic_kmag.values[i],
                        df.kic_kmag.values[i]*.05),
                  "teff": (df.iso_steff.values[i],
                           df.iso_steff_err2.values[i]),
                  "logg": (df.iso_slogg.values[i],
                           df.iso_slogg_err2.values[i]),
                  "feh": (df.iso_smet.values[i],
                          df.iso_smet_err2.values[i]),
                  "parallax": (df.parallax.values[i],
                               df.parallax_error.values[i])}

    star = sd.star(iso_params, prot[i], prot_err[i], savedir=savedir,
                   suffix=str(id).zfill(9))
    sampler = star.fit()
    star.make_plots()
