import stardate as sd
import pandas as pd

df = pd.read_csv("kane_cks_tdmra_dr2.csv")

savedir = "planet_results"

prot, prot_err = df.period, df.period_errm

N = len(df)
for i, id in enumerate(df.id_kic.values):
    print(i, "of", N)
    print("kepid = ", str(id).zfill(9))

    iso_params = {"G": (df.phot_g_mean_mag[i], df.phot_g_mean_mag[i]*.05),
                  "bp": (df.phot_bp_mean_mag[i], df.phot_bp_mean_mag[i]*.05),
                  "rp": (df.phot_rp_mean_mag[i], df.phot_rp_mean_mag[i]*.05),
                  "J": (df.kic_jmag[i], df.kic_jmag[i]*.05),
                  "H": (df.kic_hmag[i], df.kic_hmag[i]*.05),
                  "K": (df.kic_kmag[i], df.kic_kmag[i]*.05),
                  "teff": (df.iso_steff[i], df.iso_steff_err2[i]),
                  "logg": (df.iso_slogg[i], df.iso_slogg_err2[i]),
                  "feh": (df.iso_smet[i], df.iso_smet_err2[i]),
                  "parallax": (df.parallax[i], df.parallax_error[i])}

    star = sd.star(iso_params, prot[i], prot_err[i], savedir=savedir,
                   suffix=str(id).zfill(9))
    sampler = star.fit()
    star.make_plots()
